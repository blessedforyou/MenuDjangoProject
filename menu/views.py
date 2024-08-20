from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "menu/index.html"


class ProductView(TemplateView):
    template_name = "product/product.html"


class ServiceView(TemplateView):
    template_name = 'service/service.html'


class InfoView(TemplateView):
    template_name = 'info/project-info.html'