from django.shortcuts import redirect, render
from lists.models import Item

def home_page(request):
    return render(request, 'home.html')

def list_baru(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/satu-satunya-list-di-dunia/')

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})
