import os
from django.core.exceptions import ValidationError


def validate_logo_size(image):
    size = image.size
    max_size = 8 * 1024 * 1024
    if size and size > max_size:
        raise ValidationError("Размер изображения превышает 8 Мбайт")


def logo_upload_path(instance, filename):
    return os.path.join("company_logos", str(instance.owner.id), filename)
