from django.contrib import admin


from .models import (
    CustomUser,
    Theory,
    Scientist
)

admin.site.register(Scientist)
admin.site.register(Theory)
admin.site.register(CustomUser)


