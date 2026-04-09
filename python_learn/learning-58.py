files = ["a.py", "b.txt", "c.py", "d.pdf"]
python_files = [f for f in files if f.split(".")[-1]=="py"]
print(python_files)  # ['a.py', 'c.py']