import asyncio
import streamlit as st
import os
from typing import Dict, Any, List
from agents import Agent, Runner, trace
from agents import set_default_openai_key
from firecrawl import FirecrawlApp
from agents.tool import function_tool

# Set page configuration
st.set_page_config(
    page_title="OpenAI Deep Research Agent",
    page_icon="📘",
    layout="wide"
)

# Initialize session state for API keys if not exists
if "openai_api_key" not in st.session_state:
    st.session_state.openai_api_key = ""
if "firecrawl_api_key" not in st.session_state:
    st.session_state.firecrawl_api_key = ""

# Sidebar for API keys
with st.sidebar:
    st.title("API Configuration")
    openai_api_key = st.text_input(
        "OpenAI API Key", 
        value=st.session_state.openai_api_key,
        type="password"
    )
    firecrawl_api_key = st.text_input(
        "Firecrawl API Key", 
        value=st.session_state.firecrawl_api_key,
        type="password"
    )
    
    if openai_api_key:
        st.session_state.openai_api_key = openai_api_key
        os.environ["OPENAI_BASE_URL"] = "https://openrouter.ai/api/v1"
        os.environ["OPENAI_API_KEY"] = openai_api_key
        set_default_openai_key(openai_api_key)
    if firecrawl_api_key:
        st.session_state.firecrawl_api_key = firecrawl_api_key

# Main content
st.title("📘 OpenAI Deep Research Agent")
st.markdown("This OpenAI Agent from the OpenAI Agents SDK performs deep research on any topic using Firecrawl")

# Research topic input
research_topic = st.text_input("Enter your research topic:", placeholder="e.g., Latest developments in AI")

# 修改导入（如果你的 SDK 是新版，建议用 Firecrawl）
# 如果旧版 import FirecrawlApp 还能用，也可以保留，但建议检查
try:
    from firecrawl import Firecrawl
except ImportError:
    from firecrawl import FirecrawlApp as Firecrawl

@function_tool
async def deep_research(query: str, max_depth: int, time_limit: int, max_urls: int) -> Dict[str, Any]:
    """
    Perform comprehensive web research using Firecrawl's Agent endpoint (Successor to deep_research).
    """
    try:
        # 初始化 Firecrawl
        app = Firecrawl(api_key=st.session_state.firecrawl_api_key)
        
        # 定义 Prompt，将参数融入 prompt 中，因为 Agent 主要靠 prompt 驱动
        # 注意：Agent 接口通常不需要 maxDepth/maxUrls 这种底层参数，它会自动规划
        agent_prompt = f"""
        Conduct deep research on the following topic: {query}.
        Please verify facts and provide comprehensive details.
        Limit the scope to ensure completion within {time_limit} seconds roughly.
        """
        
        # 设置回调（如果 SDK 支持监听）
        # 注意：Agent 往往是阻塞或轮询的，简单起见这里用同步等待
        
        with st.spinner(f"GPT-5 Mini is coordinating Firecrawl Agent for: {query}..."):
            # 使用新的 agent 方法 (根据 SDK 版本可能是 agent 或 async_agent)
            # 如果是最新 SDK:
            response = app.agent(
                prompt=agent_prompt,
                options={
                    "search": {"limit": max_urls} # 尝试传入一些限制参数
                }
            )
            
        # 解析返回结果 (Agent 返回结构通常包含 data)
        # 注意：Agent 的返回结构可能与旧版 deep_research 不同，通常直接返回 markdown 或 json
        
        return {
            "success": True,
            "final_analysis": response.get('data', "No data returned"), # Agent 通常直接返回结果内容
            "sources_count": len(response.get('metadata', {}).get('sources', [])),
            "sources": response.get('metadata', {}).get('sources', [])
        }

    except AttributeError:
        # 如果 agent 方法也不存在，回退到基础的 search + extract
        st.warning("Agent method not found, falling back to Search...")
        try:
            search_results = app.search(query, params={"limit": max_urls, "scrapeOptions": {"formats": ["markdown"]}})
            # 简单的拼接作为分析结果
            summary = "\n\n".join([item.get('markdown', '')[:500] for item in search_results.get('data', [])])
            return {
                "success": True,
                "final_analysis": f"**Search Results Summary:**\n{summary}...",
                "sources": [item.get('url') for item in search_results.get('data', [])],
                "sources_count": len(search_results.get('data', []))
            }
        except Exception as e2:
             return {"error": f"Search fallback failed: {str(e2)}", "success": False}
             
    except Exception as e:
        st.error(f"Firecrawl Error: {str(e)}")
        return {"error": str(e), "success": False}

