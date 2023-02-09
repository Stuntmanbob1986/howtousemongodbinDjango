# howtousemongodbinDjango
DjangoTestArea, Datepicker, Forms, bokeh, write in MongoDB ...

Source Datepicker:
https://stackoverflow.com/questions/3367091/whats-the-cleanest-simplest-to-get-running-datepicker-in-django
with a few changes to make it work:
models.py added .model: class Promise(models.Model)
also added def __str__(self): return self.title (don't know if it was necessary to make it run)
views.py: 
added from .models import Promise
added from .forms import PromiseForm

After the editing:
Python manage.py makemigrations
Python manage.py migrate