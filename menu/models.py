from django.db import models
from django.urls import reverse


class Menu(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(unique=True, verbose_name="URL")

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"

    def __str__(self):
        return self.title

class MenuItem(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название доп. меню")
    url = models.CharField(max_length=200, blank=True, null=True, verbose_name="Прямой URL")
    named_url = models.CharField(max_length=200, blank=True, null=True, verbose_name="Именованный URL")
    menu = models.ForeignKey(to=Menu, on_delete=models.CASCADE, related_name="items", verbose_name="Меню")
    parent = models.ForeignKey(to='self', on_delete=models.CASCADE, related_name="children",
                               blank=True, null=True, verbose_name="Родительское меню")

    class Meta:
        verbose_name = "Доп. меню"
        verbose_name_plural = "Доп. меню"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.named_url:
            return reverse(self.named_url)
        return self.url