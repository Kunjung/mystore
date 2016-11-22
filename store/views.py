from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
	context = {
		'categories': Category.objects.all()
	}
	return render(request, 'store/index.html', context)

def product(request, id):
	context = {
		'product': Product.objects.get(id=id)
	}
	return render(request, 'store/product.html', context)

def search(request):
	search_item = request.GET.get('q')

	products = Product.objects.filter(name__contains=search_item)

	
	return render(request, 'store/search.html', { 'products': products })



def contact(request):
	return render(request, 'store/contact.html')