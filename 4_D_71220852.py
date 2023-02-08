
def nilai_total():
    print("--------Nilai Ke 1--------")
    a=int(input("Nilai Harian:"))
    b=int(input("Nilai UTS:"))
    c=int(input("Nilai UAS:"))

    print("--------Nilai Ke 2--------")
    a1=int(input("Nilai Harian:"))
    b1=int(input("Nilai UTS:"))
    c1=int(input("Nilai UAS:"))

    print("--------Total Nilai--------")
    #Tugas total 30%
    atotal=a+a1
    natotal=atotal/2
    natotal1=natotal*0.3

    #UTS total 30%
    btotal=b+b1
    nbtotal=btotal/2
    nbtotal1=nbtotal*0.3

    #UAS total 40%
    ctotal=c+c1
    nctotal=ctotal/2
    nctotal1=nctotal*0.4
    ntotal=natotal1+nbtotal1+nctotal1

    print("Total nilai yang didapat :",ntotal)

    for i in range(0,19):
        if ntotal==i:
            print("Total Nilai Dalam Huruf: E")
    for i in range(20,39):
        if ntotal==i:
            print("Total Nilai Dalam Huruf: D")
    for i in range(40,59):
        if ntotal==i:
            print("Total Nilai Dalam Huruf: C")
    for i in range(60,79):
        if ntotal==i:
            print("Total Nilai Dalam Huruf: B")
    for i in range(80,100):
        if ntotal==i:
            print("Total Nilai Dalam Huruf: A")

nilai_total()





        
    
