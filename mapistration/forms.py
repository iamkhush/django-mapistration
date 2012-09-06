from django import forms
from models import Place


class LocationForm(forms.ModelForm):
    class Meta:
        model = Place

    place = forms.CharField(widget=forms.TextInput(
                            attrs={'class': 'searchTextField'}))
    city = forms.CharField(widget=forms.HiddenInput(
                            attrs={'name': 'city'}))
    state = forms.CharField(widget=forms.HiddenInput(
                            attrs={'name': 'state'}))
    country = forms.CharField(widget=forms.HiddenInput(
                            attrs={'name': 'country'}))
    latitude = forms.CharField(widget=forms.HiddenInput(
                            attrs={'name': 'latitude'}))
    longitude = forms.CharField(widget=forms.HiddenInput(
                            attrs={'name': 'longitude'}))
