from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "wiseai_common.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import wiseai_common.users.signals  # noqa F401
        except ImportError:
            pass
