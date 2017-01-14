from django.db import models
from common.models import MarkdownModel



class AboutSection(MarkdownModel):
    """
    An about section for the about page.

    Attributes:
        position - Determines the order in which to display the sections on the page.
                   The category with the lowest position value should be displayed
                   first, the largest position value should be displayed last.
        title - The title of the about section.
    """
    title = models.CharField(max_length=250)
    position = models.PositiveIntegerField()

    class Meta:
        ordering = ['position', 'title']

    def __str__(self):
        return self.title
