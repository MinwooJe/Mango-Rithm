a, b = map(int, input().split())

c = b - 45

if c < 0 and a == 0 : 
    print(23, 60+c)
elif c < 0 :    
    print(a-1, 60+c)
else :
    print(a, c)