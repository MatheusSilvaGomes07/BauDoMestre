# Generated by Django 4.2.4 on 2023-09-13 17:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meus_personagens', '0010_tormenta_to_tormenta_ts_tormenta_carga_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallOfCthulhu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('vida', models.IntegerField(null=True)),
                ('ocupacao', models.CharField(max_length=100)),
                ('localNascimento', models.CharField(blank=True, max_length=100, null=True)),
                ('pronome', models.CharField(blank=True, max_length=10, null=True)),
                ('residencia', models.CharField(max_length=100)),
                ('idade', models.IntegerField()),
                ('forca', models.IntegerField(default=0)),
                ('con', models.IntegerField(default=0)),
                ('des', models.IntegerField(default=0)),
                ('int', models.IntegerField(default=0)),
                ('tam', models.IntegerField(default=0)),
                ('pod', models.IntegerField(default=0)),
                ('apa', models.IntegerField(default=0)),
                ('edu', models.IntegerField(default=0)),
                ('pvMax', models.IntegerField(blank=True, default=0, null=True)),
                ('pvAtual', models.IntegerField(blank=True, default=0, null=True)),
                ('magiaMax', models.IntegerField(blank=True, default=0, null=True)),
                ('magiaAtual', models.IntegerField(blank=True, default=0, null=True)),
                ('sorte', models.IntegerField(default=0)),
                ('sanidadeMax', models.IntegerField(blank=True, default=0, null=True)),
                ('sanidadeAtual', models.IntegerField(blank=True, default=0, null=True)),
                ('contabilidade', models.BooleanField(default=False)),
                ('contabilidadeMod', models.IntegerField(blank=True, null=True)),
                ('antropologia', models.BooleanField(default=False)),
                ('antropologiaMod', models.IntegerField(blank=True, null=True)),
                ('arqueologia', models.BooleanField(default=False)),
                ('arqueologiaMod', models.IntegerField(blank=True, null=True)),
                ('livre1', models.BooleanField(default=False)),
                ('livre1Nome', models.CharField(blank=True, max_length=50, null=True)),
                ('livre1Mod', models.IntegerField(blank=True, null=True)),
                ('livre2', models.BooleanField(default=False)),
                ('livre2Nome', models.CharField(blank=True, max_length=50, null=True)),
                ('livre2Mod', models.IntegerField(blank=True, null=True)),
                ('seducao', models.BooleanField(default=False)),
                ('seducaoMod', models.IntegerField(blank=True, null=True)),
                ('escalada', models.BooleanField(default=False)),
                ('escaladaMod', models.IntegerField(blank=True, null=True)),
                ('creditoMod', models.IntegerField(blank=True, null=True)),
                ('cthulhuMitosMod', models.IntegerField(blank=True, null=True)),
                ('disfarce', models.BooleanField(default=False)),
                ('disfarceMod', models.IntegerField(blank=True, null=True)),
                ('esquiva', models.BooleanField(default=False)),
                ('esquivaMod', models.IntegerField(blank=True, null=True)),
                ('dirigirAuto', models.BooleanField(default=False)),
                ('dirigirAutoMod', models.IntegerField(blank=True, null=True)),
                ('reparoEletrico', models.BooleanField(default=False)),
                ('reparoEletricoMod', models.IntegerField(blank=True, null=True)),
                ('conversaRapida', models.BooleanField(default=False)),
                ('conversaRapidaMod', models.IntegerField(blank=True, null=True)),
                ('luta', models.BooleanField(default=False)),
                ('luraMod', models.IntegerField(blank=True, null=True)),
                ('livre3', models.BooleanField(default=False)),
                ('livre3Nome', models.CharField(blank=True, max_length=50, null=True)),
                ('livre3Mod', models.IntegerField(blank=True, null=True)),
                ('armaDeFogo', models.BooleanField(default=False)),
                ('armaDeFogoMod', models.IntegerField(blank=True, null=True)),
                ('armaDeFogoPesada', models.BooleanField(default=False)),
                ('armaDeFogoPesadaMod', models.IntegerField(blank=True, null=True)),
                ('livre4', models.BooleanField(default=False)),
                ('livre4Nome', models.CharField(blank=True, max_length=50, null=True)),
                ('livre4Mod', models.IntegerField(blank=True, null=True)),
                ('primeirosSocorros', models.BooleanField(default=False)),
                ('primeirosSocorrosMod', models.IntegerField(blank=True, null=True)),
                ('historia', models.BooleanField(default=False)),
                ('historiaMod', models.IntegerField(blank=True, null=True)),
                ('intimidacao', models.BooleanField(default=False)),
                ('intimidacaoMod', models.IntegerField(blank=True, null=True)),
                ('pulo', models.BooleanField(default=False)),
                ('puloMod', models.IntegerField(blank=True, null=True)),
                ('livre5', models.BooleanField(default=False)),
                ('livre5Nome', models.CharField(blank=True, max_length=50, null=True)),
                ('livre5Mod', models.IntegerField(blank=True, null=True)),
                ('livre6', models.BooleanField(default=False)),
                ('livre6Nome', models.CharField(blank=True, max_length=50, null=True)),
                ('livre6Mod', models.IntegerField(blank=True, null=True)),
                ('livre7', models.BooleanField(default=False)),
                ('livre7Nome', models.CharField(blank=True, max_length=50, null=True)),
                ('livre7Mod', models.IntegerField(blank=True, null=True)),
                ('livre8', models.BooleanField(default=False)),
                ('livre8Nome', models.CharField(blank=True, max_length=50, null=True)),
                ('livre8Mod', models.IntegerField(blank=True, null=True)),
                ('direito', models.BooleanField(default=False)),
                ('direitoMod', models.IntegerField(blank=True, null=True)),
                ('pesquisarBiblioteca', models.BooleanField(default=False)),
                ('pesquisarBibliotecaMod', models.IntegerField(blank=True, null=True)),
                ('escutar', models.BooleanField(default=False)),
                ('escutarMod', models.IntegerField(blank=True, null=True)),
                ('chaveiro', models.BooleanField(default=False)),
                ('chaveiroMod', models.IntegerField(blank=True, null=True)),
                ('reparoMecanico', models.BooleanField(default=False)),
                ('reparoMecanicoMod', models.IntegerField(blank=True, null=True)),
                ('medicina', models.BooleanField(default=False)),
                ('medicinaMod', models.IntegerField(blank=True, null=True)),
                ('linguaNativa', models.BooleanField(default=False)),
                ('linguaNativaMod', models.IntegerField(blank=True, null=True)),
                ('navegacao', models.BooleanField(default=False)),
                ('navegacaoMod', models.IntegerField(blank=True, null=True)),
                ('persuasao', models.BooleanField(default=False)),
                ('persuasaoMod', models.IntegerField(blank=True, null=True)),
                ('livre9', models.BooleanField(default=False)),
                ('livre9Nome', models.CharField(blank=True, max_length=50, null=True)),
                ('livre9Mod', models.IntegerField(blank=True, null=True)),
                ('psicanalise', models.BooleanField(default=False)),
                ('psicanaliseMod', models.IntegerField(blank=True, null=True)),
                ('psicologia', models.BooleanField(default=False)),
                ('psicologiaMod', models.IntegerField(blank=True, null=True)),
                ('cavalgar', models.BooleanField(default=False)),
                ('cavalgarMod', models.IntegerField(blank=True, null=True)),
                ('livre10', models.BooleanField(default=False)),
                ('livre10Nome', models.CharField(blank=True, max_length=50, null=True)),
                ('livre10Mod', models.IntegerField(blank=True, null=True)),
                ('livre11', models.BooleanField(default=False)),
                ('livre11Nome', models.CharField(blank=True, max_length=50, null=True)),
                ('livre11Mod', models.IntegerField(blank=True, null=True)),
                ('livre12', models.BooleanField(default=False)),
                ('livre12Nome', models.CharField(blank=True, max_length=50, null=True)),
                ('livre12Mod', models.IntegerField(blank=True, null=True)),
                ('maosHabeis', models.BooleanField(default=False)),
                ('maosHabeisMod', models.IntegerField(blank=True, null=True)),
                ('esconder', models.BooleanField(default=False)),
                ('esconderMod', models.IntegerField(blank=True, null=True)),
                ('furtividade', models.BooleanField(default=False)),
                ('furtividadeMod', models.IntegerField(blank=True, null=True)),
                ('livre13', models.BooleanField(default=False)),
                ('livre13Nome', models.CharField(blank=True, max_length=50, null=True)),
                ('livre13Mod', models.IntegerField(blank=True, null=True)),
                ('nadar', models.BooleanField(default=False)),
                ('nadarMod', models.IntegerField(blank=True, null=True)),
                ('arremessar', models.BooleanField(default=False)),
                ('arremessarMod', models.IntegerField(blank=True, null=True)),
                ('rastrear', models.BooleanField(default=False)),
                ('rastrearMod', models.IntegerField(blank=True, null=True)),
                ('livre14', models.BooleanField(default=False)),
                ('livre14Nome', models.CharField(blank=True, max_length=50, null=True)),
                ('livre14Mod', models.IntegerField(blank=True, null=True)),
                ('livre15', models.BooleanField(default=False)),
                ('livre15Nome', models.CharField(blank=True, max_length=50, null=True)),
                ('livre15Mod', models.IntegerField(blank=True, null=True)),
                ('livre16', models.BooleanField(default=False)),
                ('livre16Nome', models.CharField(blank=True, max_length=50, null=True)),
                ('livre16Mod', models.IntegerField(blank=True, null=True)),
                ('livre17', models.BooleanField(default=False)),
                ('livre17Nome', models.CharField(blank=True, max_length=50, null=True)),
                ('livre17Mod', models.IntegerField(blank=True, null=True)),
                ('ataque1', models.CharField(max_length=100)),
                ('ataque1Mod', models.IntegerField(blank=True, null=True)),
                ('ataque1Dano', models.CharField(max_length=100)),
                ('ataque1Num', models.IntegerField(blank=True, null=True)),
                ('ataque1Alcance', models.FloatField(blank=True, null=True)),
                ('ataque1Municao', models.IntegerField(blank=True, null=True)),
                ('ataque1Defeito', models.IntegerField(blank=True, null=True)),
                ('ataque2', models.CharField(max_length=100)),
                ('ataque2Mod', models.IntegerField(blank=True, null=True)),
                ('ataque2Dano', models.CharField(max_length=100)),
                ('ataque2Num', models.IntegerField(blank=True, null=True)),
                ('ataque2Alcance', models.FloatField(blank=True, null=True)),
                ('ataque2Municao', models.IntegerField(blank=True, null=True)),
                ('ataque2Defeito', models.IntegerField(blank=True, null=True)),
                ('ataque3', models.CharField(max_length=100)),
                ('ataque3Mod', models.IntegerField(blank=True, null=True)),
                ('ataque3Dano', models.CharField(max_length=100)),
                ('ataque3Num', models.IntegerField(blank=True, null=True)),
                ('ataque3Alcance', models.FloatField(blank=True, null=True)),
                ('ataque3Municao', models.IntegerField(blank=True, null=True)),
                ('ataque3Defeito', models.IntegerField(blank=True, null=True)),
                ('ataque4', models.CharField(max_length=100)),
                ('ataque4Mod', models.IntegerField(blank=True, null=True)),
                ('ataque4Dano', models.CharField(max_length=100)),
                ('ataque4Num', models.IntegerField(blank=True, null=True)),
                ('ataque4Alcance', models.FloatField(blank=True, null=True)),
                ('ataque4Municao', models.IntegerField(blank=True, null=True)),
                ('ataque4Defeito', models.IntegerField(blank=True, null=True)),
                ('movimentacao', models.IntegerField(blank=True, null=True)),
                ('build', models.IntegerField(blank=True, null=True)),
                ('esquiva2', models.IntegerField(blank=True, null=True)),
                ('danoBonus', models.IntegerField(blank=True, null=True)),
                ('descricaoPessoal', models.TextField(blank=True, null=True)),
                ('ideologia', models.TextField(blank=True, null=True)),
                ('pessoasSignificantes', models.TextField(blank=True, null=True)),
                ('lugaresSignificativos', models.TextField(blank=True, null=True)),
                ('bensPreciosos', models.TextField(blank=True, null=True)),
                ('tracos', models.TextField(blank=True, null=True)),
                ('feridas', models.TextField(blank=True, null=True)),
                ('fobiasManias', models.TextField(blank=True, null=True)),
                ('magias', models.TextField(blank=True, null=True)),
                ('encontroEntidades', models.TextField(blank=True, null=True)),
                ('equipamentos', models.TextField(blank=True, null=True)),
                ('posses', models.TextField(blank=True, null=True)),
                ('nivelGastos', models.CharField(blank=True, max_length=100, null=True)),
                ('dinheiro', models.IntegerField(blank=True, null=True)),
                ('bens', models.CharField(blank=True, max_length=100, null=True)),
                ('lore', models.TextField(blank=True, null=True)),
                ('nomePerfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'unique_together': {('nome',)},
            },
        ),
    ]
