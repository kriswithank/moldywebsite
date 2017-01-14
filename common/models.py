from django.db import models
import markdown



class GalleryImage(models.Model):
    """
    Abstract base class for gallery images.

    Recommended when implementing: have a parent ForeignKey field.

    Attributes:
        position - Determines the order in which to display the images in the gallery.
                   The category with the lowest position value should be displayed first,
                   the largest position value should be displayed last.
        title - A title that might be displayed to users in the gallery.
        info - A caption or other misc info that may be displayed to users in the gallery.
        image - The image that is to be displayed.
    """
    position = models.PositiveIntegerField()
    title = models.CharField(max_length=500)
    info = models.TextField()
    image = models.ImageField(upload_to='images/galleries')

    class Meta:
        abstract = True



class MarkdownImage(models.Model):
    """
    An image that is assosiated with a MarkdownModel.
    """
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images')
    parent = models.ForeignKey('MarkdownModel', on_delete=models.CASCADE)



class MarkdownModel(models.Model):
    """
    A base class for models which require a simple markdown field.

    Can't be made abstract since MarkdownImage references MarkdownModel.
    """
    markdown = models.TextField()
    html = models.TextField()

    def convert_markdown(self):
        """
        Converts the body_markdown to html. This code is a modified version of
        Ole Morten Halvorsen's implementation, found here:
        http://www.omh.cc/blog/2008/aug/18/django-inserting-and-positioning-images/
        """
        image_refs = ''

        for image in self.markdownimage_set.all():
            image_url = image.image.url
            image_refs += '\n[{0}]: {1}'.format(image.name, image_url)

        return markdown.markdown('{0}\n{1}'.format(self.body_markdown, image_refs))

    def save(self):
        self.body_html = self.convert_markdown()
        super(MarkdownModel, self).save()
