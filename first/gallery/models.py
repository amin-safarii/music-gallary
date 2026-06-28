from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='artist/', blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    instagram = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    slug = models.SlugField(unique=True, blank=True)
    main_post = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    aparat_embed_code = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class SiteTheme(models.Model):
    THEME_CHOICES = [
        ('dark_luxury',   '🌑 Dark Luxury — تاریک و طلایی'),
        ('midnight_blue', '🌊 Midnight Blue — آبی نفتی'),
        ('ivory_classic', '🌿 Ivory Classic — روشن و کلاسیک'),
        ('deep_emerald',  '💎 Deep Emerald — زمردی تیره'),
        ('crimson_night', '🔴 Crimson Night — قرمز تیره'),
    ]

    theme = models.CharField(
        max_length=30,
        choices=THEME_CHOICES,
        default='dark_luxury',
        verbose_name='تم سایت'
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'تم سایت'
        verbose_name_plural = 'تنظیمات تم'

    def __str__(self):
        return self.get_theme_display()

    @classmethod
    def get_active(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj.theme
