from django.urls import path

from . import views
from .views import PromiseCreateView, detail_view, edit_view

app_name = 'datepicker'

urlpatterns = [
    # path('home/', views.home, name='home'),
    path('', PromiseCreateView.as_view()),  # class based view!
    # path('delete', views.delete, name='delete')
    path(r'^delete/(?P<id>[0-9]+)/$', views.delete, name='delete'),
    # path(r'^edit/(?P<id>[0-9]+)/$', views.edit, name='edit'),
    # path(r'^detail_view/(?P<id>[0-9]+)/$', views.detail_view, name='detail_view')
    # path(r'^detail_view/(?P<id>[0-9]+)/$', detail_view, name='detail_view'),
    path('<id>', detail_view, name='detail_view'),
    path('<id>/edit', edit_view, name='edit_view')
]
