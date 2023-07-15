# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    x, k = map(int, input().strip().split())
    string = input().strip()
    
    if eval(string) == k:
        print(True)
    else:
        print(False)
