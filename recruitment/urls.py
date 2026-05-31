from django.urls import path

from . import views

from .views import (
    home,
    apply,
    application_success,
    shortlist_application,
    interview_application,
    accept_application,
    my_applications,
)

urlpatterns = [

    # PUBLIC

    path(
        '',
        home,
        name='home'
    ),

    path(
        'apply/<slug:slug>/',
        apply,
        name='apply'
    ),

    path(
        'application-success/',
        application_success,
        name='application_success'
    ),

    # APPLICATION DETAIL

    path(
        'recruiter/application/<int:id>/',
        views.recruiter_application_detail,
        name='recruiter_application_detail'
    ),

    # SHORTLIST FORM

    path(
        'recruiter/application/<int:id>/shortlist/',
        shortlist_application,
        name='shortlist_application'
    ),

    # INTERVIEW FORM
    # MUST BE ABOVE GENERIC STATUS ROUTE

    path(
        'recruiter/application/<int:id>/interview/',
        interview_application,
        name='interview_application'
    ),

    
    path(
        'recruiter/application/<int:id>/accept/',
        accept_application,
        name='accept_application'
    ),

    path(
        'recruiter/application/<int:id>/evaluation/',
        views.interview_evaluation,
        name='interview_evaluation'
    ),

    path(
        'recruiter/application/<int:id>/reject/',
        views.reject_application,
        name='reject_application'
    ),

    # GENERIC STATUS ROUTE
    # MUST BE LAST

    path(
        'recruiter/application/<int:id>/<str:status>/',
        views.update_application_status,
        name='update_application_status'
    ),

    path(
        'applications/',
        my_applications,
        name='my_applications'
    ),

]

