from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import MasterList
from .forms import AddItemForm
# Create your views here.
def index(request):
    return render(request, 'index.html')

def list(request):
	dolist = MasterList.objects.filter(category='TODO')
	dllist = MasterList.objects.filter(category='TODL')
	buylist = MasterList.objects.filter(category='TBUY')
	context = {"dolist" : dolist, "dllist" : dllist, "buylist" : buylist,}
	return render(request, 'list.html', context)

def add(request):
	if request.method == 'POST':
		form=AddItemForm(request.POST)
		if form.is_valid():
			MasterList.name = form.cleaned_data['name']
			MasterList.url = form.cleaned_data['url']
			MasterList.category = form.cleaned_data['choice']

			w = MasterList(name=MasterList.name,url=MasterList.url,category=MasterList.category)
			w.save()
			return HttpResponseRedirect('list')
	else:
		form = AddItemForm()
	return render(request, 'add.html', {'form': form})