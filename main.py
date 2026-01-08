# 1
sonlar = []
for i in range(5):
    son = int(input("Son kirit: "))
    sonlar.append(son)

print(sonlar)

# 2
sonlar = [1, 2, 3, 4, 5]

yigindi = 0
for i in sonlar:
    yigindi += i
    print(yigindi)

# 3
a = [2, 6, 1, 3, 8, 0, 4]
print(max(a))
print(min(a))

# 4
a = [1, 2, 3, 4, 5]
print(a[::-1])

# 5
a = [0, 1, 2, 3, 4, 5, 6]
print(a[0:7:2])

# 6
a = [1, 2, 3, 4, 5, 6, 7, 8]
print(a[0:8:2])

# 7
a = [1, 2, 3, 4, 5]
yangi = []

for i in a:
    yangi.append(i * 2)

print(yangi)

# 8
a = [4, 81, 9, 2, 7, 0, 13, 61, 41, 8]
print(a.count(1))

# 9
a = [1, 2]
b = [3, 4]
c = a + b

print(c, end=" ")

# 10
a = [3, 1, 2]
a.sort()

print(a.sort())
