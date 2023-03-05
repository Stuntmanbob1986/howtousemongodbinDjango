from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import binanceData
from .forms import PromiseForm

from django.http import HttpResponse


class getBinanceData(CreateView):
    model = binanceData
    form_class = PromiseForm
    template_name = 'todoList/showbinancedata.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})


# def index(response):
#     return render(response, "todoList/showbinancedata.html", {})