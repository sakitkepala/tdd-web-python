from django.shortcuts import render

def home_page(request):
    # Yang lama ini mereturn string html statis sebagai nilai langsung:
    # return HttpResponse('<html><title>To-Do lists</title></html>')

    # Yang baru ini mereturn nilai yang sama (string html), tapi dilakukan
    # secara dinamis. String html dibuat dari template dengan bantuan
    # method `render()`. HttpRequest sekarang tidak perlu diimport dan
    # dipanggil secara eksplisit karena sudah dihandle secara internal
    # oleh method render
    return render(request, 'home.html')
