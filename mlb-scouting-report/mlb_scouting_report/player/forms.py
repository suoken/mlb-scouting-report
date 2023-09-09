from django import forms

class CreateHittingReport(forms.Form):

    name = forms.CharField(label="Name", max_length=255, required=True)

    # class Meta:
    #     fields = ["first_name", "last_name", "team"]