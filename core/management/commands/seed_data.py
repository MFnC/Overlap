from django.core.management.base import BaseCommand
from core.models import Escuderia, Peca, Circuito

class Command(BaseCommand):
    help = 'Popula o banco de dados com os dados iniciais do Overlap'

    def handle(self, *args, **options):
        self.stdout.write('Criando dados iniciais...')

        # Criar Escuderia do jogador por padrao
        Escuderia.objects.get_or_create(nome='Overlap Racing', orcamento=5000000.00)

        # Criar Circuitos
        circuitos = [
            {'nome': 'Interlagos', 'pais': 'Brasil', 'voltas': 71},
            {'nome': 'Monza', 'pais': 'Itália', 'voltas': 53},
            {'nome': 'Silverstone', 'pais': 'Reino Unido', 'voltas': 52},
            {'nome': 'Monaco', 'pais': 'Mônaco', 'voltas': 78},
        ]
        for c in circuitos:
            Circuito.objects.get_or_create(**c)

        # Criar Peças Históricas (Draft)
        pecas = [
            {'nome': 'Ayrton Senna (1988)', 'tipo': 'piloto', 'desempenho_base': 98},
            {'nome': 'Max Verstappen (2023)', 'tipo': 'piloto', 'desempenho_base': 97},
            {'nome': 'Lewis Hamilton (2020)', 'tipo': 'piloto', 'desempenho_base': 96},
            {'nome': 'RB19 (Red Bull 2023)', 'tipo': 'chassi', 'desempenho_base': 99},
            {'nome': 'MP4/4 (McLaren 1988)', 'tipo': 'chassi', 'desempenho_base': 98},
            {'nome': 'Motor Honda V6 Turbo (2023)', 'tipo': 'motor', 'desempenho_base': 95},
            {'nome': 'Motor Ferrari V12 (1995)', 'tipo': 'motor', 'desempenho_base': 90},
            {'nome': 'Adrian Newey', 'tipo': 'chefe', 'desempenho_base': 99},
        ]
        for p in pecas:
            Peca.objects.get_or_create(**p)

        self.stdout.write(self.style.SUCCESS('Seed executado com sucesso! Banco populado.'))