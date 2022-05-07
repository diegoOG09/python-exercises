from ast import While


input_string = input("Enter some data: ")

a = list(map(int, input_string.split(',')))

b = []
i = 0

while i < len(a):
  if a[i] == 2 or a[i] == 3:
    b.append(a[i])
    a[i] = 0
  else:
    i += 1

print("A =", a)
print(len(b))