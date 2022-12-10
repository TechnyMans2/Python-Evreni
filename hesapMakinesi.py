#@ttechnymans / 4 işlemli bir hesap makinesi yaptık. :)

def topla(sayi1,sayi2):
    return sayi1 + sayi2
def çıkar(sayi1,sayi2):
    return sayi1 - sayi2
def çarp(sayi1,sayi2):
    return sayi1 * sayi2
def böl(sayi1,sayi2):
    return sayi1 / sayi2

print("operosyan giriniz?")
print("1 : toplam")
print("2 : çıkar")
print("3 : çarp")
print("4 : böl")

seçenek = input("operasyon giriniz?")

sayi1 = int(input("sayi1 giriniz? "))
sayi2 = int(input("sayi2 giriniz? "))

if seçenek == '1':
    print("toplam : " + str(topla(sayi1,sayi2)))
elif seçenek == '2':
    print("çıkar : " + str(çıkar(sayi1,sayi2)))
elif seçenek == '3':
    print("çarp : " + str(çarp(sayi1,sayi2)))
elif seçenek == '4':
    print("böl : " + str(böl(sayi1,sayi2)))
else :
    print("geçersiz operasyon!")






    