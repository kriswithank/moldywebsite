from django.db import models
from common.models import TitledBasicPost
from ckeditor.fields import RichTextField



class AboutSection(TitledBasicPost):
    position = models.PositiveIntegerField()

    class Meta:
        ordering = ['position', 'title']

    def __str__(self):
        return self.title


class AboutSectionOld(models.Model):
    """
    A class model which represents the sections in the about page.

    Attributes:
        position - Determines the order in which to display the sections on the page.
                   The category with the lowest position value should be displayed first,
                   the largest position value should be displayed last.

        section_title - The title of the section. Will be displayed in the about page.

        section_content - The content of the section. Will be displayed in the about page.
    """
    position = models.PositiveIntegerField()
    section_title = models.CharField(max_length=150)
    section_content = RichTextField()

    class Meta:
        ordering = ['position', 'section_title']

    def __str__(self):
        return self.section_title
