# Generated by Django 5.0.7 on 2024-07-22 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outpost_planner_app', '0002_recipe_resource_delete_recipes_delete_resources_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Adaptive_Frame',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Adhesive',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Aldumite',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Aldumite_Drilling_Rig',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Alkanes',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Aluminum',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Amino_Acids',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Analgesic',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Antimicrobial',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Antimony',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Aqueous_Hematite',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Argon',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Aromatic',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Austenitic_Manifold',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Benzene',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Beryllium',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Biosuppressant',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Caelumite',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Caesium',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Carboxylic_Acids',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Chlorine',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Chlorosilanes',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Cobalt',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Comm_Relay',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Control_Rod',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Copper',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Cosmetic',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Drilling_Rig',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Dysprosium',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Europium',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Fiber',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Flourine',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Gastronoic_Delight',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Gold',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Hallucinogen',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Helium_3',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_High_Tensile_Spidroin',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Hypercatalyst',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Immunostimulant',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Indicite',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Indicite_Wafer',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Ionic_Liquids',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Iridium',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Iron',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Isocentered_Magnet',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Isotopic_Coolant',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Lead',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Lithium',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Lubricant',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Luxury_Textile',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Mag_Pressure_Tank',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Membrane',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Memory_Substrate',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Mercury',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Metabolic_Agent',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Microsecond_Regulator',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Molecular_Sieve',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Monopropellant',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Neodymium',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Neon',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Neurologic',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Nickel',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Nuclear_Fuel_Rod',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Nutrient',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Ornamental_Material',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Palladium',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Paramagnon_Conductor',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Pigment',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Platinum',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Plutonium',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Polymer',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Polytextile',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Positron_Battery',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Power_Circuit',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Quark_Degenerate_Tissues',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Reactive_Gauge',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Rothicite',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Rothicite_Magnet',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Sealant',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Sedative',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Semimetal_Wafer',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Silver',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Solvent',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Spice',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Sterile_Nanotubes',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Stimulant',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Structural_Materials',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Substrate_Molecule_Sieve',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Supercooled_Magnet',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Tantalum',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Tasine',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Tasine_Superconductor',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Tau_Grade_Rheostat',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Tetraflourides',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Titanium',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Toxin',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Tungsten',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Uranium',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Vanadium',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Veryl',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Veryl_Treated_Manifold',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Vytinium',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Vytinium_Fuel_Rod',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Water',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Xenon',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Ytterbium',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Zero_G_Gimbal',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='required_Zero_Wire',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='recipe_id',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
    ]
