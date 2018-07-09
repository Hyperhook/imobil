from django.db import models
from .managers import (ProprietarioQuerySet, ImovelQuerySet)

class Proprietario(models.Model):
	nome = models.CharField(max_length=80, blank=False)
	documento = models.CharField(max_length=20, blank=False)
	tel1 = models.CharField(max_length=20, blank=True)
	tel2 = models.CharField(max_length=20, blank=True)
	email = models.EmailField(blank=True)

	objects = ProprietarioQuerySet.as_manager()

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
	proprietario = models.OneToOneField(Proprietario, related_name='%(class)s_proprietario', on_delete=models.CASCADE)
	data_criacao = models.DateTimeField(auto_now_add=True)

	objects = ImovelQuerySet.as_manager()

	def proximos(self):
		pass
		# Aqui pensei em 2 formas de resolver:
		# 1: Utilizando a lib geopy, o que também ajudaria no form de criação de imovel,
		# já que podemos utilizar uma chamada assíncrona pra API de geo-serviços.
		# Faria uma comparação com uma QuerySet filtrada por cidade ( Não faria sentido selecionar imoveis
		# proximos se estão em outra cidade ) e calcularia a distancia:
		# geopy.distance.distance((self.lat, self.lon), (QuerySet.lat, QuerySet.lon)).km
		# 2: Fazendo o cálculo na mão: https://pt.wikipedia.org/wiki/Fórmula_de_Haversine
		# RADIO_TERRA = 6373.0
		# lat1 = radians(abs(self.lat))
		# lon1 = radians(abs(self.lon))
		# lat2 = radians(abs(QuerySetItem.lat))
		# lon2 = radians(abs(QuerySetItem.lon))
		# delta_lat = radians(self.lat) - radians(QuerySet.lat)
		# delta_lon = radians(self.lon) - radians(QuerySet.lon)
		# a = sin(delta_lat / 2)**2 + cos(lat1) * cos(lat2) * sin(delta_lon / 2)**2
		# c = 2 * atan2(sqrt(a), sqrt(1-a))
		# distancia = R * c

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


class Image(models.Model):
	imovel = models.ForeignKey(Imovel, related_name='imagens', on_delete=models.SET_NULL)
	img = models.ImageField(upload_to='caminho')
	# Nunca lidei com varias imagens sendo criadas ao mesmo tempo,
	# começaria dando uma olhada em FormSets para ver se atende, se não,
	# trataria na mão na view.