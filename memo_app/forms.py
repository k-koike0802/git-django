from django import forms
from .models import Memo

class PostForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'memo-form'})
        }

CHOICE_FIELD_RECODE_NUMBERS = (
    ('5', '5件'),
    ('10', '10件'),
    ('15', '15件'),
)

CHOICE_FIELD_ORDER_OPTIONS = (
    ('0', '古い順'),
    ('1', '新着順'),
)

class RecordNumberForm(forms.Form):
    record_number = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'option-form',
        'onchange': 'submit(this.form)'}), 
        choices=CHOICE_FIELD_RECODE_NUMBERS
    )

class OrderOptionForm(forms.Form):
    order_option = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'option-form',
        'onchange': 'submit(this.form)'}), 
        choices=CHOICE_FIELD_ORDER_OPTIONS
    )