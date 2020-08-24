from django.forms import ModelForm
from ro_app.models import SiteData
from django import forms
from datetime import datetime


class SiteForm(ModelForm):

    in_progress_date = forms.CharField(widget = forms.HiddenInput(), required = False)
    done_date = forms.CharField(widget = forms.HiddenInput(), required = False)
    staff_id = forms.CharField(widget = forms.HiddenInput(), required = False)
    area = forms.CharField(widget = forms.HiddenInput(), required = False)
    rt_gf = forms.CharField(widget = forms.HiddenInput(), required = False)
    str_type = forms.CharField(widget = forms.HiddenInput(), required = False)
    height = forms.CharField(widget = forms.HiddenInput(), required = False)
    email_address = forms.CharField(widget = forms.HiddenInput(), required = False)


    class Meta:
        model = SiteData
        fields = '__all__'
        widgets = {
            'request_date': forms.DateInput(attrs={'type': 'date'}),
            'last_visit': forms.DateInput(attrs={'type': 'date'}),
            'feedback': forms.DateInput(attrs={'type': 'date'}),
        }



