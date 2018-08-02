from app_plug.service import v1
from app01 import models


v1.site.register(models.UserInfo)
v1.site.register(models.Article)

print('success_app01')
