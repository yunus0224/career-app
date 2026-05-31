from accounts.models import User
from .models import CandidateProfile
from .models import Position
from django import forms
from .models import Application



class CandidateRegistrationForm(forms.ModelForm):

    # ACCOUNT INFORMATION

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-full p-4 rounded-xl border',
            'placeholder': 'Username'
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'w-full p-4 rounded-xl border',
            'placeholder': 'Email Address'
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full p-4 rounded-xl border',
            'placeholder': 'Password'
        })
    )

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-full p-4 rounded-xl border',
            'placeholder': 'First Name'
        })
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-full p-4 rounded-xl border',
            'placeholder': 'Last Name'
        })
    )

    class Meta:

        model = CandidateProfile

        fields = [
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

        widgets = {

            # PERSONAL INFORMATION

            'phone': forms.TextInput(attrs={
                'class': 'w-full p-4 rounded-xl border',
                'placeholder': 'Phone Number'
            }),

           'city': forms.TextInput(attrs={
                'class': 'w-full p-4 rounded-xl border',
                'placeholder': 'Example: Jember, East Java'
            }),
            

            'gender': forms.TextInput(attrs={
                'class': 'w-full p-4 rounded-xl border',
                'placeholder': 'Example: Male / Female'
            }),

            'status': forms.Select(attrs={
                'class': 'w-full p-4 rounded-xl border'
            }),

            'institution': forms.TextInput(attrs={
                'class': 'w-full p-4 rounded-xl border',
                'placeholder': 'Example: Universitas Jember'
            }),

            'study_program': forms.TextInput(attrs={
                'class': 'w-full p-4 rounded-xl border',
                'placeholder': 'Example: Informatics Engineering'
            }),

            'occupation': forms.TextInput(attrs={
                'class': 'w-full p-4 rounded-xl border',
                'placeholder': 'Example: Student, Freelancer, Lecturer'
            }),

            # PROFESSIONAL INFORMATION

            'scientific_field': forms.TextInput(attrs={
                'class': 'w-full p-4 rounded-xl border',
                'placeholder': 'Example: Computer Science, Education'
            }),

            'ojs_skill': forms.Select(attrs={
                'class': 'w-full p-4 rounded-xl border'
            }),

            # BIO

            'bio': forms.Textarea(attrs={
                'class': 'w-full p-4 rounded-xl border',
                'placeholder': 'Tell us about yourself',
                'rows': 5
            }),

            # DOCUMENTS

            'cv': forms.FileInput(attrs={
                'class': 'w-full p-4 rounded-xl border bg-white'
            }),

            'portfolio': forms.FileInput(attrs={
                'class': 'w-full p-4 rounded-xl border bg-white'
            }),

        }

    def save(self):

        # CREATE USER

        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )

        # CREATE CANDIDATE PROFILE

        profile = CandidateProfile.objects.create(
            user=user,
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            phone=self.cleaned_data['phone'],
            city=self.cleaned_data['city'],
            gender=self.cleaned_data['gender'],
            status=self.cleaned_data['status'],
            institution=self.cleaned_data['institution'],
            study_program=self.cleaned_data['study_program'],
            occupation=self.cleaned_data['occupation'],
            scientific_field=self.cleaned_data['scientific_field'],
            ojs_skill=self.cleaned_data['ojs_skill'],
            bio=self.cleaned_data['bio'],
            cv=self.cleaned_data['cv'],
            portfolio=self.cleaned_data.get('portfolio')
        )

        return profile


# JOURNAL ASSISTANT FORM

class AssistantRegistrationForm(CandidateRegistrationForm):
    pass


# JOURNAL MANAGER FORM

class JournalManagerRegistrationForm(CandidateRegistrationForm):

    experience = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-full p-4 rounded-xl border',
            'placeholder': 'Describe your journal management experience',
            'rows': 5
        })
    )

    indexed_journal = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-full p-4 rounded-xl border',
            'placeholder': 'Indexed / Accredited Journal Experience'
        })
    )

# CANDIDATE UPDATE FORM

