def average(a=1,b=1):
    avg=(a+b)/2
    print(type(avg))
    return avg
#n=int(input("enter the input"))
c=average(9)
print(c)
def name(**names):
    print("name",names["fname"])
name(fname="hii")

def prime(n):
    count=0
    l=[]
    if(n<0):
        return 1
    else:
        for i in range(1,n+1):
            if(n%i==0):
                count=count+1
    if(count==2):
        print("this is prime")
    else: 
          print("not prime")
n=int(input("enter num"))
prime(n)



                   

