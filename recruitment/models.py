from django.db import models
from accounts.models import User
from django.utils.text import slugify
from django.conf import settings


class CandidateProfile(models.Model):

    STATUS_CHOICES = (
        ('student', 'Mahasiswa'),
        ('freshgraduate', 'Fresh Graduate'),
        ('lecturer', 'Dosen'),
        ('freelancer', 'Freelancer'),
        ('professional', 'Professional'),
    )

    OJS_SKILL = (
        ('basic', 'Basic'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
        max_length=100
    )

    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)

    gender = models.CharField(max_length=20)

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES
    )

    institution = models.CharField(max_length=255)

    study_program = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    occupation = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    scientific_field = models.CharField(max_length=255)

    ojs_skill = models.CharField(
        max_length=30,
        choices=OJS_SKILL
    )

    bio = models.TextField(blank=True, null=True)

    cv = models.FileField(upload_to='cv/')

    portfolio = models.FileField(
        upload_to='portfolio/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Position(models.Model):

    POSITION_TYPE_CHOICES = [

        ('project', 'By Project'),
        ('sharing', 'Revenue Sharing'),

    ]

    title = models.CharField(
        max_length=255
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
        null=True
    )

    position_type = models.CharField(
        max_length=30,
        choices=POSITION_TYPE_CHOICES,
        default='project'
    )

    description = models.TextField()

    requirements = models.TextField(
        blank=True,
        null=True
    )

    fee_scheme = models.TextField(
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    recruitment_open = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = ['-created_at']

        verbose_name = 'Position'

        verbose_name_plural = 'Positions'

    def __str__(self):

        return self.title

    def save(self, *args, **kwargs):

        # AUTO GENERATE SLUG

        if not self.slug:

            self.slug = slugify(self.title)

        super().save(*args, **kwargs)
    

class Application(models.Model):

    STATUS_CHOICES = [

        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('shortlisted', 'Shortlisted'),
        ('interview', 'Interview'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),

    ]

    # RELATION

    candidate = models.ForeignKey(
        CandidateProfile,
        on_delete=models.CASCADE
    )

    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE
    )

    # APPLICATION STATUS

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    # SHORTLIST

    shortlist_notes = models.TextField(
        blank=True,
        null=True
    )

    assigned_journal = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    assigned_interviewer = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    # INTERVIEW

    interview_date = models.DateField(
        blank=True,
        null=True
    )

    interview_time = models.TimeField(
        blank=True,
        null=True
    )

    interview_link = models.URLField(
        blank=True,
        null=True
    )

    interview_notes = models.TextField(
        blank=True,
        null=True
    )

   
    start_date = models.DateField(
        blank=True,
        null=True
    )

    onboarding_notes = models.TextField(
        blank=True,
        null=True
    )

    rejection_reason = models.TextField(
        blank=True,
        null=True
    )

    # FINAL ACCEPTANCE

    onboarding_notes = models.TextField(
        blank=True,
        null=True
    )

    # TIMESTAMP

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return (
            f"{self.candidate.user.username} "
            f"- {self.position.title}"
        )


class Interviewer(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    full_name = models.CharField(
        max_length=255
    )

    expertise = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.full_name

