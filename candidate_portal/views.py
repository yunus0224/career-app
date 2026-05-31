from django.shortcuts import (
    render,
    redirect
)

from django.contrib.auth import (
    authenticate,
    login,
    logout,
    update_session_auth_hash
)

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

from recruitment.models import (
    Application,
    CandidateProfile
)
from recruitment.forms import CandidateUpdateForm


def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(request, user)

            return redirect('/dashboard/')

        return render(
            request,
            'login.html',
            {
                'error': 'Invalid username or password'
            }
        )

    return render(
        request,
        'public/login.html'
    )


def logout_view(request):

    logout(request)

    return redirect('/login/')


@login_required
def dashboard(request):

    profile = CandidateProfile.objects.get(
        user=request.user
    )

    applications = Application.objects.filter(
        candidate=profile
    )

    context = {

        'profile': profile,
        'applications': applications,

        'total_applications':
            applications.count(),

        'shortlisted_count':
            applications.filter(
                status='shortlisted'
            ).count(),

        'interview_count':
            applications.filter(
                status='interview'
            ).count(),

        'accepted_count':
            applications.filter(
                status='accepted'
            ).count(),

    }

    return render(
        request,
        'candidate/dashboard.html',
        context
    )


@login_required
def edit_profile(request):

    profile = request.user.candidateprofile

    if request.method == 'POST':

        form = CandidateUpdateForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():

            form.save()

            return redirect('/dashboard/')

    else:

        form = CandidateUpdateForm(
            instance=profile
        )

    return render(
        request,
        'candidate/edit_profile.html',
        {
            'form': form
        }
    )

@login_required
def security_settings(request):

    if request.method == 'POST':

        form = PasswordChangeForm(
            request.user,
            request.POST
        )

        for field in form.fields.values():

            field.widget.attrs.update({
                'class': 'w-full p-4 rounded-2xl border'
            })

        if form.is_valid():

            user = form.save()

            update_session_auth_hash(
                request,
                user
            )

            return redirect('/dashboard/')

    else:

        form = PasswordChangeForm(
            request.user
        )

        for field in form.fields.values():

            field.widget.attrs.update({
                'class': 'w-full p-4 rounded-2xl border'
            })

    return render(
        request,
        'candidate/security_settings.html',
        {
            'form': form
        }
    )

@login_required
def application_detail(request, id):

    application = Application.objects.get(
        id=id,
        candidate__user=request.user
    )

    return render(
        request,
        'candidate/application_detail.html',
        {
            'application': application
        }
    )