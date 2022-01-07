from django.shortcuts import render
from django.http import HttpResponse

# from product.forms import ProductForm, RawProductForm

# Create your views here.

def home_view(request):
    # print(request.user)
    return render(request, 'home.html')

def about_view(request):
    context = {
        "my_list":"this is some of my list",
        "my_number":12345,
        "some_list":['this is goood', 123, 456, 999, 'listone', 'list2', 'list3'],
    }
    return render(request, 'about.html', context)


def contact_view(request):
    # print(request.user)
    return render(request, 'contact.html')


# def edit_product(request):
#     # getting the initial value
#     initial_data  = {
#         'description': 'put in your description here'
#     } 
#     form = RawProductForm(request.POST or None)
#     context = {
#         'form':form
#     }
    
#     return render(request, 'product/product_create.html', context, initial=initial_data)
    
