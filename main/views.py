import json
from django.shortcuts import render
from django.http import JsonResponse
from .machine_learning import proses

# Create your views here.
    
def home(request):
    context = {}
    
    context['labels'] = {
        'kebersihan':"Menurut saya, kebersihan ruang kelas Departemen Matematika terjaga.",
        'sampah': "Menurut saya, tempat sampah telah tersedia di depan ruangan setiap ruang kelas Departemen Matematika dan sampah tidak pernah menumpuk.",
        'kebersihanSP': "Menurut saya, tempat sampah telah tersedia di depan ruangan setiap ruang kelas Departemen Matematika dan sampah tidak pernah menumpuk.",
        'luas': "Menurut saya, ruang kelas Departemen Matematika memiliki ukuran yang luas.",
        'kenyamananKursi': "Menurut saya, kursi di ruangan kelas sudah sesuai dengan ukuran (tidak terlalu tinggi dan tidak terlalu rendah).",
        'kebisinganKursi': "Menurut saya, kursi yang terdapat dalam ruang kelas Departemen Matematika saat ini seringkali membuat bising.",
        'jumlahKursi': "Menurut saya, jumlah kursi yang terdapat dalam ruang kelas Departemen Matematika cukup untuk digunakan dalam Kegiatan Belajar Mengajar.",
        'alatElektronik': "Menurut saya, alat-alat elektronik untuk membantu Kegiatan Belajar Mengajar seperti mikrofon dan LCD sudah lengkap.",
        'AC': "Menurut saya, jumlah AC pada ruangan sudah sesuai dengan kapasitas mahasiswa.",
        'kondisiSP': "Menurut saya, alat-alat ruangan seperti pintu, gorden, dan jendela semua berfungsi dengan baik dan tidak ada yang rusak.",
    }
    context['scales'] = {
        'Tidak Puas':1,
        'Kurang Puas':2,
        'Puas':3,
        'Sangat Puas':4
    }
    
    if request.method == "POST":
        
        kebersihan = request.POST.get('kebersihan')
        sampah = request.POST.get('sampah')
        kebersihanSP = request.POST.get('kebersihanSP')
        luas = request.POST.get('luas')
        jumlahKursi = request.POST.get('jumlahKursi')
        kebisinganKursi = request.POST.get('kebisinganKursi')
        kenyamananKursi = request.POST.get('kenyamananKursi')
        alatElektronik = request.POST.get('alatElektronik')
        ac = request.POST.get('AC')
        kondisiSP = request.POST.get('kondisiSP')

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
        input2.append(int(ac))
        input2.append(int(kondisiSP))
        input.append(input2)

        result = proses(input)
        context["result"] = result
        # dd(context)
        return render(request, "home.html", context)
        
    return render(request, 'home.html', context)