from common.models import Image, TitledBasicPost
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

        description_long - The expanded post about the equipment and what it can do,
                           should have multiple sections

        thumbnail - The image to display with description_brief, also good for use in
                    a header on the detail page.
    """
    position = models.PositiveIntegerField()
    name = models.CharField(max_length=200)
    description_brief = models.CharField(max_length=1500)
    description_long = models.ForeignKey(TitledBasicPost, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to="images/thumbnails")



class EquipmentGalleryImage(Image):
    """
    A class model for an image which is a part of the gallery of a piece of equipment.

    Attributes:
        position - Determines the order in which to display on the page. The equipment
                   with the lowest position value should be the first displayed,
                   largest position value should be the last displayed.

        gallery_subject - The piece of equipment to which the image belongs.
    """
    position = models.PositiveIntegerField()
    gallery_subject = models.ForeignKey(Equipment, on_delete=models.CASCADE)
