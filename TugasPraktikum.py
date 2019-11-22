nama1=[]
nim1=[]
nilaitugas1=[]
nilaiuts1=[]
nilaiuas1=[]
akhir1=[]
jawab = 'ya'
while jawab =='ya':
    nama = input("Nama  : ")
    kelas = input("NIM  : ")
    nilaitugas = int(input("Nilai Tugas    :"))
    nilaiuts = int(input("Nilai UTS :"))
    nilaiuas = int(input("Nilai UAS :"))
    akhir = (nilaitugas)*30/100 + (nilaiuts)*35/100 + (nilaiuas)*35/100
    
    nama1.append(nama)
    nim1.append(kelas)
    nilaitugas1.append(nilaitugas)
    nilaiuts1.append(nilaiuts)
    nilaiuas1.append(nilaiuas)
    akhir1.append(akhir)
    
    jawab = (input('tambah data?(ya/tidak)'))
    if jawab == 'tidak':
    
        print("==========================================================================");
        print("| No |  Nama   |    NIM    | Tugas | UTS | UAS | Akhir |");
        print("==========================================================================");
        for i in range(len(nama1)):
            print("|", i+1 ,"|",  nama1[i]  ,"  |",  nim1[i]  ,"|",  nilaitugas1[i]  ,"|",  nilaiuts1[i]  ,"|",  nilaiuas1[i]  ,"|",  akhir1[i],"|")
        print("CREATE BY : BILLY FAROSA")
