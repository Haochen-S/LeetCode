# edit LeetCode titles

str = input()
newStr = ""
i = 0
while (i < len(str)):
    if (str[i] == " "):
        newStr += "_"
    elif (str[i] != "."):
        newStr += str[i]
    i += 1
print()
print()
print(newStr + ".py")
print()
