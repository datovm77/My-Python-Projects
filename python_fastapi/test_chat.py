import requests
import json

# 接口地址
url = "http://127.0.0.1:8000/chat"

# 发送的数据
# payload = {
#     "messages": [{"role": "user", "content": "你好"}],
#     "model": "meta-llama/llama-3-8b-instruct:free" # 强制切换模型
# }

# 【教学演示】场景 2：客户端不传模型，使用后端默认值 (省事)
payload = {
    "messages": [
        {"role": "user", "content": "请用两句话解释什么是量子纠缠"}
    ]
}

print("--- 正在连接 Agent，准备接收流式回复 ---")

# 关键点：设置 stream=True 开启流式接收
try:
    with requests.post(url, json=payload, stream=True) as response:
        response.raise_for_status() # 检查请求是否成功

        # 循环读取数据流
        for chunk in response.iter_content(chunk_size=None):
            if chunk:
                # decode 将二进制转为文字, end='' 避免print自动换行
                print(chunk.decode("utf-8"), end="", flush=True)
except Exception as e:
    print(f"\n请求出错: {e}")

print("\n--- 回复结束 ---")