# Generated by Django 2.2 on 2019-08-24 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Publications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('isbn', models.CharField(max_length=10)),
                ('pages', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('authors', models.ManyToManyField(related_name='books', to='Book.Authors')),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='Book.Publications')),
            ],
        ),
    ]