from django.urls import path

from owner.views import create_brand,show_brand,update_brand,create_product,list_products,edit_item,delete_product,product_details
urlpatterns=[
    path("brands",create_brand),
    path("brands/<int:id>",show_brand,name="show"),
    path("brands/edit/<int:id>",update_brand,name="update"),
    path("products",create_product,name="create_product"),
    path("items",list_products,name="fetchitems"),
    path("changeproduct/<int:id>",edit_item,name="change"),
    path("remove/<int:id>",delete_product,name="delete"),
    path("show/<int:id>",product_details,name="productdetails")



]