from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile
from django.utils.translation import gettext_lazy as _


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        # Making name required
        self.fields['alt_email'].required = True
        self.fields['college'].required = True
        self.fields['phone'].required = True
        self.fields['year_of_grad'].required = True
        self.fields['address'].required = True
        self.fields['city'].required = True
        self.fields['state'].required = True

        for field in self.fields.values():
            field.error_messages = {
                'required': 'The field {fieldname} is required'.format(fieldname=field.label),
                'max_length': 'The length of the field is too long',
            }

    class Meta:
        model = Profile
        fields = ('alt_email', 'college', 'phone', 'year_of_grad', 'address', 'city', 'state')
        labels = {
            'alt_email': _('Alternate Email Address'),
            'college': _('College Name'),
            'phone': _('Phone Number'),
            'year_of_grad': _('Year of Graduation'),
            'address': _('Address'),
            'city': _('City'),
            'state': _('State'),
        }
