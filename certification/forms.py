from django import forms
from .models import CertificationDetails

GENDERS = (
        ('M', 'Male'),
        ('F', 'Female')
    )

VALIDITIES = (
    (None, 'Select Validity'),
    (1, '1 Year'),
    (2, '2 Years'),
    (3, '3 Years')
)
#
# VALIDITIES  = []
# for i in range(1,10):
#     VALIDITIES.append((i, f"{i} years(s)"))
# VALIDITIES  = tuple(VALIDITIES )

class CertificationDetailsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        #super(CertificationDetailsForm, self).__init__(*args, **kwargs)
        super().__init__(*args, **kwargs)
        self.fields['gender'].widget = forms.RadioSelect(choices=GENDERS)
        self.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['validity'].widget = forms.Select(choices=VALIDITIES)
        #self.fields['center_address'].widget = forms.FileInput()
    class Meta:
        model = CertificationDetails
        fields = ('first_name', 'last_name', 'email', 'gender', 'name', 'date', 'cost', 'marks',
                  'validity', 'center_address', 'result', 'status', 'feedback', 'ratings')

        # fields = ('first_name', 'last_name',)