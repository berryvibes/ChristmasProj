from django.contrib import admin
from.models import Product 



admin.site.site_header = "ChirstmasApp Admin"
admin.site.site_title = "ChirstmasApp Admin Portal"
admin.site.index_title = "Welcome to ChirstmasApp Administration"


def mark_as_out_of_stock(modeladmin, request, queryset):
    queryset.update(stock=0)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', "price", 'description', 'stock')
    list_editable = ('price', 'stock')
    list_per_page = 5 # show 30 items per page
    search_fields = ('name', 'description') #making name and description searchable
    actions = [mark_as_out_of_stock]

# Register your models here.
admin.site.register(Product, ProductAdmin)