class CandidateUpdateForm(forms.ModelForm):

    email = forms.EmailField( 
        required=True, 
        widget=forms.EmailInput( 
            attrs={ 
                'class': 'w-full p-4 rounded-xl border', 
                'placeholder': 'Email Address' 
                } 
            ) 
        )

    class Meta:

        model = CandidateProfile

        fields = [
            'first_name',
            'last_name',
            'email',
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

        widgets = {

            # BASIC INFORMATION

            'first_name': forms.TextInput(attrs={
                'class': 'w-full p-4 rounded-xl border',
                'placeholder': 'First Name'
            }),

            'last_name': forms.TextInput(attrs={
                'class': 'w-full p-4 rounded-xl border',
                'placeholder': 'Last Name'
            }),

            'phone': forms.TextInput(attrs={
                'class': 'w-full p-4 rounded-xl border',
                'placeholder': 'Phone Number'
            }),

            'city': forms.TextInput(attrs={
                'class': 'w-full p-4 rounded-xl border',
                'placeholder': 'Example: Jember, East Java'
            }),

            'gender': forms.TextInput(attrs={
                'class': 'w-full p-4 rounded-xl border',
                'placeholder': 'Example: Male / Female'
            }),

            'status': forms.Select(attrs={
                'class': 'w-full p-4 rounded-xl border'
            }),

            # ACADEMIC INFORMATION

            'institution': forms.TextInput(attrs={
                'class': 'w-full p-4 rounded-xl border',
                'placeholder': 'Example: University of Jember'
            }),

            'study_program': forms.TextInput(attrs={
                'class': 'w-full p-4 rounded-xl border',
                'placeholder': 'Example: Informatics Engineering'
            }),

            'occupation': forms.TextInput(attrs={
                'class': 'w-full p-4 rounded-xl border',
                'placeholder': 'Example: Student / Freelancer'
            }),

            # PROFESSIONAL INFORMATION

            'scientific_field': forms.TextInput(attrs={
                'class': 'w-full p-4 rounded-xl border',
                'placeholder': 'Example: Computer Science'
            }),

            'ojs_skill': forms.Select(attrs={
                'class': 'w-full p-4 rounded-xl border'
            }),

            'bio': forms.Textarea(attrs={
                'class': 'w-full p-4 rounded-xl border',
                'placeholder': 'Tell us about yourself',
                'rows': 5
            }),

            # DOCUMENTS

            'cv': forms.FileInput(attrs={
                'class': 'w-full p-4 rounded-xl border bg-white'
            }),

            'portfolio': forms.FileInput(attrs={
                'class': 'w-full p-4 rounded-xl border bg-white'
            }),

        }


class PositionForm(forms.ModelForm):

    class Meta:

        model = Position

        fields = [
            'title',
            'slug',
            'position_type',
            'description',
            'fee_scheme',
            'requirements',
            'is_active',
            'recruitment_open',
        ]

        widgets = {

            'title': forms.TextInput(
                attrs={
                    'class': 'w-full rounded-2xl border border-gray-200 bg-white px-5 py-4',
                    'placeholder': 'Example: Journal Manager'
                }
            ),

            'slug': forms.TextInput(
                attrs={
                    'class': 'w-full rounded-2xl border border-gray-200 bg-gray-50 px-5 py-4',
                    'placeholder': 'journal-manager'
                }
            ),

            'position_type': forms.Select(
                attrs={
                    'class': 'w-full rounded-2xl border border-gray-200 bg-white px-5 py-4'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'class': 'w-full rounded-2xl border border-gray-200 bg-white px-5 py-4',
                    'rows': 6
                }
            ),

            'fee_scheme': forms.Textarea(
                attrs={
                    'class': 'w-full rounded-2xl border border-gray-200 bg-white px-5 py-4',
                    'rows': 4
                }
            ),

            'requirements': forms.Textarea(
                attrs={
                    'class': 'w-full rounded-2xl border border-gray-200 bg-white px-5 py-4',
                    'rows': 6
                }
            ),

            'is_active': forms.CheckboxInput(
                attrs={
                    'class': 'w-5 h-5'
                }
            ),

        }



class ShortlistForm(forms.ModelForm):

    class Meta:

        model = Application

        
        fields = [

            'assigned_journal',
            'assigned_interviewer',
            'shortlist_notes'

        ]



        widgets = {
           
            'assigned_journal': forms.TextInput(
                attrs={
                    'class': '''
            w-full rounded-2xl border border-gray-200
            px-5 py-4 focus:outline-none
            focus:ring-2 focus:ring-[#163B9F]
            ''',
                    'placeholder': 'Example: Nexura'
                }
            ),

            'assigned_interviewer': forms.TextInput(
                attrs={
                    'class': '''
            w-full rounded-2xl border border-gray-200
            px-5 py-4 focus:outline-none
            focus:ring-2 focus:ring-[#163B9F]
            ''',
                    'placeholder': 'Example: Zainal Abidin'
                }
            ),
            
            'shortlist_notes': forms.Textarea(
                attrs={
                    'rows': 6,
                    'class': '''
            w-full rounded-2xl border border-gray-200
            px-5 py-4 focus:outline-none
            focus:ring-2 focus:ring-[#163B9F]
            ''',
                    'placeholder': 'Write recruiter notes...'
                }
            ),

        }



class InterviewForm(forms.ModelForm):

    class Meta:

        model = Application

        fields = [

            'interview_date',
            'interview_time',
            'interview_link',           

        ]

        widgets = {

            'interview_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'w-full rounded-2xl border border-gray-200 px-5 py-4'
                }
            ),

            'interview_time': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'class': 'w-full rounded-2xl border border-gray-200 px-5 py-4'
                }
            ),

            'interview_link': forms.URLInput(
                attrs={
                    'class': 'w-full rounded-2xl border border-gray-200 px-5 py-4',
                    'placeholder': 'https://meet.google.com/...'
                }
            ),

            'interview_notes': forms.Textarea(
                attrs={
                    'rows': 6,
                    'class': 'w-full rounded-2xl border border-gray-200 px-5 py-4',
                    'placeholder': 'Interview result, strengths, weaknesses, recommendation...'
                }
            )

        }


