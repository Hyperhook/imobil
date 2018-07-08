from django.db import models

class Proprietario(models.Model):
	nome = models.CharField(max_length=80, blank=False)
	documento = models.CharField(max_length=20, blank=False)
	tel1 = models.CharField(max_length=20, blank=True)
	tel2 = models.CharField(max_length=20, blank=True)
	email = models.EmailField(blank=True)

	def __str__(self):
		return self.nome	


class Imovel(models.Model): 
	flag_available = models.BooleanField(default=True, blank=True)
	valor_condominio = models.DecimalField(max_digits=8, decimal_places=2, blank=False)
	valor_aluguel = models.DecimalField(max_digits=8, decimal_places=2, blank=False)
	valor_iptu = models.DecimalField(max_digits=8, decimal_places=2, blank=False)
	quartos = models.PositiveSmallIntegerField(blank=True)
	banheiros = models.PositiveSmallIntegerField(blank=True)
	salas = models.PositiveSmallIntegerField(blank=True)
	vagas_garagem = models.PositiveSmallIntegerField(blank=True)
	proprietario = models.OneToOneField(Proprietario, related_name='%(class)s_proprietario', on_delete='CASCADE')
	data_criacao = models.DateTimeField(auto_now_add=True)

	class Meta:
		abstract = True


class ImovelResidencial(Imovel):
	TIPO_IMOVEL_CHOICES = (('APT', 'Apartamento'), ('CASA', 'Casa'), ('COBERTURA', 'Cobertura'))
	tipo_imovel = models.CharField(max_length=12, choices=TIPO_IMOVEL_CHOICES)

	def __str__(self):
		return self.tipo_imovel



class ImovelComercial(Imovel):
	TIPO_IMOVEL_CHOICES = (('SALA', 'Sala'), ('LOJA', 'Loja'), ('GALERIA', 'Galeria'))
	tipo_imovel = models.CharField(max_length=12, choices=TIPO_IMOVEL_CHOICES)

	def __str__(self):
		return self.tipo_imovel