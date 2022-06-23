from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.

class Post(models.Model):

    STATUS_CHOICES = (("draft", "Draft"), ("published", "Published"))

    # DB Fields
    title = models.CharField(max_length=250)

    # slugs help the title to be displayed in the links.
    slug = models.SlugField(max_length=300, unique=True, editable=False)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="blog_posts"
    )
    body = models.TextField()

    publish = models.DateTimeField(default=timezone.now)
    # check my developer notes in README.md for links for futher reading.
    # auto_now_add only updated when it is added while auto_now is on making any changes hence their use here.
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")

    class Meta:
        # In odering, "-" denotes descending order , "" i.e no prefix denotes ascending order and "?" denotes random ordering.
        ordering = ("-publish",)

    def save(self, *args, **kwargs):
        # slugify is a function that converts any string into a slug
        self.slug = slugify(self.title)
        # call the save method of the parents 
        super().save(*args, **kwargs)
        pass

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.slug})
