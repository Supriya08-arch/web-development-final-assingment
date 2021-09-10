from django.urls import path, include

urlpatterns = [
    path('instant_food/', include('instant_food.urls')),
    path('admins/', include('admins.urls')),
    path('', include('accounts.urls'))
]