class InterviewEvaluationForm(forms.ModelForm):

    class Meta:

        model = Application

        fields = [

            'interview_notes'

        ]

        widgets = {

            'interview_notes': forms.Textarea(
                attrs={
                    'rows': 8,
                    'class': '''
w-full rounded-2xl border border-gray-200
px-5 py-4
''',
                    'placeholder':
                    'Interview result, strengths, weaknesses, recommendation...'
                }
            )

        }


class AcceptanceForm(forms.ModelForm):

    class Meta:

        model = Application

        fields = [

            'assigned_journal',
            'start_date',
            'onboarding_notes'

        ]

        widgets = {

            'assigned_journal': forms.TextInput(
                attrs={
                    'class': '''
w-full rounded-2xl border border-gray-200
px-5 py-4 focus:outline-none
focus:ring-2 focus:ring-[#163B9F]
'''
                }
            ),

            'start_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': '''
w-full rounded-2xl border border-gray-200
px-5 py-4 focus:outline-none
focus:ring-2 focus:ring-[#163B9F]
'''
                }
            ),

            'onboarding_notes': forms.Textarea(
                attrs={
                    'rows': 6,
                    'class': '''
w-full rounded-2xl border border-gray-200
px-5 py-4 focus:outline-none
focus:ring-2 focus:ring-[#163B9F]
''',
                    'placeholder': 'Welcome message and onboarding instructions...'
                }
            ),

        }


class RejectionForm(forms.ModelForm):

    class Meta:

        model = Application

        fields = [

            'rejection_reason'

        ]

        widgets = {

            'rejection_reason': forms.Textarea(

                attrs={

                    'rows': 8,

                    'class': '''
w-full rounded-2xl border border-gray-200
px-5 py-4
''',

                    'placeholder':
                    'Reason for rejection...'

                }

            )

        }



