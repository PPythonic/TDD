from django.shortcuts import render, redirect
from lists.models import Item

# Create your views here.


def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)   # .objects.create 是创建新Item对象的简化方式，无需再调用.save()方法
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
