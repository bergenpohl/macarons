from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class custom_form(forms.Form):
    bpm = forms.IntegerField(min_value=60, max_value=200, initial=120, label_suffix='')
    melody = forms.ChoiceField(choices=[('rand', 'Random'), ('i1', 'Option 1'), ('i2', 'Option 2'), ('i3', 'Option 3'), ('i4', 'Option 4'), ('i5', 'Option 5'), ('i6', 'Option 6')], label_suffix='')
    bass = forms.ChoiceField(choices=[('rand', 'Random'), ('i1', 'Option 1'), ('i2', 'Option 2'), ('i3', 'Option 3'), ('i4', 'Option 4'), ('i5', 'Option 5'), ('i6', 'Option 6')], label_suffix='')
    first_eight = forms.ChoiceField(choices=[('a', 'A')], label_suffix='')
    second_eight = forms.ChoiceField(choices=[('none', 'N/A'), ('a', 'A'), ('b', 'B')], label_suffix='')
    third_eight = forms.ChoiceField(choices=[('none', 'N/A'), ('a', 'A'), ('b', 'B'), ('c', 'C')], label_suffix='')
    fourth_eight = forms.ChoiceField(choices=[('none', 'N/A'), ('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')], label_suffix='')
