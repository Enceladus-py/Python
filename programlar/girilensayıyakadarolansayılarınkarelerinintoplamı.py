b=True
def f(n):
    a=0
    for i in range(1,n+1):
        a=a+i*i
    return a

while b:
    x=int(input("1'den buyuk bir tam sayi girin. "))
    if x>1:
        print(f(x))
        b=False
        devam=int(input("devam mı?(1,0)"))
        if devam==1:
            b=True
    else:
        print("1'den buyuk girmeliydin. ")
        x=int(input("1'den buyuk bir tam sayi girin. "))


