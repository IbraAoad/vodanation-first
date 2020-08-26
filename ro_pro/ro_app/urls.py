from django.urls import path
from ro_app import views

urlpatterns = [
    path('search/', views.SearchView.as_view(), name= 'search'),
    path('detail/<int:pk>/',views.SiteDetailView.as_view(),name='detail'),
    path('main/', views.modalview, name= 'main'),
    path('remove/<int:pk>/',views.site_remove, name= 'site_remove'),
    path('edit/<int:pk>/', views.modalview, name= 'site_edit'),
    path('auto/', views.autocomplete, name='autocomplete'),

]
