from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse_lazy,reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms,models


def home(request):
    data = []
    if request.user.is_authenticated:
        data = models.Url.objects.filter(user=request.user)
    
    if request.method == "POST" and request.user.is_authenticated:
        user_form = forms.UrlForm(data=request.POST)
        if user_form.is_valid():
            use = user_form.save(commit=False)
            use.user=request.user
            use.alias = use.alias.lower()
            use.save()
            return redirect(reverse_lazy('myapp:home'))
        
    else:
        user_form =forms.UrlForm()
    return render(request,'base.html',{
                                    'user_form':user_form,
                                    'data' : data,
    })
def url_redirect(request,alias):
    try:
        
        ob = models.Url.objects.get(alias__iexact=alias)
        ob.hit += 1
        ob.save()
        return redirect(ob.link)
    except:
        raise Http404

def aliasDelete(request,pk):
    try:
        models.Url.objects.get(pk=pk).delete()
    except:
        pass

    return redirect(reverse_lazy('myapp:home'))
def urlUpdate(request,pk):
    instance = models.Url.objects.get(pk=pk)
    form = forms.UrlFormUpdate(request.POST or None, instance=instance)
    if form.is_valid():
          form.save()          
          return redirect(reverse_lazy('myapp:home'))
        
    data = []
    if request.user.is_authenticated:
        data = models.Url.objects.filter(user=request.user)
    return render(request, 'update.html', {'user_form': form,
                                        'data':data,
                                        'ins' : instance.alias,
    }) 
