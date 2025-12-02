from django.conf import settings

if settings.DEBUG:
    from django.core.files.storage import FileSystemStorage

    class MediaStorage(FileSystemStorage):
        fileoverwrite = False
        default_acl = "public-read"

    class DocumentStorage(FileSystemStorage):
        fileoverwrite = False
        default_acl = "public-read"

    class ImageSettingStorage(FileSystemStorage):
        fileoverwrite = False
        default_acl = "public-read"

else:
    from storages.backends.s3boto3 import S3Boto3Storage

    class MediaStorage(S3Boto3Storage):
        fileoverwrite = False
        default_acl = "public-read"
        location = settings.MEDIA_LOCATION

    class DocumentStorage(S3Boto3Storage):
        location = settings.DOCUMENT_LOCATION
        fileoverwrite = False
        default_acl = "public-read"

    class ImageSettingStorage(S3Boto3Storage):
        location = settings.IMAGE_SETTING_LOCATION
        fileoverwrite = False
        default_acl = "public-read"
