import os
from django.core.exceptions import ValidationError


def validate_logo_size(image):
    size = os.path.getsize(image)
    size_mbites = size/(1024*1024)
    max_size = 8
    if size_mbites and size_mbites>max_size:
        raise ValidationError('Размер изображения превышает 8 Мбайт')

def logo_upload_path(instance, filename):
    return os.path.join("company_logos", str(instance.owner.id), filename)