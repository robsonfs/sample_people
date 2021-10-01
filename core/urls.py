from django.urls import path

from .views import people_list


urlpatterns = [
    path('list/', people_list),
]
