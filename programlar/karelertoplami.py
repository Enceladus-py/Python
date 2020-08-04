def f(n):
    a=0
    for i in range(1,n+1):
        a=a+i*i
    return a
x=int(input("1'den buyuk bir tam sayi girin. "))
if x>1:
    print(f(x))
    input()
else:
    print("1'den buyuk girmeliydin. ")
    input()
