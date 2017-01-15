from common.models import GalleryImage, MarkdownModel
from django.db import models



class Product(MarkdownModel):
    """
    A model describing projects that have been completed.

    Attributes:
        position - Determines the order in which to display the products on the page.
                   The category with the lowest position value should be displayed first,
                   the largest position value should be displayed last.
        slug - The slug for the project page.
        name - The name of the product.
        short_desc - A short description to be displayed on the product index page.
        long_desc - A longer description that thoughly explains the project in depth.
                    Should be displayed on the project page.
        completion_date - The date that the project was completed. Null if unfinished.
        thumbnail - A thumbnail to be displayed on the product index page.
    """
    position = models.PositiveIntegerField()
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=1000)
    short_desc = models.TextField()
    completion_date = models.DateField(null=True)
    thumbnail = models.ImageField(upload_to='products/images/thumbnails')

    class Meta:
        ordering = ['position', 'name']

    def __str__(self):
        return self.name



class ProductGalleryImage(GalleryImage):
    """
    Images to be displayed in a gallery for a product.
    """
    parent = models.ForeignKey('Product', on_delete=models.CASCADE)
