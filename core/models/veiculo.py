from django.db import models


class Veiculo(models.Model):
    ano = models.IntegerField(blank=True, default=0)
    preco = models.DecimalField(max_digits=7, decimal_places=2, blank=True, default=0)
    modelo = models.ForeignKey('Modelo', on_delete=models.PROTECT, blank=True, null=True, related_name='veiculos')
    cor = models.ForeignKey('Cor', on_delete=models.PROTECT, blank=True, null=True, related_name='veiculos')
    acessorios = models.ManyToManyField('Acessorio', blank=True, related_name='veiculos')

    def __str__(self):
        return f'{self.modelo} - {self.ano}'
