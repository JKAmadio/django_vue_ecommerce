from django.shortcuts import get_object_or_404, get_list_or_404, render
from .models import Category, Product

# Create your views here.
def product_detail(request, slug_category, slug_product):
	category = get_object_or_404(Category, slug=slug_category)
	product = get_object_or_404(Product, slug=slug_product)
	context = {
		'product': product,
		'category': category
	}
	return render(request, 'product_detail.html', context)

def category(request, slug_category):
	category = get_object_or_404(Category, slug=slug_category)
	products_category = get_list_or_404(Product, category=category)
	context = {
		'category': category,
		'products_category': products_category
		}
	return render(request, 'category.html', context)
