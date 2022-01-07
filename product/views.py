from django.shortcuts import redirect, render, get_object_or_404
from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.


#pure django form
# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == 'POST':
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#     context = {
#         'form':my_form
#     }
#     return render (request, 'product/product_create.html', context)


#raw html form
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form':form
    }
    
    return render(request, 'product/product_create.html', context)


# working with forms( create view)
# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()

#     context = {
#         'form':form
#     }
    
#     return render(request, 'product/product_create.html', context)



def product_detail_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
        'object':obj
    }
    
    return render(request, 'product/product_detail.html', context)


def product_update_view(request, id=id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid:
        form.save()
    return render (request, 'product/product_create.html')


def product_list_view(request):
    list = Product.objects.all()
    context = {
        'my_list':list
    }
    return render(request,'product/product_list.html', context)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('listview')
    context = {
        'object':obj
    }
    return render(request, 'product/product_delete.html')
        