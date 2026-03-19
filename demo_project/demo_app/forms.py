from django import forms

from django_cotton_uswds.mixins import USWDSFormMixin

REASON_CHOICES = [
    ("", "- Select -"),
    ("question", "General question"),
    ("feedback", "Feedback"),
    ("support", "Technical support"),
]


class DemoForm(USWDSFormMixin, forms.Form):
    name = forms.CharField(
        max_length=100,
        help_text="Enter your full legal name.",
    )
    email = forms.EmailField()
    reason = forms.ChoiceField(choices=REASON_CHOICES)
