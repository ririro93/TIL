# SITE_ID
>[stackoverflow](https://stackoverflow.com/questions/25468676/django-sites-model-what-is-and-why-is-site-id-1)

- this shows which site this application will use when there are multiple sites. The default is set to `example.com`. 
- must create a diff settings file with each SITE_ID
- must change this to use allauth features
- to see the id of each site in admin
    ```python
    from django.contrib import admin
    from django.contrib.sites.models import Site

    admin.site.unregister(Site)
    class SiteAdmin(admin.ModelAdmin):
        fields = ('id', 'name', 'domain')
        readonly_fields = ('id',)
        list_display = ('id', 'name', 'domain')
        list_display_links = ('name',)
        search_fields = ('name', 'domain')
    admin.site.register(Site, SiteAdmin)
    ```

