from django.db import models

class Contato(models.Model):
	contato_id = models.AutoField(primary_key = True)
	contato_nome = models.CharField(max_length=45, verbose_name = 'Nome')
	contato_sobrenome = models.CharField(max_length=45, verbose_name = 'Sobrenome')
	contato_email = models.EmailField(max_length=255, blank=True, verbose_name='Email')
	
	def __unicode__(self):
		return self.contato_nome
	
	class Meta:
		db_table = 'contato'
		verbose_name = 'Contato'
		verbose_name_plural = 'Contatos'
		ordering = ['contato_nome']
		
class Telefone(models.Model):	
	telefone_id = models.AutoField(primary_key=True)
	telefone_numero = models.CharField(max_length=135, verbose_name='Numero')
	contato = models.ForeignKey(Contato)
	
	def __unicode__(self):
		return self.telefone_numero
	
	class Meta:
		db_table = 'telefone'
		verbose_name = 'Telefone'
		verbose_name_plural = 'telefones'
		ordering = ['telefone_numero']
