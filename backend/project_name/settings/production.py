from .base import *


DEBUG = False

SECRET_KEY = env("SECRET_KEY")
ALLOWED_HOSTS = env("ALLOWED_HOSTS", "*").split(",")

DATABASES["default"]["ATOMIC_REQUESTS"] = True

STATIC_URL = "static/"
STATIC_ROOT = base_dir_join("staticfiles")

MEDIA_ROOT = base_dir_join("mediafiles")
MEDIA_URL = "/media/"

# Celery
CELERY_BROKER_URL = env("CELERY_BROKER_URL", default="")
CELERY_RESULT_BACKEND = env("REDIS_URL")
CELERY_SEND_TASK_ERROR_EMAILS = True

# Whitenoise
# STORAGES = {
#     "default": {
#         "BACKEND": "django.core.files.storage.FileSystemStorage",
#     },
#     "staticfiles": {
#         "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
#     },
# }

CORS_ALLOWED_ORIGINS = env("CORS_ALLOWED_ORIGINS", "").split(",")
CSRF_TRUSTED_ORIGINS = env("CSRF_TRUSTED_ORIGINS", "").split(",")
