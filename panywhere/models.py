from django.core.validators import MaxLengthValidator
from django.db import models

# Create your models here.
class Comment(models.Model):
    class Meta:
        ordering = ['-posted_on']
    poster = models.CharField(max_length=255, verbose_name='Name')
    content = models.TextField(validators=[MaxLengthValidator(256**2)], verbose_name='Comment')
    posted_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "Comment by %s: \"%s\"" % (self.poster,
                                          self.content[47:]+"..."
                                          if len(self.content)>=50
                                          else self.content
        )
