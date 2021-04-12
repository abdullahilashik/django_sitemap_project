from django.contrib.sitemaps import Sitemap
from .models import Blog

class BlogSitemap(Sitemap):

    changefreq = 'daily'
    priority = 1
    
    def items(self):
        return Blog.objects.all()
    
    def location(self, item):
        return '/details/' + str(item.id)

class StaticSitemap(Sitemap):
    changefreq = 'never'
    priority = 0.7

    def items(self):
        return ['/home','/contact']
    
    def location(self,item):
        return item