from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm
from .models import WishList, Product


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {"title": "WishList| About Project"})


def list_page(request, pk):
    """
    FBV - views основаны на функциях
    CBV - views на классах
    :param pk:
    :param request:
    :return:
    """
    wishlist = get_object_or_404(WishList, pk=pk)
    form = ProductForm

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            wishlist.product.add(Product.objects.last())
            return redirect('wish_list_page', wishlist.pk)

    context = {
        'wishlist': wishlist,
        'is_owner_list': wishlist.owner == request.user,
        'form': form
    }
    return render(request, 'wish_list.html', context)
