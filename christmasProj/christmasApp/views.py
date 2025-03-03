from django.shortcuts import render
from django.contrib import messages  # Ensure this is correctly importe
from .forms import ProductForm
from .models import Product
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .forms import ProductForm
from user.decorators import seller_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator





# Create your views here.


def base(request):
    return render(request, 'christmasApp/base.html')


def index(request):
    return render(request, 'christmasApp/index.html')

# def shop(request):
#     products= Product.objects.all()
#     return render(request, 'christmasApp/shop.html', {'products': products})

class ShopView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'christmasApp/shop.html' # specify the template name
    context_object_name = 'products' # Name for accessing the proucts in the template


# add product
@method_decorator(seller_required, name='dispatch')
class ShopCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'christmasApp/add_product.html'
    success_url = reverse_lazy('shop')
    pk_url_kwarg = 'product_id' 

    def form_valid(self, form):
        form.instance.user = self.request.user  # Set the product's user to the current user
        return super().form_valid(form)


# Update product
@method_decorator(seller_required, name='dispatch')
class ShopUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'christmasApp/update_product.html'
    pk_url_kwarg = 'product_id' 

    def get_success_url(self):
        # Use reverse_lazy with the product_id passed
        return reverse_lazy('shop_details', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        messages.success(self.request, "Product updated successfully!")
        return super().form_valid(form)


# class ShopDetailView(DetailView):
#     model = Product
#     template_name = 'christmasApp/product_details.html'
#     context_object_name = 'product'

class ShopDetailView(DetailView):
    model = Product
    template_name = 'christmasApp/shop_details.html'  # Adjust to your template name
    context_object_name = 'product'  # This ensures `product` is available in the template


# delete view
class ShopDeleteView(DeleteView):
    model = Product
    template_name = 'christmasApp/delete.html'
    success_url = reverse_lazy('shop')  # or redirect to 'product_details' view

def about(request):
    return render(request, 'christmasApp/about.html')

def cart(request):
    return render(request, 'christmasApp/cart.html')

def checkout(request):
    return render(request, 'christmasApp/checkout.html')

def wishlist(request):
    return render(request, 'christmasApp/wishlist.html')

def underconstruction(request):
    return render(request, 'christmasApp/underconstruction.html')

def blog(request):
    return render(request, 'christmasApp/blog.html')

def blogdetails(request):
    return render(request, 'christmasApp/blogdetails.html')

def productdetails(request):
    return render(request, 'christmasApp/product_details.html')

def contact(request):
    return render(request, 'christmasApp/contact.html')