from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from recruiter.models import Notification

from django.contrib.admin.views.decorators import (
    staff_member_required
)

from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail

from .models import (
    Position,
    Application,
    CandidateProfile
)
from django.contrib import messages

from .forms import (
    AssistantRegistrationForm,
    JournalManagerRegistrationForm,
    InterviewForm,
    AcceptanceForm,
    ShortlistForm,
    InterviewEvaluationForm,
    RejectionForm
)


# =========================================
# HOME
# =========================================

def home(request):

    positions = Position.objects.filter(
        is_active=True
    )

    return render(
        request,
        'public/home.html',
        {
            'positions': positions
        }
    )


# =========================================
# APPLY POSITION
# =========================================

def apply(request, slug):

    position = get_object_or_404(
        Position,
        slug=slug
    )
    

    # CEK STATUS LOWONGAN

    if not position.recruitment_open:

        messages.error(
            request,
            "This recruitment position is already closed."
        )

        return redirect('home')

    # JOURNAL MANAGER FORM

    if slug == 'journal-manager':

        form_class = JournalManagerRegistrationForm

    # JOURNAL ASSISTANT FORM

    else:

        form_class = AssistantRegistrationForm

    form = form_class()

    if request.method == 'POST':

        form = form_class(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            candidate = form.save()

            application = Application.objects.create(
                candidate=candidate,
                position=position
            )

            Notification.objects.create(

                title='New Application Submitted',

                message=f'''
                    New candidate applied for:

                    {position.title}

                    Candidate:
                    {candidate.first_name} {candidate.last_name}
                    '''
                    )

            # =========================================
            # EMAIL NOTIFICATION
            # =========================================

            candidate_email = candidate.user.email

            candidate_name = (
                f"{candidate.first_name} "
                f"{candidate.last_name}"
            )

            position_name = position.title

            # EMAIL TO CANDIDATE

            send_mail(
                'Application Submitted Successfully',

                f'''
Dear {candidate_name},

Thank you for applying to Litera Publishing.

Your application for:

{position_name}

has been successfully submitted.

Our recruitment team will review your application and contact you regarding the next recruitment stage.

Best regards,
Litera Publishing Recruitment Team
''',

                None,

                [candidate_email],

                fail_silently=False
            )

            # EMAIL TO ADMIN / RECRUITER

            send_mail(
                'New Candidate Application',

                f'''
New candidate application submitted.

Candidate:
{candidate_name}

Position:
{position_name}

Institution:
{candidate.institution}

Please review the application through the recruiter dashboard.
''',

                None,

                ['literaintegranusantara@gmail.com'],

                fail_silently=False
            )

            return redirect(
                '/application-success/'
            )

    return render(
        request,
        'public/apply.html',
        {
            'form': form,
            'position': position
        }
    )


# =========================================
# APPLICATION SUCCESS
# =========================================

def application_success(request):

    return render(
        request,
        'application_success.html'
    )


# =========================================
# RECRUITER APPLICATION DETAIL
# =========================================

@login_required
def recruiter_application_detail(request, id):

    application = get_object_or_404(
        Application,
        id=id
    )

    return render(
        request,
        'recruiter/application_detail.html',
        {
            'application': application
        }
    )


# =========================================
# UPDATE APPLICATION STATUS
# =========================================

@login_required
def update_application_status(
    request,
    id,
    status
):

    application = get_object_or_404(
        Application,
        id=id
    )

    # UPDATE STATUS

    application.status = status

    application.save()

    # CANDIDATE INFO

    candidate_email = application.candidate.user.email

    candidate_name = (
        f"{application.candidate.first_name} "
        f"{application.candidate.last_name}"
    )

    position_name = application.position.title

    # =========================================
    # EMAIL CONTENT
    # =========================================

    if status == 'shortlisted':

        subject = 'Application Shortlisted'

        message = f'''
Dear {candidate_name},

Congratulations!

Your application for the position:

{position_name}

has been shortlisted for the next recruitment stage.

Please wait for further information from Litera Publishing.

Best regards,
Litera Publishing Recruitment Team
'''

    elif status == 'interview':

        subject = 'Interview Invitation'

        message = f'''
Dear {candidate_name},

You are invited to attend an interview session for:

{position_name}

Interview Date:
{application.interview_date}

Interview Time:
{application.interview_time}

Meeting Link:
{application.interview_link}

Please prepare accordingly.

Best regards,
Litera Publishing Recruitment Team
'''

    elif status == 'accepted':

        subject = 'Application Accepted'

        message = f'''
Dear {candidate_name},

Congratulations!

You have been ACCEPTED for:

{position_name}

Assigned Journal:
{application.assigned_journal}

Welcome to Litera Publishing.

Best regards,
Litera Publishing Recruitment Team
'''

    elif status == 'rejected':

        subject = 'Application Rejected'

        message = f'''
Dear {candidate_name},

Thank you for participating in our recruitment process for:

{position_name}

After careful consideration, we regret to inform you that your application has not been selected for this opportunity.

We appreciate your interest in Litera Publishing and wish you success in your future endeavors.

Best regards,
Litera Publishing Recruitment Team
'''

    else:

        subject = 'Application Status Updated'

        message = f'''
Dear {candidate_name},

Your application status has been updated.

Current Status:
{status}

Best regards,
Litera Publishing Recruitment Team
'''

    # =========================================
    # SEND EMAIL
    # =========================================

    send_mail(
        subject,
        message,
        None,
        [candidate_email],
        fail_silently=False
    )

    return redirect(
        f'/recruiter/application/{id}/'
    )


@staff_member_required
def recruiter_create_position(request):

    if request.method == 'POST':

        Position.objects.create(

            title=request.POST.get('title'),

            slug=request.POST.get('slug'),

            position_type=request.POST.get('position_type'),

            description=request.POST.get('description'),

            fee_scheme=request.POST.get('fee_scheme'),

            requirements=request.POST.get('requirements'),

            is_active=True if request.POST.get('is_active') else False

        )

        return redirect(
            '/recruiter/positions/'
        )

    return render(
        request,
        'recruiter/create_position.html'
    )

@login_required
def shortlist_application(request, id):

    application = get_object_or_404(
        Application,
        id=id
    )

    form = ShortlistForm(
        instance=application
    )

    if request.method == 'POST':

        form = ShortlistForm(
            request.POST,
            instance=application
        )

        if form.is_valid():

            shortlist = form.save(
                commit=False
            )

            shortlist.status = 'shortlisted'

            shortlist.save()

            # EMAIL

            send_mail(

                'Application Shortlisted',

                f'''
Dear {application.candidate.first_name},

Congratulations!

Your application for:

{application.position.title}

has been shortlisted for the next recruitment stage.

Best regards,
Litera Publishing
''',

                None,

                [
                    application.candidate.user.email
                ],

                fail_silently=False
            )

            return redirect(
                f'/recruiter/application/{id}/'
            )

    return render(
        request,
        'recruiter/shortlist_form.html',
        {
            'form': form,
            'application': application
        }
    )


@staff_member_required
def interview_application(request, id):

    application = get_object_or_404(
        Application,
        id=id
    )

    if request.method == 'POST':

        form = InterviewForm(
            request.POST,
            instance=application
        )

        if form.is_valid():

            interview = form.save(
                commit=False
            )

            interview.status = 'interview'

            interview.save()

            # SEND EMAIL

            send_mail(

                'Interview Invitation - Litera Publishing',

                f'''
Dear {application.candidate.first_name},

Congratulations!

You have been invited to the interview stage.

Interview Schedule:

Date:
{application.interview_date}

Time:
{application.interview_time}

Meeting Link:
{application.interview_link}

Best regards,
Litera Publishing Recruitment Team
                ''',

                None,

                [
                    application.candidate.user.email
                ],

                fail_silently=False

            )

            return redirect(
                f'/recruiter/application/{application.id}/'
            )

    else:

        form = InterviewForm(
            instance=application
        )

    return render(

        request,

        'recruiter/interview_form.html',

        {

            'application': application,
            'form': form,

        }

    )


@staff_member_required
def accept_application(request, id):

    application = get_object_or_404(
        Application,
        id=id
    )

    if request.method == 'POST':

        form = AcceptanceForm(
            request.POST,
            instance=application
        )

        if form.is_valid():

            accepted = form.save(
                commit=False
            )

            accepted.status = 'accepted'

            accepted.save()

            send_mail(

                'Congratulations - Accepted',

                f'''
Dear {application.candidate.first_name},

Congratulations!

You have been accepted as:

{application.position.title}

Assigned Journal:
{application.assigned_journal}

Starting Date:
{application.start_date}

Best regards,
Litera Publishing Recruitment Team
                ''',

                None,

                [
                    application.candidate.user.email
                ],

                fail_silently=False
            )

            return redirect(
                f'/recruiter/application/{application.id}/'
            )

    else:

        form = AcceptanceForm(
            instance=application
        )

    return render(

        request,

        'recruiter/acceptance_form.html',

        {

            'application': application,
            'form': form,

        }

    )

@staff_member_required
def interview_evaluation(request, id):

    application = get_object_or_404(
        Application,
        id=id
    )

    if request.method == 'POST':

        form = InterviewEvaluationForm(
            request.POST,
            instance=application
        )

        if form.is_valid():

            form.save()

            return redirect(
                f'/recruiter/application/{id}/'
            )

    else:

        form = InterviewEvaluationForm(
            instance=application
        )

    return render(

        request,

        'recruiter/interview_evaluation.html',

        {

            'application': application,
            'form': form

        }

    )


@staff_member_required
def reject_application(request, id):

    application = get_object_or_404(
        Application,
        id=id
    )

    if request.method == 'POST':

        form = RejectionForm(
            request.POST,
            instance=application
        )

        if form.is_valid():

            rejected = form.save(
                commit=False
            )

            rejected.status = 'rejected'

            rejected.save()

            return redirect(
                f'/recruiter/application/{id}/'
            )

    else:

        form = RejectionForm(
            instance=application
        )

    return render(

        request,

        'recruiter/rejection_form.html',

        {

            'application': application,
            'form': form

        }

    )


@login_required
def my_applications(request):

    profile = get_object_or_404(
        CandidateProfile,
        user=request.user
    )

    applications = Application.objects.filter(
        candidate=profile
    ).select_related(
        'position'
    ).order_by(
        '-created_at'
    )

    context = {

        'profile': profile,
        'applications': applications,

    }

    return render(
        request,
        'candidate/applications.html',
        context
    )





