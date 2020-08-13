# Generated by Django 3.1 on 2020-08-13 12:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unidade', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('setores', '0001_initial'),
        ('funcionarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='setores',
            field=models.ManyToManyField(to='setores.Setor'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='unidade',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='unidade.unidade'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='funcionario',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.PROTECT, to='auth.user'),
            preserve_default=False,
        ),
    ]
