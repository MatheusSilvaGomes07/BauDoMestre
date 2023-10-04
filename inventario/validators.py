from django.core.exceptions import ValidationError
import os

def validate_file_extension(value):
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.pdf', '.doc', '.docx', '.txt']
    ext = os.path.splitext(value.name)[1]
    if not ext.lower() in valid_extensions:
        raise ValidationError('Este tipo de arquivo não é suportado. As extensões permitidas são: .jpg, .jpeg, .png, .gif, .pdf, .doc, .docx, .txt')
