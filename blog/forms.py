from django import forms

class SortingForm(forms.Form):
    keyword = forms.CharField( max_length=100,required=False)
    country = forms.ChoiceField( choices=[
        (0,'None'),
        (1,'ASC'),
        (-1,'DESC')
    ],required=False)
    city = forms.ChoiceField( choices=[
        (0,'None'),
        (1,'ASC'),
        (-1,'DESC')
    ],required=False)

class CreateCommentForm(forms.Form):
    text = forms.CharField(max_length = 250)

