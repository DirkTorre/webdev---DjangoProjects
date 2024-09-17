from django.urls import path
from django_filters.views import FilterView

from . import views
from .filters import BookFilter, BookFilter2

app_name = 'filter'

urlpatterns = [
    path('search/', views.book_list, name='search'),
    path('classsearch/', FilterView.as_view(filterset_class=BookFilter2, template_name='filter/book_list_class.html'), name='classsearch'),


]