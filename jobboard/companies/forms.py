from django import forms
from companies.models import Complaint


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['reason']
        labels = {'reason':'Причина жалобы'}
        help_texts ={'reason':'Укажите, что именно нарушает данная вакансия.'}
        widgets = {'reason': forms.Textarea(attrs={
            'rows':4,
            'placeholder':'Опишите причину жалобы...',
            'class':'form-control'
        })}