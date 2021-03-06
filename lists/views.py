from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError

from lists.models import Item, List
from lists.forms import FormItem


def home_page(request):
    # Mengoper objek `FormItem` ke template sebagai context, dengan key 'form'.
    # Hmm... mirip context di Odoo?
    return render(request, 'home.html', {'form': FormItem()})

def list_baru(request):
    list_ = List.objects.create()
    item = Item.objects.create(text=request.POST['item_text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = 'Kamu gak boleh bikin item list kosong'
        return render(request, 'home.html', {'error': error})
    return redirect(list_)

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    error = None
    
    if request.method == 'POST':
        try:
            item = Item(text=request.POST['item_text'], list=list_)
            item.full_clean()
            item.save()
            return redirect(list_)
        except:
            error = 'Kamu gak boleh bikin item list kosong'
    
    return render(request, 'list.html', {'list': list_, 'error': error})
