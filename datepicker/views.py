from django.http import HttpResponse
from django.shortcuts import render
from .models import Promise
from .forms import PromiseForm
from django.views.generic.edit import CreateView
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime

client = MongoClient('localhost', 27017)
db = client.django_db
entries = db.entries


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

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            # print('form: ', form)
            print(type(form.cleaned_data['made_on']))
            print('form.cleaned_data: ', form.cleaned_data)
            # entries.insert_one(form.cleaned_data)
            # will not work, because mongodb don't accept datetime.date objects
            entries.insert_one({
                'title': form.cleaned_data['title'],
                'description': form.cleaned_data['description'],
                'made_on': datetime.combine(form.cleaned_data['made_on'], datetime.min.time())
            })
            return HttpResponse('result')

        # form = PromiseForm()
        # return HttpResponse('result')


