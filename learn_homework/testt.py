import os
import base64
from openai import OpenAI

# ================= 配置区域 =================
# 1. 这里填你的 GETGOAPI 的 Key
API_KEY = "sk-VozehGIanZ5PcgTB3BjyZbITp1m1eiYwn64kyGPRafwGOE2B" 

# 2. 这里填 GETGOAPI 的接口地址 (通常是这个，如果有变动请查看官方文档)
BASE_URL = "https://api.getgoapi.com/v1" 
# 或者可能是 "https://api.getgoapi.com/v1/chat/completions" 的前缀，通常写到 /v1 即可

# 3. 模型名称 (你说的是 gemini3flash，请务必去后台确认准确的字符串 ID)
# 常见的可能是 "gemini-1.5-flash" 或 "gemini-2.0-flash-exp"
# 假设你在平台看到的 ID 是这个：
MODEL_NAME = "gemini-3-flash-preview" 
# ===========================================

def encode_image(image_path):
    """
    将本地图片转换为 Base64 格式，这是 API 接收图片的标准姿势。
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def test_multimodal_call():
    print(f"正在尝试连接 API: {BASE_URL} ...")
    
    # 初始化客户端 (假装我们是 OpenAI，其实连的是 GetGoAPI)
    client = OpenAI(
        api_key=API_KEY,
        base_url=BASE_URL
    )

    # 准备测试素材
    image_path = "test_image.png" # 确保你目录下有这张图
    
    # 检查图片是否存在
    if not os.path.exists(image_path):
        print(f"错误：找不到 {image_path}，请截个图放在脚本旁边。")
        return

    # 图片转码
    base64_image = encode_image(image_path)
    print("图片读取并转码成功，正在发送请求...")

    try:
        # 发送请求
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": [
                        # 1. 传入文字指令
                        {
                            "type": "text", 
                            "text": "这张图里是什么内容？请用中文简单总结一下，并告诉我这如果是学习资料，我该怎么学？"
                        },
                        # 2. 传入图片数据
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=1000  # 限制输出长度
        )

        # 打印结果
        print("\n======== AI 回复 ========")
        print(response.choices[0].message.content)
        print("=========================")
        print("测试成功！API 通路和多模态功能正常。")

    except Exception as e:
        print("\n测试失败！报错信息如下：")
        print(e)
        print("\n排错建议：")
        print("1. 检查 API_KEY 是否正确。")
        print("2. 检查 MODEL_NAME 是否在 GetGoAPI 支持列表中 (有的平台叫 gemini-pro-vision)。")
        print("3. 检查余额是否充足。")

if __name__ == "__main__":
    test_multimodal_call()