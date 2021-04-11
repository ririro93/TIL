# admin

## Referencing a Foreign Key Field
> [stackoverflow](https://stackoverflow.com/questions/163823/can-list-display-in-a-django-modeladmin-display-attributes-of-foreignkey-field)

- `short_description` is useful to remember too
```python
class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ['title', 'get_name', ]

    def get_name(self, obj):
        return obj.author.name
    get_name.admin_order_field  = 'author'  #Allows column order sorting
    get_name.short_description = 'Author Name'  #Renames column head

    #Filtering on side - for some reason, this works
    #list_filter = ['title', 'author__name']

admin.site.register(Book, BookAdmin)
```