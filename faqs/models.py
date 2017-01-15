from common.models import MarkdownModel
from django.db import models



class FaqCategory(models.Model):
    """
    A class model for seperating frequently asked quesitons into categories.

    Attributes:
        position - Determines the order in which to display the categories on the page.
                   The category with the lowest position value should be displayed first,
                   the largest position value should be displayed last.

        display_text - The category name which will be displayed.
    """
    position = models.PositiveIntegerField()
    display_text = models.CharField(max_length=150)

    class Meta:
        ordering = ['position', 'display_text']

    def __str__(self):
        return self.display_text




class Faq(MarkdownModel):
    """
    A class model for a frequently asked question, extends TitledBasicPost.

    Attributes:
        title - The title of the Faq.

        position - Determines the order in which to display the faqs on the page.
                   The faq with the lowest position value should be the first displayed,
                   largest position value should be the last displayed.

        category - The FaqCategory to which the faq belongs to.
    """
    title = models.CharField(max_length=250)
    position = models.PositiveIntegerField()
    category = models.ForeignKey(FaqCategory, on_delete=models.CASCADE)
