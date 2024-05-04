from django.shortcuts import render, redirect

from phones.models import Phone

SORT_FIELDS = {
    'name': 'name',
    'min_price': 'price',
    'max_price': '-price'
}

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    sort_field = SORT_FIELDS.get(sort)
    if sort_field:
        phones = Phone.objects.all().order_by(sort_field)
    else:
        phones = Phone.objects.all()
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
