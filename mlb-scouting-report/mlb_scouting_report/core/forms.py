from django import forms


TEST_CHOICES = (
    ("TOR", "Toronto Blue Jays"),
    ("DET", "Detroit Tigers"),
)

class CreateHittingReport(forms.Form):
    name = forms.CharField(label="Name", max_length=255, required=True)
    team = forms.ChoiceField(label="Team", choices=TEST_CHOICES)

    # class Meta:
    #     fields = ["first_name", "last_name", "team"]