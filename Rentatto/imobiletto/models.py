from django.db import models

class Proprietario(models.Model):
	nome = models.CharField()
	documento = models.CharField()
	tel1 = models.CharField()
	tel2 = models.CharField()
	email = models.CharField()


class Imovel(models.Model):
	TIPO_IMOVEL = ((COMERCIAL, 'Comercial'), (RESIDENCIAL, 'Residencial'))
	TIPO_RESIDENCIAL = ((APARTAMENTO, 'Apartamento'), (CASA, 'Casa'), (COBERTURA, 'Cobertura'))
	TIPO_COMERCIAL = ((SALA, 'Sala'), (LOJA, 'Loja'), (GALERIA, 'Galeria'))
	
	flag_available = models.BooleanField()
	valor_condominio = models.FloatField()
	valor_aluguel = models.FloatField()
	valor_iptu = models.FloatField()
	quartos = models.IntegerField()
	banheiros = models.IntegerField()
	salas = models.IntegerField()
	vagas_garagem = models.IntegerField()
	proprietario = models.ForeignKey(Proprietario)
