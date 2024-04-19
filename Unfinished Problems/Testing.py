
import string


x = []

y = [11,12]
x += [14, 15]


def convertToString(num):
    ansStr = ""
    numStr = str(num)
    for c in numStr:
        ansStr += string.ascii_lowercase[int(c)]
    return ansStr


words = [1,2,3,4,5]
for word in words:
    word = word * 10

print(words)