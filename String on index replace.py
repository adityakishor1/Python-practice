s = "a,b,c,d,e"
indices= [2, 3, 0, 4, 1]
chars= s.split(",")
result = [None]*len(chars)
for i, idx in enumerate(indices):
    result[idx] = chars[i]

print(result)
