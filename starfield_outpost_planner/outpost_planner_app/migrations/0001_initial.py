# Generated by Django 5.0.7 on 2024-07-25 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OutpostModule',
            fields=[
                ('moduleID', models.SmallIntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('category', models.CharField(max_length=50)),
                ('power', models.SmallIntegerField()),
                ('recipeID', models.SmallIntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('recipeID', models.SmallIntegerField(primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('requiredAldumite', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredAlkanes', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredAluminum', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredAntimony', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredAqueousHematite', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredArgon', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredBenzene', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredBeryllium', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredCaelumite', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredCaesium', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredCarboxylicAcids', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredChlorine', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredChlorosilanes', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredCobalt', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredCopper', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredDysprosium', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredEuropium', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredFlourine', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredGold', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredHelium3', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredIndicite', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredIonicLiquids', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredIridium', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredIron', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredLead', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredLithium', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredMercury', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredNeodymium', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredNeon', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredNickel', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredPalladium', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredPlatinum', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredPlutonium', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredRothicite', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredSilver', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredTantalum', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredTasine', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredTetraflourides', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredTitanium', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredTungsten', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredUranium', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredVanadium', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredVeryl', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredVytinium', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredWater', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredXenon', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredYtterbium', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredAdhesive', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredAminoAcids', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredAnalgesic', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredAntimicrobial', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredAromatic', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredBiosuppressant', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredCosmetic', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredFiber', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredGastronoicDelight', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredHallucinogen', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredHighTensileSpidroin', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredHypercatalyst', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredImmunostimulant', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredLubricant', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredLuxuryTextile', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredMembrane', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredMemorySubstrate', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredMetabolicAgent', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredNeurologic', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredNutrient', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredOrnamentalMaterial', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredPigment', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredPolymer', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredQuarkDegenerateTissues', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredSealant', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredSedative', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredSolvent', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredSpice', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredStimulant', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredStructuralMaterials', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredToxin', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredAdaptiveFrame', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredAldumiteDrillingRig', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredAusteniticManifold', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredCommRelay', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredControlRod', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredDrillingRig', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredIndiciteWafer', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredIsocenteredMagnet', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredIsotopicCoolant', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredMagPressureTank', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredMicrosecondRegulator', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredMolecularSieve', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredMonopropellant', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredNuclearFuelRod', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredParamagnonConductor', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredPolytextile', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredPositronBattery', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredPowerCircuit', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredReactiveGauge', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredRothiciteMagnet', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredSemimetalWafer', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredSterileNanotubes', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredSubstrateMoleculeSieve', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredSupercooledMagnet', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredTasineSuperconductor', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredTauGradeRheostat', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredVerylTreatedManifold', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredVytiniumFuelRod', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredZeroWire', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('requiredZeroGGimbal', models.SmallIntegerField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('resource_ID', models.SmallIntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=10, unique=True)),
                ('inorganic', models.BooleanField()),
                ('manufactured', models.BooleanField()),
                ('organic', models.BooleanField()),
                ('recipeID', models.SmallIntegerField(blank=True, default=None, null=True)),
            ],
        ),
    ]
