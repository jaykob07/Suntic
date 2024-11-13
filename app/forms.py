from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'description', 'pdf_file', 'approver']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-6 mb-0'),
                Column('approver', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'description',
            'pdf_file',
            Submit('submit', 'Save Document', css_class='btn-primary')
        )