# Keep the original agents
research_agent = Agent(
    name="research_agent",
    model="openai/gpt-5-mini",
    instructions="""You are a research assistant that can perform deep web research on any topic.

    When given a research topic or question:
    1. Use the deep_research tool to gather comprehensive information
       - Always use these parameters:
         * max_depth: 3 (for moderate depth)
         * time_limit: 180 (3 minutes)
         * max_urls: 10 (sufficient sources)
    2. The tool will search the web, analyze multiple sources, and provide a synthesis
    3. Review the research results and organize them into a well-structured report
    4. Include proper citations for all sources
    5. Highlight key findings and insights
    """,
    tools=[deep_research]
)

elaboration_agent = Agent(
    name="elaboration_agent",
    instructions="""You are an expert content enhancer specializing in research elaboration.

    When given a research report:
    1. Analyze the structure and content of the report
    2. Enhance the report by:
       - Adding more detailed explanations of complex concepts
       - Including relevant examples, case studies, and real-world applications
       - Expanding on key points with additional context and nuance
       - Adding visual elements descriptions (charts, diagrams, infographics)
       - Incorporating latest trends and future predictions
       - Suggesting practical implications for different stakeholders
    3. Maintain academic rigor and factual accuracy
    4. Preserve the original structure while making it more comprehensive
    5. Ensure all additions are relevant and valuable to the topic
    """
)

async def run_research_process(topic: str):
    """Run the complete research process."""
    # Step 1: Initial Research
    with st.spinner("Conducting initial research..."):
        research_result = await Runner.run(research_agent, topic)
        initial_report = research_result.final_output
    
    # Display initial report in an expander
    with st.expander("View Initial Research Report"):
        st.markdown(initial_report)
    
    # Step 2: Enhance the report
    with st.spinner("Enhancing the report with additional information..."):
        elaboration_input = f"""
        RESEARCH TOPIC: {topic}
        
        INITIAL RESEARCH REPORT:
        {initial_report}
        
        Please enhance this research report with additional information, examples, case studies, 
        and deeper insights while maintaining its academic rigor and factual accuracy.
        """
        
        elaboration_result = await Runner.run(elaboration_agent, elaboration_input)
        enhanced_report = elaboration_result.final_output
    
    return enhanced_report

# Main research process
if st.button("Start Research", disabled=not (openai_api_key and firecrawl_api_key and research_topic)):
    if not openai_api_key or not firecrawl_api_key:
        st.warning("Please enter both API keys in the sidebar.")
    elif not research_topic:
        st.warning("Please enter a research topic.")
    else:
        try:
            # Create placeholder for the final report
            report_placeholder = st.empty()
            
            # Run the research process
            enhanced_report = asyncio.run(run_research_process(research_topic))
            
            # Display the enhanced report
            report_placeholder.markdown("## Enhanced Research Report")
            report_placeholder.markdown(enhanced_report)
            
            # Add download button
            st.download_button(
                "Download Report",
                enhanced_report,
                file_name=f"{research_topic.replace(' ', '_')}_report.md",
                mime="text/markdown"
            )
            
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Footer
st.markdown("---")
st.markdown("Powered by OpenAI Agents SDK and Firecrawl") 