from django.urls import reverse_lazy
from django.views.generic import FormView

from myapps.text_converter.forms import TextConverterForm
from myapps.text_converter.services import TextConverterService


# Create your views here.
class ConvertTextFormView(FormView):
    template_name = 'myapps/convert_text_from_view.html'
    form_class = TextConverterForm

    def form_valid(self, form):
        file = form.cleaned_data['text']
        file_text = file.read().decode('utf-8')
        converted_text = TextConverterService(file_text).converted_text
        return self.render_to_response(self.get_context_data(
            form=form, converted_text=converted_text, file_name=file.name
        ))
