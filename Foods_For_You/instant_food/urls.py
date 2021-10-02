from django.urls import path
from . import views

urlpatterns = [
    path('homepage', views.homepage),
    path('catagoery_form', views.catagoery_form),
    path('get_catagoery', views.get_catagoery),
    path('delete_catagoery/<int:catagoery_id>', views.delete_catagoery),
    path('update_catagoery/<int:catagoery_id>', views.catagoery_update_form),

    path('meals_form', views.meals_form),
    path('get_meals', views.get_meals),
    path('delete_meals/<int:meals_id>', views.delete_meals),
    path('update_meals/<int:meals_id>', views.meals_update_form),

    path('get_catagoery_user', views.show_categories),
    path('get_meals_user', views.show_meals),
    path('menu', views.menu),
    path('add_to_cart/<int:meals_id>',views.add_to_cart),
    path('mycart', views.show_cart_items),
    path('remove_cart_item/<int:cart_id>', views.remove_cart_item),
    path('order_form/<int:meals_id>/<int:cart_id>', views.order_form),
    path('my_order', views.my_order),
    path('esewa_verify', views.esewa_verify),


]

