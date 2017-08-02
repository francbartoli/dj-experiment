from django.contrib import admin

from .models import Case, Catalog, Experiment, FieldGroup, Value

admin.site.register(Experiment)
admin.site.register(Case)
admin.site.register(FieldGroup)
admin.site.register(Catalog)
admin.site.register(Value)
