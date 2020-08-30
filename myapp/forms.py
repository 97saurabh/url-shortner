from django import forms
from django.contrib.auth.models import User
from .models import Url


class UrlForm(forms.ModelForm):
    class Meta():
        model = Url
        fields = ('alias','link')
    alias = forms.CharField(required=False)    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['alias'].label = 'Alias ( its optional ) '
        self.fields['link'].label = "Url"
    def is_valid(self):
        
        valid = super(UrlForm, self).is_valid()
        if not valid:
            return valid
        al = self.cleaned_data['alias']
        if Url.objects.filter(alias__iexact=al).exists():
            self._errors['Alerady Taken By Someone'] = 'Preserve Words You can not Use it.'
            return False



        lst = ['myapp','admin']
        if self.cleaned_data['alias'] in lst:
            self._errors['Preserve Words You can not Use it.'] = 'Preserve Words You can not Use it.'
            return False
        
        return True

class UrlFormUpdate(forms.ModelForm):
    class Meta():
        model = Url
        fields = ('link',)