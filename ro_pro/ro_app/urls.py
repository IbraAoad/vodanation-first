from django.urls import path
from ro_app import views

urlpatterns = [
    path('search/', views.SearchView.as_view(), name= 'search'),
    path('detail/<int:pk>/',views.SiteDetailView.as_view(),name='detail'),
    path('add/', views.add_view, name= 'add_record'),
    path('<int:pk>/remove/',views.site_remove, name= 'site_remove'),
    path('<int:pk>/edit/', views.update_view, name= 'site_edit'),
    path('', views.autocomplete, name='autocomplete'),

]
