from django.urls import path

# from . import views
from .views import PromiseCreateView

urlpatterns = [
    # path('', views.index, name='index')
    path('', PromiseCreateView.as_view()),  # class based view!
]
