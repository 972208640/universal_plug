class BasePlugModel:
    def __init__(self, model_class, site):
        self.model_class = model_class
        self.site = site


class AppPlugSite(object):
    def __init__(self):
        self._registry = {}
        self.app_name = "app_plug"
        self.namespace = "app_plug"

    def register(self, model_class, app_plug_model_class=BasePlugModel):
        self._registry[model_class] = app_plug_model_class(model_class, self)


site = AppPlugSite()
