import os
from django.core.exceptions import ValidationError


def validate_avatar_size(image):
    size = os.path.getsize(image)
    size_mbites = size/(1024*1024)
    max_size = 8
    if size_mbites and size_mbites>max_size:
        raise ValidationError('Размер изображения превышает 8 Мбайт')

def avatar_upload_path(instance, filename):
    return os.path.join("avatars", str(instance.user.id), filename)