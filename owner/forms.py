from django import forms
from django.forms import ModelForm
from .models import Product
from django import forms


class CreateBrandForm(forms.Form):
    brand_name = forms.CharField()


class ProductCreateForm(ModelForm):
    class Meta:
        model=Product
        fields="__all__"
        widgets={
                "mobile_name":forms.TextInput(attrs={"class":"form-control p-2"}),
                "spec":forms.Textarea(attrs={"class":"form-control p-2"})
        }

    def clean(self):
        cleaned_data=super().clean()
        price=cleaned_data.get("price")
        if price<500:
            msg="invalid price"
            self.add_error("price",msg)


