from django import forms
from django.contrib.auth.models import User


class NewGameForm(forms.Form):
    name = forms.CharField()
    players = forms.ModelMultipleChoiceField(queryset=User.objects.all())


# this is an atempt to add a field when user clicks a button
# class NewGameForm(forms.Form):
#     # print(User.objects.all())
#     field1 = forms.CharField()
#     extra_field_count = forms.CharField(widget=forms.HiddenInput())
#
#     def __init__(self, *args, **kwargs):
#         extra_fields = kwargs.pop('extra', 0)
#
#         super(NewGameForm, self).__init__(*args, **kwargs)
#         self.fields['extra_field_count'].initial = extra_fields
#
#         for index in range(int(extra_fields)):
#             # generate extra fields in the number specified via extra_fields
#             self.fields['extra_field_{index}'.format(index=index)] = \
#                 forms.CharField()