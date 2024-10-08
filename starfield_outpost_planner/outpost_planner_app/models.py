from django.db import models
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist


# 387 unique base-game outpost module recipes
class OutpostModule(models.Model):
    objects = models.Manager()
    moduleID = models.SmallIntegerField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=50, unique=True, null=False)
    category = models.CharField(max_length=50, unique=False, null=False)
    power = models.SmallIntegerField(null=False, unique=False)
    recipeID = models.SmallIntegerField(null=False, unique=True)

    def get_recipe(self):
        try:
            rec = Recipe.objects.get(recipeID=self.recipeID)
            r_dict = rec.get_recipe()
            return r_dict
        except (ObjectDoesNotExist, MultipleObjectsReturned) as e:
            print(f"{type(e)}: {e} getting recipe {repr(self.recipeID)}")
        return dict()


# 421 unique base-game crafting recipes
#   (387 outpost modules, 34 manufactured resources)
class Recipe(models.Model):
    objects = models.Manager()
    recipeID = models.SmallIntegerField(primary_key=True, unique=True, null=False)
    description = models.CharField(max_length=10, null=True, blank=True, default=None)
    requiredAldumite = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredAlkanes = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredAluminum = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredAntimony = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredAqueousHematite = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredArgon = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredBenzene = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredBeryllium = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredCaelumite = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredCaesium = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredCarboxylicAcids = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredChlorine = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredChlorosilanes = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredCobalt = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredCopper = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredDysprosium = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredEuropium = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredFlourine = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredGold = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredHelium3 = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredIndicite = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredIonicLiquids = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredIridium = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredIron = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredLead = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredLithium = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredMercury = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredNeodymium = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredNeon = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredNickel = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredPalladium = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredPlatinum = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredPlutonium = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredRothicite = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredSilver = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredTantalum = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredTasine = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredTetraflourides = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredTitanium = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredTungsten = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredUranium = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredVanadium = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredVeryl = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredVytinium = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredWater = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredXenon = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredYtterbium = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredAdhesive = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredAminoAcids = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredAnalgesic = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredAntimicrobial = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredAromatic = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredBiosuppressant = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredCosmetic = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredFiber = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredGastronoicDelight = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredHallucinogen = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredHighTensileSpidroin = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredHypercatalyst = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredImmunostimulant = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredLubricant = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredLuxuryTextile = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredMembrane = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredMemorySubstrate = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredMetabolicAgent = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredNeurologic = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredNutrient = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredOrnamentalMaterial = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredPigment = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredPolymer = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredQuarkDegenerateTissues = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredSealant = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredSedative = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredSolvent = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredSpice = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredStimulant = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredStructuralMaterials = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredToxin = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredAdaptiveFrame = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredAldumiteDrillingRig = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredAusteniticManifold = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredCommRelay = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredControlRod = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredDrillingRig = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredIndiciteWafer = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredIsocenteredMagnet = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredIsotopicCoolant = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredMagPressureTank = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredMicrosecondRegulator = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredMolecularSieve = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredMonopropellant = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredNuclearFuelRod = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredParamagnonConductor = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredPolytextile = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredPositronBattery = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredPowerCircuit = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredReactiveGauge = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredRothiciteMagnet = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredSemimetalWafer = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredSterileNanotubes = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredSubstrateMoleculeSieve = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredSupercooledMagnet = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredTasineSuperconductor = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredTauGradeRheostat = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredVerylTreatedManifold = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredVytiniumFuelRod = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredZeroWire = models.SmallIntegerField(null=True, blank=True, default=None)
    requiredZeroGGimbal = models.SmallIntegerField(null=True, blank=True, default=None)

    def get_recipe(self):
        # returns dictionary of the non-None(Null) crafting resources required by the recipe
        prefix = 'required'
        soln = {attr.removeprefix(prefix): int(getattr(self, attr)) for attr in dir(self)
                if (attr.startswith(prefix) and getattr(self, attr))}
        return soln


# 166 unique base-game crafting resources
#   47 inorganic
#   34 manufactured
#   31 organic
class Resource(models.Model):
    objects = models.Manager()
    resource_ID = models.SmallIntegerField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=10, unique=True, null=False)
    inorganic = models.BooleanField(unique=False, null=False)
    manufactured = models.BooleanField(unique=False, null=False)
    organic = models.BooleanField(unique=False, null=False)
    recipeID = models.SmallIntegerField(unique=False, null=True, blank=True, default=None)


def main():

    print("OutpostModule route:")
    om = OutpostModule.objects.get('87')
    print(f"OutpostModule.objects.get('87'): {om}")
    mr = om.get_recipe()
    print(f"om.get_recipe(): {mr}")

    print("Recipe route:")
    rec = Recipe.objects.get('121')
    print(f"Recipe.objects.get('121'): {rec}")
    r = rec.get_recipe()
    print(f"rec.get_recipe(): {r}")


if __name__ == "__main__":
    main()
