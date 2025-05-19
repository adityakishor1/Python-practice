n = int(input("Enter number of elements: "))

arr = []
print("Enter the elements:")
for _ in range(n):
    arr.append(int(input()))

print("Elements divisible by both 5 and 7:")
for num in arr:
    if num % 5 == 0 and num % 7 == 0:
        print(num, end=" ")
