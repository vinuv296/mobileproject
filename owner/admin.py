from django.contrib import admin
from owner.models import Brand,Product,Cart,Orders


# Register your models here.
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Orders)