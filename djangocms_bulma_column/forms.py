from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import MultiColumns


class MultiColumnForm(forms.ModelForm):
    NUM_COLUMNS = (
        (0, "0"),
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
        (6, "6"),
        (7, "7"),
        (8, "8"),
        (9, "9"),
        (10, "10"),
        (11, "11"),
        (12, "12"),
    )

    create = forms.ChoiceField(
        choices=NUM_COLUMNS,
        label=_("Create Columns"),
        help_text=_("Create this number of columns")
    )

    class Meta:
        model = MultiColumns
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')
