from django.contrib import admin
from site_electro.models import Product,Category,ContactInfo,Photo

admin.site.register(Category)
# admin.site.register(Product)
admin.site.register(ContactInfo)
admin.site.register(Photo)