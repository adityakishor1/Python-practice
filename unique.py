def find_unique(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

arr = [2, 3, 5, 4, 5, 6]
a= find_unique(arr)
print("unique number",a)
