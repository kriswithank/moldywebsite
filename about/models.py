from django.db import models
from common.models import TitledBasicPost



class AboutSection(TitledBasicPost):
    """
    A class model which represents a secion in the about page. Is a typical
    TitledBasicPost but with a position.

    Attributes:
        position - Determines the order in which to display the sections on the page.
                   The category with the lowest position value should be displayed
                   first, the largest position value should be displayed last.
    """
    position = models.PositiveIntegerField()

    class Meta:
        ordering = ['position', 'title']

    def __str__(self):
        return self.title
