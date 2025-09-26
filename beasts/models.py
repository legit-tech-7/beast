from django.db import models

class Contestant(models.Model):
    PRONOUN_CHOICES = [
        ('she/her', 'She/Her'),
        ('he/him', 'He/Him'),
        ('they/them', 'They/Them'),
        ('other', 'Other'),
    ]

    ETHNICITY_CHOICES = [
        ('white', 'White'),
        ('black', 'Black/African American'),
        ('hispanic', 'Hispanic/Latino'),
        ('asian', 'Asian'),
        ('native_american', 'American Indian/Alaska Native'),
        ('pacific_islander', 'Native Hawaiian/Pacific Islander'),
        ('two_or_more', 'Two or more Races'),
        ('decline', 'Decline to Answer'),
    ]

    YES_NO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    dob = models.DateField(help_text="Date of Birth FOR VERIFICATION PURPOSES ONLY PURSUANT TO 18 U.S.C. §§ 2256 ET SEQ.")
    pronouns = models.CharField(max_length=10, choices=PRONOUN_CHOICES)
    social_handles = models.TextField(help_text="Instagram, Facebook, X, YouTube, TikTok, Twitch, Threads, Reddit, etc.")
    ethnicity = models.CharField(max_length=20, choices=ETHNICITY_CHOICES)
    nationality = models.CharField(max_length=50)
    how_did_you_hear = models.TextField()
    employer_feelings = models.TextField()
    occupation = models.CharField(max_length=100)
    know_anyone = models.TextField(blank=True, null=True)
    desired_prize = models.DecimalField(max_digits=10, decimal_places=2)
    competed_before = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='no')
    prior_url = models.URLField(blank=True, null=True)

    registration_feep_aid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
