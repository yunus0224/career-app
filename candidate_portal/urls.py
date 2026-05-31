from django.urls import path

from .views import (
    login_view,
    logout_view,
    dashboard,
    edit_profile,
    security_settings,
    application_detail
)

urlpatterns = [

    path(
        'login/',
        login_view,
        name='login'
    ),

    path(
        'logout/',
        logout_view,
        name='logout'
    ),

    path(
        'dashboard/',
        dashboard,
        name='dashboard'
    ),

    path(
        'edit-profile/',
        edit_profile,
        name='edit_profile'
    ),

    path(
        'security-settings/',
        security_settings,
        name='security_settings'
    ),

    path(
    'application/<int:id>/',
        application_detail,
        name='application_detail'
    ),

]