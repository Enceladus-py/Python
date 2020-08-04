x=0
while x==0:
  a=int(input("hangi sayinin carpim tablosu olsun? "))
  d=int(input("kaca kadar carpilsin? "))
  liste1=range(1,d+1)
  for b in liste1:
     c=b*a
     print(a,"x",b,"=",c)
  x=int(input("baska istiyorsan 0'a bas. "))
else:
  print("program bitti.")
  y=input()

