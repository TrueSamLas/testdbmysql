from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import ModuleForm, PurchaseForm, SellForm, PercentForm
from .models import Register, Products, Percent
from django.db import connection
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


def index(request):
    records = None
    with connection.cursor() as cursor:
        cursor.execute("""SELECT p.title, p.descriprions, r.n_quantite, r.n_price FROM products as p
        join register as r on p.idproducts = r.product
        and r.ts = (select max(ts) from register where register.product = r.product)
        """)
        records = cursor.fetchall()
    records_dict = []
    for elem in records:
        records_dict.append({"title": elem[0],
                             "descriprions": elem[1],
                             "n_quantite": elem[2],
                             "n_price": elem[3]})
    print(records_dict)
    return render(request, 'myapp/index.html', {'title': 'Главная страница',
                                                'records': records_dict})


# def products(request):
#     data = Products.objects.order_by('idproducts')
#     return render(request, 'myapp/products.html', {'title': 'Товары',
#                                                    'records': data})


class ProductList(ListView):
    model = Products
    template_name = 'myapp/products.html'
    context_object_name = 'records'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Товары'
        return context

    def get_queryset(self):
        return Products.objects.order_by('title')


class CreateProduct(CreateView):
    model = Products
    template_name = 'myapp/createproduct.html'
    success_url = reverse_lazy('products')
    form_class = ModuleForm
    # fields = ['title', 'descriprions']
    extra_context = {
        'title': 'Добавление товара',
    }


class UpdateProduct(UpdateView):
    model = Products
    template_name = 'myapp/createproduct.html'
    success_url = reverse_lazy('products')
    form_class = ModuleForm
    extra_context = {
        'title': 'Редактирование товара',
    }


class DeleteProduct(DeleteView):
    model = Products
    success_url = reverse_lazy('products')


# Операции
class RegisterList(ListView):
    model = Register
    template_name = 'myapp/register.html'
    context_object_name = 'records'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Операции'
        return context

    def get_queryset(self):
        return Register.objects.order_by('-ts')


class CreateRegister(CreateView):
    model = Register
    template_name = 'myapp/purchase_form.html'
    success_url = reverse_lazy('register')
    form_class = PurchaseForm
    extra_context = {
        'title': 'Покупка товара',
    }


class CreateRegisterSell(CreateView):
    model = Register
    template_name = 'myapp/sell_form.html'
    success_url = reverse_lazy('register')
    form_class = SellForm
    extra_context = {
        'title': 'Продажа товара',
    }


class PercentList(ListView):
    model = Percent
    template_name = 'myapp/percents.html'
    context_object_name = 'records'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Проценты'
        return context

    def get_queryset(self):
        return Percent.objects.order_by('idpercent')


class CreatePercent(CreateView):
    model = Percent
    template_name = 'myapp/percent_form.html'
    success_url = reverse_lazy('percents')
    form_class = PercentForm
    extra_context = {
        'title': 'Добавление процента',
    }


def profit(request):
    profits = None
    with connection.cursor() as cursor:
        cursor.execute("""SELECT *, products.title from register join products ON register.product = products.idproducts
        JOIN profit ON  profit.idregister = register.idregister
        """)
        profits = cursor.fetchall()
    profits_dict = []
    for elem in profits:
        profits_dict.append({"ts": elem[0],
                             "quantite": elem[1],
                             "price": elem[2],
                             "total": elem[3],
                             "n_profit": elem[4],
                             "rate": elem[5]})
    print(profits_dict)
    return render(request, 'myapp/profits.html', {'title': 'Прибыль',
                                                'records': profits_dict})