from django import forms
from Fusion.models import *

class ExampleForm(forms.Form):
    first_answer = forms.CharField(label="Yodel", max_length=50)

class VendorRegistraionForm(forms.ModelForm):
    class Meta:
        model = VendorRegistraion
        fields = "__all__"

class SmallBusinessRegistraionForm(forms.ModelForm):
    class Meta:
        model = SmallBusinessRegistration
        fields = "__all__"
