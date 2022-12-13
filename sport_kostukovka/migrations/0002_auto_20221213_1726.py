# Generated by Django 3.2.16 on 2022-12-13 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sport_kostukovka', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'Спортивные события'},
        ),
        migrations.AddField(
            model_name='news',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sport_kostukovka.category'),
        ),
    ]
