from django.urls import path
from . import views
from .views import ShopView, ShopCreateView, ShopUpdateView, ShopDetailView, ShopDeleteView


urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('add/', ShopCreateView.as_view(), name='add_product'),
    path('product/<int:product_id>/update/', ShopUpdateView.as_view(), name='update_product'),

    path('about', views.about, name='about'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('underconstruction', views.underconstruction, name='underconstruction'),
    path('blog', views.blog, name='blog'),
    path('blogdetails', views.blogdetails, name='blogdetails'),
    # path('product/<int:pk>/', ShopDetailView.as_view(), name='product_details'),
    
    path('product/<int:pk>/', ShopDetailView.as_view(), name='shop_details'),
    path('product/<int:pk>/delete/', ShopDeleteView.as_view(), name='delete_product'),


    path('productdetails', views.productdetails, name='product_details'),
    path('contact', views.contact, name='contact'),

]