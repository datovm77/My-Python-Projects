import os
import time

def merge_code_files(source_dir, output_dir="merged_code"):
    """
    遍历指定目录，将不同类型的代码文件分别合并到不同的Markdown文件中。
    """
    
    # 1. 定义需要提取的文件后缀名及其对应的Markdown语言标签
    # 格式: { '.后缀': 'markdown语言标记' }
    EXTENSION_MAP = {
        # C/C++
        '.c': 'c',
        '.h': 'c',
        '.cpp': 'cpp',
        '.hpp': 'cpp',
        '.cc': 'cpp',
        
        # Python
        '.py': 'python',
        
        # Java
        '.java': 'java',
        
        # Web
        '.html': 'html',
        '.css': 'css',
        '.js': 'javascript',
        '.ts': 'typescript',
        '.json': 'json',
        
        # Others
        '.go': 'go',
        '.rs': 'rust',
        '.sh': 'bash',
        '.sql': 'sql',
        '.md': 'markdown',
        '.txt': 'text'
    }

    # 需要忽略的文件夹
    IGNORE_DIRS = {'.git', '.idea', '.vscode', '__pycache__', 'node_modules', 'build', 'dist', 'bin', 'obj'}

    # 用于存储内容的字典： key=后缀名, value=内容列表
    content_buffer = {ext: [] for ext in EXTENSION_MAP.keys()}

    print(f"🚀 开始扫描目录: {source_dir}")
    
    file_count = 0
    
    # 2. 遍历目录
    for root, dirs, files in os.walk(source_dir):
        # 修改 dirs 列表以通过引用跳过忽略的目录
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for file in files:
            file_ext = os.path.splitext(file)[1].lower()
            
            if file_ext in EXTENSION_MAP:
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, source_dir) # 获取相对路径
                
                # 读取文件内容
                content = read_file_content(file_path)
                
                if content is not None:
                    # 格式化为 Markdown
                    lang_tag = EXTENSION_MAP[file_ext]
                    formatted_block = (
                        f"## File: {rel_path}\n"
                        f"```{lang_tag}\n"
                        f"{content}\n"
                        f"```\n\n"
                        f"---\n\n"
                    )
                    content_buffer[file_ext].append(formatted_block)
                    file_count += 1
                    print(f"  [+] 已处理: {rel_path}")

    # 3. 写入输出文件
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"\n💾 正在写入文件到 '{output_dir}/' ...")
    
    generated_files = []
    
    # 将同一类后缀（例如 .c 和 .h）可以考虑合并，或者严格按照后缀分开
    # 这里我们按照后缀名严格分开导出
    for ext, blocks in content_buffer.items():
        if blocks: # 如果该类型有内容
            # 生成文件名，例如 code_py.md, code_c.md
            clean_ext = ext.replace('.', '')
            output_filename = os.path.join(output_dir, f"source_{clean_ext}.md")
            
            with open(output_filename, 'w', encoding='utf-8') as f:
                f.write(f"# Merged {ext} Files\n")
                f.write(f"Generated at: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                f.write("".join(blocks))
            
            generated_files.append(output_filename)

    print("\n✅ 处理完成!")
    print(f"共扫描并处理了 {file_count} 个代码文件。")
    print("生成的文件列表:")
    for f in generated_files:
        print(f"  -> {f}")

def read_file_content(filepath):
    """尝试用不同的编码读取文件"""
    encodings = ['utf-8', 'gbk', 'utf-16', 'latin-1']
    for enc in encodings:
        try:
            with open(filepath, 'r', encoding=enc) as f:
                return f.read()
        except Exception:
            continue
    print(f"  [!] 警告: 无法读取文件 (编码未知): {filepath}")
    return None

if __name__ == "__main__":
    # ================= 配置区域 =================
    
    # 设置你要扫描的代码根目录 ('.' 代表当前目录)
    TARGET_DIRECTORY = r"D:\work_study" 
    
    # ===========================================
    
    merge_code_files(TARGET_DIRECTORY)