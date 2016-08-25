from common.models import TitledBasicPost
from django.db import models



class Equipment(models.Model):
    """
    A class model for a piece of equipment, extends TitledBasicPost.
    Attributes:
        position - Determines the order in which to display on the page. The equipment
                   with the lowest position value should be the first displayed,
                   largest position value should be the last displayed.

        name - What the piece of equipment is refered to as.

        description_brief - A brief description to display with a thumbnail for the
                            overview.

        thumbnail - The image to display with description_brief, also good for use in
                    a header on the detail page.
    """
    position = models.PositiveIntegerField()
    name = models.CharField(max_length=200)
    description_brief = models.CharField(max_length=1500)
    thumbnail = models.ImageField(upload_to="images/thumbnails")


class EquipmentGalleryImage(models.Model):
    """
    A class model for an image which is a part of the gallery of a piece of equipment.

    Attributes:
        position - Determines the order in which to display on the page. The equipment
                   with the lowest position value should be the first displayed,
                   largest position value should be the last displayed.

        parent - The piece of equipment to which the image belongs.
    """
    position = models.PositiveIntegerField()
    image = models.ImageField(upload_to="image")
    parent = models.ForeignKey(Equipment, on_delete=models.CASCADE)



class EquipmentLongDescriptionSection(TitledBasicPost):
    """
    A clone of a titled basic post, used so that a reverse relationship could be used.

    Attributes:
        position - Determines the order in which to display on the page. The equipment
                   with the lowest position value should be the first displayed,
                   largest position value should be the last displayed.

        parent - The piece of equipment to which the image belongs.
    """
    position = models.PositiveIntegerField()
    parent = models.ForeignKey(Equipment, on_delete=models.CASCADE)
