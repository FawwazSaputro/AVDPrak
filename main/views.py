from django.shortcuts import render
from .machine_learning import proses

# Create your views here.
def home(request):
    if request.method == 'POST':
        kebersihan = request.POST.get('kebersihan')
        sampah = request.POST.get('sampah')
        kebersihanSP = request.POST.get('kebersihanSP')
        luas = request.POST.get('luas')
        jumlahKursi = request.POST.get('jumlahKursi')
        kebisinganKursi = request.POST.get('kebisinganKursi')
        kenyamananKursi = request.POST.get('kenyamananKursi')
        alatElektronik = request.POST.get('alatElektronik')
        AC = request.POST.get('AC')
        kondisiSP = request.POST.get('kondisiSP')
# Kebersihan,Sampah,Kebersihan_SP,Luas,Kenyamanan_Kursi,Kebisingan_Kursi,Jumlah_Kursi,Alat_Elektronik,AC,Kondisi_SP
        input = []
        input2 = []

        input2.append(int(kebersihan))
        input2.append(int(sampah))
        input2.append(int(kebersihanSP))
        input2.append(int(luas))
        input2.append(int(kenyamananKursi))
        input2.append(int(kebisinganKursi))
        input2.append(int(jumlahKursi))
        input2.append(int(alatElektronik))
        input2.append(int(AC))
        input2.append(int(kondisiSP))
        input.append(input2)

        result = proses(input)
        context = {"result":result}
        return render(request,"output.html",context)
    
    else:
        return render(request,"index.html")

    #     input = {
    #         "kebersihan":kebersihan,
    #         "sampah":sampah,
    #         'kebersihanSP' :kebersihanSP,
    #         'luas' :luas,
    #         'jumlahKursi' :jumlahKursi,
    #         'kebisinganKursi' :kebisinganKursi,
    #         'kenyamananKursi' :kenyamananKursi,
    #         'alatElektronik' :alatElektronik,
    #         'AC' :AC,
    #         'kondisiSP' :kondisiSP,
    #     }
    #     result = process(input)
    #     context = {"result":result}
    #     return render(request,"output.html",context)
    # elif request.method == 'GET':
    #     return render(request,'index.html')