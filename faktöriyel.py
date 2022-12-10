#@technymans / faktöriyel işlem 

sayi = int(input("sayi : " ))

faktoriyel = 1

if sayi<0:
    print("negatif sayılar hesaplanamaz")
elif sayi==0:
    print("sonuç 1")
else:
   for i in range(1,sayi+1):
       faktoriyel = faktoriyel * i
   print("sonuç : ",faktoriyel)         
       
    