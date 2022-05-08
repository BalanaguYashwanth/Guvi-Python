a = input("enter the name")
print(a)

 <select idref="RiskCommercialAutoRiskInput.Type">
        <case idref="Coll_076_B_SX_01.BasePremium" type="float" select="MobileHome" />
        <case idref="Coll_076_B_SX_01.BasePremium" type="float" select="MobileHomeContents" />
        <case idref="Coll_077_B_SX_01.BasePremium" type="float" select="Motorcycle" />
        <case idref="Coll_032_B_SX_01.BasePremium" type="float" select="PrivatePassenger" />
        <case idref="CovCollisionPrivate.BasePremiumTruck" type="float" select="Truck,TruckTractor,Trailer,ServiceUtilityTrailer" />
        <case idref="CovCollisionPrivate.BasePremiumPublic" type="float" select="PublicVehicle" />
        <case idref="Coll_064_C_SX_01.BasePremium" type="float" select="Ambulance" />
        <case idref="Coll_073_B_SX_01.BasePremium" type="float" select="GolfMobile" />
        <case idref="Coll_066_B_SX_01.BasePremium" type="float" select="AntiqueAuto" />
        <case idref="CovCollisionPrivate.BasePremiumGarage" type="float" select="Garage" />
        <case idref="CovCollisionPrivate.BasePremiumSemitrailer" type="float" select="Semitrailer" />
        <case idref="Coll_072_B_SX_01.BasePremium" type="float" select="FuneralDirectors" />
        <case idref="Coll_079_B_SX_01.BasePremium" type="float" select="RepossessedAutos" />
        <case idref="Coll_080_B_SX_01.BasePremium" type="float" select="Snowmobile" />
        <case idref="Coll_081_X_SX_01.BasePremium" type="float" select="SpecialOrMobileEquipment" />
        <case idref="Coll_069_C_SX_01.BasePremium" type="float" select="DriveAway" />
        <case idref="Coll_070_C_SX_01.BasePremium" type="float" select="FinancedAuto" />
        <case idref="Coll_084_B_SX_01.BasePremium" type="float" select="AllTerrainUtilityTaskVehicle" />
        <otherwise idref="CovCollisionPrivate.BasePremiumTruck" type="float" />
      </select>


if RiskCommercialAutoRiskInput.Type is MobileHomeContents then
if RiskCommercialAutoRiskInput.Type is Motorcycle then
if RiskCommercialAutoRiskInput.Type is PrivatePassenger then
if RiskCommercialAutoRiskInput.Type is Truck,TruckTracker, Trailer,ServiceUtilityTrailer then
if RiskCommercialAutoRiskInput.Type is PublicVehicle then
if RiskCommercialAutoRiskInput.Type is Ambulance then
if RiskCommercialAutoRiskInput.Type is GolfMobile then
if RiskCommercialAutoRiskInput.Type is AntiqueAuto then
if RiskCommercialAutoRiskInput.Type is Garage then
if RiskCommercialAutoRiskInput.Type is Semitrailer then
if RiskCommercialAutoRiskInput.Type is FuneralDirectors then
if RiskCommercialAutoRiskInput.Type is RepossessedAutos then
if RiskCommercialAutoRiskInput.Type is Snowmobile then
if RiskCommercialAutoRiskInput.Type is SpecialOrMobileEquipment then
if RiskCommercialAutoRiskInput.Type is DriveAway then
if RiskCommercialAutoRiskInput.Type is FinancedAuto then
if RiskCommercialAutoRiskInput.Type is AllTerrainUtilityTaskVehicle then

Coll_076_B_SX_01.BaseLossCostRate
Coll_101_A_SX_01.PhysicalDamageMultiplier
Coll_098_B_SX_01.DeductibleCredit
Coll_076_B_SX_01.MobileHomeFactor
CovCollisionPrivate.LeasingShortTermFactor

<argument op="eq" idref="Coll_070_C_SX_01.BaseLossCostRate" type="float" />
<argument op="multiply" idref="Coll_070_C_SX_01.DeductibleFactor" type="float" />
<argument op="multiply" idref="Coll_070_C_SX_01.TermFactor" type="float" />

Coll_070_C_SX_01.BaseLossCostRate
Coll_070_C_SX_01.DeductibleFactor
Coll_070_C_SX_01.TermFactor