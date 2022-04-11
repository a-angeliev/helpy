from django.core.exceptions import ValidationError


def validate_image(image):
    file_size = image.file.size
    limit_mb = 10
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError(f"Max size of file is {limit_mb} KB")