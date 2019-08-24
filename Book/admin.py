from django.contrib import admin

from Book.models import Books, Authors, Publications

admin.site.register(Books)
admin.site.register(Authors)
admin.site.register(Publications)
