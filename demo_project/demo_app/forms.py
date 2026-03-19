from django import forms

from django_cotton_uswds.mixins import USWDSFormMixin

REASON_CHOICES = [
    ("", "- Select -"),
    ("question", "General question"),
    ("feedback", "Feedback"),
    ("support", "Technical support"),
]

CONTACT_METHOD_CHOICES = [
    ("email", "Email"),
    ("phone", "Phone"),
    ("mail", "Mail"),
]

INTEREST_CHOICES = [
    ("design", "Design"),
    ("development", "Development"),
    ("research", "Research"),
    ("policy", "Policy"),
]


class DemoForm(USWDSFormMixin, forms.Form):
    name = forms.CharField(
        max_length=100,
        help_text="Enter your full legal name.",
    )
    email = forms.EmailField()
    message = forms.CharField(
        widget=forms.Textarea,
        help_text="Provide details about your inquiry.",
    )
    agree_to_terms = forms.BooleanField(
        required=False,
        label="I agree to the terms and conditions",
    )
    reason = forms.ChoiceField(choices=REASON_CHOICES)
    contact_method = forms.ChoiceField(
        choices=CONTACT_METHOD_CHOICES,
        widget=forms.RadioSelect,
        label="Preferred contact method",
    )
    interests = forms.MultipleChoiceField(
        choices=INTEREST_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Areas of interest",
    )
    attachment = forms.FileField(
        required=False,
        label="Supporting document",
        widget=forms.ClearableFileInput(attrs={"width": "md"}),
    )
