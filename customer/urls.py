from django.urls import path
from customer.views import registration,login_view,log_out,index,user_home,item_details,add_to_cart,my_cart,delete_product_cart,place_order,my_orders,cancel_order

urlpatterns=[
    path("index",index,name="index"),
    path("account",registration,name="registration"),
    path("login",login_view,name="signin"),
    path("signout",log_out,name="signout"),
    path("home",user_home,name="user_home"),
    path("item_details/<int:id>",item_details,name="item_details"),
    path("add_to_cart/<int:id>",add_to_cart,name="addtocart"),
    path("carts",my_cart,name="carts"),
    path("remove_cart/<int:id>",delete_product_cart,name="removecart"),
    path("placeorder/<int:id>/<int:cid>",place_order,name="placeorder"),
    path("myorder",my_orders,name="myorder"),
    path("cancel-order/<int:id>",cancel_order,name="cancel_order"),

]