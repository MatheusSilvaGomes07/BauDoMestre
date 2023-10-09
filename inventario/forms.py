from django import forms
from .models import Pasta, File

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result
    
class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = '__all__'
        exclude = ['owner', 'pasta']
    file = MultipleFileField()

class PastaForm(forms.ModelForm):
    class Meta:
        model = Pasta
        fields = '__all__'
        exclude = ['owner', 'divisao']

