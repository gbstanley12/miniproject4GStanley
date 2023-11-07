from django import forms

class MoviePollForm(forms.Form):
    # Example field
    rating = forms.ChoiceField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
