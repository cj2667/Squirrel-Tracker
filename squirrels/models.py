from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    Latitude = models.CharField(
        max_length = 100,
        help_text=_('Latitude of Squirrel'),
    )


    Longitude = models.CharField(
        max_length = 100,
        help_text=_('Longitude of Squirrel'),
    )

    Unique_Squirrel_ID = models.CharField(
        max_length=100,
        help_text=_('ID of Squirrel'),
    )
    


    AM = 'AM'
    PM = 'PM'
    
    SHIFT_CHOICES = [
        (AM, _('AM')),
        (PM, _('PM')),
    ]

    Shift = models.CharField(
        max_length = 15,
        help_text=_('Shift of Squirrel'),
        choices=SHIFT_CHOICES,
    )
    

    Date = models.DateField(
        auto_now = False,
        auto_now_add = False,
        help_text=_('yyyy-mm-dd'),
        
    )
    
    

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    UNKNOWN = '?'

    AGE_CHOICES = [
        (ADULT, _('Adult')),
        (JUVENILE, _('Juvenile')),
        (UNKNOWN, _('?')),
    ]

    Age =  models.CharField(
        max_length = 15,
        help_text=_('Age of Squirrel'),
        choices=AGE_CHOICES,
        # black = True
    )



    TRUE = 'true'
    FALSE = 'false'

    TF_CHOICES = [
        (TRUE, _('true')),
        (FALSE, _('false')),
    ]
    
    Running = models.CharField(
        max_length = 15,
        help_text = ('If Squirrel Running'),
        choices = TF_CHOICES,
        default = '',
    )


    Chasing = models.CharField(
        max_length = 15,
        help_text = ('If Squirrel Chasing'),
        choices = TF_CHOICES,
        default = '',
    )


    Climbing = models.CharField(
        max_length = 15,
        help_text = ('If Squirrel Climbing'),
        choices = TF_CHOICES,
        default = '',
    )

    Eating = models.CharField(
        max_length = 15,
        help_text = ('If Squirrel Eating'),
        choices = TF_CHOICES,
        default = '',
    )

    Foraging = models.CharField(
        max_length = 15,
        help_text = ('If Squirrel Foraging'),
        choices = TF_CHOICES,
        default = '',
    )











    def __str__(self):
        return self.Unique_Squirrel_ID
