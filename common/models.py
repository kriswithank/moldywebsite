from django.core.urlresolvers import reverse
from django.conf import settings
from django.db import models
import markdown



class NavMenuItem(models.Model):
    """
    A class model for navigation menu items. Each nav menu item should represent a single
    navigation menu entry.

    Attributes:
        position - Determines the order in which to display the navigation menu items.
                   The item with the lowest position value should be the first displayed,
                   largest position value should be the last displayed.

        display_text - The text which will be visible in the navigation menu.

        reference_url_name - The name of the url which the navigation menu item references.
                             This name should be in one of the url confs.
    """
    position = models.PositiveIntegerField()
    display_text = models.CharField(max_length=25)
    reference_url_name = models.CharField(max_length=75)

    def __str__(self):
        return self.display_text



class PostImage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="image")
    parent = models.ForeignKey('BasicPost', on_delete=models.CASCADE, null=True)



class BasicPost(models.Model):
    body_markdown = models.TextField()
    body_html = models.TextField()

    def convert_markdown(self):
        """
        Converts the body_markdown to html. This code is a modified version of
        Ole Morten Halvorsen's implementation, found here:
        http://www.omh.cc/blog/2008/aug/18/django-inserting-and-positioning-images/
        """
        image_refs = ""

        for image in self.postimage_set.all():
            image_url = image.image.url
            image_refs += '\n[{0}]: {1}'.format(image.name, image_url)

        return markdown.markdown('{0}\n{1}'.format(self.body_markdown, image_refs))

    def save(self):
        self.body_html = self.convert_markdown()
        super(BasicPost, self).save()



class TitledBasicPost(BasicPost):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
