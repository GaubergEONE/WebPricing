from django.urls import path
from . import views

urlpatterns = [
    path('ya_disk/', views.get_ya_links),
    path('ya_links/', views.YalinksViewSet.as_view({'get': 'list'})),
    path('wardrobe-filters/', views.WardrobesFiltersViewSet.as_view({'get': 'list'})),
    path('wardrobe-prices/', views.WardrobesPricesViewSet.as_view({'get': 'list'})),
    path('wardrobes/', views.WardrobesViewSet.as_view({'get': 'list'})),
]