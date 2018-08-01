from django.apps import AppConfig


class AppPlugConfig(AppConfig):
    name = 'app_plug'

    def ready(self):
        super(AppPlugConfig, self).ready()

        from django.utils.module_loading import autodiscover_modules
        autodiscover_modules('plug')
