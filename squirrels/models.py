from django.db import models

class Squirrel(model.Model):
    Latitude = models.CharField(
        max_length = 100,
        help_text=_('Latitude of Squirrel'),
    )


    Longitude = models.CharField(
        max_length = 100,
        help_text=_('Longitude of Squirrel'),
    )

    Unique_Squirrel_ID = models.CharField(
        max_lenth=100,
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
    

    Date = models.CharField(
        max_length = 20,
        help_text=_('Date of finding Squirrel'),
        blank = False,
        null = True,
    )
    
    

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    UNKNOWN = '?'


    AGE_CHOICES = [
        (ADULT, _('Adult')),
        (JUVENILE, _('Juvenile')),
        (UNKNOWN, _('?')),
    ]

    Age =  model.CharField(
        max_length = 15,
        help_text=_('Age of Squirrel'),
        blank = False, #not sure about this
        null = True,   #not sure about this
    )
