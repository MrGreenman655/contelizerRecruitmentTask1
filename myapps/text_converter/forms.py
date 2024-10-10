from django.core.validators import FileExtensionValidator
from django.forms import forms, FileField, widgets


class TextConverterForm(forms.Form):
    text = FileField(
        label='Text file',
        validators=[
            FileExtensionValidator(
                allowed_extensions=['txt'],
            )],
    )
