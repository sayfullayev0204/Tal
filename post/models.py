from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from django.contrib import admin
from parler.admin import TranslatableAdmin
from embed_video.fields import EmbedVideoField

# Model
class Yangiliklar(TranslatableModel):
    translations = TranslatedFields(
        sarlavha=models.CharField(max_length=255, verbose_name="Sarlavha"),
        matn=models.TextField(verbose_name="Matn"),
    )
    main_image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name="Asosiy rasm")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Sana")

    def __str__(self):
        return self.safe_translation_getter("sarlavha", any_language=True) or "No Title"


class Image(models.Model):
    article = models.ForeignKey(Yangiliklar, related_name='images', on_delete=models.CASCADE, verbose_name="Yangilik")
    image = models.ImageField(upload_to='images/', verbose_name="Qo'shimcha rasm")

    def __str__(self):
        return f"Image for {self.article.safe_translation_getter('sarlavha', any_language=True) or 'No Title'}"

class Videolar(TranslatableModel):
    translations = TranslatedFields(
        sarlavha = models.CharField(max_length=200),
        matn = models.TextField(blank=True,null=True)
    )
    video = models.URLField()
    date = models.DateField(auto_now_add=True)

class OAV(TranslatableModel):
    translations = TranslatedFields(
        sarlavha = models.CharField(max_length=200),
    )
    audio = models.FileField(blank=True, upload_to='oav')
    file = models.FileField(blank=True, upload_to='oav')
    date = models.DateField(auto_now_add=True)

class Tabrik(TranslatableModel):
    translations = TranslatedFields(
        sarlavha = models.CharField(max_length=200),
        matn = models.TextField(blank=True,null=True)
    )
    date = models.DateField(auto_now_add=True)

class Elon(TranslatableModel):
    translations = TranslatedFields(
        sarlavha = models.CharField(max_length=200),
        matn = models.TextField(),
        file = models.FileField(blank=True, upload_to='elon')
    )
    date = models.DateField(auto_now_add=True)

class Turi(TranslatableModel):
    translations = TranslatedFields(
        nomi = models.CharField(max_length=500)
    )
    def __str__(self) -> str:
        return self.nomi

class Korporativ(TranslatableModel):
    turi = models.ForeignKey(Turi, on_delete=models.CASCADE)
    translations = TranslatedFields(
        nomi = models.CharField(max_length=200),
        image = models.ImageField(upload_to='korpo/', null=True, blank=True),
        file = models.FileField(upload_to='korpo/', blank=True,null=True),
        matn = models.TextField(blank=True, null=True)
    )
    date = models.DateField(auto_now_add=True)

class Intraktiv(TranslatableModel):
    translations = TranslatedFields(
        nomi = models.CharField(max_length=200),
        image = models.ImageField(upload_to='intrak/', null=True, blank=True),
        file = models.FileField(upload_to='intrak/', blank=True,null=True),
        matn = models.TextField(blank=True, null=True)
    )
    date = models.DateField(auto_now_add=True)
