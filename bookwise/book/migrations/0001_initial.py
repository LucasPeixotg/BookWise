# Generated by Django 4.2.5 on 2023-09-26 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('isbn', models.CharField(max_length=13)),
                ('release_year', models.IntegerField()),
                ('modified_date', models.DateField(auto_now_add=True)),
                ('authors', models.CharField(max_length=200)),
                ('library_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.library')),
            ],
        ),
    ]
