from django.urls import path
from ro_app import views

urlpatterns = [
    path('search/', views.civil_view, name= 'search'),
    path('detail/<int:pk>/',views.civil_view,name='detail'),
    path('add/', views.civil_view, name= 'add'),
    path('remove/<int:pk>/',views.civil_view, name= 'site_remove'),
    path('edit/<int:pk>/', views.civil_view, name= 'site_edit'),
    # path('auto/', views.autocomplete, name='autocomplete'),
    
]
 