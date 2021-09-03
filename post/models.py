from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User

from django.utils.text import slugify

from django.shortcuts import reverse

from django.db.models.signals import pre_save


class PublishedManager(models.Manager):
    """Published manager ...."""

    def get_queryset(self):
        """Query set filter according to publish..."""
        return super(PublishedManager,
                     self).get_queryset()\
                     .filter(status='published')


class Post(models.Model):
    """Post database model ...."""

    STATUS_CHOICES = (('draft', 'Draft'),
                      ('published', 'Published'),
                      )

    title = models.CharField(max_length=100)

    slug = models.SlugField(max_length=230,
                            unique_for_date='publish')

    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')

    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='draft')

    objects = models.Manager()

    published = PublishedManager()  # Our custom manager.

    class Meta:
        """meta class .."""

        ordering = ('-publish',)

    def __str__(self):
        """Resturn object name ..."""
        return self.title

    def get_absolute_url(self):
        """Revarse url mapping..."""
        try:
            return reverse("posts_api:post_detail", kwargs={"slug": self.slug})
        except:
            None

    @property
    def comments(self):
        """Resturn queryset of comment..."""
        instance = self
        qs = Comment.objects.filter(post=instance)
        return qs


def create_sluge_default(instance, new_sluge=None):
    """Creating sluge field through title..."""
    slug = slugify(instance.title)

    if new_sluge:
        slug = new_sluge
    qs = Post.objects.filter(slug=slug).order_by("-id")

    if qs.exists():
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_sluge_default(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    """Pre_save and then trigger..."""
    if not instance.slug:
        instance.slug = create_sluge_default(instance)


pre_save.connect(pre_save_post_receiver, sender=Post)  # save and call the pre_save_post_reciver_function


class Comment(models.Model):
    """comment database ..."""

    parent = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        """Meta class..."""

        ordering = ["-created_at", "-updated_at"]
