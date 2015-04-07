from django.forms import forms




class UploadForm(forms.Form):
    csvfile = forms.FileField(
        label='Select a CSV file',
    )