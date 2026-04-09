###begin
s = input().strip()

punctuations = ".!?"
ending_punc = ""

if s[-1] in punctuations:
    ending_punc = s[-1]
    s = s[:-1]

words = s.split()
words.reverse()

result = " ".join(words)
print(result + ending_punc)

###end 