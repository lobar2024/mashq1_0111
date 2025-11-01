#1- misol
tupl = (1, 91, 0, 7, 5)
print(tupl)

sum = 0
for i in tupl:
    sum += i

print(f"Tuple yigindisi : {sum}")

#2-misol
t = ()
t = list(t)
for i in range(5):
    t.append(int(input(f"{i+1} - son kirit: ")))

t = tuple(t)
print(f"Eng kattasi : {max(t)}")

#2-misol ikkinchi usul
numbers = tuple(map(int, input("sonlar kirit: ").split()))
max_num = max(numbers)
print(f"Eng kattasi :{max_num}")

#3-misol
tup1 = (2, 7, 81, 4)
tup2 = (5, 9, 12, 10)
tup = tup1 + tup2
print(f"Birlashgan yangi tuple: {tup}")

#4-misol
tupll = (2, 30, 4, 73, 9)
juft = tuple(filter(lambda a: a % 2 == 0, tupll))
print(juft)

#5-misol
tuplee = (7, 12, 23, 3, 8, 9)
print(tuplee)

tuplee = tuplee[::-1]
print(tuplee)
