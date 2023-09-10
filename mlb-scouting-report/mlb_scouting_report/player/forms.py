from django import forms
from .models import Team, Hitter, ThrowingArm, ToolGrades

class HittingReportForm(forms.ModelForm):
    name = forms.CharField(label="Player", max_length=255, required=True)
    team = forms.ModelChoiceField(label="Team", queryset=Team.objects.all())
    pos = forms.ChoiceField(label="Pos", choices=Hitter.FieldPosition.choices)
    bats = forms.ChoiceField(label="Bats", choices=Hitter.BattingPosition.choices)
    throws = forms.ChoiceField(label="Throws", choices=ThrowingArm.choices)
    tool_grades = forms.ChoiceField(label="Tool Grades", choices=ToolGrades.choices)

    class Meta:
        model = Hitter
        fields = ["hit", "power", "fielding", "throwing", "run"]