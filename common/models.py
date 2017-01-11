from django.db import models
import markdown



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
