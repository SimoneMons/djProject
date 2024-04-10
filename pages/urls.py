from django.urls import path

from .views import home_page_view

urlpatterns = [
    path("/test", home_page_view, name="home"),
]