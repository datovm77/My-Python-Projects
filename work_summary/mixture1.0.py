import streamlit as st
import asyncio
import os
from openai import AsyncOpenAI, OpenAI
# streamlit run mixture1.0.py
# Set up the Streamlit app
st.title("Mixture-of-Agents LLM App")

# Get API key from the user
OpenAI_api_key = st.text_input("Enter your OpenAI API Key:", type="password")

if OpenAI_api_key:
    os.environ["OpenAI_API_KEY"] = OpenAI_api_key
    client = OpenAI(api_key=OpenAI_api_key,base_url="https://openrouter.ai/api/v1")
    async_client = AsyncOpenAI(api_key=OpenAI_api_key,base_url="https://openrouter.ai/api/v1")

    # Define the models
    reference_models = [
    "openai/gpt-5.2",                
    "google/gemini-3-pro-preview",
    "deepseek/deepseek-r1-0528:free"
    ]
    aggregator_model = "anthropic/claude-opus-4.5"

    # Define the aggregator system prompt
    aggregator_system_prompt = """You have been provided with a set of responses from various open-source models to the latest user query. Your task is to synthesize these responses into a single, high-quality response. It is crucial to critically evaluate the information provided in these responses, recognizing that some of it may be biased or incorrect. Your response should not simply replicate the given answers but should offer a refined, accurate, and comprehensive reply to the instruction. Ensure your response is well-structured, coherent, and adheres to the highest standards of accuracy and reliability. Responses from models:"""

    # Get user input
    user_prompt = st.text_input("Enter your question:")

    async def run_llm(model,placeholder):
        stream = await async_client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": user_prompt}],
            temperature=0.9,
            max_tokens=4096,
            stream=True
        )
        full_text = ""
        header = f"**{model}**\n\n"
        async for chunk in stream:
            content = chunk.choices[0].delta.content
            if content:
                full_text += content
                placeholder.markdown(header + full_text+"▌")
        placeholder.markdown(header + full_text)
        return full_text

    async def main():
        cols = st.columns(len(reference_models))
        tasks = []
         
        for model,col in zip(reference_models,cols):
            with col:
                ph = st.empty()
                task = run_llm(model,placeholder=ph)
                tasks.append(task)

        result = await asyncio.gather(*tasks)
        st.divider()
        context_text = ",".join(result)
        # Aggregate responses
        st.subheader("Aggregated Response:")
        finalStream = await async_client.chat.completions.create(
            model=aggregator_model,
            messages=[
                {"role": "system", "content": aggregator_system_prompt},
                {"role": "user", "content": context_text},
            ],
            stream=True,
        )
        
        # Display aggregated response
        response_container = st.empty()
        full_response = ""
        async for chunk in finalStream:
            content = chunk.choices[0].delta.content or ""
            full_response += content
            response_container.markdown(full_response + "▌")
        response_container.markdown(full_response)

    if st.button("Get Answer"):
        if user_prompt:
            asyncio.run(main())
        else:
            st.warning("Please enter a question.")

else:
    st.warning("Please enter your OpenAI API key to use the app.")

# Add some information about the app
st.sidebar.title("About this app")
st.sidebar.write(
    "This app demonstrates a Mixture-of-Agents approach using multiple Language Models (LLMs) "
    "to answer a single question."
)

st.sidebar.subheader("How it works:")
st.sidebar.markdown(
    """
    1. The app sends your question to multiple LLMs:
        - Qwen/Qwen2-72B-Instruct
        - Qwen/Qwen1.5-72B-Chat
        - mistralai/Mixtral-8x22B-Instruct-v0.1
        - databricks/dbrx-instruct
    2. Each model provides its own response
    3. All responses are then aggregated using Mixtral-8x22B-Instruct-v0.1
    4. The final aggregated response is displayed
    """
)

st.sidebar.write(
    "This approach allows for a more comprehensive and balanced answer by leveraging multiple AI models."
)