from django.db import models
from django.utils.text import slugify
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class JournalPost(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = JournalPost.objects.all().filter(slug__iexact=original_slug).count()

        count = 1
        slug = original_slug
        while queryset:
            slug = f"{original_slug}-{count}"
            count += 1
            queryset = Journal.objects.all().filter(slug__iexact=slug).count()

        self.slug = slug

        super(JournalPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title