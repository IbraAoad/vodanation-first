from django.contrib import admin
from ro_app.models import SiteData

from ro_app.models import ConsVals,ReqVals,StatVals,SiteVals,BuilVals,ActVals,StarVals


# Register your models here.
admin.site.register(ConsVals)
admin.site.register(ReqVals)
admin.site.register(StatVals)
admin.site.register(SiteVals)
admin.site.register(BuilVals)
admin.site.register(ActVals)
admin.site.register(StarVals)

class SiteDataAdmin(admin.ModelAdmin):
    readonly_fields = ('updated_at',)

admin.site.register(SiteData, SiteDataAdmin)
