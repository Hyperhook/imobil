from django.db import models


class ProprietarioQuerySet(models.QuerySet):
    def com_cnpj(self):
        return self.filter(documento__regex=r'.{14}.*')

    def com_cpf(self):
        return self.filter(documento__regex=r'.{11}.*')


class ImovelQuerySet(models.QuerySet):
    def disponivel(self):
        return self.filter(flag_available=True)

    def com_garagem(self):
        return self.filter(vagas_garagem__isnull=False)
