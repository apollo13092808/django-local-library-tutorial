import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy


class RenewBookForm(forms.Form):
    """Form for a librarian to renew books."""
    renewal_date = forms.DateField(help_text='Enter a date between now and 4 weeks (default 3).')

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Check date if not in past
        if data < datetime.date.today():
            raise ValidationError(gettext_lazy('Invalid date - renewal in past'))

        # Check date is in range librarian allowed to change (+4 weeks)
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(gettext_lazy('Invalid date - renewal more than 4 weeks ahead'))

        return data
