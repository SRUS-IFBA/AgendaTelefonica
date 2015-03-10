from contato.models import Contato, Telefone
from django.contrib import admin

class TelefoneInline(admin.TabularInline):
    model = Telefone
    extra = 0
	
class ContatoAdmin(admin.ModelAdmin):
    model = Contato
    list_display = ['contato_nome', 'contato_email']
    search_fields = ['contato_nome']
    inlines = [TelefoneInline]
    save_on_top = True
admin.site.register(Contato, ContatoAdmin)
	
	


