from django.contrib import admin
from django.utils.html import format_html

from .models import (
    Position,
    CandidateProfile,
    Application
)


# POSITION ADMIN

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'position_type',
        'is_active',
        'created_at'
    )

    list_filter = (
        'position_type',
        'is_active'
    )

    search_fields = (
        'title',
    )

    prepopulated_fields = {
        'slug': ('title',)
    }


# CANDIDATE PROFILE ADMIN

@admin.register(CandidateProfile)
class CandidateProfileAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'institution',
        'study_program',
        'scientific_field',
        'ojs_skill'
    )

    list_filter = (
        'status',
        'ojs_skill'
    )

    search_fields = (
        'user__username',
        'institution',
        'scientific_field'
    )

    readonly_fields = (
        'cv_preview',
        'portfolio_preview',
    )

    fieldsets = (

        ('Account Information', {
            'fields': (
                'user',
            )
        }),

        ('Personal Information', {
            'fields': (
                'phone',
                'city',
                'gender',
                'status',
            )
        }),

        ('Academic Information', {
            'fields': (
                'institution',
                'study_program',
                'occupation',
                'scientific_field',
                'ojs_skill',
            )
        }),

        ('Professional Information', {
            'fields': (
                'bio',
            )
        }),

        ('Documents', {
            'fields': (
                'cv',
                'cv_preview',
                'portfolio',
                'portfolio_preview',
            )
        }),

    )

    def cv_preview(self, obj):

        if obj.cv:

            return format_html(
                '<a href="{}" target="_blank">View CV</a>',
                obj.cv.url
            )

        return "-"

    cv_preview.short_description = "CV File"

    def portfolio_preview(self, obj):

        if obj.portfolio:

            return format_html(
                '<a href="{}" target="_blank">View Portfolio</a>',
                obj.portfolio.url
            )

        return "-"

    portfolio_preview.short_description = "Portfolio File"


# APPLICATION ADMIN

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):

    list_display = (
        'candidate',
        'position',
        'status',
        'assigned_journal',
        'created_at'
    )

    list_filter = (
        'status',
        'position'
    )

    search_fields = (
        'candidate__user__username',
    )

    ordering = (
        '-created_at',
    )

    fieldsets = (

        ('Candidate Information', {
            'fields': (
                'candidate',
                'position',
                'status',
            )
        }),

        ('Recruitment Process', {
            'fields': (
                'assigned_journal',
                'interview_notes',
                'interview_date',
                'interview_time',
                'interview_link',
            )
        }),

    )