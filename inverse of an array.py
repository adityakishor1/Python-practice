def inverse_array(arr):
    n = len(arr)
    inv = [0] * n
    for i in range(n):
        inv[arr[i]] = i
    return inv

arr = [2, 0, 1]
inv = inverse_array(arr)
print("Inverse array:", inv)
