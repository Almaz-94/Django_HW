from django import forms
from newsletter.models import Newsletter


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class NewsletterForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Newsletter
        exclude = ('creator', 'status')


class ManagerNewsletterForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = ('is_active',)

