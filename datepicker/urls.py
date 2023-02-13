from django.urls import path

from . import views
from .views import PromiseCreateView

app_name = 'datepicker'

urlpatterns = [
    # path('', views.index, name='index')
    path('', PromiseCreateView.as_view()),  # class based view!
    path(r'^delete/(?P<id>[0-9]+)/$', views.delete, name='delete')
]
