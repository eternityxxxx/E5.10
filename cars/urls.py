from django.urls import path

from .views import CarListView, CarSearchView, home


urlpatterns = [
    path('', CarListView.as_view(), name='car_list'),
    path('home/', home),
    path('search/', CarSearchView.as_view(), name='car_search'),
]

