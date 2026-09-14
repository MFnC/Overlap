from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='resultadogp',
            index=models.Index(fields=['escuderia', 'circuito'], name='core_result_escuder_3a12ab_idx'),
        ),
    ]