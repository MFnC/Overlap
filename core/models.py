from django.db import models

class Escuderia(models.Model):
    nome = models.CharField(max_length=100)
    orcamento = models.DecimalField(max_digits=12, decimal_places=2, default=1000000.00)
    pontos = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

class Peca(models.Model):
    TIPO_CHOICES = [
        ('piloto', 'Piloto'),
        ('chassi', 'Chassi'),
        ('motor', 'Motor'),
        ('chefe', 'Chefe de Equipe'),
        ('mecanico', 'Mecânicos'),
    ]
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    desempenho_base = models.IntegerField(default=70)

    def __str__(self):
        return f"{self.nome} ({self.tipo})"

class Circuito(models.Model):
    nome = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    voltas = models.IntegerField(default=50)

    def __str__(self):
        return self.nome

class ResultadoGP(models.Model):
    escuderia = models.ForeignKey(Escuderia, on_delete=models.CASCADE, related_name='resultados')
    circuito = models.ForeignKey(Circuito, on_delete=models.CASCADE)
    posicao = models.IntegerField()
    pontos_ganhos = models.IntegerField()

    class Meta:
        indexes = [
            models.Index(fields=['escuderia', 'circuito']),
        ]