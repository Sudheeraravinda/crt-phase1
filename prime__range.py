def prime(n):
    for j in range(2, (n//2)+1):
        if n % j == 0:
            return False
    return True
        
n1 = int(input())
n2 = int(input())
for i in range(n1,n2+1):
    if prime(i):
        print(i , end = " ")
