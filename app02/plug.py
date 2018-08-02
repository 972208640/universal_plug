from app_plug.service import v1
from app02 import models


v1.site.register(models.Plane)

print('success_app02')
