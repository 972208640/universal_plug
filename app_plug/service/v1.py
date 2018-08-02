from django.http import HttpResponse


class BasePlugModel:
    def __init__(self, model_class, site):
        self.model_class = model_class
        self.site = site

    def another_urls(self):
        """
        钩子函数，用于自定义额外的URL
        :return:
        """
        return []

    def get_urls(self):
        """
        配置最后一段URL用于增删改查等操作
        :return:
        """
        from django.urls import re_path
        # 获取包名和类名,方便日后反向生成URL
        info = self.model_class._meta.app_label, self.model_class._meta.model_name
        urlpatterns = [
            re_path(r'^$', self.list_view, name='%s_%s_list' % info),
            re_path(r'^add/$', self.add_view, name='%s_%s_add' % info),
            re_path(r'^(.+)/delete/$', self.delete_view, name='%s_%s_delete' % info),
            re_path(r'^(.+)/change/$', self.change_view, name='%s_%s_change' % info),
            # re_path(r'^(.+)/detail/$', self.detail_view, name='%s_%s_detail' % info),
        ]
        urlpatterns += self.another_urls()
        return urlpatterns

    @property
    def urls(self):
        return self.get_urls()

    def list_view(self, request):
        """
        查
        :param request:
        :return:
        """
        info = self.model_class._meta.app_label, self.model_class._meta.model_name
        data = '%s_%s_list' % info
        return HttpResponse(data)

    def add_view(self, request):
        """
        增
        :param request:
        :return:
        """
        info = self.model_class._meta.app_label, self.model_class._meta.model_name
        data = '%s_%s_add' % info
        return HttpResponse(data)

    def delete_view(self, request, pk):
        """
        删
        :param request:
        :return:
        """
        info = self.model_class._meta.app_label, self.model_class._meta.model_name
        data = '%s_%s_delete' % info
        return HttpResponse(data)

    def change_view(self, request, pk):
        """
        改
        :param request:
        :return:
        """
        info = self.model_class._meta.app_label, self.model_class._meta.model_name
        data = '%s_%s_change' % info
        return HttpResponse(data)


class AppPlugSite(object):
    def __init__(self):
        self._registry = {}
        self.app_name = "app_plug"
        self.namespace = "app_plug"

    def register(self, model_class, app_plug_model_class=BasePlugModel):
        self._registry[model_class] = app_plug_model_class(model_class, self)

    def get_urls(self):
        """
        封装url至列表
        :return: 装有url的列表
        """
        from django.conf.urls import include
        from django.urls import re_path
        # urlpatterns变量名不能更改，因为include内部实现寻找url时就是查找urlpatterns变量获取
        urlpatterns = [
            # url(r'^$', self.index, name='index'),
            re_path(r'^login/$', self.login, name='login'),
            re_path(r'^logout/$', self.logout, name='logout'),
        ]
        # 根据model动态生成URL
        for model_class, plug_model_obj in self._registry.items():
            # 获取包名和类名
            app_label = model_class._meta.app_label
            model_name = model_class._meta.model_name
            # 拼接URL
            urlpatterns += [re_path(r'^%s/%s/' % (app_label, model_name), include(plug_model_obj.urls)), ]
        return urlpatterns

    @property
    def urls(self):
        """
        创建URL对应关系
        :return: 元组类型：url关系列表或模块（模块内部必须有urlpatterns属性）；app_name；namespace
        """

        return self.get_urls(), self.app_name, self.namespace

    def login(self, request):
        return HttpResponse('login-success')

    def logout(self, request):
        return HttpResponse('logout-success')


site = AppPlugSite()
