from common.models import GalleryImage, MarkdownModel
from django.db import models



class Equipment(MarkdownModel):
    """
    A piece of equipment.
    Attributes:
        position - Determines the order in which to display on the page. The equipment
                   with the lowest position value should be the first displayed,
                   largest position value should be the last displayed.

        name - Title for the equipment.

        description_brief - A brief description to display with a thumbnail for the
                            overview.

        thumbnail - The image to display with description_brief, also good for use in
                    a header on the detail page.

        markdown - Inherited form MarkdownModel. The markdown for an extended description.

        html - Inherited from MarkdownModel. The html of markdown.
    """
    position = models.PositiveIntegerField()
    name = models.CharField(max_length=200)
    short_desc = models.CharField(max_length=1500)
    thumbnail = models.ImageField(upload_to="images/thumbnails")

    def __str__(self):
        return self.name



class EquipmentGalleryImage(GalleryImage):
    """
    Images to be displayed in a gallery for a peice of equipment.
    """
    parent = models.ForeignKey(Equipment, on_delete=models.CASCADE)
