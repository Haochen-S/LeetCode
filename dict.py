

dict = {}

x = "x"
y = "y"

dict[x] = 1

dict[x] = dict.get(x, 0) + 1


print(dict)
print(dict[x])

print(dict.get(y))


