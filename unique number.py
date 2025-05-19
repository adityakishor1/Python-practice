def find_unique(arr):
    result=0
    for num in arr:
        result ^= num
    return result

arr= [1,4,3,5,2,3,5,1,4]
a= find_unique(arr)
print("unique number",a)
