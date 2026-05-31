from django.urls import path

from .views import (
    recruiter_dashboard,
    recruiter_positions,
    recruiter_create_position,
    recruiter_edit_position,
    recruiter_delete_position,
    recruiter_candidates,
    recruiter_applications,
    export_applications_excel,
    export_applications_pdf,
)

urlpatterns = [

    # =========================================
    # DASHBOARD
    # =========================================

    path(
        'dashboard/',
        recruiter_dashboard,
        name='recruiter_dashboard'
    ),

    # =========================================
    # POSITIONS MANAGEMENT
    # =========================================

    path(
        'positions/',
        recruiter_positions,
        name='recruiter_positions'
    ),

    path(
        'positions/create/',
        recruiter_create_position,
        name='recruiter_create_position'
    ),

    path(
        'positions/<int:id>/edit/',
        recruiter_edit_position,
        name='recruiter_edit_position'
    ),

    path(
        'positions/<int:id>/delete/',
        recruiter_delete_position,
        name='recruiter_delete_position'
    ),

    path(
        'candidates/',
        recruiter_candidates,
        name='recruiter_candidates'
    ),

    path(
        'applications/',
        recruiter_applications,
        name='recruiter_applications'
    ),

    path(
        'applications/export/excel/',
        export_applications_excel,
        name='export_applications_excel'
    ),

    path(
        'applications/export/pdf/',
        export_applications_pdf,
        name='export_applications_pdf'
    ),
    

]