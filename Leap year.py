# python script to check leap year
x=int(input("Enter an year"))
result="leap year" if x%400==0 else "Leap year" if x%4==0 and x%100!=0 else "non leap year"
print(result)
