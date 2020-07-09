from django import forms

from lists.models import Item


ERROR_ITEM_KOSONG = "Kamu gak boleh bikin item list kosong"

class FormItem(forms.models.ModelForm):

    class Meta:
        model = Item
        fields = ('text',)
        widgets={
            'text': forms.fields.TextInput(attrs={
                'placeholder': 'Masukkan satu item to-do',
                'class': 'form-control input-lg'
            }),
        }
        error_messages = {
            'text': {'required': ERROR_ITEM_KOSONG}
        }
