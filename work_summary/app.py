import streamlit as st   ##前端界面
import os                ##用于处理与操作系统相关的任务。比如读取文件路径、创建文件夹、检查环境变量等
import json
import base64            ##将二进制数据（如图片、PDF）编码为 ASCII 字符串。在 Web 开发中，常用于在 JSON 或 HTML 中直接嵌入图片数据。
from openai import OpenAI##人工智能接口
import pdfplumber        ##解析PDF
import docx              ##用于创建、修改和读取 Microsoft Word (.docx) 文件。

##streamlit run app.py

# ================= 配置区域 =================
API_KEY = "" # 记得填回你的 Key
BASE_URL = "https://api.getgoapi.com/v1"
MODEL_NAME = "gemini-3-pro-preview"   ##gemini-3-flash-preview   gemini-3-pro-preview
HISTORY_FILE = "history.json"
PROFILE_FILE = "profile.txt"  
# ===========================================

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

# --- 核心功能函数 ---

def load_data():
    """读取历史记录和个人档案"""
    history = []
    profile = "暂无详细档案（这是第一周）"
    
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            try: history = json.load(f)
            except: pass
            
    if os.path.exists(PROFILE_FILE):
        with open(PROFILE_FILE, "r", encoding="utf-8") as f:
            profile = f.read()
            
    return history, profile

def save_data(new_summary, new_profile):
    """保存周报到历史，并覆盖更新个人档案"""
    # 1. 保存历史列表
    history, _ = load_data()
    history.append(new_summary)
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)
        
    # 2. 覆盖更新个人档案 (这是关键！AI会把最新的能力值写进这里)
    with open(PROFILE_FILE, "w", encoding="utf-8") as f:
        f.write(new_profile)

def encode_image(uploaded_file):
    bytes_data = uploaded_file.getvalue()
    return base64.b64encode(bytes_data).decode('utf-8')

def extract_text_from_file(uploaded_file):
    file_type = uploaded_file.name.split('.')[-1].lower()
    text = ""
    try:
        if file_type == 'pdf':
            with pdfplumber.open(uploaded_file) as pdf:
                for page in pdf.pages: text += page.extract_text() + "\n"
        elif file_type == 'docx':
            doc = docx.Document(uploaded_file)
            for para in doc.paragraphs: text += para.text + "\n"
        elif file_type in ['txt', 'c', 'cpp', 'py', 'java', 'md']:
            text = uploaded_file.read().decode("utf-8", errors='ignore')
    except Exception as e:
        return f"[读取出错: {str(e)}]"
    return f"\n--- 文件名: {uploaded_file.name} ---\n{text}\n"

def call_ai_advanced(user_base_input, current_profile, current_text, current_images):
    """
    调用：要求 AI 同时输出【周报】和【更新后的档案】
    """
    
    # 这里的 System Prompt 是核心，教 AI 怎么维护你的“技能树”
    system_prompt = """
    你是一位经验丰富的高级技术导师（Tech Lead），擅长代码审查（Code Review）和循循善诱的教学。你需要基于学生上传的学习材料（代码或笔记）以及他/她的历史档案，完成以下两项核心任务：

    ### 任务一：生成深度学习周报
    请不仅仅是总结，而是进行“对比式教学”。内容必须包含：
    1. **📚 核心知识点内化**：提取本周代码或文档中涉及的关键技术名词、算法原理或语法特性，解释其核心概念。
    2. **⚔️ 代码逻辑演练与优化（重点）**：
       - 仔细审阅学生提交的代码。
       - 选取几段逻辑不够优美、效率低下或有bug的代码片段。
       - **展示对比**：先展示【学生原代码】，紧接着展示【AI优化后的代码】。
       - **深度解析**：详细说明优化了哪里（例如：时间复杂度从O(n^2)降到了O(n)、利用了更高级的库函数、增强了鲁棒性、或者代码风格更Pythonic）。让学生直观感受到逻辑的差距。
    3. **📉 待改进之处**：明确指出学生当前思维上的误区、代码规范问题或逻辑漏洞。
    4. **📅 下周计划**：基于本周表现，推荐下一步的学习路径。

    ### 任务二：全局能力档案更新
    更新学生的长期能力画像。请注意：
    - **增量更新**：千万不要删除他以前掌握的知识，将本周新学的知识点“融合”或者“增添”进现有的技能树中。
    - **动态评级**：根据本周代码质量（如是否只会写过程式代码，还是懂面向对象），调整对其技术深度的评估。
    - **记录弱点**：如果本周代码暴露出基础不牢（如变量命名差、不懂异常处理），请务必记录在案。
    ---
    【严格输出格式约束】
    为了保证系统能正确解析，请务必严格遵守以下标记格式，不要添加任何额外的开头或结尾寒暄：

    [REPORT_START]
    这里使用 Markdown 格式输出周报（必须包含上述的“代码对比”和“知识点”板块）。
    示例结构：
    ## 📚 本周知识点
    ...
    ## ⚔️ 代码实战与优化对比
    ### 案例：[具体功能/函数名]
    **❌ 学生原逻辑：**
    ```python
    # 代码...
    ```
    **✅ AI 优化后逻辑：**
    ```python
    # 代码...
    ```
    **💡 优化点解析：**
    ...
    [REPORT_END]

    [PROFILE_START]
    这里输出纯文本格式的档案：
    【已掌握技能树】：[语言/框架/算法列表...]
    【当前技术评级】：[例如：Python入门/进阶/算法新手...]
    【顽固弱点】：[例如：递归逻辑混乱/不写注释/内存管理概念模糊...]
    【最近更新备注】：[简述本周新增了什么能力]
    [PROFILE_END]
    **诚实原则**: 如果用户上传的文件内容为空或无法识别，请在报告中委婉地提示用户“无法读取有效内容”，不要编造分析结果。请全程使用中文回答。
    """

    user_content_blocks = []
    
    context_text = f"""
    【学生初始自述】: {user_base_input}
    
    【当前的全局能力档案 (截止到上周)】: 
    {current_profile}
    
    【本周新上传的材料内容】:
    {current_text}
    """
    
    user_content_blocks.append({"type": "text", "text": context_text})
    
    for img_base64 in current_images:
        user_content_blocks.append({
            "type": "image_url",
            "image_url": {"url": f"data:image/png;base64,{img_base64}"}
        })
        
    user_content_blocks.append({
        "type": "text", 
        "text": "请开始分析，务必严格遵守 [REPORT_START] 和 [PROFILE_START] 的格式分隔。"
    })

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content_blocks}
            ],
            max_tokens=8196 
        )
        raw_content = response.choices[0].message.content
        return raw_content
    except Exception as e:
        return f"ERROR: {e}"

