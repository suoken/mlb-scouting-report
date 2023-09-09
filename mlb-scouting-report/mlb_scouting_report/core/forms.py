from django import forms


TEST_CHOICES = (
    ("TOR", "Toronto Blue Jays"),
    ("DET", "Detroit Tigers"),
)

class CreateHittingReport():
    first_name = forms.CharField(max_length=255, required=True)
    last_name = forms.CharField(max_length=255, required=True)
    team = forms.ChoiceField(choices=TEST_CHOICES)

    class Meta:
        fields = ["first_name", "last_name", "team"]