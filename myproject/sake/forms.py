from django import forms

from sake.models import SakeModel,SakeTypeModel,MakerModel


class SakeForm(forms.ModelForm):

    class Meta():
        model = SakeModel
        fields = {'name','image','maker',}


class SakeTypeForm(forms.ModelForm):
    class Meta():
        model = SakeTypeModel
        fields = {'sake', 'aroma', 'taste',}


class MakerForm(forms.ModelForm):
    class Meta():
        model = MakerModel
        fields = {'name', 'location',}