# --- 解析 AI 回复的辅助函数 ---
def parse_ai_response(raw_text):
    """把 AI 的长回复切成：周报 和 档案 两部分"""
    report = "生成出错，未找到报告内容"
    profile = "生成出错，未找到档案内容"
    
    if "[REPORT_START]" in raw_text and "[REPORT_END]" in raw_text:
        report = raw_text.split("[REPORT_START]")[1].split("[REPORT_END]")[0].strip()
        
    if "[PROFILE_START]" in raw_text and "[PROFILE_END]" in raw_text:
        profile = raw_text.split("[PROFILE_START]")[1].split("[PROFILE_END]")[0].strip()
        
    return report, profile

# --- Streamlit 页面 ---

st.set_page_config(page_title="AI 学习导师", layout="wide")
st.title("AI 学习导师")

# 加载数据
history_data, current_profile = load_data()

with st.sidebar:
    st.header("📊 全局能力画像")
    st.info("这是 AI 眼中的你（不仅是这周，而是累积的你）：")
    # 把档案显示在侧边栏，让你看到 AI 记得住！
    st.text_area("档案内容", value=current_profile, height=400, disabled=True)
    
    st.divider()
    st.header("历史周报")
    for idx, record in enumerate(history_data):
        with st.expander(f"第 {idx+1} 周"):
            st.markdown(record)

st.subheader("📂 本周学习材料上传")
user_bg = st.text_input("如果有新的特殊情况请补充（比如：这周生病了没怎么学）", "")
uploaded_files = st.file_uploader("拖入文件...", accept_multiple_files=True)

if st.button("🚀 生成总结并更新档案", type="primary"):
    if not uploaded_files:
        st.warning("请先上传文件")
    else:
        status_box = st.status("AI 正在大脑风暴...", expanded=True)
        
        # 1. 预处理
        status_box.write("👀 正在看文件...")
        text_buffer = ""
        img_list = []
        for file in uploaded_files:
            ftype = file.name.split('.')[-1].lower()
            if ftype in ['png', 'jpg', 'jpeg']:
                img_list.append(encode_image(file))
            else:
                text_buffer += extract_text_from_file(file)
        
        # 2. 调用 AI
        status_box.write("🧠 正在对比旧档案与新知识...")
        raw_response = call_ai_advanced(user_bg, current_profile, text_buffer, img_list)
        
        if "ERROR" in raw_response:
            status_box.update(label="出错了", state="error")
            st.error(raw_response)
        else:
            # 3. 解析与保存
            status_box.write("📝 正在更新数据库...")
            new_report, new_profile_content = parse_ai_response(raw_response)
            
            save_data(new_report, new_profile_content)
            
            status_box.update(label="完成！", state="complete", expanded=False)
            
            st.divider()
            col1, col2 = st.columns([2, 1])
            with col1:
                st.subheader("📄 本周学习报告")
                st.markdown(new_report)
            with col2:
                st.subheader("🔄 更新后的能力档案")
                st.caption("AI 已经把这些写入了长期记忆：")
                st.code(new_profile_content, language="text")
                st.toast("记忆已同步更新！刷新页面可见侧边栏变化。")