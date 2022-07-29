# Generated by Django 4.0.6 on 2022-07-29 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userdetail', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='img_path',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='cooking', max_length=30),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('food_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userdetail.itemdetail')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userdetail.order')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userdetail.cart')),
                ('food_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userdetail.itemdetail')),
            ],
        ),
    ]