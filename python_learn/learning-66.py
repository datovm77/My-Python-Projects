import re

text = "I have a cat and a dog"
print(re.findall(r"cat|dog", text))  # ['cat', 'dog']

# 配合分组使用
text = "image.jpg photo.png icon.gif document.pdf"
print(re.findall(r"\w+\.(?:jpg|png|gif)", text))