from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import (
    path,
    include
)
from django.contrib.auth import views as auth_views
from candidate_portal.forms import (
    CareerPasswordResetForm
)



urlpatterns = [

    path(
        'admin/',
        admin.site.urls
    ),

    path(
        '',
        include('recruitment.urls')
    ),

    path(
        '',
        include('candidate_portal.urls')
    ),

    path(
    'recruiter/',
        include('recruiter.urls')
    ),

    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='auth/password_reset.html',
            form_class=CareerPasswordResetForm
        ),
        name='password_reset'
    ),

    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='auth/password_reset_done.html'
        ),
        name='password_reset_done'
    ),

    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='auth/password_reset_confirm.html'
        ),
        name='password_reset_confirm'
    ),

    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='auth/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),

]

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )



admin.site.site_header = "Litera Career Hub"
admin.site.site_title = "Litera Admin"
admin.site.index_title = "Litera Publishing Administration"