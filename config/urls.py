from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import (
    path,
    include
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

]

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )



admin.site.site_header = "Litera Career Hub"
admin.site.site_title = "Litera Admin"
admin.site.index_title = "Litera Publishing Administration"