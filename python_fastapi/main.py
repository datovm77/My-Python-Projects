import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
from openai import OpenAI
from fastapi.responses import StreamingResponse
from dotenv import load_dotenv

# 1. 加载环境变量
load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

# 2. 初始化 OpenAI 客户端 (指向 OpenRouter)
# OpenRouter 本质上是一个“路由器”，兼容 OpenAI 协议
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY,
)

app = FastAPI()

# 3. 定义请求模型
# 我们模仿 OpenAI 的官方格式：接收一个消息列表
class ChatRequest(BaseModel):
    messages: List[Dict[str, str]] 
    # 示例: [{"role": "user", "content": "你好"}]
    model: str = "openai/gpt-oss-120b" 
    # 你可以在 OpenRouter 上找任何你喜欢的免费或付费模型

# 4. 核心逻辑：生成器函数
# 这个函数会像流水线一样，拿到一点数据就 yield (产出) 一点
def generate_stream(messages: list, model: str):
    try:
        stream = client.chat.completions.create(
            model=model,
            messages=messages,
            stream=True, # 关键：开启流式模式
            # OpenRouter 建议加这俩 Header，方便在排行榜显示你的应用（可选）
            extra_headers={
                "HTTP-Referer": "https://your-site.com", 
                "X-Title": "My FastAgent", 
            }
        )
        
        for chunk in stream:
            # 提取增量内容
            content = chunk.choices[0].delta.content
            if content:
                yield content

    except Exception as e:
        yield f"Error: {str(e)}"

# 5. 定义 API 接口
@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    # 使用 StreamingResponse 包装生成器
    return StreamingResponse(
        generate_stream(request.messages, request.model), 
        media_type="text/event-stream"
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)