# Generated by Django 2.0.2 on 2018-03-23 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chessgames', '0002_auto_20180323_1212'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChessField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_id', models.PositiveSmallIntegerField(verbose_name='id na szachownicy')),
                ('chessgame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chessgames.ChessGame', verbose_name='szachownica')),
            ],
            options={
                'verbose_name_plural': 'pola szachownic',
                'verbose_name': 'pole szachownicy',
            },
        ),
        migrations.CreateModel(
            name='ChessPiece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='chesslogic.ChessField', verbose_name='położenie na szachownicy')),
                ('side', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chessgames.Side', verbose_name='strona')),
            ],
            options={
                'verbose_name_plural': 'figury',
                'verbose_name': 'figura',
            },
        ),
        migrations.CreateModel(
            name='ChessPieceMove',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='kiedy wykonany')),
                ('from_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='chesslogic.ChessField', verbose_name='skąd')),
            ],
            options={
                'verbose_name_plural': 'ruchy figur',
                'verbose_name': 'ruch figury',
            },
        ),
        migrations.CreateModel(
            name='ChessPieceType',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, verbose_name='nazwa')),
                ('value', models.PositiveSmallIntegerField(default=1, verbose_name='wartość punktowa')),
            ],
            options={
                'verbose_name_plural': 'rodzaje figur',
                'verbose_name': 'rodzaj figury',
            },
        ),
        migrations.AddField(
            model_name='chesspiecemove',
            name='promotion_type',
            field=models.ForeignKey(blank=True, help_text='Jeśli ruch powoduje promocję piona, zostanie on zamieniony na figurę tego typu.', null=True, on_delete=django.db.models.deletion.CASCADE, to='chesslogic.ChessPieceType', verbose_name='typ figury promocji'),
        ),
        migrations.AddField(
            model_name='chesspiecemove',
            name='to_field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='chesslogic.ChessField', verbose_name='dokąd'),
        ),
        migrations.AddField(
            model_name='chesspiece',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='chesslogic.ChessPieceType', verbose_name='typ'),
        ),
        migrations.AlterUniqueTogether(
            name='chessfield',
            unique_together={('field_id', 'chessgame')},
        ),
    ]
