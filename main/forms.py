from django import forms
class Product_Create_Form(forms.Form):
    name=forms.CharField()
    price=forms.IntegerField()
    description=forms.CharField()

    def clean_price(self):
        price=self.cleaned_data['price']
        if price<0:
            raise forms.ValidationError("Invalid Input")
        return price

