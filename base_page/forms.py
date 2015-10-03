from django.forms import ModelForm
from django.utils.translation import ugettext as _
from news.models import article
from ckeditor.widgets import CKEditorWidget
from django.forms import widgets

class AddNewForm(ModelForm):
    class Meta:
        model = article
        fields = ['head', 'text']
        widgets = {
                   'text': CKEditorWidget(),
                   'head': widgets.TextInput(),
        }
