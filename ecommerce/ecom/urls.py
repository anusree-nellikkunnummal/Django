from django.urls import path
from ecom import views

urlpatterns = [

    path('', views.home, name='home'),
    path('login', views.logs, name='login'),
    path('register', views.register, name='register'),
    path('single_item', views.single_item, name='single_item'),
    path('watch_list', views.watch_list, name='watch_list'),
    path('brand_view', views.brand_view, name='brand_view'),
    path('category_view', views.category_view, name='category_view'),
    path('service_view/<int:id>', views.service_view, name='service_view'),
    path('select_item/<int:id>', views.select_item, name='select_item'),
    path('faq', views.faq, name='faq'),
    path('cart', views.cart, name='cart'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('add_wishlist/<int:id>', views.add_wishlist, name='add_wishlist'),
    path('add_bag/<int:id>', views.add_bag, name='add_bag'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('popular_brand', views.popular_brand, name='popular_brand'),
    path('place_order', views.place_order, name='place_order'),

    
]