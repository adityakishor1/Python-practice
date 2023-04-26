def nextprime(n):
    while True:
        n+=1
        for i in range(2,n):
            if n%i==0:
                break
        else:
            return n 
print("[+]next prime number is:",nextprime(int(input("[+]Enter a number:"))))    
