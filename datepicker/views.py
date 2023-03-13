from django.http import HttpResponse, HttpResponseRedirect
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


class PromiseCreateView(CreateView):
    model = Promise
    form_class = PromiseForm
    # the cg part
    # template_name = '_promise_form.html'
    template_name = 'todoList/datepicker.html'
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
            print('form.cleaned_data: ', form.cleaned_data)
            print('form: ', form)
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
    # print(f'id: {id}, type(id): {type(id)}')
    # print(f'ObjectId(id): {ObjectId(id)}')
    entries.delete_one({"_id": ObjectId(id)})

    # return render(request, '_promise_form.html', {'form': form, 'entries': all_entries})
    return redirect('/datepicker')

'''
def edit(request, id=None):
    template_name = 'todoList/datepicker.html'
    form_class = PromiseForm
    if id:
        entry = get_object_or_404(Promise, pk=ObjectId(id))
        print('id in if: ', id)
    print(id)
'''

def detail_view(request, id):
    template_name = 'datepicker/detail_view.html'
    model = Promise
    form = PromiseForm
    entry = entries.find_one({"_id": ObjectId(id)})
    print(entry)

    return render(request, template_name, {'entry': entry})


def edit_view(request, id):
    template_name = 'datepicker/edit_view.html'
    entry = entries.find_one({"_id": ObjectId(id)})
    form = PromiseForm(request.POST or None)
    print('form: ', form.changed_data)

    if form.is_valid():
        form.save()
        entries.find_one_and_update({"_id": ObjectId(id)}, {"$set": {"title": form.cleaned_data['title'],
                                                                     'description': form.cleaned_data['description'],
                                                                     'made_on': datetime.combine(form.cleaned_data['made_on'], datetime.min.time())}}, upsert=False)
        # return HttpResponseRedirect("datepicker/")
        return redirect('/datepicker')

    return render(request, template_name, {'form': form, 'entry': entry})


# def home(response):
#     return render(response, "main/home.html", {})
