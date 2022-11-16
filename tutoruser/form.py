from django import forms
from .models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

class ProfileForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        FormHelper.form_method = 'POST'

        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('save', 'save'))

    class Meta:
        model = Profile
        fields=['firstname','lastname','bio','age','educationlevel','address','religion','university','depertment','phone', 'email','experience','ongoingtuition','facebook','twitter','youtube','linkedin']
        