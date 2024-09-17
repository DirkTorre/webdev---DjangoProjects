from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.BookListView.as_view(), name="index"),
    path("api/", views.BookListAPIView.as_view(), name="api"),
]
