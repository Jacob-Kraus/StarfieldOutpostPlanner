# Generated by Django 5.0.7 on 2024-07-22 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outpost_planner_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('recipe_id', models.SmallIntegerField(primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(default=None, max_length=10, null=True)),
                ('required_Aldumite', models.SmallIntegerField(default=None, null=True)),
                ('required_Alkanes', models.SmallIntegerField(default=None, null=True)),
                ('required_Aluminum', models.SmallIntegerField(default=None, null=True)),
                ('required_Antimony', models.SmallIntegerField(default=None, null=True)),
                ('required_Aqueous_Hematite', models.SmallIntegerField(default=None, null=True)),
                ('required_Argon', models.SmallIntegerField(default=None, null=True)),
                ('required_Benzene', models.SmallIntegerField(default=None, null=True)),
                ('required_Beryllium', models.SmallIntegerField(default=None, null=True)),
                ('required_Caelumite', models.SmallIntegerField(default=None, null=True)),
                ('required_Caesium', models.SmallIntegerField(default=None, null=True)),
                ('required_Carboxylic_Acids', models.SmallIntegerField(default=None, null=True)),
                ('required_Chlorine', models.SmallIntegerField(default=None, null=True)),
                ('required_Chlorosilanes', models.SmallIntegerField(default=None, null=True)),
                ('required_Cobalt', models.SmallIntegerField(default=None, null=True)),
                ('required_Copper', models.SmallIntegerField(default=None, null=True)),
                ('required_Dysprosium', models.SmallIntegerField(default=None, null=True)),
                ('required_Europium', models.SmallIntegerField(default=None, null=True)),
                ('required_Flourine', models.SmallIntegerField(default=None, null=True)),
                ('required_Gold', models.SmallIntegerField(default=None, null=True)),
                ('required_Helium_3', models.SmallIntegerField(default=None, null=True)),
                ('required_Indicite', models.SmallIntegerField(default=None, null=True)),
                ('required_Ionic_Liquids', models.SmallIntegerField(default=None, null=True)),
                ('required_Iridium', models.SmallIntegerField(default=None, null=True)),
                ('required_Iron', models.SmallIntegerField(default=None, null=True)),
                ('required_Lead', models.SmallIntegerField(default=None, null=True)),
                ('required_Lithium', models.SmallIntegerField(default=None, null=True)),
                ('required_Mercury', models.SmallIntegerField(default=None, null=True)),
                ('required_Neodymium', models.SmallIntegerField(default=None, null=True)),
                ('required_Neon', models.SmallIntegerField(default=None, null=True)),
                ('required_Nickel', models.SmallIntegerField(default=None, null=True)),
                ('required_Palladium', models.SmallIntegerField(default=None, null=True)),
                ('required_Platinum', models.SmallIntegerField(default=None, null=True)),
                ('required_Plutonium', models.SmallIntegerField(default=None, null=True)),
                ('required_Rothicite', models.SmallIntegerField(default=None, null=True)),
                ('required_Silver', models.SmallIntegerField(default=None, null=True)),
                ('required_Tantalum', models.SmallIntegerField(default=None, null=True)),
                ('required_Tasine', models.SmallIntegerField(default=None, null=True)),
                ('required_Tetraflourides', models.SmallIntegerField(default=None, null=True)),
                ('required_Titanium', models.SmallIntegerField(default=None, null=True)),
                ('required_Tungsten', models.SmallIntegerField(default=None, null=True)),
                ('required_Uranium', models.SmallIntegerField(default=None, null=True)),
                ('required_Vanadium', models.SmallIntegerField(default=None, null=True)),
                ('required_Veryl', models.SmallIntegerField(default=None, null=True)),
                ('required_Vytinium', models.SmallIntegerField(default=None, null=True)),
                ('required_Water', models.SmallIntegerField(default=None, null=True)),
                ('required_Xenon', models.SmallIntegerField(default=None, null=True)),
                ('required_Ytterbium', models.SmallIntegerField(default=None, null=True)),
                ('required_Adhesive', models.SmallIntegerField(default=None, null=True)),
                ('required_Amino_Acids', models.SmallIntegerField(default=None, null=True)),
                ('required_Analgesic', models.SmallIntegerField(default=None, null=True)),
                ('required_Antimicrobial', models.SmallIntegerField(default=None, null=True)),
                ('required_Aromatic', models.SmallIntegerField(default=None, null=True)),
                ('required_Biosuppressant', models.SmallIntegerField(default=None, null=True)),
                ('required_Cosmetic', models.SmallIntegerField(default=None, null=True)),
                ('required_Fiber', models.SmallIntegerField(default=None, null=True)),
                ('required_Gastronoic_Delight', models.SmallIntegerField(default=None, null=True)),
                ('required_Hallucinogen', models.SmallIntegerField(default=None, null=True)),
                ('required_High_Tensile_Spidroin', models.SmallIntegerField(default=None, null=True)),
                ('required_Hypercatalyst', models.SmallIntegerField(default=None, null=True)),
                ('required_Immunostimulant', models.SmallIntegerField(default=None, null=True)),
                ('required_Lubricant', models.SmallIntegerField(default=None, null=True)),
                ('required_Luxury_Textile', models.SmallIntegerField(default=None, null=True)),
                ('required_Membrane', models.SmallIntegerField(default=None, null=True)),
                ('required_Memory_Substrate', models.SmallIntegerField(default=None, null=True)),
                ('required_Metabolic_Agent', models.SmallIntegerField(default=None, null=True)),
                ('required_Neurologic', models.SmallIntegerField(default=None, null=True)),
                ('required_Nutrient', models.SmallIntegerField(default=None, null=True)),
                ('required_Ornamental_Material', models.SmallIntegerField(default=None, null=True)),
                ('required_Pigment', models.SmallIntegerField(default=None, null=True)),
                ('required_Polymer', models.SmallIntegerField(default=None, null=True)),
                ('required_Quark_Degenerate_Tissues', models.SmallIntegerField(default=None, null=True)),
                ('required_Sealant', models.SmallIntegerField(default=None, null=True)),
                ('required_Sedative', models.SmallIntegerField(default=None, null=True)),
                ('required_Solvent', models.SmallIntegerField(default=None, null=True)),
                ('required_Spice', models.SmallIntegerField(default=None, null=True)),
                ('required_Stimulant', models.SmallIntegerField(default=None, null=True)),
                ('required_Structural_Materials', models.SmallIntegerField(default=None, null=True)),
                ('required_Toxin', models.SmallIntegerField(default=None, null=True)),
                ('required_Adaptive_Frame', models.SmallIntegerField(default=None, null=True)),
                ('required_Aldumite_Drilling_Rig', models.SmallIntegerField(default=None, null=True)),
                ('required_Austenitic_Manifold', models.SmallIntegerField(default=None, null=True)),
                ('required_Comm_Relay', models.SmallIntegerField(default=None, null=True)),
                ('required_Control_Rod', models.SmallIntegerField(default=None, null=True)),
                ('required_Drilling_Rig', models.SmallIntegerField(default=None, null=True)),
                ('required_Indicite_Wafer', models.SmallIntegerField(default=None, null=True)),
                ('required_Isocentered_Magnet', models.SmallIntegerField(default=None, null=True)),
                ('required_Isotopic_Coolant', models.SmallIntegerField(default=None, null=True)),
                ('required_Mag_Pressure_Tank', models.SmallIntegerField(default=None, null=True)),
                ('required_Microsecond_Regulator', models.SmallIntegerField(default=None, null=True)),
                ('required_Molecular_Sieve', models.SmallIntegerField(default=None, null=True)),
                ('required_Monopropellant', models.SmallIntegerField(default=None, null=True)),
                ('required_Nuclear_Fuel_Rod', models.SmallIntegerField(default=None, null=True)),
                ('required_Paramagnon_Conductor', models.SmallIntegerField(default=None, null=True)),
                ('required_Polytextile', models.SmallIntegerField(default=None, null=True)),
                ('required_Positron_Battery', models.SmallIntegerField(default=None, null=True)),
                ('required_Power_Circuit', models.SmallIntegerField(default=None, null=True)),
                ('required_Reactive_Gauge', models.SmallIntegerField(default=None, null=True)),
                ('required_Rothicite_Magnet', models.SmallIntegerField(default=None, null=True)),
                ('required_Semimetal_Wafer', models.SmallIntegerField(default=None, null=True)),
                ('required_Sterile_Nanotubes', models.SmallIntegerField(default=None, null=True)),
                ('required_Substrate_Molecule_Sieve', models.SmallIntegerField(default=None, null=True)),
                ('required_Supercooled_Magnet', models.SmallIntegerField(default=None, null=True)),
                ('required_Tasine_Superconductor', models.SmallIntegerField(default=None, null=True)),
                ('required_Tau_Grade_Rheostat', models.SmallIntegerField(default=None, null=True)),
                ('required_Veryl_Treated_Manifold', models.SmallIntegerField(default=None, null=True)),
                ('required_Vytinium_Fuel_Rod', models.SmallIntegerField(default=None, null=True)),
                ('required_Zero_Wire', models.SmallIntegerField(default=None, null=True)),
                ('required_Zero_G_Gimbal', models.SmallIntegerField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('resource_id', models.SmallIntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=10, unique=True)),
                ('inorganic', models.BooleanField()),
                ('manufactured', models.BooleanField()),
                ('organic', models.BooleanField()),
                ('recipe_id', models.SmallIntegerField(default=None, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Recipes',
        ),
        migrations.DeleteModel(
            name='Resources',
        ),
        migrations.AlterField(
            model_name='outpostmodule',
            name='category',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='outpostmodule',
            name='module_id',
            field=models.SmallIntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='outpostmodule',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='outpostmodule',
            name='power',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='outpostmodule',
            name='recipe_id',
            field=models.SmallIntegerField(unique=True),
        ),
    ]