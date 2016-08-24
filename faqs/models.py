from django.db import models
from ckeditor.fields import RichTextField



DEFAULT_FAQ_CATEGORY = 1



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





class FaqOld(models.Model):
    """
    A class model for a frequently asked question.

    Attributes:
        position - Determines the order in which to display the faqs on the page.
                   The faq with the lowest position value should be the first displayed,
                   largest position value should be the last displayed.

        question_text - The frequently asked question.

        answer_text - The answer to the frequently asked question.

        category - The FaqCategory to which the faq belongs to.
    """
    position = models.PositiveIntegerField()
    question_text = models.CharField(max_length=250)
    answer_text = RichTextField()
    category = models.ForeignKey(FaqCategory, on_delete=models.DO_NOTHING, default=DEFAULT_FAQ_CATEGORY)

    def __str__(self):
        return self.question_text
