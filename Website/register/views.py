from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from .models import Users
from django.core.urlresolvers import reverse
from django.views import generic
from .forms import NameForm
from django.utils import timezone

class IndexView(generic.ListView):
    template_name='register/index.html'
    context_object_name='NameList'
    
    def get_queryset(self):
        return Users.objects.order_by('rollno')[:5]


# Create your views here.
class DetailView(generic.DetailView):
    model=Users
    template_name='register/detail.html'
    
global context
def thanks(request):
    #u=Users(name="hello",rollno=31312,date=timezone.now())
    #u.save()
    return render(request,'register/thanks.html')

def new(request):
    if request.method=="post":
        form=NameForm(request.POST)
        if form.is_valid():
            n=form.cleaned_data['your_name']
            r=form.cleaned_data['your_roll']
            d=timezone.now()
            print "Here"
            ctx={}
            ctx['result'] =request.POST.get('your_name')
            return render(request,'register/thanks.html',ctx)
    else:
        print "I am here "
        form=NameForm()
    return render(request,'register/new.html',{'form':form})