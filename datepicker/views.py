from django.http import HttpResponse
from django.shortcuts import render
from .models import Promise
from .forms import PromiseForm
from django.views.generic.edit import CreateView


# def index(request):
#     return HttpResponse("datepicker")


class PromiseCreateView(CreateView):
    model = Promise
    form_class = PromiseForm
    # the cg part
    template_name = 'promise_form.html'
    def get(self, request):
        # return HttpResponse('result')
        form = self.form_class()

        return render(request, self.template_name, {'form': form})

    # def post(self, request):
        # form = PromiseForm()
        # return HttpResponse('result')


