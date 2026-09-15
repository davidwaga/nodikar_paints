from django import forms
from .models import QuoteRequest

class QuoteRequestForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = ["name", "phone", "email", "product", "quantity", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Your name"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "+256 7XX XXX XXX"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email address"}),
            "product": forms.Select(attrs={"class": "form-select"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control", "min": 1}),
            "message": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Tell us what you need..."}),
        }
