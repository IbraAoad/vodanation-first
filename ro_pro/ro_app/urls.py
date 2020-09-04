from django.urls import path
from ro_app import views

urlpatterns = [
    path('search/', views.civil_fn, name= 'search'),
    path('detail/<int:pk>/',views.civil_fn,name='detail'),
    path('add/', views.civil_fn, name= 'add'),
    path('remove/<int:pk>/',views.civil_fn, name= 'site_remove'),
    path('edit/<int:pk>/', views.civil_fn, name= 'site_edit'),
    # path('auto/', views.autocomplete, name='autocomplete'),
    
]
 