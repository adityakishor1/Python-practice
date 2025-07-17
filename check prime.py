def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

student_id = int(input("Enter student ID: "))

# Sum of digits
digit_sum = sum(int(d) for d in str(student_id))

# Check if sum is prime
if is_prime(digit_sum):
    k = 1
else:
    k = 0

print("k =", k)
