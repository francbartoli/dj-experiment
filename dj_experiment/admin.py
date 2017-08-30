from django.contrib import admin

from .models import (Case, CaseBelongingness, CaseKeyValue, Catalog, Dataset,
                     Experiment, FieldBelongingness, FieldGroup, FieldKeyValue,
                     Value)

admin.site.register(Experiment)
admin.site.register(Case)
admin.site.register(FieldGroup)
admin.site.register(Catalog)
admin.site.register(Value)
admin.site.register(CaseKeyValue)
admin.site.register(FieldKeyValue)
admin.site.register(Dataset)
admin.site.register(CaseBelongingness)
admin.site.register(FieldBelongingness)
