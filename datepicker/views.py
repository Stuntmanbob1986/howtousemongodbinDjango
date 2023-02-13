from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
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
        all_entries = entries.find()

        return render(request, self.template_name, {'form': form, 'entries': all_entries})

    def post(self, request):
        form = self.form_class(request.POST)
        all_entries = entries.find()
        if form.is_valid():
            form.save()
            # print(type(form.cleaned_data['made_on']))
            # print('form.cleaned_data: ', form.cleaned_data)
            # entries.insert_one(form.cleaned_data)
            # will not work, because mongodb don't accept datetime.date objects
            entries.insert_one({
                'title': form.cleaned_data['title'],
                'description': form.cleaned_data['description'],
                'made_on': datetime.combine(form.cleaned_data['made_on'], datetime.min.time())
            })
            form = self.form_class()

            return render(request, self.template_name, {'form': form, 'entries': all_entries, 'successful_submit': True})
        else:
            return render(request, self.template_name, {'form': form, 'entries': all_entries})

        # form = PromiseForm()
        # return HttpResponse('result')


def delete(request, id):
    print(id)
    entry = get_object_or_404(Promise, id=id)
    print(entry)

    if request.method == 'POST':
        entry.delete()
        return redirect('/')

    return render(request, 'promise_form.html', {'entry': entry})
