from django.contrib import admin
from .models import (
    GeneralSettinModel,
    ImageModel,
    SkillModel,
    SkillTypeModel,
    SocialModel,
    Document,
    Messages,
)


@admin.register(GeneralSettinModel)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "parameter",
        "description",
        "updated",
        "created",
    ]
    list_filter = ["name", "parameter", "updated", "created"]
    search_fields = ["name", "parameter", "updated", "created"]
    list_editable = ["parameter", "description"]
    list_per_page = 10
    date_hierarchy = "created"


@admin.register(ImageModel)
class ImageModelAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "image_tag",
        "updated",
        "created",
    ]


@admin.register(SkillModel)
class SkillModelAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "updated",
        "created",
    ]


@admin.register(SkillTypeModel)
class SkillTypeModelAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "updated",
        "created",
    ]


@admin.register(SocialModel)
class SocialModelAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "link",
        "icon",
        "updated",
        "created",
    ]
    list_filter = ["id", "link", "updated", "created"]
    search_fields = ["id", "link", "updated", "created"]
    list_editable = [
        "link",
        "icon",
    ]


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "order",
        "document",
        "slug",
        "document_text",
        "updated",
        "created",
    ]
    list_filter = ["id", "slug", "updated", "created"]
    search_fields = ["id", "slug", "updated", "created"]
    list_editable = [
        "slug",
        "order",
        "document",
        "document_text",
    ]
    prepopulated_fields = {"slug": ("slug",)}


@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "email",
        "subject",
        "message",
        "updated",
        "created",
    ]
    list_filter = ["id", "name", "email", "updated", "created"]
    search_fields = ["id", "name", "email", "updated", "created"]
    list_editable = [
        "name",
        "email",
        "subject",
        "message",
    ]
    list_per_page = 10
    date_hierarchy = "created"
