from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

class ThrowingArm(models.TextChoices):
    RIGHT = "R", "Right"
    LEFT = "L", "Left"

class ToolGrades(models.IntegerChoices):
    """
    Tool Grades increments are based on the 20-80 Scouting Scale
    """
    THIRTY = 30, "30"
    THIRTY_FIVE = 35, "35"
    FOURTY = 40, "40"
    FOURTY_FIVE = 45, "45"
    FIFTY = 50, "50"
    FIFTY_FIVE = 55, "55"
    SIXTY = 60, "60"
    SIXTY_FIVE = 65, "65"
    SEVENTY = 70, "70"
    SEVENTY_FIVE = 75, "75"
    EIGHTY = 80, "80"
    
class Team(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    
class Player(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name="players")
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ("-last_name",)
    
    def __str__(self):
        return self.last_name
    
    
class Hitter(models.Model):
    """
    Represents a baseball hitter with various skill ratings and assessments
    """

    class BattingPosition(models.TextChoices):
        RIGHT = "R", "Right"
        LEFT = "L", "Left"
        SWITCH = "Switch"

    class FieldPosition(models.TextChoices):
        PITCHER = "P", "Pitcher"
        CATCHER = "C", "Catcher"
        FIRST_BASEMAN = "1B", "First Baseman"
        SECOND_BASEMAN = "2B", "Second Baseman"
        THIRD_BASEMAN = "3B", "Third Baseman"
        SHORTSTOP = "SS", "Shortstop"
        LEFT_FIELD = "LF", "Left Field"
        CENTER_FIELD = "CF", "Center Field"
        RIGHT_FIELD = "RF", "Right Field"
        DESIGNATED_HITTER = "DH", "Designated Hitter"

    player = models.ForeignKey(Player, related_name="hitters", on_delete=models.CASCADE)

    report_date = models.DateField(auto_now_add=True)
    declarative_statement = models.TextField(blank=True, null=True)
    field_position = models.CharField(max_length=10, choices=FieldPosition.choices)
    batting_position = models.CharField(max_length=10, choices=BattingPosition.choices)
    throwing_arm = models.CharField(max_length=10, choices=ThrowingArm.choices)

    hit = models.IntegerField(choices=ToolGrades.choices)
    hit_future_value = models.IntegerField(choices=ToolGrades.choices)
    hit_comments = models.TextField(max_length=255, blank=True, null=True)

    power = models.IntegerField(choices=ToolGrades.choices)
    power_future_value = models.IntegerField(choices=ToolGrades.choices)
    power_comments = models.TextField(max_length=255, blank=True, null=True)

    fielding = models.IntegerField(choices=ToolGrades.choices)
    fielding_future_value = models.IntegerField(choices=ToolGrades.choices)
    fielding_comments = models.TextField(max_length=255, blank=True, null=True)
    
    throwing = models.IntegerField(choices=ToolGrades.choices)
    throwing_future_value = models.IntegerField(choices=ToolGrades.choices)
    throwing_comments = models.TextField(max_length=255, blank=True, null=True)
    
    run = models.IntegerField(choices=ToolGrades.choices)
    run_future_value = models.IntegerField(choices=ToolGrades.choices)
    run_comments = models.TextField(max_length=255, blank=True, null=True)

    overall_grade = models.IntegerField(choices=ToolGrades.choices)
    future_grade = models.IntegerField(choices=ToolGrades.choices)

    class Meta:
        ordering = ("-report_date",)

    def __str__(self):
        return self.player.last_name


class Pitcher(models.Model):
    """
    Represents a baseball pitcher with various skill ratings and assessments
    """
    class PitchingPositions(models.TextChoices):
        STARTING_PITCHER = "SP", "Starting Pitcher"
        RELIEF_PITCHER = "RP", "Relief Pitcher"
        CLOSING_PITCHER = "CL", "Closing Pitcher"

    player = models.ForeignKey(Player, related_name="pitchers", on_delete=models.CASCADE)

    report_date = models.DateField(auto_now_add=True)
    declarative_statement = models.TextField(max_length=1024, blank=True, null=True)
    position = models.CharField(max_length=10, choices=PitchingPositions.choices)
    throwing_arm = models.CharField(max_length=20, choices=ThrowingArm.choices)

    overall_grade = models.IntegerField(choices=ToolGrades.choices)
    future_grade = models.IntegerField(choices=ToolGrades.choices)

    class Meta:
        ordering = ("-report_date",)

    def __str__(self):
        return self.player.last_name

class Pitch(models.Model):
    """
    Represents the pitch that the pitcher throws and the evaluation of the pitch
    """
    class PitchType(models.TextChoices):
        FOUR_SEAM_FASTBALL = "Four-seam Fastball"
        TWO_SEAM_FASTBALL = "Two-seam Fastball"
        CUTTER = "Cutter"
        SPLITTER = "Splitter"
        SLIDER = "Slider"
        CURVEBALL = "Curveball"
        FORKBALL = "Forkball"
        SLURVE = "Slurve"
        SCREWBALL = "Screwball"
        CHANGEUP = "Changeup"
        PALMBALL = "Palmball"
        CIRCLE_CHANGEUP = "Circle Changeup"
        KNUCKLEBALL = "Kunckleball"
        EEPHUS = "Eephus"
        KNUCKLE_CURVE = "Knuckle Curve"
        SINKER = "Sinker"
        SWEEPER = "Sweeper"

    pitcher = models.ForeignKey(Pitcher, related_name="pitches", on_delete=models.CASCADE)
    pitch_type = models.CharField(max_length=20, choices=PitchType.choices)
    velocity_low = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(120)])
    velocity_high = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(120)])
    grade = models.IntegerField(choices=ToolGrades.choices)
    pitch_future_value = models.IntegerField(choices=ToolGrades.choices)
    comments = models.TextField(max_length=1024)

    def clean(self):
        if self.velocity_low > self.velocity_high:
            raise ValidationError("velocity_low cannot be greater than velocity_high") # handle this gracefully
        
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
