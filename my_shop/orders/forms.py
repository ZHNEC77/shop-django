from django import forms

from orders.models import Order


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Иван'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Парамонов'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
                             'class': 'form-control', 'placeholder': 'berezkintiviigrival26letshkoly@mail.ru'}))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Россия, Ростов-на-Дону, ул.Народного ополчения, дом 7',
    }))

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'address')
