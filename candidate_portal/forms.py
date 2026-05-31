from django import forms
from django.contrib.auth.forms import PasswordResetForm
from accounts.models import User
from recruitment.models import CandidateProfile
from django import forms


class CareerPasswordResetForm(
    PasswordResetForm
):

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": (
                    "w-full p-4 rounded-2xl "
                    "border border-gray-300 "
                    "focus:ring-2 "
                    "focus:ring-[#163B9F]"
                ),
                "placeholder":
                    "Enter your email address"
            }
        )
    )


class CandidateUpdateForm(forms.ModelForm):

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'w-full p-4 rounded-2xl border'
            }
        )
    )

class Meta:

    model = CandidateProfile

    fields = [
        'first_name',
        'last_name',
        'phone',
        'city',
        'gender',
        'status',
        'institution',
        'study_program',
        'occupation',
        'scientific_field',
        'ojs_skill',
        'bio',
        'cv',
        'portfolio',
    ]
