from django.shortcuts import get_list_or_404, render
from ..store.models import Product

# Create your views here.
def frontpage(request):
	products = get_list_or_404(Product)
	context = {'products': products}
	return render(request, 'frontpage.html', context)

def contact(request):
	return render(request, 'contact.html')