from django.http import HttpResponse
from django.shortcuts import render
from .models import product
from .forms import ProductForm

# Create your views here.
def home_view(request, *args, **kwargs):
    my_context={
        "my_text": "home a place where I can go",
        "my_number": 123,
        "my_list": [234, 5665, 345],
    }
    return render(request, "home.html", my_context)

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def product_detail_view(request):
    obj = product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    #     'price': obj.price,
    #     'summary': obj.summary,
    # }
    context = {
        'object': obj,
    }
    
    return render(request, "products/product_detail.html", context)

# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#     obj = product.objects.get(id=1)

#     context = {
#         'form': form,
#     }
    
#     return render(request, "products/product_create.html", context)

def product_create_view(request):
    context = {}
    return render(request, "products/product_create.html", context)