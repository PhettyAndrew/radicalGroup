from django.contrib import admin
from .models import Info, Team, Building, Components, Plan, Subscribe

# Register your models here.
admin.site.register(Info)
admin.site.register(Team)
admin.site.register(Building)
admin.site.register(Components)
admin.site.register(Plan)
admin.site.register(Subscribe)
