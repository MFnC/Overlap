from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Circuito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=50)),
                ('voltas', models.IntegerField(default=50)),
            ],
        ),
        migrations.CreateModel(
            name='Escuderia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('orcamento', models.DecimalField(decimal_places=2, default=1000000.0, max_digits=12)),
                ('pontos', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Peca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('tipo', models.CharField(choices=[('piloto', 'Piloto'), ('chassi', 'Chassi'), ('motor', 'Motor'), ('chefe', 'Chefe de Equipe'), ('mecanico', 'Mecânicos')], max_length=20)),
                ('desempenho_base', models.IntegerField(default=70)),
            ],
        ),
        migrations.CreateModel(
            name='ResultadoGP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posicao', models.IntegerField()),
                ('pontos_ganhos', models.IntegerField()),
                ('circuito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.circuito')),
                ('escuderia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resultados', to='core.escuderia')),
            ],
        ),
    ]