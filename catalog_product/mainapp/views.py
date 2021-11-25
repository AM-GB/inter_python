from django.db import models
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404
from .models import Product, ProductCategory
from mainapp.forms import AdminProductCreateForm


class PageTitleMixin:
    page_title_key = 'page_title'
    page_title = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.page_title_key] = self.page_title
        return context


def index(request):
    all_products = Product.objects.all()
    context = {
        'page_title': 'Главная',
        'all_products': all_products,
    }
    return render(request, 'mainapp/index.html', context)


class ProductCreate(PageTitleMixin, CreateView):
    model = Product
    form_class = AdminProductCreateForm
    success_url = reverse_lazy('base:index')
    page_title = 'создание'


def category(request, pk):
    # category = get_object_or_404(ProductCategory, pk=pk)
    products = Product.objects.prefetch_related(
        'category').filter(category=pk)

    context = {
        'page_title': 'товары категории',
        # 'category': category,
        'all_products': products,
    }
    return render(request, 'mainapp/index.html', context)
