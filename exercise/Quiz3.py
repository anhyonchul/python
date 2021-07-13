#1번

a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a :print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

print()

#2번

result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1

print(result)
print()

#3번

i = 0
while True:
    i += 1
    if i > 5:
        break
    print(i * "*")

print()

#3-1 이중포문으로

for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end="")
    print()
        
print()

#4번

for i in range(1, 101):
    print(i, end=" ")

print()
print()

#5번

a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in a:
    total += score
avg = total / len(a)
print(avg)

print()

#6번

number = [1,2,3,4,5]
result = [n*2 for n in number if n%2==1]
print(result)


