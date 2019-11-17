from django.contrib import admin
from app.models import Character, Relationship, Sibling, House, Allegiance, User, Thread, Post

# Register your models here.
admin.site.register(Character)
admin.site.register(Relationship)
admin.site.register(Sibling)
admin.site.register(House)
admin.site.register(Allegiance)
admin.site.register(User)
admin.site.register(Thread)
admin.site.register(Post)

