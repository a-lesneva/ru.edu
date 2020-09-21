from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import School


class SchoolsViewSitemap(Sitemap):
    def items(self):
        return ['schools:schools']

    def location(self, item):
        return reverse(item)
