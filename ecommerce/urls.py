from django.urls import path
from . import views

app_name = 'ecommerce'

urlpatterns = [
    path('', views.home, name='home-page'),
    path('cards/', views.cards_view, name='cards'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('logout-user/', views.logout_user, name='logout'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<int:id>/', views.remove_from_cart, name='remove-from-cart'),
    path('buy-product/<int:id>/', views.buy_product, name='buy-product'),
    path('purchased-products/', views.purchased_products, name='purchased-products'),
    path('buy-all-products/', views.buy_all_products, name='buy-all-products'),
    path('delete-purchased-product/<int:id>/', views.delete_purchased_product, name='delete-purchased-product'),
]
