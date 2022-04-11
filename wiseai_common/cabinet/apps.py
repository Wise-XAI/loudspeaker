from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CabinetConfig(AppConfig):
    name = 'wiseai_common.cabinet'
    verbose_name = _("Cabinet")
    default_auto_field = 'django.db.models.BigAutoField'
