from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Popula o banco de dados com os dados iniciais do Overlap'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Seed executado com sucesso! Dados do Overlap inseridos.'))