from django import forms
from catalog.models import Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin,forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        bad_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        cleaned_data = self.cleaned_data['name'].lower()
        if any([bad_word in cleaned_data for bad_word in bad_words]):
            raise forms.ValidationError('Использовано недопустимое слово в названии')

        return cleaned_data
