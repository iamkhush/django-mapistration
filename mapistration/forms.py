from django import forms
from models import Place


class LocationForm(forms.ModelForm):
    class Meta:
        model = Place

    place = forms.CharField(widget=forms.TextInput(attrs={
                                'class': 'searchTextField'}))
    city = forms.CharField(widget=forms.HiddenInput(attrs={
                    'name': 'city'}), required=False)
    state = forms.CharField(widget=forms.HiddenInput(attrs={
                    'name': 'state'}), required=False)
    country = forms.CharField(widget=forms.HiddenInput(attrs={
                    'name': 'country'}), required=False)
    latitude = forms.CharField(widget=forms.HiddenInput(attrs={
                    'name': 'latitude'}), required=False)
    longitude = forms.CharField(widget=forms.HiddenInput(attrs={
                    'name': 'longitude'}), required=False)
