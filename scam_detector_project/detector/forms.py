from django import forms

class JobForm(forms.Form):
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Paste job description here...',
            'rows': 6,
            'style': 'background: rgba(255,255,255,0.8);'
        })
    )