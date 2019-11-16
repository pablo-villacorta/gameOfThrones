from django.contrib import admin
from lore.models import Character, Relationship, Sibling, House, Allegiance

# Register your models here.
admin.site.register(Character)
admin.site.register(Relationship)
admin.site.register(Sibling)
admin.site.register(House)
admin.site.register(Allegiance)

