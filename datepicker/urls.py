from django.urls import path

from . import views
from .views import PromiseCreateView

app_name = 'datepicker'

urlpatterns = [
    # path('home/', views.home, name='home'),
    path('', PromiseCreateView.as_view()),  # class based view!
    # path('delete', views.delete, name='delete')
    path(r'^delete/(?P<id>[0-9]+)/$', views.delete, name='delete')
]
