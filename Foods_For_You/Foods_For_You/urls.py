from django.urls import path, include

urlpatterns = [
    path('instant_food/', include('meals.urls')),
    path('admins/', include('admins.urls')),
    path('', include('accounts.urls'))
]

