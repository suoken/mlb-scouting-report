from django import forms
from .models import Team, Hitter, ThrowingArm, ToolGrades, Pitcher, Pitch
from django.forms import inlineformset_factory

class HittingReportForm(forms.ModelForm):
    player = forms.CharField(label="Player", required=True, max_length=255)
    team = forms.ModelChoiceField(label="Team", queryset=Team.objects.all(), empty_label="Select", to_field_name="code")
    field_position = forms.ChoiceField(label="Pos", choices=Hitter.FieldPosition.choices)
    batting_position = forms.ChoiceField(label="Bats", choices=Hitter.BattingPosition.choices)
    throwing_arm = forms.ChoiceField(label="Throws", choices=ThrowingArm.choices)

    hit = forms.ChoiceField(label="Hit", choices=ToolGrades.choices)
    hit_future_value = forms.ChoiceField(label="FV", choices=ToolGrades.choices)
    hit_comments = forms.CharField(label="Comments", max_length=255, required=False)

    power = forms.ChoiceField(label="Power", choices=ToolGrades.choices)
    power_future_value = forms.ChoiceField(label="FV", choices=ToolGrades.choices)
    power_comments = forms.CharField(label="Comments", max_length=255, required=False)

    fielding = forms.ChoiceField(label="Fielding", choices=ToolGrades.choices)
    fielding_future_value = forms.ChoiceField(label="FV", choices=ToolGrades.choices)
    fielding_comments = forms.CharField(label="Comments", max_length=255, required=False)

    throwing = forms.ChoiceField(label="Throwing", choices=ToolGrades.choices)
    throwing_future_value = forms.ChoiceField(label="FV", choices=ToolGrades.choices)
    throwing_comments = forms.CharField(label="Comments", max_length=255, required=False)
    
    run = forms.ChoiceField(label="Run", choices=ToolGrades.choices)
    run_future_value = forms.ChoiceField(label="FV", choices=ToolGrades.choices)
    run_comments = forms.CharField(label="Comments", max_length=255, required=False)

    overall_grade = forms.ChoiceField(label="Overall Grade", choices=ToolGrades.choices)
    future_grade = forms.ChoiceField(label="Future Grade", choices=ToolGrades.choices)
    
    class Meta:
        model = Hitter
        exclude = ('player', )
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

class PitchingReportForm(forms.ModelForm):
    player = forms.CharField(label="Player", max_length=255, required=True)
    team = forms.ModelChoiceField(label="Team", queryset=Team.objects.all(), to_field_name="code")
    position = forms.ChoiceField(label="Pos", choices=Pitcher.PitchingPositions.choices)
    throwing_arm = forms.ChoiceField(label="Throws", choices=ThrowingArm.choices)
    report_date = forms.DateField(label="Report Date")

    overall_grade = forms.ChoiceField(label="Overall Grade", choices=ToolGrades.choices)
    future_grade = forms.ChoiceField(label="Future Grade", choices=ToolGrades.choices)

    class Meta:
        model = Pitcher
        fields = ['team', 'position', 'throwing_arm', 'overall_grade', 'future_grade']
        exclude = ('report_date', 'player')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

class PitchForm(forms.ModelForm):
    pitch_type = forms.ChoiceField(label="Pitch", choices=Pitch.PitchType.choices)

    class Meta:
        model = Pitch
        fields = ['pitch_type', 'velocity_low', 'velocity_high', 'grade', 'pitch_future_value', 'comments']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

PitchFormSet = inlineformset_factory(Pitcher, Pitch, form=PitchForm, extra=4, can_delete=False)
PitchFormEditSet = inlineformset_factory(Pitcher, Pitch, form=PitchForm, extra=0, can_delete=False)