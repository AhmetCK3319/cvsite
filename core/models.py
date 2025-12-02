from django.db import models
from django.utils.safestring import mark_safe
from django.core.validators import MinValueValidator, MaxValueValidator
from resume.custom_storages import DocumentStorage, ImageSettingStorage


class AbstractModel(models.Model):
    updated = models.DateTimeField(
        auto_now=True, verbose_name="güncelleme tarihi", help_text=""
    )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="oluşturulma tarihi", help_text=""
    )

    class Meta:
        abstract = True


class GeneralSettinModel(AbstractModel):
    objects = None
    name = models.CharField(
        max_length=100, verbose_name="isim", help_text="", blank=True, default=""
    )
    description = models.TextField(
        verbose_name="açıklama", help_text="", blank=True, default=""
    )
    parameter = models.CharField(
        max_length=255, verbose_name="parametre", help_text="", blank=True, default=""
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "General Setting"
        verbose_name = "General Settings"
        ordering = ["-created"]


class ImageModel(AbstractModel):
    name = models.CharField(
        max_length=100, verbose_name="isim", help_text="", blank=True, default=""
    )
    image = models.ImageField(
        storage=ImageSettingStorage(),
        verbose_name="resim",
        help_text="",
        blank=True,
        default="",
    )

    def __str__(self):
        return self.name

    def image_tag(self):
        if self.image:
            return mark_safe(
                f'<img src="{self.image.url}" style="border-radius:50px;" height="50"/>'
            )
        else:
            return ""

    image_tag.short_description = "Image"

    class Meta:
        verbose_name_plural = "Image"
        verbose_name = "Images"


class SkillTypeModel(AbstractModel):
    name = models.CharField(
        max_length=100, verbose_name="isim", help_text="", blank=True, default=""
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Skill Type"
        verbose_name = "Skill Types"


class SkillModel(AbstractModel):
    order = models.IntegerField(default=0, verbose_name="sıra", help_text="")
    name = models.CharField(
        max_length=100, verbose_name="isim", help_text="", blank=True, default=""
    )
    description = models.TextField(
        verbose_name="açıklama", help_text="", blank=True, default=""
    )
    percent = models.IntegerField(
        default=50,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name="yüzde",
    )
    skiltype = models.ForeignKey(
        SkillTypeModel,
        on_delete=models.CASCADE,
        verbose_name="skill tipi",
        help_text="",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Skill"
        verbose_name = "Skills"
        ordering = ["order"]


class SocialModel(AbstractModel):
    objects = None
    order = models.IntegerField(default=0, verbose_name="sıra", help_text="")
    link = models.URLField(
        verbose_name="link",
        help_text="Lütfen doğru url adresi giriniz..",
        blank=True,
        default="",
    )
    icon = models.CharField(
        max_length=100, verbose_name="ikon", help_text="", blank=True, default=""
    )

    def __str__(self):
        return self.link

    class Meta:
        verbose_name_plural = "Social"
        verbose_name = "Socials"
        ordering = ["order"]


class Document(AbstractModel):
    objects = None
    order = models.IntegerField(default=0, verbose_name="sıra", help_text="")
    slug = models.SlugField(
        max_length=100, verbose_name="slug", help_text="", blank=True, default=""
    )
    document_text = models.CharField(
        max_length=100,
        verbose_name="döküman metni",
        help_text="",
        blank=True,
        default="",
    )
    document = models.FileField(
        storage=DocumentStorage(),
        verbose_name="dosya",
        help_text="",
        blank=True,
        default="",
    )

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name_plural = "Document"
        verbose_name = "Documents"


class Messages(AbstractModel):
    objects = None
    name = models.CharField(
        max_length=100, verbose_name="isim", help_text="", blank=True, default=""
    )
    email = models.EmailField(
        verbose_name="email", help_text="", blank=True, default=""
    )
    subject = models.CharField(
        max_length=100, verbose_name="konu", help_text="", blank=True, default=""
    )
    message = models.TextField(
        verbose_name="mesaj", help_text="", blank=True, default=""
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Message"
        verbose_name = "Messages"
        ordering = ["-created"]
