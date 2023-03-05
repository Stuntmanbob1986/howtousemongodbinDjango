from django.urls import path
from . import views
from .views import getBinanceData

urlpatterns = [
    # path('', views.index, name='index'), # ignore after creating class based view
    path('', getBinanceData.as_view()),
]