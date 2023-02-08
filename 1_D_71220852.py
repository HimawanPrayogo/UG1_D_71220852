print("============ KASIR ============")

a=int(input("Harga barang:"))
b=input("Apakah anda membeli barang lagi? [yes/no] :")

while True:
    if b=="yes":
        a1=int(input("Harga barang:"))
        b=input("Apakah anda membeli barang lagi? [yes/no] :")
        c=a+a1
    elif b=="no":
        print("TOTAL BELANJA:",c)
        break
    else:
        print("INVALID")
        break
