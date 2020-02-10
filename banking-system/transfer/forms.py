from django import forms
from .models import transfer

class TransferForm(forms.ModelForm):
    class Meta:
        model = transfer
        fields=["receiver","amount"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(TransferForm, self).__init__(*args, **kwargs)

    