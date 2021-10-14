from django.contrib import admin
from . models import *
# Register your models here.


admin.site.register(A_Home)
admin.site.register(B_About)
admin.site.register(C_Skil_text)
admin.site.register(D_Skil)
admin.site.register(E_resume_text)
admin.site.register(F_Summary)
admin.site.register(G_Education)
admin.site.register(H_Services_text)
admin.site.register(I_Services)
admin.site.register(J_Portfolio_text)
admin.site.register(K_Portfolio)
admin.site.register(L_Contact)
admin.site.register(A_Links)


@admin.register(M_message)
class Message(admin.ModelAdmin):
    list_display = ['name', 'email']