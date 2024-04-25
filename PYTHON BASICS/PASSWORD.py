password='abc123'#password attempts
count=3
while 0<count<=4 :
    x= input('Enter password:')
    if (x==password):
        print('Access granted')
        break
    else:
        count-=1
        print('you have enter the wrong password. ',count,' attempts left')
        if(count==0):
            print('system has been blocked')