from collections import Counter
s= "fitaacademy"
freq= Counter(s)
Sorted_chars= sorted(freq.items(), key= lambda x:(-x[1], x[0]))
result = "".join(char * Count for char, Count in Sorted_chars)
print(result)
