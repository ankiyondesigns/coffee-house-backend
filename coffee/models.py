from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class CoffeeProduct(models.Model):
    MEASUREMENT_CHOICES = [
        ('kg', 'Kilograms'),
        ('mg', 'Milligrams'),
        ('g', 'Grams'),
    ]

    image = models.ImageField(upload_to='coffee_products/')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    #name = models.CharField(max_length=255, null=True, blank=True)
    #description = models.TextField(null=True, blank=True)
    measurement_value = models.PositiveIntegerField(null=True, blank=True)
    measurement_unit = models.CharField(
        max_length=2,
        choices=MEASUREMENT_CHOICES,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.measurement_unit



class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
                        .filter(status=Post.Status.PUBLISHED)

class Post(models.Model):
    
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    
    
    banner = models.ImageField(upload_to='blog_banner/')
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='blog_posts')
    #body = models.TextField()
    body = RichTextUploadingField(blank=True, null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                                choices=Status.choices,
                                default=Status.DRAFT)
    

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    class Meta:
        ordering = ['-publish']
        indexes = [
                    models.Index(fields=['-publish']),
        ]
    
    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse('post_detail',
                                args=[self.slug])