def prime(n):#prime number

    if n==1:
        print(n,' is not a prime number')
    elif n>1:
        for i in range(2,n):
            if(n%i)==0:
                print(n,' is not a prime number')
                print(i,'times',n//i,'is',n)
                break
            else:
                print(n,' is  a prime number')

n=int(input('enter the number :'))
num=prime(n)
