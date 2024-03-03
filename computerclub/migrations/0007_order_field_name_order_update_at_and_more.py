# Generated by Django 4.2.8 on 2024-03-03 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('computerclub', '0006_administrator_data_passport_alter_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='field_name',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='administrator',
            name='data_passport',
            field=models.IntegerField(default=7777999888, verbose_name='Паспорт'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Open', 'Открыт'), ('Close', 'Закрыт')], max_length=50, verbose_name='Статус заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='computerclub.user', verbose_name='Имя клиента'),
        ),
    ]
