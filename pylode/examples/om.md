Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE) 2.8.10

# Ontology of units of Measure (OM)

## Metadata
* **URI**
  * `http://opendata.caceres.es/def/ontomunicipio#`
* **Creators(s)**
  * Hajo Rijgersberg, Don Willems, Xin-Ying Ren, Mari Wigham, Jan Top
* **Version Information**
  * 2.0.7
* **Ontology RDF**
  * RDF ([om.ttl](turtle))
### Description
<p>The Ontology of units of Measure (OM) 2.0 models concepts and relations important to scientific research. It has a strong focus on units, quantities, measurements, and dimensions.</p>

## Table of Contents
1. [Classes](#classes)
1. [Object Properties](#objectproperties)
1. [Functional Properties](#functionalproperties)
1. [Datatype Properties](#datatypeproperties)
1. [Annotation Properties](#annotationproperties)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Classes
[1040 nm Lockwood magnitude](#1040nmLockwoodmagnitude),
[Alfvén number](#Alfvnnumber),
[Alfvén number unit](#Alfvnnumberunit),
[B magnitude](#Bmagnitude),
[B magnitude at maximum brightness](#Bmagnitudeatmaximumbrightness),
[B magnitude at minimum brightness](#Bmagnitudeatminimumbrightness),
[Celsius temperature](#Celsiustemperature),
[Celsius temperature scale](#Celsiustemperaturescale),
[Celsius temperature unit](#Celsiustemperatureunit),
[Corynebacterium bovis count (specific)](#Corynebacteriumboviscount(specific)),
[Corynebacterium bovis count (volumetric)](#Corynebacteriumboviscount(volumetric)),
[Corynebacterium count (specific)](#Corynebacteriumcount(specific)),
[Corynebacterium count (volumetric)](#Corynebacteriumcount(volumetric)),
[Cousins magnitude](#Cousinsmagnitude),
[Cowling number](#Cowlingnumber),
[Cowling number unit](#Cowlingnumberunit),
[Enterobacteriaceae count (specific)](#Enterobacteriaceaecount(specific)),
[Enterobacteriaceae count (volumetric)](#Enterobacteriaceaecount(volumetric)),
[Enterococcus count (specific)](#Enterococcuscount(specific)),
[Enterococcus count (volumetric)](#Enterococcuscount(volumetric)),
[Escherichia coli count (specific)](#Escherichiacolicount(specific)),
[Escherichia coli count (volumetric)](#Escherichiacolicount(volumetric)),
[Euler number](#Eulernumber),
[Euler number unit](#Eulernumberunit),
[Fahrenheit temperature](#Fahrenheittemperature),
[Fahrenheit temperature scale](#Fahrenheittemperaturescale),
[Fahrenheit temperature unit](#Fahrenheittemperatureunit),
[Fourier number](#Fouriernumber),
[Fourier number for mass transfer](#Fouriernumberformasstransfer),
[Fourier number for mass transfer unit](#Fouriernumberformasstransferunit),
[Fourier number unit](#Fouriernumberunit),
[Froude number](#Froudenumber),
[Froude number unit](#Froudenumberunit),
[Grashof number](#Grashofnumber),
[Grashof number for mass transfer](#Grashofnumberformasstransfer),
[Grashof number for mass transfer unit](#Grashofnumberformasstransferunit),
[Grashof number unit](#Grashofnumberunit),
[Hartmann number](#Hartmannnumber),
[Hartmann number unit](#Hartmannnumberunit),
[Hubble constant](#Hubbleconstant),
[Hubble constant at present epoch](#Hubbleconstantatpresentepoch),
[Hubble constant unit](#Hubbleconstantunit),
[I magnitude](#Imagnitude),
[Jeans mass](#Jeansmass),
[Johnson magnitude](#Johnsonmagnitude),
[Klebsiella count (specific)](#Klebsiellacount(specific)),
[Klebsiella count (volumetric)](#Klebsiellacount(volumetric)),
[Knudsen number](#Knudsennumber),
[Knudsen number unit](#Knudsennumberunit),
[Lewis number](#Lewisnumber),
[Lewis number unit](#Lewisnumberunit),
[Listeria monocytogenes count (specific)](#Listeriamonocytogenescount(specific)),
[Listeria monocytogenes count (volumetric)](#Listeriamonocytogenescount(volumetric)),
[Mach number](#Machnumber),
[Mach number unit](#Machnumberunit),
[Nusselt number](#Nusseltnumber),
[Nusselt number for mass transfer](#Nusseltnumberformasstransfer),
[Nusselt number for mass transfer unit](#Nusseltnumberformasstransferunit),
[Nusselt number unit](#Nusseltnumberunit),
[Prandtl number](#Prandtlnumber),
[Prandtl number unit](#Prandtlnumberunit),
[Péclet number](#Pcletnumber),
[Péclet number for mass transfer](#Pcletnumberformasstransfer),
[Péclet number for mass transfer unit](#Pcletnumberformasstransferunit),
[Péclet number unit](#Pcletnumberunit),
[R magnitude](#Rmagnitude),
[Rankine temperature](#Rankinetemperature),
[Rankine temperature scale](#Rankinetemperaturescale),
[Rankine temperature unit](#Rankinetemperatureunit),
[Rayleigh number](#Rayleighnumber),
[Rayleigh number unit](#Rayleighnumberunit),
[Reynolds number](#Reynoldsnumber),
[Reynolds number unit](#Reynoldsnumberunit),
[Réaumur temperature](#Raumurtemperature),
[Réaumur temperature scale](#Raumurtemperaturescale),
[Réaumur temperature unit](#Raumurtemperatureunit),
[SI prefix](#SIprefix),
[Salmonella count (specific)](#Salmonellacount(specific)),
[Salmonella count (volumetric)](#Salmonellacount(volumetric)),
[Schmidt number](#Schmidtnumber),
[Schmidt number unit](#Schmidtnumberunit),
[Serratia marcescens count (specific)](#Serratiamarcescenscount(specific)),
[Serratia marcescens count (volumetric)](#Serratiamarcescenscount(volumetric)),
[Stanton number](#Stantonnumber),
[Stanton number for mass transfer](#Stantonnumberformasstransfer),
[Stanton number for mass transfer unit](#Stantonnumberformasstransferunit),
[Stanton number unit](#Stantonnumberunit),
[Staphylococcus aureus count (specific)](#Staphylococcusaureuscount(specific)),
[Staphylococcus aureus count (volumetric)](#Staphylococcusaureuscount(volumetric)),
[Streptococcus agalactiae count (specific)](#Streptococcusagalactiaecount(specific)),
[Streptococcus agalactiae count (volumetric)](#Streptococcusagalactiaecount(volumetric)),
[Streptococcus dysgalactiae count (specific)](#Streptococcusdysgalactiaecount(specific)),
[Streptococcus dysgalactiae count (volumetric)](#Streptococcusdysgalactiaecount(volumetric)),
[Streptococcus uberis count (specific)](#Streptococcusuberiscount(specific)),
[Streptococcus uberis count (volumetric)](#Streptococcusuberiscount(volumetric)),
[Strouhal number](#Strouhalnumber),
[Strouhal number unit](#Strouhalnumberunit),
[Strömgren magnitude](#Strmgrenmagnitude),
[Temperature_scale](#Temperature_scale),
[Thuan and Gunn magnitude](#ThuanandGunnmagnitude),
[Tycho broadband magnitude](#Tychobroadbandmagnitude),
[U magnitude](#Umagnitude),
[V amplitude](#Vamplitude),
[V magnitude](#Vmagnitude),
[V magnitude at maximum brightness](#Vmagnitudeatmaximumbrightness),
[V magnitude at minimum brightness](#Vmagnitudeatminimumbrightness),
[Weber number](#Webernumber),
[Weber number unit](#Webernumberunit),
[aberration](#aberration),
[aberration in latitude](#aberrationinlatitude),
[aberration in longitude](#aberrationinlongitude),
[absolute bolometric magnitude](#absolutebolometricmagnitude),
[absolute magnitude](#absolutemagnitude),
[absorbed dose](#absorbeddose),
[absorbed dose rate](#absorbeddoserate),
[absorbed dose rate unit](#absorbeddoserateunit),
[absorbed dose unit](#absorbeddoseunit),
[acceleration](#acceleration),
[acceleration unit](#accelerationunit),
[acetic acid mass fraction](#aceticacidmassfraction),
[acidity](#acidity),
[acoustic firmness](#acousticfirmness),
[action](#action),
[action unit](#actionunit),
[activity](#activity),
[activity unit](#activityunit),
[admittance](#admittance),
[albedo](#albedo),
[altitude](#altitude),
[ambient dose equivalent](#ambientdoseequivalent),
[amount of money](#amountofmoney),
[amount of money unit](#amountofmoneyunit),
[amount of substance](#amountofsubstance),
[amount of substance concentration](#amountofsubstanceconcentration),
[amount of substance concentration unit](#amountofsubstanceconcentrationunit),
[amount of substance flow](#amountofsubstanceflow),
[amount of substance flow unit](#amountofsubstanceflowunit),
[amount of substance fraction](#amountofsubstancefraction),
[amount of substance fraction flow](#amountofsubstancefractionflow),
[amount of substance fraction unit](#amountofsubstancefractionunit),
[amount of substance unit](#amountofsubstanceunit),
[amphiphilicity](#amphiphilicity),
[amplitude](#amplitude),
[angle](#angle),
[angle unit](#angleunit),
[angular acceleration](#angularacceleration),
[angular acceleration unit](#angularaccelerationunit),
[angular displacement](#angulardisplacement),
[angular momentum](#angularmomentum),
[angular momentum unit](#angularmomentumunit),
[angular size](#angularsize),
[angular speed](#angularspeed),
[angular speed unit](#angularspeedunit),
[angular velocity](#angularvelocity),
[annual aberration](#annualaberration),
[apparent diameter](#apparentdiameter),
[apparent distance modulus](#apparentdistancemodulus),
[apparent magnitude](#apparentmagnitude),
[application area](#applicationarea),
[area](#area),
[area density](#areadensity),
[area density rate](#areadensityrate),
[area density rate unit](#areadensityrateunit),
[area density unit](#areadensityunit),
[area fraction](#areafraction),
[area fraction unit](#areafractionunit),
[area unit](#areaunit),
[atomic mass](#atomicmass),
[azimuth](#azimuth),
[b magnitude](#bmagnitude),
[binary prefix](#binaryprefix),
[body label mass](#bodylabelmass),
[body mass](#bodymass),
[bolometric correction](#bolometriccorrection),
[bolometric magnitude](#bolometricmagnitude),
[bond albedo](#bondalbedo),
[breadth](#breadth),
[brightness temperature](#brightnesstemperature),
[bud stadium](#budstadium),
[bud stadium day 0](#budstadiumday0),
[bud stadium day 4](#budstadiumday4),
[bud stadium day 7](#budstadiumday7),
[bulk modulus](#bulkmodulus),
[cap mass](#capmass),
[capacitance](#capacitance),
[capacitance unit](#capacitanceunit),
[carton mass](#cartonmass),
[catalytic activity](#catalyticactivity),
[catalytic activity concentration](#catalyticactivityconcentration),
[catalytic activity concentration unit](#catalyticactivityconcentrationunit),
[catalytic activity unit](#catalyticactivityunit),
[cause end of vase life Botrytis](#causeendofvaselifeBotrytis),
[cause end of vase life abscised buds](#causeendofvaselifeabscisedbuds),
[cause end of vase life abscised flowers](#causeendofvaselifeabscisedflowers),
[cause end of vase life abscised leaves](#causeendofvaselifeabscisedleaves),
[cause end of vase life blue flowers](#causeendofvaselifeblueflowers),
[cause end of vase life dry buds](#causeendofvaselifedrybuds),
[cause end of vase life dry flowers](#causeendofvaselifedryflowers),
[cause end of vase life dry leaves](#causeendofvaselifedryleaves),
[cause end of vase life malformed buds](#causeendofvaselifemalformedbuds),
[cause end of vase life malformed flowers](#causeendofvaselifemalformedflowers),
[cause end of vase life nonturgid flowers](#causeendofvaselifenonturgidflowers),
[cause end of vase life nonturgid leaves](#causeendofvaselifenonturgidleaves),
[cause end of vase life rotten flowers](#causeendofvaseliferottenflowers),
[cause end of vase life rotten leaves](#causeendofvaseliferottenleaves),
[cause end of vase life wilted flowers](#causeendofvaselifewiltedflowers),
[cause end of vase life wilted leaves](#causeendofvaselifewiltedleaves),
[cause end of vase life yellow leaves](#causeendofvaselifeyellowleaves),
[circumference](#circumference),
[co-rotation radius](#co-rotationradius),
[cold gas mass fraction](#coldgasmassfraction),
[coliform bacteria count (specific)](#coliformbacteriacount(specific)),
[coliform bacteria count (volumetric)](#coliformbacteriacount(volumetric)),
[collision frequency](#collisionfrequency),
[color area fraction](#colorareafraction),
[colour index](#colourindex),
[colour temperature](#colourtemperature),
[column number density](#columnnumberdensity),
[column number density unit](#columnnumberdensityunit),
[compound unit](#compoundunit),
[compressive stress](#compressivestress),
[contact angle](#contactangle),
[cosmological constant](#cosmologicalconstant),
[cost](#cost),
[coverage](#coverage),
[critical density](#criticaldensity),
[cubic prefixed metre](#cubicprefixedmetre),
[current density](#currentdensity),
[current density unit](#currentdensityunit),
[curvature constant](#curvatureconstant),
[curvature constant unit](#curvatureconstantunit),
[cut-off wavelength](#cut-offwavelength),
[dark noise](#darknoise),
[date](#Date),
[deceleration parameter](#decelerationparameter),
[deceleration parameter unit](#decelerationparameterunit),
[declination](#declination),
[density](#density),
[density parameter](#densityparameter),
[density parameter for baryonic matter](#densityparameterforbaryonicmatter),
[density parameter for matter](#densityparameterformatter),
[density parameter for radiation](#densityparameterforradiation),
[density parameter for vacuum](#densityparameterforvacuum),
[density parameter unit](#densityparameterunit),
[density unit](#densityunit),
[depth](#depth),
[detective quantum efficiency](#detectivequantumefficiency),
[detectivity](#detectivity),
[detectivity unit](#detectivityunit),
[diameter](#diameter),
[diameter (angle)](#diameter(angle)),
[dimension](#dimension),
[directional dose equivalent](#directionaldoseequivalent),
[disodium ethylene diamine tetra acetate mass fraction](#disodiumethylenediaminetetraacetatemassfraction),
[displacement](#displacement),
[distance](#distance),
[distance modulus](#distancemodulus),
[diurnal aberration](#diurnalaberration),
[dose equivalent](#doseequivalent),
[dose equivalent unit](#doseequivalentunit),
[drainage speed](#drainagespeed),
[dry body mass](#drybodymass),
[dry mass](#drymass),
[dry matter mass fraction](#drymattermassfraction),
[duration](#duration),
[dynamic modulus](#dynamicmodulus),
[dynamic range](#dynamicrange),
[dynamic range unit](#dynamicrangeunit),
[dynamic viscosity](#dynamicviscosity),
[dynamic viscosity unit](#dynamicviscosityunit),
[eccentricity](#eccentricity),
[ecliptic latitude](#eclipticlatitude),
[ecliptic longitude](#eclipticlongitude),
[egg mass fraction](#eggmassfraction),
[elasticity tensor](#elasticitytensor),
[electric charge](#electriccharge),
[electric charge density](#electricchargedensity),
[electric charge density unit](#electricchargedensityunit),
[electric charge unit](#electricchargeunit),
[electric current](#electriccurrent),
[electric current unit](#electriccurrentunit),
[electric dipole moment](#electricdipolemoment),
[electric dipole moment unit](#electricdipolemomentunit),
[electric field](#electricfield),
[electric field unit](#electricfieldunit),
[electric flux density](#electricfluxdensity),
[electric flux density unit](#electricfluxdensityunit),
[electric potential](#electricpotential),
[electric potential unit](#electricpotentialunit),
[electrical conductance](#electricalconductance),
[electrical conductance unit](#electricalconductanceunit),
[electrical conductivity](#electricalconductivity),
[electrical conductivity unit](#electricalconductivityunit),
[electrical resistance](#electricalresistance),
[electrical resistance unit](#electricalresistanceunit),
[electrical resistivity](#electricalresistivity),
[electrical resistivity unit](#electricalresistivityunit),
[electromotive force](#electromotiveforce),
[electron temperature](#electrontemperature),
[ellipticity](#ellipticity),
[energy](#energy),
[energy density](#energydensity),
[energy density unit](#energydensityunit),
[energy unit](#energyunit),
[enthalpy](#enthalpy),
[entropy](#entropy),
[entropy unit](#entropyunit),
[epoch](#epoch),
[epoch at maximum brightness](#epochatmaximumbrightness),
[exposure](#exposure),
[exposure to x and γ rays](#exposuretoxandrays),
[exposure to x and γ rays unit](#exposuretoxandraysunit),
[exposure unit](#exposureunit),
[external browning](#externalbrowning),
[extinction](#extinction),
[extinction at waveband](#extinctionatwaveband),
[extinction at wavelength](#extinctionatwavelength),
[extinction in B](#extinctioninB),
[extinction in U](#extinctioninU),
[extinction in V](#extinctioninV),
[fat mass fraction](#fatmassfraction),
[firmness (penetrometer) (method 1)](#firmness(penetrometer)(method1)),
[firmness (penetrometer) (method 2)](#firmness(penetrometer)(method2)),
[first Cowling number](#firstCowlingnumber),
[first Cowling number unit](#firstCowlingnumberunit),
[fixed point](#fixedpoint),
[fixed zero point](#fixedzeropoint),
[flowpack mass](#flowpackmass),
[fluidity](#fluidity),
[fluidity unit](#fluidityunit),
[font size](#fontsize),
[font size unit](#fontsizeunit),
[force](#force),
[force unit](#forceunit),
[frequency](#frequency),
[frequency unit](#frequencyunit),
[friction](#friction),
[function](#function),
[g magnitude](#gmagnitude),
[galactic cylindrical polar angle coordinate](#galacticcylindricalpolaranglecoordinate),
[galactic latitude](#galacticlatitude),
[galactic longitude](#galacticlongitude),
[gas constant](#gasconstant),
[gas constant unit](#gasconstantunit),
[gelatin mass fraction](#gelatinmassfraction),
[geometrical albedo](#geometricalalbedo),
[gram per prefixed litre](#gramperprefixedlitre),
[gravitational acceleration](#gravitationalacceleration),
[guar gum mass fraction](#guargummassfraction),
[half-life](#half-life),
[heat](#heat),
[heat capacity](#heatcapacity),
[heat capacity unit](#heatcapacityunit),
[heat flow rate](#heatflowrate),
[heat flux density](#heatfluxdensity),
[heat transfer coefficient](#heattransfercoefficient),
[heat transfer coefficient unit](#heattransfercoefficientunit),
[height](#height),
[hour angle](#hourangle),
[hydrophilicity](#hydrophilicity),
[hydrophobicity](#hydrophobicity),
[illuminance](#illuminance),
[illuminance unit](#illuminanceunit),
[impulse](#impulse),
[inductance](#inductance),
[inductance unit](#inductanceunit),
[information capacity](#informationcapacity),
[information capacity unit](#informationcapacityunit),
[initial mass function](#initialmassfunction),
[integrated magnitude](#integratedmagnitude),
[internal energy](#internalenergy),
[interval scale](#intervalscale),
[intrinsic colour index](#intrinsiccolourindex),
[ionization temperature](#ionizationtemperature),
[irradiance](#irradiance),
[kerma](#kerma),
[kinematic viscosity](#kinematicviscosity),
[kinematic viscosity unit](#kinematicviscosityunit),
[kinetic energy](#kineticenergy),
[label mass](#labelmass),
[lactose mass fraction](#lactosemassfraction),
[length](#length),
[length unit](#lengthunit),
[light time](#lighttime),
[limiting magnitude](#limitingmagnitude),
[linear strain](#linearstrain),
[lipophilicity](#lipophilicity),
[locust bean gum mass fraction](#locustbeangummassfraction),
[loss modulus](#lossmodulus),
[luminance](#luminance),
[luminance unit](#luminanceunit),
[luminosity function](#luminosityfunction),
[luminous efficacy](#luminousefficacy),
[luminous efficacy unit](#luminousefficacyunit),
[luminous energy](#luminousenergy),
[luminous energy unit](#luminousenergyunit),
[luminous flux](#luminousflux),
[luminous flux unit](#luminousfluxunit),
[luminous intensity](#luminousintensity),
[luminous intensity unit](#luminousintensityunit),
[magnetic Reynolds number](#magneticReynoldsnumber),
[magnetic Reynolds number unit](#magneticReynoldsnumberunit),
[magnetic field](#magneticfield),
[magnetic field unit](#magneticfieldunit),
[magnetic flux](#magneticflux),
[magnetic flux density](#magneticfluxdensity),
[magnetic flux density unit](#magneticfluxdensityunit),
[magnetic flux unit](#magneticfluxunit),
[magnetomotive force](#magnetomotiveforce),
[magnetomotive force unit](#magnetomotiveforceunit),
[magnitude](#magnitude),
[magnitude at maximum brightness](#magnitudeatmaximumbrightness),
[magnitude at minimum brightness](#magnitudeatminimumbrightness),
[magnitude unit](#magnitudeunit),
[manual firmness](#manualfirmness),
[mass](#mass),
[mass flow](#massflow),
[mass flow unit](#massflowunit),
[mass fraction](#massfraction),
[mass fraction unit](#massfractionunit),
[mass unit](#massunit),
[measure](#measure),
[metallicity](#metallicity),
[metre per prefixed second (time)](#metreperprefixedsecond(time)),
[metre per prefixed second (time) squared](#metreperprefixedsecond(time)squared),
[moderated starch mass fraction](#moderatedstarchmassfraction),
[modulus of elasticity](#modulusofelasticity),
[molality](#molality),
[molality unit](#molalityunit),
[molar energy](#molarenergy),
[molar energy unit](#molarenergyunit),
[molar entropy](#molarentropy),
[molar entropy unit](#molarentropyunit),
[molar heat capacity](#molarheatcapacity),
[molar heat capacity unit](#molarheatcapacityunit),
[molar mass](#molarmass),
[molar mass unit](#molarmassunit),
[molar volume](#molarvolume),
[molar volume unit](#molarvolumeunit),
[mole per prefixed litre](#moleperprefixedlitre),
[mole per prefixed metre](#moleperprefixedmetre),
[moment of force](#momentofforce),
[moment of force unit](#momentofforceunit),
[moment of inertia](#momentofinertia),
[moment of inertia unit](#momentofinertiaunit),
[momentum](#momentum),
[momentum unit](#momentumunit),
[mustard powder mass fraction](#mustardpowdermassfraction),
[neck ring mass](#neckringmass),
[noise equivalent power](#noiseequivalentpower),
[normal albedo](#normalalbedo),
[normal strain](#normalstrain),
[normal stress](#normalstress),
[normalised detectivity](#normaliseddetectivity),
[number](#number),
[number Botrytis](#numberBotrytis),
[number Botrytis 0](#numberBotrytis0),
[number Botrytis 1](#numberBotrytis1),
[number Botrytis 2](#numberBotrytis2),
[number Botrytis 3](#numberBotrytis3),
[number Botrytis 4](#numberBotrytis4),
[number abscised buds](#numberabscisedbuds),
[number abscised flowers](#numberabscisedflowers),
[number abscised leaves](#numberabscisedleaves),
[number blue-discolored flowers](#numberblue-discoloredflowers),
[number bud stadium](#numberbudstadium),
[number bud stadium 1](#numberbudstadium1),
[number bud stadium 2](#numberbudstadium2),
[number bud stadium 3](#numberbudstadium3),
[number bud stadium 4](#numberbudstadium4),
[number bud stadium 5](#numberbudstadium5),
[number buds](#numberbuds),
[number color](#numbercolor),
[number color 1](#numbercolor1),
[number color 2](#numbercolor2),
[number color 3](#numbercolor3),
[number color 4](#numbercolor4),
[number color 5](#numbercolor5),
[number density](#numberdensity),
[number density unit](#numberdensityunit),
[number dry buds](#numberdrybuds),
[number dry flowers](#numberdryflowers),
[number dry leaves](#numberdryleaves),
[number external browning](#numberexternalbrowning),
[number external browning 1](#numberexternalbrowning1),
[number external browning 2](#numberexternalbrowning2),
[number external browning 3](#numberexternalbrowning3),
[number external browning 4](#numberexternalbrowning4),
[number external browning 5](#numberexternalbrowning5),
[number flowers](#numberflowers),
[number leaves](#numberleaves),
[number malformed buds](#numbermalformedbuds),
[number malformed flowers](#numbermalformedflowers),
[number manual firmness](#numbermanualfirmness),
[number manual firmness 0](#numbermanualfirmness0),
[number manual firmness 0.5](#numbermanualfirmness0.5),
[number manual firmness 1](#numbermanualfirmness1),
[number manual firmness 1.5](#numbermanualfirmness1.5),
[number manual firmness 2](#numbermanualfirmness2),
[number manual firmness 2.5](#numbermanualfirmness2.5),
[number manual firmness 3](#numbermanualfirmness3),
[number manual firmness 3.5](#numbermanualfirmness3.5),
[number manual firmness 4](#numbermanualfirmness4),
[number manual firmness 4.5](#numbermanualfirmness4.5),
[number manual firmness 5](#numbermanualfirmness5),
[number nonturgid flowers](#numbernonturgidflowers),
[number nonturgid leaves](#numbernonturgidleaves),
[number pulp browning](#numberpulpbrowning),
[number pulp browning 1](#numberpulpbrowning1),
[number pulp browning 2](#numberpulpbrowning2),
[number pulp browning 3](#numberpulpbrowning3),
[number pulp browning 4](#numberpulpbrowning4),
[number pulp browning 5](#numberpulpbrowning5),
[number rotten flowers](#numberrottenflowers),
[number rotten leaves](#numberrottenleaves),
[number unit](#numberunit),
[number vascular browning](#numbervascularbrowning),
[number vascular browning 1](#numbervascularbrowning1),
[number vascular browning 2](#numbervascularbrowning2),
[number vascular browning 3](#numbervascularbrowning3),
[number vascular browning 4](#numbervascularbrowning4),
[number vascular browning 5](#numbervascularbrowning5),
[number wilted flowers](#numberwiltedflowers),
[number wilted leaves](#numberwiltedleaves),
[number yellow leaves](#numberyellowleaves),
[organ dose equivalent](#organdoseequivalent),
[overrun](#overrun),
[peak wavelength](#peakwavelength),
[percentage](#percentage),
[percentage unit](#percentageunit),
[period](#period),
[period of variability](#periodofvariability),
[permeability (earth science)](#permeability(earthscience)),
[permeability (earth science) unit](#permeability(earthscience)unit),
[permeability of free space](#permeabilityoffreespace),
[permeability of free space unit](#permeabilityoffreespaceunit),
[permeance (electromagnetic)](#permeance(electromagnetic)),
[permeance (electromagnetic) unit](#permeance(electromagnetic)unit),
[permeance (materials science)](#permeance(materialsscience)),
[permeance (materials science) unit](#permeance(materialsscience)unit),
[permittivity](#permittivity),
[permittivity unit](#permittivityunit),
[personal dose equivalent](#personaldoseequivalent),
[photographic amplitude](#photographicamplitude),
[photographic magnitude](#photographicmagnitude),
[photographic magnitude at maximum brightness](#photographicmagnitudeatmaximumbrightness),
[photographic magnitude at minimum brightness](#photographicmagnitudeatminimumbrightness),
[planetary aberration](#planetaryaberration),
[point](#point),
[potassium sorbate mass fraction](#potassiumsorbatemassfraction),
[potential difference](#potentialdifference),
[potential energy](#potentialenergy),
[power](#power),
[power density](#powerdensity),
[power density unit](#powerdensityunit),
[power unit](#powerunit),
[prefix](#prefix),
[prefixed ampere](#prefixedampere),
[prefixed are](#prefixedare),
[prefixed becquerel](#prefixedbecquerel),
[prefixed bit](#prefixedbit),
[prefixed byte](#prefixedbyte),
[prefixed calorie (mean)](#prefixedcalorie(mean)),
[prefixed candela](#prefixedcandela),
[prefixed coulomb](#prefixedcoulomb),
[prefixed degree Celsius](#prefixeddegreeCelsius),
[prefixed electronvolt](#prefixedelectronvolt),
[prefixed farad](#prefixedfarad),
[prefixed gram](#prefixedgram),
[prefixed gram per litre](#prefixedgramperlitre),
[prefixed gram per prefixed litre](#prefixedgramperprefixedlitre),
[prefixed gray](#prefixedgray),
[prefixed henry](#prefixedhenry),
[prefixed hertz](#prefixedhertz),
[prefixed joule](#prefixedjoule),
[prefixed katal](#prefixedkatal),
[prefixed kelvin](#prefixedkelvin),
[prefixed litre](#prefixedlitre),
[prefixed lumen](#prefixedlumen),
[prefixed lux](#prefixedlux),
[prefixed metre](#prefixedmetre),
[prefixed metre per prefixed secon (time) squared](#prefixedmetreperprefixedsecon(time)squared),
[prefixed metre per prefixed second (time)](#prefixedmetreperprefixedsecond(time)),
[prefixed metre per second (time)](#prefixedmetrepersecond(time)),
[prefixed metre per second (time) squared](#prefixedmetrepersecond(time)squared),
[prefixed metre prefixed gram](#prefixedmetreprefixedgram),
[prefixed molair](#prefixedmolair),
[prefixed mole](#prefixedmole),
[prefixed mole per litre](#prefixedmoleperlitre),
[prefixed mole per metre](#prefixedmolepermetre),
[prefixed mole per prefixed litre](#prefixedmoleperprefixedlitre),
[prefixed mole per prefixed metre](#prefixedmoleperprefixedmetre),
[prefixed newton](#prefixednewton),
[prefixed ohm](#prefixedohm),
[prefixed pascal](#prefixedpascal),
[prefixed poise](#prefixedpoise),
[prefixed radian](#prefixedradian),
[prefixed second (time)](#prefixedsecond(time)),
[prefixed second (time) squared](#prefixedsecond(time)squared),
[prefixed siemens](#prefixedsiemens),
[prefixed sievert](#prefixedsievert),
[prefixed steradian](#prefixedsteradian),
[prefixed stokes](#prefixedstokes),
[prefixed tesla](#prefixedtesla),
[prefixed tonne](#prefixedtonne),
[prefixed unified atomic mass unit](#prefixedunifiedatomicmassunit),
[prefixed unit](#prefixedunit),
[prefixed volt](#prefixedvolt),
[prefixed watt](#prefixedwatt),
[prefixed weber](#prefixedweber),
[pressure](#pressure),
[pressure unit](#pressureunit),
[protein mass fraction](#proteinmassfraction),
[pulp browning](#pulpbrowning),
[quality mark](#qualitymark),
[quality mark flower(s)](#qualitymarkflower(s)),
[quality mark leafs](#qualitymarkleafs),
[quality mark total](#qualitymarktotal),
[quantity](#quantity),
[quantity of dimension one](#quantityofdimensionone),
[quantity of dimension one unit](#quantityofdimensiononeunit),
[quantum efficiency](#quantumefficiency),
[quantum efficiency unit](#quantumefficiencyunit),
[radiance](#radiance),
[radiance unit](#radianceunit),
[radiant energy](#radiantenergy),
[radiant flux](#radiantflux),
[radiant intensity](#radiantintensity),
[radiant intensity unit](#radiantintensityunit),
[radius](#radius),
[radius (angle)](#radius(angle)),
[ratio](#ratio),
[ratio scale](#ratioscale),
[ratio unit](#ratiounit),
[red magnitude](#redmagnitude),
[reddening](#reddening),
[reddening (B-V)](#reddening(B-V)),
[reddening (U-B)](#reddening(U-B)),
[relative humidity](#relativehumidity),
[relative humidity unit](#relativehumidityunit),
[reluctance](#reluctance),
[reluctance unit](#reluctanceunit),
[resonance energy](#resonanceenergy),
[responsivity](#responsivity),
[responsivity unit](#responsivityunit),
[right ascension](#rightascension),
[salt mass fraction](#saltmassfraction),
[salt strength](#saltstrength),
[scale](#scale),
[scale factor](#scalefactor),
[scale height](#scaleheight),
[scale length](#scalelength),
[secular aberration](#secularaberration),
[shear loss modulus](#shearlossmodulus),
[shear modulus](#shearmodulus),
[shear rate](#shearrate),
[shear rate unit](#shearrateunit),
[shear storage modulus](#shearstoragemodulus),
[shear strain](#shearstrain),
[shear stress](#shearstress),
[singular unit](#singularunit),
[solid angle](#solidangle),
[solid angle unit](#solidangleunit),
[soy bean mass fraction](#soybeanmassfraction),
[specific amylase activity](#specificamylaseactivity),
[specific catalytic activity](#specificcatalyticactivity),
[specific catalytic activity unit](#specificcatalyticactivityunit),
[specific energy](#specificenergy),
[specific energy imparted](#specificenergyimparted),
[specific energy unit](#specificenergyunit),
[specific entropy](#specificentropy),
[specific entropy unit](#specificentropyunit),
[specific heat capacity](#specificheatcapacity),
[specific heat capacity unit](#specificheatcapacityunit),
[specific protease activity](#specificproteaseactivity),
[specific viable count unit](#specificviablecountunit),
[specific volume](#specificvolume),
[specific volume unit](#specificvolumeunit),
[spectral response](#spectralresponse),
[speed](#speed),
[speed unit](#speedunit),
[square prefixed metre](#squareprefixedmetre),
[starch VA40 mass fraction](#starchVA40massfraction),
[starch VA85 mass fraction](#starchVA85massfraction),
[starch mass fraction](#starchmassfraction),
[stellar aberration](#stellaraberration),
[stem end rot](#stemendrot),
[stem end rot area fraction](#stemendrotareafraction),
[stick stone](#stickstone),
[storage modulus](#storagemodulus),
[strain](#strain),
[strain tensor](#straintensor),
[strain unit](#strainunit),
[straw mass](#strawmass),
[stress](#stress),
[stress tensor](#stresstensor),
[stress unit](#stressunit),
[sugar mass fraction](#sugarmassfraction),
[supergalactic latitude](#supergalacticlatitude),
[supergalactic longitude](#supergalacticlongitude),
[surface tension](#surfacetension),
[surface tension unit](#surfacetensionunit),
[symbol rate](#symbolrate),
[symbol rate unit](#symbolrateunit),
[system of units](#systemofunits),
[temperature](#temperature),
[temperature rate](#temperaturerate),
[temperature rate unit](#temperaturerateunit),
[temperature unit](#temperatureunit),
[thermal conductivity](#thermalconductivity),
[thermal conductivity unit](#thermalconductivityunit),
[thermal diffusivity](#thermaldiffusivity),
[thermal diffusivity unit](#thermaldiffusivityunit),
[thermal insulance](#thermalinsulance),
[thermal insulance unit](#thermalinsulanceunit),
[thermal resistance](#thermalresistance),
[thermal resistance unit](#thermalresistanceunit),
[thermodynamic temperature](#thermodynamictemperature),
[thermodynamic temperature scale](#thermodynamictemperaturescale),
[thermodynamic temperature unit](#thermodynamictemperatureunit),
[thickness](#thickness),
[thrust](#thrust),
[time](#time),
[time constant](#timeconstant),
[time unit](#timeunit),
[top mass](#topmass),
[torque](#torque),
[torque unit](#torqueunit),
[total 3D start-end distance](#total3Dstart-enddistance),
[total density parameter](#totaldensityparameter),
[total distance travelled](#totaldistancetravelled),
[total number buds](#totalnumberbuds),
[total number flowers](#totalnumberflowers),
[total number leaves](#totalnumberleaves),
[true distance modulus](#truedistancemodulus),
[tween mass fraction](#tweenmassfraction),
[u magnitude](#umagnitude),
[unit](#unit),
[unit division](#unitdivision),
[unit exponentiation](#unitexponentiation),
[unit multiple](#unitmultiple),
[unit multiplication](#unitmultiplication),
[v magnitude](#vmagnitude),
[vascular browning](#vascularbrowning),
[vase life](#vaselife),
[vase plus water mass](#vasepluswatermass),
[vase plus water plus flower mass](#vasepluswaterplusflowermass),
[velocity](#velocity),
[viable count (specific)](#viablecount(specific)),
[viable count (volumetric)](#viablecount(volumetric)),
[visual albedo](#visualalbedo),
[volume](#volume),
[volume fraction](#volumefraction),
[volume fraction unit](#volumefractionunit),
[volume strain](#volumestrain),
[volume unit](#volumeunit),
[volumetric flow rate](#volumetricflowrate),
[volumetric flow rate unit](#volumetricflowrateunit),
[volumetric heat capacity](#volumetricheatcapacity),
[volumetric heat capacity unit](#volumetricheatcapacityunit),
[volumetric viable count unit](#volumetricviablecountunit),
[water mass fraction](#watermassfraction),
[wave number unit](#wavenumberunit),
[wavelength](#wavelength),
[wavenumber](#wavenumber),
[weight](#weight),
[wetting angle](#wettingangle),
[whey protein aggregate mass fraction](#wheyproteinaggregatemassfraction),
[whey protein beads mass fraction](#wheyproteinbeadsmassfraction),
[whey protein mass fraction](#wheyproteinmassfraction),
[white light magnitude](#whitelightmagnitude),
[white light magnitude at maximum brightness](#whitelightmagnitudeatmaximumbrightness),
[white light magnitude at minimum brightness](#whitelightmagnitudeatminimumbrightness),
[width](#width),
[work](#work),
[x range](#xrange),
[xanthan mass fraction](#xanthanmassfraction),
[xy 2D start-end distance](#xy2Dstart-enddistance),
[xy distance travelled](#xydistancetravelled),
[y magnitude](#ymagnitude),
[y range](#yrange),
[yeast and fungi count (specific)](#yeastandfungicount(specific)),
[yeast and fungi count (volumetric)](#yeastandfungicount(volumetric)),
[z range](#zrange),
[zenith distance](#zenithdistance),
[β_narrow magnitude](#_narrowmagnitude),
[β_wide magnitude](#_widemagnitude),
### aberration
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Aberration`
Description | <p>The apparent angular displacement of the observed position of a celestial object from its geometric position, caused by the finite velocity of light in combination with the motions of the observer and of the observed object.</p>
Super-classes |[om:AngularDisplacement](http://opendata.caceres.es/def/ontomunicipio#AngularDisplacement) (c)<br />
Sub-classes |[om:StellarAberration](http://opendata.caceres.es/def/ontomunicipio#StellarAberration) (c)<br />[om:PlanetaryAberration](http://opendata.caceres.es/def/ontomunicipio#PlanetaryAberration) (c)<br />
### aberration in latitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AberrationInLatitude`
Description | <p>The apparent angular displacement in ecliptical latitude of the observed position of a celestial object from its geometric position, caused by the finite velocity of light in combination with the motions of the observer and of the observed object.</p>
Super-classes |[om:AngularDisplacement](http://opendata.caceres.es/def/ontomunicipio#AngularDisplacement) (c)<br />
### aberration in longitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AberrationInLongitude`
Description | <p>The apparent angular displacement in ecliptical longitude of the observed position of a celestial object from its geometric position, caused by the finite velocity of light in combination with the motions of the observer and of the observed object.</p>
Super-classes |[om:AngularDisplacement](http://opendata.caceres.es/def/ontomunicipio#AngularDisplacement) (c)<br />
### absolute bolometric magnitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AbsoluteBolometricMagnitude`
Description | <p>The absolute magnitude (see absolute magnitude) of a star is a measure of its total energy emission per second, or luminosity, i.e., the bolometric magnitude from a standard distance (10 pc).</p>
Super-classes |[om:BolometricMagnitude](http://opendata.caceres.es/def/ontomunicipio#BolometricMagnitude) (c)<br />
### absolute magnitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AbsoluteMagnitude`
Description | <p>Logarithmic measure of the brightness of an object as seen from a standard distance of 10 pc. Units usually not indicated (http://en.wikipedia.org/wiki/Magnitude_(astronomy).</p>
Super-classes |[om:Magnitude](http://opendata.caceres.es/def/ontomunicipio#Magnitude) (c)<br />
### absorbed dose
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AbsorbedDose`
Description | <p>Absorbed dose is the energy deposited in a medium by ionizing radiation. It is a derived quantity in the International System of Units. Absorbed dose is energy divided by mass.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:specificEnergyOrAbsorbedDoseOrDoseEquivalent-Dimension](http://opendata.caceres.es/def/ontomunicipio#specificEnergyOrAbsorbedDoseOrDoseEquivalent-Dimension) (c)<br />
Sub-classes |[om:SpecificEnergyImparted](http://opendata.caceres.es/def/ontomunicipio#SpecificEnergyImparted) (c)<br />[om:Kerma](http://opendata.caceres.es/def/ontomunicipio#Kerma) (c)<br />
### absorbed dose rate
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AbsorbedDoseRate`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:absorbedDoseRate-Dimension](http://opendata.caceres.es/def/ontomunicipio#absorbedDoseRate-Dimension) (c)<br />
### absorbed dose rate unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AbsorbedDoseRateUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### absorbed dose unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AbsorbedDoseUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### acceleration
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Acceleration`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:acceleration-Dmension](http://opendata.caceres.es/def/ontomunicipio#acceleration-Dmension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:GravitationalAcceleration](http://opendata.caceres.es/def/ontomunicipio#GravitationalAcceleration) (c)<br />
### acceleration unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AccelerationUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### acetic acid mass fraction
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AceticAcidMassFraction`
Description | <p>The fraction of the mass of acetic acid in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### acidity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Acidity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### acoustic firmness
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AcousticFirmness`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### action
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Action`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:actionOrAngularMomentum-Dimension](http://opendata.caceres.es/def/ontomunicipio#actionOrAngularMomentum-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### action unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ActionUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### activity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Activity`
Description | <p>Activity is the decay rate of a radioactive substance. It is a derived quantity in the International System of Units. Activity is 1 divided by time.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:frequency-Dimension](http://opendata.caceres.es/def/ontomunicipio#frequency-Dimension) (c)<br />
### activity unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ActivityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### admittance
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Admittance`
Description | <p>Admittance is a measure of how easily a circuit or device will allow a current to flow. It is electric current divided by electric potential.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### albedo
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Albedo`
Description | <p>Ratio between radiation falling onto an object and the radiation reflected or scattered back. Or the ratio between the illumination and observed brightness.</p>
Super-classes |[om:QuantityOfDimensionOne](http://opendata.caceres.es/def/ontomunicipio#QuantityOfDimensionOne) (c)<br />
Sub-classes |[om:GeometricalAlbedo](http://opendata.caceres.es/def/ontomunicipio#GeometricalAlbedo) (c)<br />[om:NormalAlbedo](http://opendata.caceres.es/def/ontomunicipio#NormalAlbedo) (c)<br />[om:VisualAlbedo](http://opendata.caceres.es/def/ontomunicipio#VisualAlbedo) (c)<br />[om:BondAlbedo](http://opendata.caceres.es/def/ontomunicipio#BondAlbedo) (c)<br />
### Alfvén number
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AlfvenNumber`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
### Alfvén number unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AlfvenNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### altitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Altitude`
Description | <p>The angular distance of a celestial body above or below the horizon, measured along the great circle passing through the body and the zenith.</p>
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
### ambient dose equivalent
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AmbientDoseEquivalent`
Super-classes |[om:DoseEquivalent](http://opendata.caceres.es/def/ontomunicipio#DoseEquivalent) (c)<br />
### amount of money
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AmountOfMoney`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:Cost](http://opendata.caceres.es/def/ontomunicipio#Cost) (c)<br />
### amount of money unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AmountOfMoneyUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### amount of substance
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AmountOfSubstance`
Description | <p>Amount of substance is the number of elementary entities such as atoms, molecules, electrons, particles, etc. present in a phenomenon. It is a base quantity in the International System of Units.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:amountOfSubstance-Dimension](http://opendata.caceres.es/def/ontomunicipio#amountOfSubstance-Dimension) (c)<br />
Has members |[om:amountOfSubstanceOfASystemThatContainsAsManyElementaryEntitiesAsThereAreAtomsIn0.012KilogramOfCarbon12](http://opendata.caceres.es/def/ontomunicipio#amountOfSubstanceOfASystemThatContainsAsManyElementaryEntitiesAsThereAreAtomsIn0.012KilogramOfCarbon12)<br />
### amount of substance concentration
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AmountOfSubstanceConcentration`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:amountOfSubstanceConcentration-Dimension](http://opendata.caceres.es/def/ontomunicipio#amountOfSubstanceConcentration-Dimension) (c)<br />
### amount of substance concentration unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AmountOfSubstanceConcentrationUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### amount of substance flow
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AmountOfSubstanceFlow`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### amount of substance flow unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AmountOfSubstanceFlowUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### amount of substance fraction
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AmountOfSubstanceFraction`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
### amount of substance fraction flow
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AmountOfSubstanceFractionFlow`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### amount of substance fraction unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AmountOfSubstanceFractionUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### amount of substance unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AmountOfSubstanceUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### amphiphilicity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Amphiphilicity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### amplitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Amplitude`
Description | <p>The difference between the maximum and minimum magnitudes of a variable star, i.e., the total range of its brightness.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Sub-classes |[om:VAmplitude](http://opendata.caceres.es/def/ontomunicipio#VAmplitude) (c)<br />[om:PhotographicAmplitude](http://opendata.caceres.es/def/ontomunicipio#PhotographicAmplitude) (c)<br />
### angle
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Angle`
Description | <p>Angle is the ratio between an arc and its radius.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
Sub-classes |[om:ContactAngle](http://opendata.caceres.es/def/ontomunicipio#ContactAngle) (c)<br />[om:EclipticLatitude](http://opendata.caceres.es/def/ontomunicipio#EclipticLatitude) (c)<br />[om:EclipticLongitude](http://opendata.caceres.es/def/ontomunicipio#EclipticLongitude) (c)<br />[om:SupergalacticLongitude](http://opendata.caceres.es/def/ontomunicipio#SupergalacticLongitude) (c)<br />[om:HourAngle](http://opendata.caceres.es/def/ontomunicipio#HourAngle) (c)<br />[om:Diameter-Angle](http://opendata.caceres.es/def/ontomunicipio#Diameter-Angle) (c)<br />[om:RightAscension](http://opendata.caceres.es/def/ontomunicipio#RightAscension) (c)<br />[om:SupergalacticLatitude](http://opendata.caceres.es/def/ontomunicipio#SupergalacticLatitude) (c)<br />[om:GalacticLatitude](http://opendata.caceres.es/def/ontomunicipio#GalacticLatitude) (c)<br />[om:Azimuth](http://opendata.caceres.es/def/ontomunicipio#Azimuth) (c)<br />[om:AngularDisplacement](http://opendata.caceres.es/def/ontomunicipio#AngularDisplacement) (c)<br />[om:ApparentDiameter](http://opendata.caceres.es/def/ontomunicipio#ApparentDiameter) (c)<br />[om:GalacticCylindricalPolarAngleCoordinate](http://opendata.caceres.es/def/ontomunicipio#GalacticCylindricalPolarAngleCoordinate) (c)<br />[om:Altitude](http://opendata.caceres.es/def/ontomunicipio#Altitude) (c)<br />[om:Declination](http://opendata.caceres.es/def/ontomunicipio#Declination) (c)<br />[om:GalacticLongitude](http://opendata.caceres.es/def/ontomunicipio#GalacticLongitude) (c)<br />[om:ZenithDistance](http://opendata.caceres.es/def/ontomunicipio#ZenithDistance) (c)<br />[om:Radius-Angle](http://opendata.caceres.es/def/ontomunicipio#Radius-Angle) (c)<br />[om:WettingAngle](http://opendata.caceres.es/def/ontomunicipio#WettingAngle) (c)<br />
### angle unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AngleUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### angular acceleration
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AngularAcceleration`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:angularAcceleration-Dmension](http://opendata.caceres.es/def/ontomunicipio#angularAcceleration-Dmension) (c)<br />
### angular acceleration unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AngularAccelerationUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### angular displacement
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AngularDisplacement`
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
Sub-classes |[om:Aberration](http://opendata.caceres.es/def/ontomunicipio#Aberration) (c)<br />[om:AnnualAberration](http://opendata.caceres.es/def/ontomunicipio#AnnualAberration) (c)<br />[om:AberrationInLongitude](http://opendata.caceres.es/def/ontomunicipio#AberrationInLongitude) (c)<br />[om:DiurnalAberration](http://opendata.caceres.es/def/ontomunicipio#DiurnalAberration) (c)<br />[om:AberrationInLatitude](http://opendata.caceres.es/def/ontomunicipio#AberrationInLatitude) (c)<br />[om:SecularAberration](http://opendata.caceres.es/def/ontomunicipio#SecularAberration) (c)<br />
### angular momentum
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AngularMomentum`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:actionOrAngularMomentum-Dimension](http://opendata.caceres.es/def/ontomunicipio#actionOrAngularMomentum-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### angular momentum unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AngularMomentumUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### angular size
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AngularSize`
Super-classes |[om:SolidAngle](http://opendata.caceres.es/def/ontomunicipio#SolidAngle) (c)<br />
### angular speed
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AngularSpeed`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:angularSpeed-Dimension](http://opendata.caceres.es/def/ontomunicipio#angularSpeed-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:AngularVelocity](http://opendata.caceres.es/def/ontomunicipio#AngularVelocity) (c)<br />
### angular speed unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AngularSpeedUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### angular velocity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AngularVelocity`
Super-classes |[om:AngularSpeed](http://opendata.caceres.es/def/ontomunicipio#AngularSpeed) (c)<br />
### annual aberration
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AnnualAberration`
Description | <p>The component of the stellar abberation resulting from the motion of the Earth about the Sun. The abberation is the apparent angular displacement of the observed position of a celestial object from its geometric position, caused by the finite velocity of light in combination with the motions of the observer and of the observed object.</p>
Super-classes |[om:AngularDisplacement](http://opendata.caceres.es/def/ontomunicipio#AngularDisplacement) (c)<br />
### apparent diameter
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ApparentDiameter`
Description | <p>The angle that the actual diameter of an object makes in the sky; also known as angular size. Most often small, so units are mostly arcminutes, arcseconds, or even milli- or microarcseconds.</p>
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
### apparent distance modulus
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ApparentDistanceModulus`
Super-classes |[om:DistanceModulus](http://opendata.caceres.es/def/ontomunicipio#DistanceModulus) (c)<br />
### apparent magnitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ApparentMagnitude`
Description | <p>Logarithmic measure of the apparent brightness of an object. Units usually not indicated(http://en.wikipedia.org/wiki/Magnitude_(astronomy).</p>
Super-classes |[om:Magnitude](http://opendata.caceres.es/def/ontomunicipio#Magnitude) (c)<br />
### application area
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ApplicationArea`
Description | <p>An application area groups quantities and units of measure for application areas such as scientific disciplines (e.g., thermodynamics, mechanics).</p>
In domain of |[om:usesQuantity](http://opendata.caceres.es/def/ontomunicipio#usesQuantity) (op)<br />[om:usesUnit](http://opendata.caceres.es/def/ontomunicipio#usesUnit) (op)<br />
Has members |[om:informationTechnology](http://opendata.caceres.es/def/ontomunicipio#informationTechnology)<br />[om:chemistry](http://opendata.caceres.es/def/ontomunicipio#chemistry)<br />[om:fluidMechanics](http://opendata.caceres.es/def/ontomunicipio#fluidMechanics)<br />[om:typography](http://opendata.caceres.es/def/ontomunicipio#typography)<br />[om:astronomyAndAstrophysics](http://opendata.caceres.es/def/ontomunicipio#astronomyAndAstrophysics)<br />[om:commonApplicationArea](http://opendata.caceres.es/def/ontomunicipio#commonApplicationArea)<br />[om:shipping](http://opendata.caceres.es/def/ontomunicipio#shipping)<br />[om:geometry](http://opendata.caceres.es/def/ontomunicipio#geometry)<br />[om:chemicalPhysics](http://opendata.caceres.es/def/ontomunicipio#chemicalPhysics)<br />[om:electromagnetism](http://opendata.caceres.es/def/ontomunicipio#electromagnetism)<br />[om:thermodynamics](http://opendata.caceres.es/def/ontomunicipio#thermodynamics)<br />[om:radiometryAndRadiobiology](http://opendata.caceres.es/def/ontomunicipio#radiometryAndRadiobiology)<br />[om:cosmology](http://opendata.caceres.es/def/ontomunicipio#cosmology)<br />[om:photometry](http://opendata.caceres.es/def/ontomunicipio#photometry)<br />[om:mechanics](http://opendata.caceres.es/def/ontomunicipio#mechanics)<br />[om:economics](http://opendata.caceres.es/def/ontomunicipio#economics)<br />[om:fluidMechanicsDimensionlessNumbers](http://opendata.caceres.es/def/ontomunicipio#fluidMechanicsDimensionlessNumbers)<br />
### area
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Area`
Description | <p>Area expresses the two-dimensional size of a defined part of a surface, typically a region bounded by a closed curve. It is a derived quantity in the International System of Units. Area is length squared.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:area-Dimension](http://opendata.caceres.es/def/ontomunicipio#area-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### area density
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AreaDensity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### area density rate
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AreaDensityRate`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### area density rate unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AreaDensityRateUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### area density unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AreaDensityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### area fraction
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AreaFraction`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
Sub-classes |[om:StemEndRotAreaFraction](http://opendata.caceres.es/def/ontomunicipio#StemEndRotAreaFraction) (c)<br />[om:Coverage](http://opendata.caceres.es/def/ontomunicipio#Coverage) (c)<br />[om:ColorAreaFraction](http://opendata.caceres.es/def/ontomunicipio#ColorAreaFraction) (c)<br />
### area fraction unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AreaFractionUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### area unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AreaUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### atomic mass
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#AtomicMass`
Super-classes |[om:Mass](http://opendata.caceres.es/def/ontomunicipio#Mass) (c)<br />
### azimuth
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Azimuth`
Description | <p>The angular distance measured clockwise along the horizon from a specified reference point (usually north) to the intersection with the great circle drawn from the zenith through a body on the celestial sphere.</p>
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
### B magnitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#BMagnitude`
Description | <p>Johnson B magnitude. The Johnson B band is a standard filter in the blue area. The central wavelength is 440nm and the bandwidth is 100nm.  The filter to be used is the Corning 5030 filter plus the Schott GG13 filter.</p>
Super-classes |[om:JohnsonMagnitude](http://opendata.caceres.es/def/ontomunicipio#JohnsonMagnitude) (c)<br />
Sub-classes |[om:BMagnitudeAtMaximumBrightness](http://opendata.caceres.es/def/ontomunicipio#BMagnitudeAtMaximumBrightness) (c)<br />[om:BMagnitudeAtMinimumBrightness](http://opendata.caceres.es/def/ontomunicipio#BMagnitudeAtMinimumBrightness) (c)<br />
### B magnitude at maximum brightness
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#BMagnitudeAtMaximumBrightness`
Description | <p>Johnson B magnitude at maximum brightness (i.e. for a variable star). The Johnson B band is a standard filter in the blue area. The central wavelength is 440nm and the bandwidth is 100nm.  The filter to be used is the Corning 5030 filter plus the Schott GG13 filter.</p>
Super-classes |[om:BMagnitude](http://opendata.caceres.es/def/ontomunicipio#BMagnitude) (c)<br />[om:MagnitudeAtMaximumBrightness](http://opendata.caceres.es/def/ontomunicipio#MagnitudeAtMaximumBrightness) (c)<br />
### B magnitude at minimum brightness
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#BMagnitudeAtMinimumBrightness`
Description | <p>Johnson B magnitude at minimum brightness (i.e. for a variable star). The Johnson B band is a standard filter in the blue area. The central wavelength is 440nm and the bandwidth is 100nm.  The filter to be used is the Corning 5030 filter plus the Schott GG13 filter.</p>
Super-classes |[om:BMagnitude](http://opendata.caceres.es/def/ontomunicipio#BMagnitude) (c)<br />[om:MagnitudeAtMinimumBrightness](http://opendata.caceres.es/def/ontomunicipio#MagnitudeAtMinimumBrightness) (c)<br />
### β_narrow magnitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#BetaNarrowMagnitude`
Description | <p>β_narrow  Magnitude in the Strömgren-Crawford photometric system with a peak wavelength at 485.8 nm and a peak-half-width of 2.9 nm.</p>
Super-classes |[om:StroemgrenMagnitude](http://opendata.caceres.es/def/ontomunicipio#StroemgrenMagnitude) (c)<br />
### β_wide magnitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#BetaWideMagnitude`
Description | <p>β_wide  Magnitude in the Strömgren-Crawford photometric system with a peak wavelength at 485 nm and a peak-half-width of 12.9 nm.</p>
Super-classes |[om:StroemgrenMagnitude](http://opendata.caceres.es/def/ontomunicipio#StroemgrenMagnitude) (c)<br />
### binary prefix
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#BinaryPrefix`
Description | <p>IEC prefix</p>
Super-classes |[om:Prefix](http://opendata.caceres.es/def/ontomunicipio#Prefix) (c)<br />
Has members |[om:exbi](http://opendata.caceres.es/def/ontomunicipio#exbi)<br />[om:gibi](http://opendata.caceres.es/def/ontomunicipio#gibi)<br />[om:tebi](http://opendata.caceres.es/def/ontomunicipio#tebi)<br />[om:yobi](http://opendata.caceres.es/def/ontomunicipio#yobi)<br />[om:kibi](http://opendata.caceres.es/def/ontomunicipio#kibi)<br />[om:mebi](http://opendata.caceres.es/def/ontomunicipio#mebi)<br />[om:pebi](http://opendata.caceres.es/def/ontomunicipio#pebi)<br />[om:zebi](http://opendata.caceres.es/def/ontomunicipio#zebi)<br />
### body label mass
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#BodyLabelMass`
Super-classes |[om:LabelMass](http://opendata.caceres.es/def/ontomunicipio#LabelMass) (c)<br />
### body mass
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#BodyMass`
Super-classes |[om:Mass](http://opendata.caceres.es/def/ontomunicipio#Mass) (c)<br />
### bolometric correction
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#BolometricCorrection`
Description | <p>The visual magnitude of an object minus its bolometric magnitude.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### bolometric magnitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#BolometricMagnitude`
Description | <p>The magnitude of a star measured across all wavelengths, so that it takes into account the total amount of energy radiated. If a star is a strong infrared or ultraviolet emitter, its bolometric magnitude  will differ greatly from its visual magnitude.</p>
Super-classes |[om:Magnitude](http://opendata.caceres.es/def/ontomunicipio#Magnitude) (c)<br />
Sub-classes |[om:AbsoluteBolometricMagnitude](http://opendata.caceres.es/def/ontomunicipio#AbsoluteBolometricMagnitude) (c)<br />
### bond albedo
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#BondAlbedo`
Description | <p>Is the fraction of the total incident solar radiation - the radiation at all wavelengths - that is reflected or scattered by an object in all directions.</p>
Super-classes |[om:Albedo](http://opendata.caceres.es/def/ontomunicipio#Albedo) (c)<br />
### breadth
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Breadth`
Super-classes |[om:Length](http://opendata.caceres.es/def/ontomunicipio#Length) (c)<br />
### brightness temperature
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#BrightnessTemperature`
Description | <p>The temperature that a blackbody would need to have in order to emit radiation of the observed intensity at a given wavelength (mostly used in radio astronomy).</p>
Super-classes |[om:ThermodynamicTemperature](http://opendata.caceres.es/def/ontomunicipio#ThermodynamicTemperature) (c)<br />
### bud stadium
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#BudStadium`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Sub-classes |[om:BudStadiumDay7](http://opendata.caceres.es/def/ontomunicipio#BudStadiumDay7) (c)<br />[om:BudStadiumDay4](http://opendata.caceres.es/def/ontomunicipio#BudStadiumDay4) (c)<br />[om:BudStadiumDay0](http://opendata.caceres.es/def/ontomunicipio#BudStadiumDay0) (c)<br />
### bud stadium day 0
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#BudStadiumDay0`
Super-classes |[om:BudStadium](http://opendata.caceres.es/def/ontomunicipio#BudStadium) (c)<br />
### bud stadium day 4
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#BudStadiumDay4`
Super-classes |[om:BudStadium](http://opendata.caceres.es/def/ontomunicipio#BudStadium) (c)<br />
### bud stadium day 7
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#BudStadiumDay7`
Super-classes |[om:BudStadium](http://opendata.caceres.es/def/ontomunicipio#BudStadium) (c)<br />
### bulk modulus
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#BulkModulus`
Description | <p>Bulk modulus is a substance's resistance to uniform compression.</p>
Super-classes |[om:DynamicModulus](http://opendata.caceres.es/def/ontomunicipio#DynamicModulus) (c)<br />
### cap mass
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CapMass`
Super-classes |[om:Mass](http://opendata.caceres.es/def/ontomunicipio#Mass) (c)<br />
### capacitance
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Capacitance`
Description | <p>Capacitance is the ability to hold electrical charge. It is a derived quantity in the International System of Units. Capacitance is electric charge divided by electric potential.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:capacitance-Dimension](http://opendata.caceres.es/def/ontomunicipio#capacitance-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### capacitance unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CapacitanceUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### carton mass
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CartonMass`
Super-classes |[om:Mass](http://opendata.caceres.es/def/ontomunicipio#Mass) (c)<br />
### catalytic activity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CatalyticActivity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:catalyticActivity-Dimension](http://opendata.caceres.es/def/ontomunicipio#catalyticActivity-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### catalytic activity concentration
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CatalyticActivityConcentration`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:catalyticActivityConcentration-Dimension](http://opendata.caceres.es/def/ontomunicipio#catalyticActivityConcentration-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### catalytic activity concentration unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CatalyticActivityConcentrationUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### catalytic activity unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CatalyticActivityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### cause end of vase life abscised buds
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeAbscisedBuds`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### cause end of vase life abscised flowers
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeAbscisedFlowers`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### cause end of vase life abscised leaves
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeAbscisedLeaves`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### cause end of vase life blue flowers
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeBlueFlowers`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### cause end of vase life Botrytis
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeBotrytis`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### cause end of vase life dry buds
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeDryBuds`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### cause end of vase life dry flowers
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeDryFlowers`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### cause end of vase life dry leaves
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeDryLeaves`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### cause end of vase life malformed buds
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeMalformedBuds`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### cause end of vase life malformed flowers
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeMalformedFlowers`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### cause end of vase life nonturgid flowers
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeNonturgidFlowers`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### cause end of vase life nonturgid leaves
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeNonturgidLeaves`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### cause end of vase life rotten flowers
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeRottenFlowers`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### cause end of vase life rotten leaves
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeRottenLeaves`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### cause end of vase life wilted flowers
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeWiltedFlowers`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### cause end of vase life wilted leaves
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeWiltedLeaves`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### cause end of vase life yellow leaves
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeYellowLeaves`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### Celsius temperature
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CelsiusTemperature`
Super-classes |[om:Temperature](http://opendata.caceres.es/def/ontomunicipio#Temperature) (c)<br />
Restrictions |[om:hasScale](http://opendata.caceres.es/def/ontomunicipio#hasScale) (op) **value** [om:CelsiusScale](http://opendata.caceres.es/def/ontomunicipio#CelsiusScale) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### Celsius temperature scale
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CelsiusTemperatureScale`
Super-classes |[om:Scale](http://opendata.caceres.es/def/ontomunicipio#Scale) (c)<br />
### Celsius temperature unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CelsiusTemperatureUnit`
Super-classes |[om:TemperatureUnit](http://opendata.caceres.es/def/ontomunicipio#TemperatureUnit) (c)<br />
### circumference
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Circumference`
Super-classes |[om:Length](http://opendata.caceres.es/def/ontomunicipio#Length) (c)<br />
### co-rotation radius
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Co-RotationRadius`
Description | <p>The radius (distance from the galaxy's centre) at which the stars move at the same speed as the spiral pattern or bar in a galaxy.</p>
Super-classes |[om:Radius](http://opendata.caceres.es/def/ontomunicipio#Radius) (c)<br />
### cold gas mass fraction
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ColdGasMassFraction`
Description | <p>The fraction of the mass of a galaxy that is in the form of cold gas ~10s K.</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### collision frequency
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CollisionFrequency`
Description | <p>Collision frequency is the average number of collisions between reacting molecules per unit time.</p>
Super-classes |[om:Frequency](http://opendata.caceres.es/def/ontomunicipio#Frequency) (c)<br />
### color area fraction
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ColorAreaFraction`
Super-classes |[om:AreaFraction](http://opendata.caceres.es/def/ontomunicipio#AreaFraction) (c)<br />
### colour index
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ColourIndex`
Description | <p>The difference between the apparent magnitude of a star at two different wavelengths (always the shorter-wavelength magnitude minus the longer-wavelength magnitude) to give a quantification of the star's colour. The magnitude of an object at different wavelengths are measured by using different filters before the detector. Often the Johnson system with UBV passbands are used. Other passbands may also be used (for instance g-r).</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Sub-classes |[om:IntrinsicColourIndex](http://opendata.caceres.es/def/ontomunicipio#IntrinsicColourIndex) (c)<br />
### colour temperature
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ColourTemperature`
Description | <p>The temperature of a blackbody that has the same colour index as a given star.</p>
Super-classes |[om:ThermodynamicTemperature](http://opendata.caceres.es/def/ontomunicipio#ThermodynamicTemperature) (c)<br />
### column number density
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ColumnNumberDensity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:columnNumberDensity-Dimension](http://opendata.caceres.es/def/ontomunicipio#columnNumberDensity-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### column number density unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ColumnNumberDensityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### compound unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CompoundUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
Sub-classes |[om:UnitExponentiation](http://opendata.caceres.es/def/ontomunicipio#UnitExponentiation) (c)<br />[om:UnitMultiplication](http://opendata.caceres.es/def/ontomunicipio#UnitMultiplication) (c)<br />[om:UnitDivision](http://opendata.caceres.es/def/ontomunicipio#UnitDivision) (c)<br />
### compressive stress
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CompressiveStress`
Description | <p>Compressive stress is a stress that, when applied, acts towards the center of a material.</p>
Super-classes |[om:Stress](http://opendata.caceres.es/def/ontomunicipio#Stress) (c)<br />
### contact angle
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ContactAngle`
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
### cosmological constant
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CosmologicalConstant`
Description | <p>The cosmological constant.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### cost
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Cost`
Super-classes |[om:AmountOfMoney](http://opendata.caceres.es/def/ontomunicipio#AmountOfMoney) (c)<br />
### Cousins magnitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CousinsMagnitude`
Description | <p>A magnitude measured in one of Cousins standard passbands (using a standard filter, i.e. I or R).</p>
Super-classes |[om:Magnitude](http://opendata.caceres.es/def/ontomunicipio#Magnitude) (c)<br />
Sub-classes |[om:RMagnitude](http://opendata.caceres.es/def/ontomunicipio#RMagnitude) (c)<br />[om:IMagnitude](http://opendata.caceres.es/def/ontomunicipio#IMagnitude) (c)<br />
### coverage
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Coverage`
Super-classes |[om:AreaFraction](http://opendata.caceres.es/def/ontomunicipio#AreaFraction) (c)<br />
### Cowling number
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CowlingNumber`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
### Cowling number unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CowlingNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### critical density
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CriticalDensity`
Description | <p>The density needed for a closed universe.</p>
Super-classes |[om:Density](http://opendata.caceres.es/def/ontomunicipio#Density) (c)<br />
### cubic prefixed metre
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CubicPrefixedMetre`
Super-classes |[om:UnitExponentiation](http://opendata.caceres.es/def/ontomunicipio#UnitExponentiation) (c)<br />
Has members |[om:cubicKilometre](http://opendata.caceres.es/def/ontomunicipio#cubicKilometre)<br />[om:cubicTerametre](http://opendata.caceres.es/def/ontomunicipio#cubicTerametre)<br />[om:cubicDecametre](http://opendata.caceres.es/def/ontomunicipio#cubicDecametre)<br />[om:cubicAttometre](http://opendata.caceres.es/def/ontomunicipio#cubicAttometre)<br />[om:cubicDecimetre](http://opendata.caceres.es/def/ontomunicipio#cubicDecimetre)<br />[om:cubicMegametre](http://opendata.caceres.es/def/ontomunicipio#cubicMegametre)<br />[om:cubicZettametre](http://opendata.caceres.es/def/ontomunicipio#cubicZettametre)<br />[om:cubicExametre](http://opendata.caceres.es/def/ontomunicipio#cubicExametre)<br />[om:cubicMillimetre](http://opendata.caceres.es/def/ontomunicipio#cubicMillimetre)<br />[om:cubicPicometre](http://opendata.caceres.es/def/ontomunicipio#cubicPicometre)<br />[om:cubicCentimetre](http://opendata.caceres.es/def/ontomunicipio#cubicCentimetre)<br />[om:cubicPetametre](http://opendata.caceres.es/def/ontomunicipio#cubicPetametre)<br />[om:cubicYottametre](http://opendata.caceres.es/def/ontomunicipio#cubicYottametre)<br />[om:cubicYoctometre](http://opendata.caceres.es/def/ontomunicipio#cubicYoctometre)<br />[om:cubicMicrometre](http://opendata.caceres.es/def/ontomunicipio#cubicMicrometre)<br />[om:cubicNanometre](http://opendata.caceres.es/def/ontomunicipio#cubicNanometre)<br />[om:cubicGigametre](http://opendata.caceres.es/def/ontomunicipio#cubicGigametre)<br />[om:cubicZeptometre](http://opendata.caceres.es/def/ontomunicipio#cubicZeptometre)<br />[om:cubicHectometre](http://opendata.caceres.es/def/ontomunicipio#cubicHectometre)<br />[om:cubicFemtometre](http://opendata.caceres.es/def/ontomunicipio#cubicFemtometre)<br />
### current density
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CurrentDensity`
Description | <p>Current density is the density of flow of a conserved charge. It is a derived quantity in the International System of Units. Current density is electric current divided by area.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:currentDensity-Dimension](http://opendata.caceres.es/def/ontomunicipio#currentDensity-Dimension) (c)<br />
### current density unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CurrentDensityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### curvature constant
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CurvatureConstant`
Description | <p>The curvature constant k=-1, 0, or 1.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
### curvature constant unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#CurvatureConstantUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### cut-off wavelength
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Cut-OffWavelength`
Description | <p>Either: wavelengths at which the detectivity (D) falls to 0, or the wavelengths at which the detectivity falls to 1% of the peak value, or the wavelengths at which the normalised detectivity (D*) has fallen to half its peak value.</p>
Super-classes |[om:Wavelength](http://opendata.caceres.es/def/ontomunicipio#Wavelength) (c)<br />
### dark noise
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#DarkNoise`
Description | <p>Output from a detector when unilluminated - usually as RMS voltage or current (Kitchin, Astrophysical Techniques, IoP, Table 1.1.2).</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### date
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Date`
Super-classes |[om:Time](http://opendata.caceres.es/def/ontomunicipio#Time) (c)<br />
Sub-classes |[om:Epoch](http://opendata.caceres.es/def/ontomunicipio#Epoch) (c)<br />
### deceleration parameter
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#DecelerationParameter`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### deceleration parameter unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#DecelerationParameterUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### declination
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Declination`
Description | <p>The angular distance on the celestial sphere north or south of the celestial equator. It is measured along the hour circle passing through the celestial object. Declination is usually given in combination with right ascension or hour angle.</p>
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
### density
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Density`
Description | <p>Density is the concentration of matter. It is a derived quantity in the International System of Units. Density is mass divided by volume.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:density-Dimension](http://opendata.caceres.es/def/ontomunicipio#density-Dimension) (c)<br />
Sub-classes |[om:CriticalDensity](http://opendata.caceres.es/def/ontomunicipio#CriticalDensity) (c)<br />
### density parameter
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#DensityParameter`
Description | <p>Ratio of the average density and the critical density.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:DensityParameterForMatter](http://opendata.caceres.es/def/ontomunicipio#DensityParameterForMatter) (c)<br />[om:DensityParameterForBaryonicMatter](http://opendata.caceres.es/def/ontomunicipio#DensityParameterForBaryonicMatter) (c)<br />[om:DensityParameterForVacuum](http://opendata.caceres.es/def/ontomunicipio#DensityParameterForVacuum) (c)<br />[om:TotalDensityParameter](http://opendata.caceres.es/def/ontomunicipio#TotalDensityParameter) (c)<br />[om:DensityParameterForRadiation](http://opendata.caceres.es/def/ontomunicipio#DensityParameterForRadiation) (c)<br />
### density parameter for baryonic matter
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#DensityParameterForBaryonicMatter`
Description | <p>The density parameter for baryonic (oridnary) matter.</p>
Super-classes |[om:DensityParameter](http://opendata.caceres.es/def/ontomunicipio#DensityParameter) (c)<br />
### density parameter for matter
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#DensityParameterForMatter`
Description | <p>The density parameter for matter (either baryonic or dark).</p>
Super-classes |[om:DensityParameter](http://opendata.caceres.es/def/ontomunicipio#DensityParameter) (c)<br />
### density parameter for radiation
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#DensityParameterForRadiation`
Description | <p>The density parameter for radiation.</p>
Super-classes |[om:DensityParameter](http://opendata.caceres.es/def/ontomunicipio#DensityParameter) (c)<br />
### density parameter for vacuum
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#DensityParameterForVacuum`
Description | <p>The density parameter for vacuum.</p>
Super-classes |[om:DensityParameter](http://opendata.caceres.es/def/ontomunicipio#DensityParameter) (c)<br />
### density parameter unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#DensityParameterUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### density unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#DensityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### depth
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Depth`
Super-classes |[om:Length](http://opendata.caceres.es/def/ontomunicipio#Length) (c)<br />
### detective quantum efficiency
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#DetectiveQuantumEfficiency`
Description | <p>Square of ratio between the output signal noise ratio and the input signal noise ratio.</p>
Super-classes |[om:QuantumEfficiency](http://opendata.caceres.es/def/ontomunicipio#QuantumEfficiency) (c)<br />
### detectivity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Detectivity`
Description | <p>Reciprocal of Noise equivalent power. The signal-to-noise ratio for incident radiation of unit intensity.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### detectivity unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#DetectivityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### diameter
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Diameter`
Super-classes |[om:Length](http://opendata.caceres.es/def/ontomunicipio#Length) (c)<br />
### diameter (angle)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Diameter-Angle`
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
### dimension
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Dimension`
Description | <p>Dimensions are abstract properties of units and quantities neglecting their vectorial or tensorial character and all numerical factors including their sign.</p>
In domain of |[om:hasSILuminousIntensityDimensionExponent](http://opendata.caceres.es/def/ontomunicipio#hasSILuminousIntensityDimensionExponent) (dp)<br />[om:hasSIElectricCurrentDimensionExponent](http://opendata.caceres.es/def/ontomunicipio#hasSIElectricCurrentDimensionExponent) (dp)<br />[om:hasSIMassDimensionExponent](http://opendata.caceres.es/def/ontomunicipio#hasSIMassDimensionExponent) (dp)<br />[om:hasSILengthDimensionExponent](http://opendata.caceres.es/def/ontomunicipio#hasSILengthDimensionExponent) (dp)<br />[om:hasSIAmountOfSubstanceDimensionExponent](http://opendata.caceres.es/def/ontomunicipio#hasSIAmountOfSubstanceDimensionExponent) (dp)<br />[om:hasSIThermodynamicTemperatureDimensionExponent](http://opendata.caceres.es/def/ontomunicipio#hasSIThermodynamicTemperatureDimensionExponent) (dp)<br />[om:hasSITimeDimensionExponent](http://opendata.caceres.es/def/ontomunicipio#hasSITimeDimensionExponent) (dp)<br />
In range of |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op)<br />
Has members |[om:electricPotential-Dimension](http://opendata.caceres.es/def/ontomunicipio#electricPotential-Dimension)<br />[om:heatTransferCoefficient-Dimension](http://opendata.caceres.es/def/ontomunicipio#heatTransferCoefficient-Dimension)<br />[om:specificCatalyticActivity-Dimension](http://opendata.caceres.es/def/ontomunicipio#specificCatalyticActivity-Dimension)<br />[om:exposure-Dimension](http://opendata.caceres.es/def/ontomunicipio#exposure-Dimension)<br />[om:thermalInsulance-Dimension](http://opendata.caceres.es/def/ontomunicipio#thermalInsulance-Dimension)<br />[om:kinematicViscosityOrThermalDiffusivity-Dimension](http://opendata.caceres.es/def/ontomunicipio#kinematicViscosityOrThermalDiffusivity-Dimension)<br />[om:power-Dimension](http://opendata.caceres.es/def/ontomunicipio#power-Dimension)<br />[om:volumetricFlowRate-Dimension](http://opendata.caceres.es/def/ontomunicipio#volumetricFlowRate-Dimension)<br />[om:electricalResistance-Dimension](http://opendata.caceres.es/def/ontomunicipio#electricalResistance-Dimension)<br />[om:massFlow-Dimension](http://opendata.caceres.es/def/ontomunicipio#massFlow-Dimension)<br />[om:magneticFluxDensity-Dimension](http://opendata.caceres.es/def/ontomunicipio#magneticFluxDensity-Dimension)<br />[om:radiance-Dimension](http://opendata.caceres.es/def/ontomunicipio#radiance-Dimension)<br />[om:amountOfSubstance-Dimension](http://opendata.caceres.es/def/ontomunicipio#amountOfSubstance-Dimension)<br />[om:wavenumber-Dimension](http://opendata.caceres.es/def/ontomunicipio#wavenumber-Dimension)<br />[om:luminousFlux-Dimension](http://opendata.caceres.es/def/ontomunicipio#luminousFlux-Dimension)<br />[om:capacitance-Dimension](http://opendata.caceres.es/def/ontomunicipio#capacitance-Dimension)<br />[om:angularAcceleration-Dmension](http://opendata.caceres.es/def/ontomunicipio#angularAcceleration-Dmension)<br />[om:specificVolume-Dimension](http://opendata.caceres.es/def/ontomunicipio#specificVolume-Dimension)<br />[om:specificEntropyOrSpecificHeatCapacity-Dimension](http://opendata.caceres.es/def/ontomunicipio#specificEntropyOrSpecificHeatCapacity-Dimension)<br />[om:inductanceOrPermeance-Electromagnetic-Dimension](http://opendata.caceres.es/def/ontomunicipio#inductanceOrPermeance-Electromagnetic-Dimension)<br />[om:angularSpeed-Dimension](http://opendata.caceres.es/def/ontomunicipio#angularSpeed-Dimension)<br />[om:reluctance-Dimension](http://opendata.caceres.es/def/ontomunicipio#reluctance-Dimension)<br />[om:volumetricHeatCapacity-Dimension](http://opendata.caceres.es/def/ontomunicipio#volumetricHeatCapacity-Dimension)<br />[om:luminousEnergy-Dimension](http://opendata.caceres.es/def/ontomunicipio#luminousEnergy-Dimension)<br />[om:magneticFlux-Dimension](http://opendata.caceres.es/def/ontomunicipio#magneticFlux-Dimension)<br />[om:length-Dimension](http://opendata.caceres.es/def/ontomunicipio#length-Dimension)<br />[om:electricField-Dimension](http://opendata.caceres.es/def/ontomunicipio#electricField-Dimension)<br />[om:numberDensity-Dimension](http://opendata.caceres.es/def/ontomunicipio#numberDensity-Dimension)<br />[om:electricalConductance-Dimension](http://opendata.caceres.es/def/ontomunicipio#electricalConductance-Dimension)<br />[om:electricDipoleMoment-Dimension](http://opendata.caceres.es/def/ontomunicipio#electricDipoleMoment-Dimension)<br />[om:surfaceTension-Dimension](http://opendata.caceres.es/def/ontomunicipio#surfaceTension-Dimension)<br />[om:exposureToXAndGammaRays-Dimension](http://opendata.caceres.es/def/ontomunicipio#exposureToXAndGammaRays-Dimension)<br />[om:thermalResistance-Dimension](http://opendata.caceres.es/def/ontomunicipio#thermalResistance-Dimension)<br />[om:currentDensity-Dimension](http://opendata.caceres.es/def/ontomunicipio#currentDensity-Dimension)<br />[om:time-Dimension](http://opendata.caceres.es/def/ontomunicipio#time-Dimension)<br />[om:entropyOrHeatCapacity-Dimension](http://opendata.caceres.es/def/ontomunicipio#entropyOrHeatCapacity-Dimension)<br />[om:electricCurrent-Dimension](http://opendata.caceres.es/def/ontomunicipio#electricCurrent-Dimension)<br />[om:electricCharge-Dimension](http://opendata.caceres.es/def/ontomunicipio#electricCharge-Dimension)<br />[om:area-Dimension](http://opendata.caceres.es/def/ontomunicipio#area-Dimension)<br />[om:pressure-Dimension](http://opendata.caceres.es/def/ontomunicipio#pressure-Dimension)<br />[om:catalyticActivityConcentration-Dimension](http://opendata.caceres.es/def/ontomunicipio#catalyticActivityConcentration-Dimension)<br />[om:volume-Dimension](http://opendata.caceres.es/def/ontomunicipio#volume-Dimension)<br />[om:permeance-MaterialsScience-Dimension](http://opendata.caceres.es/def/ontomunicipio#permeance-MaterialsScience-Dimension)<br />[om:actionOrAngularMomentum-Dimension](http://opendata.caceres.es/def/ontomunicipio#actionOrAngularMomentum-Dimension)<br />[om:thermalConductivity-Dimension](http://opendata.caceres.es/def/ontomunicipio#thermalConductivity-Dimension)<br />[om:permeabilityOfFreeSpace-Dimension](http://opendata.caceres.es/def/ontomunicipio#permeabilityOfFreeSpace-Dimension)<br />[om:speed-Dimension](http://opendata.caceres.es/def/ontomunicipio#speed-Dimension)<br />[om:frequency-Dimension](http://opendata.caceres.es/def/ontomunicipio#frequency-Dimension)<br />[om:absorbedDoseRate-Dimension](http://opendata.caceres.es/def/ontomunicipio#absorbedDoseRate-Dimension)<br />[om:energyDensity-Dimension](http://opendata.caceres.es/def/ontomunicipio#energyDensity-Dimension)<br />[om:luminance-Dimension](http://opendata.caceres.es/def/ontomunicipio#luminance-Dimension)<br />[om:mass-Dimension](http://opendata.caceres.es/def/ontomunicipio#mass-Dimension)<br />[om:catalyticActivity-Dimension](http://opendata.caceres.es/def/ontomunicipio#catalyticActivity-Dimension)<br />[om:electricalResistivity-Dimension](http://opendata.caceres.es/def/ontomunicipio#electricalResistivity-Dimension)<br />[om:luminousIntensity-Dimension](http://opendata.caceres.es/def/ontomunicipio#luminousIntensity-Dimension)<br />[om:dynamicViscosity-Dimension](http://opendata.caceres.es/def/ontomunicipio#dynamicViscosity-Dimension)<br />[om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne)<br />[om:luminousEfficacy-Dimension](http://opendata.caceres.es/def/ontomunicipio#luminousEfficacy-Dimension)<br />[om:acceleration-Dmension](http://opendata.caceres.es/def/ontomunicipio#acceleration-Dmension)<br />[om:permittivity-Dimension](http://opendata.caceres.es/def/ontomunicipio#permittivity-Dimension)<br />[om:molarEnergy-Dimension](http://opendata.caceres.es/def/ontomunicipio#molarEnergy-Dimension)<br />[om:electricFluxDensity-Dimension](http://opendata.caceres.es/def/ontomunicipio#electricFluxDensity-Dimension)<br />[om:thermodynamicTemperature-Dimension](http://opendata.caceres.es/def/ontomunicipio#thermodynamicTemperature-Dimension)<br />[om:energy-Dimension](http://opendata.caceres.es/def/ontomunicipio#energy-Dimension)<br />[om:powerDensity-Dimension](http://opendata.caceres.es/def/ontomunicipio#powerDensity-Dimension)<br />[om:density-Dimension](http://opendata.caceres.es/def/ontomunicipio#density-Dimension)<br />[om:electricChargeDensity-Dimension](http://opendata.caceres.es/def/ontomunicipio#electricChargeDensity-Dimension)<br />[om:electricalConductivity-Dimension](http://opendata.caceres.es/def/ontomunicipio#electricalConductivity-Dimension)<br />[om:columnNumberDensity-Dimension](http://opendata.caceres.es/def/ontomunicipio#columnNumberDensity-Dimension)<br />[om:specificEnergyOrAbsorbedDoseOrDoseEquivalent-Dimension](http://opendata.caceres.es/def/ontomunicipio#specificEnergyOrAbsorbedDoseOrDoseEquivalent-Dimension)<br />[om:illuminance-Dimension](http://opendata.caceres.es/def/ontomunicipio#illuminance-Dimension)<br />[om:fluidity-Dimension](http://opendata.caceres.es/def/ontomunicipio#fluidity-Dimension)<br />[om:MagneticField-Dimension](http://opendata.caceres.es/def/ontomunicipio#MagneticField-Dimension)<br />[om:amountOfSubstanceConcentration-Dimension](http://opendata.caceres.es/def/ontomunicipio#amountOfSubstanceConcentration-Dimension)<br />[om:force-Dimension](http://opendata.caceres.es/def/ontomunicipio#force-Dimension)<br />[om:molarEntropyOrMolarHeatCapacityOrGasConstant-Dimension](http://opendata.caceres.es/def/ontomunicipio#molarEntropyOrMolarHeatCapacityOrGasConstant-Dimension)<br />
### directional dose equivalent
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#DirectionalDoseEquivalent`
Super-classes |[om:DoseEquivalent](http://opendata.caceres.es/def/ontomunicipio#DoseEquivalent) (c)<br />
### disodium ethylene diamine tetra acetate mass fraction
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#DisodiumEthyleneDiamineTetreAcetateMassFraction`
Description | <p>The fraction of the mass of disodium ethylene diamine tetra acetate in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### displacement
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Displacement`
Super-classes |[om:Length](http://opendata.caceres.es/def/ontomunicipio#Length) (c)<br />
### distance
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Distance`
Super-classes |[om:Length](http://opendata.caceres.es/def/ontomunicipio#Length) (c)<br />
Sub-classes |[om:xy2DStartEndDistance](http://opendata.caceres.es/def/ontomunicipio#xy2DStartEndDistance) (c)<br />[om:DistanceModulus](http://opendata.caceres.es/def/ontomunicipio#DistanceModulus) (c)<br />[om:Total3DStartEndDistance](http://opendata.caceres.es/def/ontomunicipio#Total3DStartEndDistance) (c)<br />[om:TotalDistanceTravelled](http://opendata.caceres.es/def/ontomunicipio#TotalDistanceTravelled) (c)<br />[om:xyDistanceTravelled](http://opendata.caceres.es/def/ontomunicipio#xyDistanceTravelled) (c)<br />
### distance modulus
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#DistanceModulus`
Description | <p>The difference between the apparent magnitude (m) of an astronomical object, such as a star, and its absolute magnitude (M), used as a distance measurement. Distances can be expressed in distance modulii as $$m-M = 5\log d + 10 = 10-5 log \varpi$$ where (d) is the distance in kiloparsec and (\varpi) is the parallax in milliarcseconds.</p>
Super-classes |[om:Distance](http://opendata.caceres.es/def/ontomunicipio#Distance) (c)<br />
Sub-classes |[om:TrueDistanceModulus](http://opendata.caceres.es/def/ontomunicipio#TrueDistanceModulus) (c)<br />[om:ApparentDistanceModulus](http://opendata.caceres.es/def/ontomunicipio#ApparentDistanceModulus) (c)<br />
### diurnal aberration
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#DiurnalAberration`
Description | <p>The component of the stellar abberation resulting from the diurnal motion of the observer around the centre of the Earth. The abberation is the apparent angular displacement of the observed position of a celestial object from its geometric position, caused by the finite velocity of light in combination with the motions of the observer and of the observed object.</p>
Super-classes |[om:AngularDisplacement](http://opendata.caceres.es/def/ontomunicipio#AngularDisplacement) (c)<br />
### dose equivalent
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#DoseEquivalent`
Description | <p>Dose equivalent is a measure of the radiation dose to tissue where an attempt has been made to allow for the different relative biological effects of different types of ionizing radiation.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:specificEnergyOrAbsorbedDoseOrDoseEquivalent-Dimension](http://opendata.caceres.es/def/ontomunicipio#specificEnergyOrAbsorbedDoseOrDoseEquivalent-Dimension) (c)<br />
Sub-classes |[om:DirectionalDoseEquivalent](http://opendata.caceres.es/def/ontomunicipio#DirectionalDoseEquivalent) (c)<br />[om:OrganDoseEquivalent](http://opendata.caceres.es/def/ontomunicipio#OrganDoseEquivalent) (c)<br />[om:AmbientDoseEquivalent](http://opendata.caceres.es/def/ontomunicipio#AmbientDoseEquivalent) (c)<br />[om:PersonalDoseEquivalent](http://opendata.caceres.es/def/ontomunicipio#PersonalDoseEquivalent) (c)<br />
### dose equivalent unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#DoseEquivalentUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### drainage speed
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#DrainageSpeed`
Super-classes |[om:Speed](http://opendata.caceres.es/def/ontomunicipio#Speed) (c)<br />
### dry body mass
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#DryBodyMass`
Super-classes |[om:DryMass](http://opendata.caceres.es/def/ontomunicipio#DryMass) (c)<br />
### dry mass
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#DryMass`
Super-classes |[om:Mass](http://opendata.caceres.es/def/ontomunicipio#Mass) (c)<br />
Sub-classes |[om:DryBodyMass](http://opendata.caceres.es/def/ontomunicipio#DryBodyMass) (c)<br />
### dry matter mass fraction
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#DryMatterMassFraction`
Description | <p>The fraction of the mass of dry matter in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### duration
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Duration`
Super-classes |[om:Time](http://opendata.caceres.es/def/ontomunicipio#Time) (c)<br />
Has members |[om:durationOf9192631770PeriodsOfTheRadiationCorrespondingToTheTransitionBetweenTheTwoHyperfineLevelsOfTheGroundStateOfTheCesium133Atom](http://opendata.caceres.es/def/ontomunicipio#durationOf9192631770PeriodsOfTheRadiationCorrespondingToTheTransitionBetweenTheTwoHyperfineLevelsOfTheGroundStateOfTheCesium133Atom)<br />
### dynamic modulus
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#DynamicModulus`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:pressure-Dimension](http://opendata.caceres.es/def/ontomunicipio#pressure-Dimension) (c)<br />
Sub-classes |[om:LossModulus](http://opendata.caceres.es/def/ontomunicipio#LossModulus) (c)<br />[om:StorageModulus](http://opendata.caceres.es/def/ontomunicipio#StorageModulus) (c)<br />[om:ElasticityTensor](http://opendata.caceres.es/def/ontomunicipio#ElasticityTensor) (c)<br />[om:ShearModulus](http://opendata.caceres.es/def/ontomunicipio#ShearModulus) (c)<br />[om:BulkModulus](http://opendata.caceres.es/def/ontomunicipio#BulkModulus) (c)<br />[om:ModulusOfElasticity](http://opendata.caceres.es/def/ontomunicipio#ModulusOfElasticity) (c)<br />
### dynamic range
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#DynamicRange`
Description | <p>Ratio between the saturation output and the dark signal, sometimes only over the region of linearity.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
### dynamic range unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#DynamicRangeUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### dynamic viscosity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#DynamicViscosity`
Description | <p>Viscosity is the definite resistance to change of form of many materials.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dynamicViscosity-Dimension](http://opendata.caceres.es/def/ontomunicipio#dynamicViscosity-Dimension) (c)<br />
### dynamic viscosity unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#DynamicViscosityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### eccentricity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Eccentricity`
Description | <p>A measure of the deviation from a circle for an orbit.</p>
Super-classes |[om:QuantityOfDimensionOne](http://opendata.caceres.es/def/ontomunicipio#QuantityOfDimensionOne) (c)<br />
### ecliptic latitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#EclipticLatitude`
Description | <p>The angular distance on the celestial sphere north or south of the ecliptic (the path of the Sun on the celestial sphere during one year). It is measured along the great circle passing through the object and the ecliptic poles and perpendicular to the ecliptic.</p>
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
### ecliptic longitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#EclipticLongitude`
Description | <p>The angular distance on the celestial sphere measured clockwise from the vernal equinox along the ecliptic (the path of the Sun on the celestial sphere during one year) to the intersection with the great circle drawn from the ecliptical north pole through the object.</p>
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
### egg mass fraction
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#EggMassFraction`
Description | <p>The fraction of the mass of egg in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### elasticity tensor
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ElasticityTensor`
Super-classes |[om:DynamicModulus](http://opendata.caceres.es/def/ontomunicipio#DynamicModulus) (c)<br />
### electric charge
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ElectricCharge`
Description | <p>Electric charge is a conserved property of some subatomic particles, which determines their electromagnetic interaction. It is a derived quantity in the International System of Units. Electric charge is electric current times time.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:electricCharge-Dimension](http://opendata.caceres.es/def/ontomunicipio#electricCharge-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### electric charge density
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ElectricChargeDensity`
Description | <p>Electric charge density is the amount of electric charge in a volume. It is a derived quantity in the International System of Units. Electric charge density is electric charge divided by volume.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:electricChargeDensity-Dimension](http://opendata.caceres.es/def/ontomunicipio#electricChargeDensity-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### electric charge density unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ElectricChargeDensityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### electric charge unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ElectricChargeUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### electric current
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ElectricCurrent`
Description | <p>Electric current is the flow of electric charge. It is a base quantity in the International System of Units. Electric current is electric charge divided by time.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:electricCurrent-Dimension](http://opendata.caceres.es/def/ontomunicipio#electricCurrent-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Has members |[om:constantCurrentThatProducesAnAttractiveForceOf2e-7NewtonPerMetreOfLengthBetweenTwoStraightParallelConductorsOfInfiniteLengthAndNegligibleCircularCrossSectionPlacedOneMetreApartInAVacuum](http://opendata.caceres.es/def/ontomunicipio#constantCurrentThatProducesAnAttractiveForceOf2e-7NewtonPerMetreOfLengthBetweenTwoStraightParallelConductorsOfInfiniteLengthAndNegligibleCircularCrossSectionPlacedOneMetreApartInAVacuum)<br />
### electric current unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ElectricCurrentUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### electric dipole moment
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ElectricDipoleMoment`
Description | <p>Electric dipole moment is a measure of the polarity of a system of electric charges.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:electricDipoleMoment-Dimension](http://opendata.caceres.es/def/ontomunicipio#electricDipoleMoment-Dimension) (c)<br />
### electric dipole moment unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ElectricDipoleMomentUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### electric field
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ElectricField`
Description | <p>Electric field is a property of the space surrounding an electric charge or in the presence of a time-varying magnetic field which exerts a forceon other electrically charged objects.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:electricField-Dimension](http://opendata.caceres.es/def/ontomunicipio#electricField-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### electric field unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ElectricFieldUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### electric flux density
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ElectricFluxDensity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:electricFluxDensity-Dimension](http://opendata.caceres.es/def/ontomunicipio#electricFluxDensity-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### electric flux density unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ElectricFluxDensityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### electric potential
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ElectricPotential`
Description | <p>Electric potential is the potential energy per unit charge associated with static (time-invariant) electric field.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:electricPotential-Dimension](http://opendata.caceres.es/def/ontomunicipio#electricPotential-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:PotentialDifference](http://opendata.caceres.es/def/ontomunicipio#PotentialDifference) (c)<br />[om:ElectromotiveForce](http://opendata.caceres.es/def/ontomunicipio#ElectromotiveForce) (c)<br />
### electric potential unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ElectricPotentialUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### electrical conductance
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ElectricalConductance`
Description | <p>Electrical conductance is a measure of how easily electricity flows along a certain path through an electrical element.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:electricalConductance-Dimension](http://opendata.caceres.es/def/ontomunicipio#electricalConductance-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### electrical conductance unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ElectricalConductanceUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### electrical conductivity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ElectricalConductivity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:electricalConductivity-Dimension](http://opendata.caceres.es/def/ontomunicipio#electricalConductivity-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### electrical conductivity unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ElectricalConductivityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### electrical resistance
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ElectricalResistance`
Description | <p>Electrical resistance is the degree to which an object opposes an electric current through it. It is a derived quantity in the International System of Units.  Electrical resistance is electric potential divided by electric current.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:electricalResistance-Dimension](http://opendata.caceres.es/def/ontomunicipio#electricalResistance-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### electrical resistance unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ElectricalResistanceUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### electrical resistivity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ElectricalResistivity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:electricalResistivity-Dimension](http://opendata.caceres.es/def/ontomunicipio#electricalResistivity-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### electrical resistivity unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ElectricalResistivityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### electromotive force
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ElectromotiveForce`
Description | <p>Electromotive force is that which causes a flow of current.</p>
Super-classes |[om:ElectricPotential](http://opendata.caceres.es/def/ontomunicipio#ElectricPotential) (c)<br />
### electron temperature
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ElectronTemperature`
Description | <p>The temperature determined by the mean kinetic energy of free electrons in a plasma; also known as kinetic temperature.</p>
Super-classes |[om:ThermodynamicTemperature](http://opendata.caceres.es/def/ontomunicipio#ThermodynamicTemperature) (c)<br />
### ellipticity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Ellipticity`
Description | <p>A measure of the amount by which an object, such as a planet or a galaxy, deviates from a perfect sphere.</p>
Super-classes |[om:QuantityOfDimensionOne](http://opendata.caceres.es/def/ontomunicipio#QuantityOfDimensionOne) (c)<br />
### energy
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Energy`
Description | <p>Energy can be defined as the ability to do work. It is a derived quantity in the International System of Units.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:energy-Dimension](http://opendata.caceres.es/def/ontomunicipio#energy-Dimension) (c)<br />
Sub-classes |[om:InternalEnergy](http://opendata.caceres.es/def/ontomunicipio#InternalEnergy) (c)<br />[om:RadiantEnergy](http://opendata.caceres.es/def/ontomunicipio#RadiantEnergy) (c)<br />[om:PotentialEnergy](http://opendata.caceres.es/def/ontomunicipio#PotentialEnergy) (c)<br />[om:Work](http://opendata.caceres.es/def/ontomunicipio#Work) (c)<br />[om:Enthalpy](http://opendata.caceres.es/def/ontomunicipio#Enthalpy) (c)<br />[om:Heat](http://opendata.caceres.es/def/ontomunicipio#Heat) (c)<br />[om:KineticEnergy](http://opendata.caceres.es/def/ontomunicipio#KineticEnergy) (c)<br />
### energy density
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#EnergyDensity`
Description | <p>Energy density is the amount of energy stored in a given system or region of space per unit volume.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:energyDensity-Dimension](http://opendata.caceres.es/def/ontomunicipio#energyDensity-Dimension) (c)<br />
### energy density unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#EnergyDensityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### energy unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#EnergyUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### enthalpy
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Enthalpy`
Description | <p>Enthalpy is the sum of the internal energy of a system plus the product of the pressure-volume work done on the system.</p>
Super-classes |[om:Energy](http://opendata.caceres.es/def/ontomunicipio#Energy) (c)<br />
### entropy
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Entropy`
Description | <p>Entropy is a measure of the unavailability of a system’s energy to do work.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:entropyOrHeatCapacity-Dimension](http://opendata.caceres.es/def/ontomunicipio#entropyOrHeatCapacity-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### entropy unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#EntropyUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### epoch
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Epoch`
Super-classes |[om:Date](http://opendata.caceres.es/def/ontomunicipio#Date) (c)<br />
Sub-classes |[om:EpochAtMaximumBrightness](http://opendata.caceres.es/def/ontomunicipio#EpochAtMaximumBrightness) (c)<br />
### epoch at maximum brightness
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#EpochAtMaximumBrightness`
Description | <p>A moment when the object (i.e. a variable star) was at maximum brightness.</p>
Super-classes |[om:Epoch](http://opendata.caceres.es/def/ontomunicipio#Epoch) (c)<br />
### Euler number
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#EulerNumber`
Description | <p>The Euler number is a dimensionless number that expresses the relationship between a local pressure drop e.g. over a restriction and the kinetic energy per unit volume.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
### Euler number unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#EulerNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### exposure
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Exposure`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:exposure-Dimension](http://opendata.caceres.es/def/ontomunicipio#exposure-Dimension) (c)<br />
### exposure to x and γ rays
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ExposureToXAndGammaRays`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:exposureToXAndGammaRays-Dimension](http://opendata.caceres.es/def/ontomunicipio#exposureToXAndGammaRays-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### exposure to x and γ rays unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ExposureToXAndGammaRaysUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### exposure unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ExposureUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### external browning
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ExternalBrowning`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### extinction
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Extinction`
Description | <p>Total extinction at a specific wavelength. The extinction is caused by dust and gas between a star and the observer. It is the difference between the observed magnitude and the magnitude the source would have had if no extinction had taken place.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Sub-classes |[om:ExtinctionAtWavelength](http://opendata.caceres.es/def/ontomunicipio#ExtinctionAtWavelength) (c)<br />[om:ExtinctionAtWaveband](http://opendata.caceres.es/def/ontomunicipio#ExtinctionAtWaveband) (c)<br />
### extinction at waveband
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ExtinctionAtWaveband`
Super-classes |[om:Extinction](http://opendata.caceres.es/def/ontomunicipio#Extinction) (c)<br />
Sub-classes |[om:ExtinctionInU](http://opendata.caceres.es/def/ontomunicipio#ExtinctionInU) (c)<br />[om:ExtinctionInB](http://opendata.caceres.es/def/ontomunicipio#ExtinctionInB) (c)<br />[om:ExtinctionInV](http://opendata.caceres.es/def/ontomunicipio#ExtinctionInV) (c)<br />
### extinction at wavelength
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ExtinctionAtWavelength`
Super-classes |[om:Extinction](http://opendata.caceres.es/def/ontomunicipio#Extinction) (c)<br />
### extinction in B
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ExtinctionInB`
Super-classes |[om:ExtinctionAtWaveband](http://opendata.caceres.es/def/ontomunicipio#ExtinctionAtWaveband) (c)<br />
### extinction in U
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ExtinctionInU`
Super-classes |[om:ExtinctionAtWaveband](http://opendata.caceres.es/def/ontomunicipio#ExtinctionAtWaveband) (c)<br />
### extinction in V
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ExtinctionInV`
Super-classes |[om:ExtinctionAtWaveband](http://opendata.caceres.es/def/ontomunicipio#ExtinctionAtWaveband) (c)<br />
### Fahrenheit temperature
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#FahrenheitTemperature`
Super-classes |[om:Temperature](http://opendata.caceres.es/def/ontomunicipio#Temperature) (c)<br />
Restrictions |[om:hasScale](http://opendata.caceres.es/def/ontomunicipio#hasScale) (op) **value** [om:FahrenheitScale](http://opendata.caceres.es/def/ontomunicipio#FahrenheitScale) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### Fahrenheit temperature scale
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#FahrenheitTemperatureScale`
Super-classes |[om:Scale](http://opendata.caceres.es/def/ontomunicipio#Scale) (c)<br />
### Fahrenheit temperature unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#FahrenheitTemperatureUnit`
Super-classes |[om:TemperatureUnit](http://opendata.caceres.es/def/ontomunicipio#TemperatureUnit) (c)<br />
### fat mass fraction
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#FatMassFraction`
Description | <p>The fraction of the mass of fat in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### firmness (penetrometer) (method 1)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Firmness-Penetrometer-Method1`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### firmness (penetrometer) (method 2)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Firmness-Penetrometer-Method2`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### first Cowling number
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#FirstCowlingNumber`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
### first Cowling number unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#FirstCowlingNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### fixed point
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#FixedPoint`
Super-classes |[om:Point](http://opendata.caceres.es/def/ontomunicipio#Point) (c)<br />
Restrictions |[om:hasPoint](http://opendata.caceres.es/def/ontomunicipio#hasPoint) (op) **only** ([om:FixedPoint](http://opendata.caceres.es/def/ontomunicipio#FixedPoint) (c))<br />
Sub-classes |[om:FixedZeroPoint](http://opendata.caceres.es/def/ontomunicipio#FixedZeroPoint) (c)<br />
Has members |[om:_54.3584OnTheKelvinScale](http://opendata.caceres.es/def/ontomunicipio#_54.3584OnTheKelvinScale)<br />[om:approximately17OnTheKelvinScale](http://opendata.caceres.es/def/ontomunicipio#approximately17OnTheKelvinScale)<br />[om:_83.8058OnTheKelvinScale](http://opendata.caceres.es/def/ontomunicipio#_83.8058OnTheKelvinScale)<br />[om:_-218.7916OnTheCelsiusScale](http://opendata.caceres.es/def/ontomunicipio#_-218.7916OnTheCelsiusScale)<br />[om:_156.5985OnTheCelsiusScale](http://opendata.caceres.es/def/ontomunicipio#_156.5985OnTheCelsiusScale)<br />[om:_-259.3467OnTheCelsiusScale](http://opendata.caceres.es/def/ontomunicipio#_-259.3467OnTheCelsiusScale)<br />[om:_1234.93OnTheKelvinScale](http://opendata.caceres.es/def/ontomunicipio#_1234.93OnTheKelvinScale)<br />[om:_933.473OnTheKelvinScale](http://opendata.caceres.es/def/ontomunicipio#_933.473OnTheKelvinScale)<br />[om:_302.9146OnTheKelvinScale](http://opendata.caceres.es/def/ontomunicipio#_302.9146OnTheKelvinScale)<br />[om:approximately-252.85OnTheCelsiusScale](http://opendata.caceres.es/def/ontomunicipio#approximately-252.85OnTheCelsiusScale)<br />[om:_-248.5939OnTheCelsiusScale](http://opendata.caceres.es/def/ontomunicipio#_-248.5939OnTheCelsiusScale)<br />[om:_1064.18OnTheCelsiusScale](http://opendata.caceres.es/def/ontomunicipio#_1064.18OnTheCelsiusScale)<br />[om:_-189.3442OnTheCelsiusScale](http://opendata.caceres.es/def/ontomunicipio#_-189.3442OnTheCelsiusScale)<br />[om:_1084.62OnTheCelsiusScale](http://opendata.caceres.es/def/ontomunicipio#_1084.62OnTheCelsiusScale)<br />[om:_3To5OnTheKelvinScale](http://opendata.caceres.es/def/ontomunicipio#_3To5OnTheKelvinScale)<br />[om:_-270.15To-268.15OnTheCelsiusScale](http://opendata.caceres.es/def/ontomunicipio#_-270.15To-268.15OnTheCelsiusScale)<br />[om:_961.78OnTheCelsiusScale](http://opendata.caceres.es/def/ontomunicipio#_961.78OnTheCelsiusScale)<br />[om:_273.16OnTheKelvinScale](http://opendata.caceres.es/def/ontomunicipio#_273.16OnTheKelvinScale)<br />[om:_660.323OnTheCelsiusScale](http://opendata.caceres.es/def/ontomunicipio#_660.323OnTheCelsiusScale)<br />[om:_13.8033OnTheKelvinScale](http://opendata.caceres.es/def/ontomunicipio#_13.8033OnTheKelvinScale)<br />[om:_429.7485OnTheKelvinScale](http://opendata.caceres.es/def/ontomunicipio#_429.7485OnTheKelvinScale)<br />[om:approximately203OnTheKelvinScale](http://opendata.caceres.es/def/ontomunicipio#approximately203OnTheKelvinScale)<br />[om:_234.3156OnTheKelvinScale](http://opendata.caceres.es/def/ontomunicipio#_234.3156OnTheKelvinScale)<br />[om:_692.677OnTheKelvinScale](http://opendata.caceres.es/def/ontomunicipio#_692.677OnTheKelvinScale)<br />[om:approximately-256.15OnTheCelsiusScale](http://opendata.caceres.es/def/ontomunicipio#approximately-256.15OnTheCelsiusScale)<br />[om:_-38.8344OnTheCelsiusScale](http://opendata.caceres.es/def/ontomunicipio#_-38.8344OnTheCelsiusScale)<br />[om:_24.5561OnTheKelvinScale](http://opendata.caceres.es/def/ontomunicipio#_24.5561OnTheKelvinScale)<br />[om:_505.078OnTheKelvinScale](http://opendata.caceres.es/def/ontomunicipio#_505.078OnTheKelvinScale)<br />[om:_419.527OnTheCelsiusScale](http://opendata.caceres.es/def/ontomunicipio#_419.527OnTheCelsiusScale)<br />[om:_1337.33OnTheKelvinScale](http://opendata.caceres.es/def/ontomunicipio#_1337.33OnTheKelvinScale)<br />[om:_1357.77OnTheKelvinScale](http://opendata.caceres.es/def/ontomunicipio#_1357.77OnTheKelvinScale)<br />[om:_29.7646OnTheCelsiusScale](http://opendata.caceres.es/def/ontomunicipio#_29.7646OnTheCelsiusScale)<br />[om:_0.01OnTheCelsiusScale](http://opendata.caceres.es/def/ontomunicipio#_0.01OnTheCelsiusScale)<br />[om:_231.928OnTheCelsiusScale](http://opendata.caceres.es/def/ontomunicipio#_231.928OnTheCelsiusScale)<br />
### fixed zero point
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#FixedZeroPoint`
Super-classes |[om:FixedPoint](http://opendata.caceres.es/def/ontomunicipio#FixedPoint) (c)<br />
### flowpack mass
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#FlowpackMass`
Super-classes |[om:Mass](http://opendata.caceres.es/def/ontomunicipio#Mass) (c)<br />
### fluidity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Fluidity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:fluidity-Dimension](http://opendata.caceres.es/def/ontomunicipio#fluidity-Dimension) (c)<br />
### fluidity unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#FluidityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### font size
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#FontSize`
Super-classes |[om:Length](http://opendata.caceres.es/def/ontomunicipio#Length) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### font size unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#FontSizeUnit`
Super-classes |[om:LengthUnit](http://opendata.caceres.es/def/ontomunicipio#LengthUnit) (c)<br />
### force
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Force`
Description | <p>Force is the extent to which an object with mass can be caused to accelerate. It is a derived quantity in the International System of Units. Force is mass times acceleration.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:force-Dimension](http://opendata.caceres.es/def/ontomunicipio#force-Dimension) (c)<br />
Sub-classes |[om:Thrust](http://opendata.caceres.es/def/ontomunicipio#Thrust) (c)<br />[om:Friction](http://opendata.caceres.es/def/ontomunicipio#Friction) (c)<br />[om:Weight](http://opendata.caceres.es/def/ontomunicipio#Weight) (c)<br />
### force unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ForceUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### Fourier number
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#FourierNumber`
Description | <p>The Fourier number is a dimensionless number that characterises heat conduction. It is the ratio of heat conduction rate to rate of thermal energy storage. The Fourier number is a dimensionless time.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
### Fourier number for mass transfer
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#FourierNumberForMassTransfer`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### Fourier number for mass transfer unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#FourierNumberForMassTransferUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### Fourier number unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#FourierNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### frequency
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Frequency`
Description | <p>Frequency is a measure of the number of occurrences of a repeating event per unit time.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:frequency-Dimension](http://opendata.caceres.es/def/ontomunicipio#frequency-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:CollisionFrequency](http://opendata.caceres.es/def/ontomunicipio#CollisionFrequency) (c)<br />
### frequency unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#FrequencyUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### friction
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Friction`
Description | <p>Friction is a force that resists the relative motion of solid surfaces, fluid layers, or material elements sliding against each other.</p>
Super-classes |[om:Force](http://opendata.caceres.es/def/ontomunicipio#Force) (c)<br />
### Froude number
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#FroudeNumber`
Description | <p>The Froude number is a dimensionless number that compares inertial and gravitational forces. It may be used to quantify the resistance of an object moving through water, and compare objects of different sizes.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### Froude number unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#FroudeNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### function
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Function`
In range of |[om:hasAggregateFunction](http://opendata.caceres.es/def/ontomunicipio#hasAggregateFunction) (op)<br />
Has members |[om:standardDeviation](http://opendata.caceres.es/def/ontomunicipio#standardDeviation)<br />[om:first](http://opendata.caceres.es/def/ontomunicipio#first)<br />[om:last](http://opendata.caceres.es/def/ontomunicipio#last)<br />[om:average](http://opendata.caceres.es/def/ontomunicipio#average)<br />[om:product](http://opendata.caceres.es/def/ontomunicipio#product)<br />[om:minimum](http://opendata.caceres.es/def/ontomunicipio#minimum)<br />[om:maximum](http://opendata.caceres.es/def/ontomunicipio#maximum)<br />[om:count](http://opendata.caceres.es/def/ontomunicipio#count)<br />[om:sum](http://opendata.caceres.es/def/ontomunicipio#sum)<br />
### galactic cylindrical polar angle coordinate
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#GalacticCylindricalPolarAngleCoordinate`
Description | <p>The angle from the Galactic centre between the perpendicular projection of the Sun on the Galactic plane and the projection of the object. This is one of the three Galactic Cylindrical Polar Coordinates.</p>
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
### galactic latitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#GalacticLatitude`
Description | <p>The angular distance on the celestial sphere north or south of the galactic equator. It is measured along the great circle passing through the object and the galactic poles and perpendicular to the galactic equator.</p>
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
### galactic longitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#GalacticLongitude`
Description | <p>The angular distance on the celestial sphere measured clockwise from the galactic centre (as defined by the International Astronomical Union (IAU)) along the galactic equator to the intersection with the great circle drawn from the galactic north pole through the object.</p>
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
### gas constant
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#GasConstant`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:molarEntropyOrMolarHeatCapacityOrGasConstant-Dimension](http://opendata.caceres.es/def/ontomunicipio#molarEntropyOrMolarHeatCapacityOrGasConstant-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### gas constant unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#GasConstantUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### gelatin mass fraction
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#GelatinMassFraction`
Description | <p>The fraction of the mass of gelatin in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### geometrical albedo
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#GeometricalAlbedo`
Description | <p>Ratio between the brightness of an object as seen from the direction of a hypothetical white, diffusely reflecting sphere of the same size and at the same distance.</p>
Super-classes |[om:Albedo](http://opendata.caceres.es/def/ontomunicipio#Albedo) (c)<br />
### gram per prefixed litre
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#GramPerPrefixedLitre`
Super-classes |[om:UnitDivision](http://opendata.caceres.es/def/ontomunicipio#UnitDivision) (c)<br />
Has members |[om:gramPerPetalitre](http://opendata.caceres.es/def/ontomunicipio#gramPerPetalitre)<br />[om:gramPerFemtolitre](http://opendata.caceres.es/def/ontomunicipio#gramPerFemtolitre)<br />[om:gramPerExalitre](http://opendata.caceres.es/def/ontomunicipio#gramPerExalitre)<br />[om:gramPerHectolitre](http://opendata.caceres.es/def/ontomunicipio#gramPerHectolitre)<br />[om:gramPerDecalitre](http://opendata.caceres.es/def/ontomunicipio#gramPerDecalitre)<br />[om:gramPerDecilitre](http://opendata.caceres.es/def/ontomunicipio#gramPerDecilitre)<br />[om:gramPerTeralitre](http://opendata.caceres.es/def/ontomunicipio#gramPerTeralitre)<br />[om:gramPerYottalitre](http://opendata.caceres.es/def/ontomunicipio#gramPerYottalitre)<br />[om:gramPerGigalitre](http://opendata.caceres.es/def/ontomunicipio#gramPerGigalitre)<br />[om:gramPerPicolitre](http://opendata.caceres.es/def/ontomunicipio#gramPerPicolitre)<br />[om:gramPerAttolitre](http://opendata.caceres.es/def/ontomunicipio#gramPerAttolitre)<br />[om:gramPerYoctolitre](http://opendata.caceres.es/def/ontomunicipio#gramPerYoctolitre)<br />[om:gramPerKilolitre](http://opendata.caceres.es/def/ontomunicipio#gramPerKilolitre)<br />[om:gramPerMillilitre](http://opendata.caceres.es/def/ontomunicipio#gramPerMillilitre)<br />[om:gramPerMicrolitre](http://opendata.caceres.es/def/ontomunicipio#gramPerMicrolitre)<br />[om:gramPerMegalitre](http://opendata.caceres.es/def/ontomunicipio#gramPerMegalitre)<br />[om:gramPerCentilitre](http://opendata.caceres.es/def/ontomunicipio#gramPerCentilitre)<br />[om:gramPerZeptolitre](http://opendata.caceres.es/def/ontomunicipio#gramPerZeptolitre)<br />[om:gramPerNanolitre](http://opendata.caceres.es/def/ontomunicipio#gramPerNanolitre)<br />[om:gramPerZettalitre](http://opendata.caceres.es/def/ontomunicipio#gramPerZettalitre)<br />
### Grashof number
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#GrashofNumber`
Description | <p>The Grashof number is a dimensionless number that approximates the ratio of buoyancy to viscous force that acts on a fluid.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### Grashof number for mass transfer
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#GrashofNumberForMassTransfer`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
### Grashof number for mass transfer unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#GrashofNumberForMassTransferUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### Grashof number unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#GrashofNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### gravitational acceleration
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#GravitationalAcceleration`
Super-classes |[om:Acceleration](http://opendata.caceres.es/def/ontomunicipio#Acceleration) (c)<br />
### guar gum mass fraction
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#GuarGumMassFraction`
Description | <p>The fraction of the mass of guar gum in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### half-life
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Half-Life`
Super-classes |[om:Time](http://opendata.caceres.es/def/ontomunicipio#Time) (c)<br />
### Hartmann number
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#HartmannNumber`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
### Hartmann number unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#HartmannNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### heat
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Heat`
Description | <p>Heat is any flow of energy from one body or system to another due to a difference in temperature.</p>
Super-classes |[om:Energy](http://opendata.caceres.es/def/ontomunicipio#Energy) (c)<br />
### heat capacity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#HeatCapacity`
Description | <p>Heat capacity is the heat required to increase the temperature of a system or substance one unit temperature.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:entropyOrHeatCapacity-Dimension](http://opendata.caceres.es/def/ontomunicipio#entropyOrHeatCapacity-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### heat capacity unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#HeatCapacityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### heat flow rate
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#HeatFlowRate`
Super-classes |[om:Power](http://opendata.caceres.es/def/ontomunicipio#Power) (c)<br />
### heat flux density
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#HeatFluxDensity`
Super-classes |[om:PowerDensity](http://opendata.caceres.es/def/ontomunicipio#PowerDensity) (c)<br />
### heat transfer coefficient
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#HeatTransferCoefficient`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:heatTransferCoefficient-Dimension](http://opendata.caceres.es/def/ontomunicipio#heatTransferCoefficient-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### heat transfer coefficient unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#HeatTransferCoefficientUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### height
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Height`
Super-classes |[om:Length](http://opendata.caceres.es/def/ontomunicipio#Length) (c)<br />
### hour angle
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#HourAngle`
Description | <p>The angular distance on the celestial sphere measured westward along the celestial equator from the meridian to the hour circle that passes through the celestial object.</p>
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
### Hubble constant
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#HubbleConstant`
Description | <p>The Hubble constant (NOT a constant over time).</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:HubbleConstantAtPresentEpoch](http://opendata.caceres.es/def/ontomunicipio#HubbleConstantAtPresentEpoch) (c)<br />
### Hubble constant at present epoch
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#HubbleConstantAtPresentEpoch`
Description | <p>The Hubble constant at the present epoch (a constant).</p>
Super-classes |[om:HubbleConstant](http://opendata.caceres.es/def/ontomunicipio#HubbleConstant) (c)<br />
### Hubble constant unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#HubbleConstantUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### hydrophilicity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Hydrophilicity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### hydrophobicity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Hydrophobicity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### I magnitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#IMagnitude`
Description | <p>I magnitude in the Cousins photometric system.</p>
Super-classes |[om:CousinsMagnitude](http://opendata.caceres.es/def/ontomunicipio#CousinsMagnitude) (c)<br />
### illuminance
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Illuminance`
Description | <p>Illuminance is the total luminous flux incident on a surface per unit area.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:illuminance-Dimension](http://opendata.caceres.es/def/ontomunicipio#illuminance-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### illuminance unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#IlluminanceUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### impulse
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Impulse`
Description | <p>Impulse is the integral of a force with respect to time.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### inductance
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Inductance`
Description | <p>Inductance is that property in an electrical circuit where a change in the current flowing through that circuit induces an electromotive force that opposes the change in current.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:inductanceOrPermeance-Electromagnetic-Dimension](http://opendata.caceres.es/def/ontomunicipio#inductanceOrPermeance-Electromagnetic-Dimension) (c)<br />
### inductance unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#InductanceUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### information capacity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#InformationCapacity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Has members |[om:informationCapacityOfOneBinaryDigit](http://opendata.caceres.es/def/ontomunicipio#informationCapacityOfOneBinaryDigit)<br />
### information capacity unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#InformationCapacityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### initial mass function
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#InitialMassFunction`
Description | <p>The number of stars in mass fraction dM around mass M. Used in Salpeter's Initial Mass Function (IMF).</p>
Super-classes |[om:NumberDensity](http://opendata.caceres.es/def/ontomunicipio#NumberDensity) (c)<br />
### integrated magnitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#IntegratedMagnitude`
Description | <p>The apparent magnitude that an extended object, such as a nebula or galaxy, would have if all its light were concentrated at a starlike point.</p>
Super-classes |[om:Magnitude](http://opendata.caceres.es/def/ontomunicipio#Magnitude) (c)<br />
### internal energy
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#InternalEnergy`
Description | <p>The internal energy of a thermodynamic system, or a body with well-defined boundaries is the total of the kinetic energy due to the motion of molecules (translational, rotational, vibrational) and the potential energy associated with the vibrational and electric energy of atoms within molecules or crystals.</p>
Super-classes |[om:Energy](http://opendata.caceres.es/def/ontomunicipio#Energy) (c)<br />
### interval scale
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#IntervalScale`
Super-classes |[om:Scale](http://opendata.caceres.es/def/ontomunicipio#Scale) (c)<br />
Has members |[om:ReaumurScale](http://opendata.caceres.es/def/ontomunicipio#ReaumurScale)<br />[om:FahrenheitScale](http://opendata.caceres.es/def/ontomunicipio#FahrenheitScale)<br />[om:CelsiusScale](http://opendata.caceres.es/def/ontomunicipio#CelsiusScale)<br />
### intrinsic colour index
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#IntrinsicColourIndex`
Description | <p>The colour index a star would have in the absence of interstellar extinction (reddening). It is assumed that all stars of the same spectral type and luminosity class have the same colour index.</p>
Super-classes |[om:ColourIndex](http://opendata.caceres.es/def/ontomunicipio#ColourIndex) (c)<br />
### ionization temperature
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#IonizationTemperature`
Description | <p>The temperature of a gas or plasma derived from the relative numbers of neutral atoms and ions. Specifically, it is the temperature for which the Saha equations would predict these relative numbers, assuming the atoms and ions are in thermodynamic equilibrium.</p>
Super-classes |[om:ThermodynamicTemperature](http://opendata.caceres.es/def/ontomunicipio#ThermodynamicTemperature) (c)<br />
### irradiance
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Irradiance`
Description | <p>Irradiance is the power of electromagnetic radiation at a surface per unit area.</p>
Super-classes |[om:PowerDensity](http://opendata.caceres.es/def/ontomunicipio#PowerDensity) (c)<br />
### Jeans mass
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#JeansMass`
Description | <p>The critical mass of a molecular cloud, above which it will be unstable to collapse.</p>
Super-classes |[om:Mass](http://opendata.caceres.es/def/ontomunicipio#Mass) (c)<br />
### Johnson magnitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#JohnsonMagnitude`
Description | <p>A magnitude measured in one of Johnson's standard passbands (using a standard filter, i.e. U, B, or V).</p>
Super-classes |[om:Magnitude](http://opendata.caceres.es/def/ontomunicipio#Magnitude) (c)<br />
Sub-classes |[om:BMagnitude](http://opendata.caceres.es/def/ontomunicipio#BMagnitude) (c)<br />[om:VMagnitude](http://opendata.caceres.es/def/ontomunicipio#VMagnitude) (c)<br />[om:UMagnitude](http://opendata.caceres.es/def/ontomunicipio#UMagnitude) (c)<br />
### kerma
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Kerma`
Super-classes |[om:AbsorbedDose](http://opendata.caceres.es/def/ontomunicipio#AbsorbedDose) (c)<br />
### kinematic viscosity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#KinematicViscosity`
Description | <p>Kinematic viscosity is the ratio of viscosity to density.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:kinematicViscosityOrThermalDiffusivity-Dimension](http://opendata.caceres.es/def/ontomunicipio#kinematicViscosityOrThermalDiffusivity-Dimension) (c)<br />
### kinematic viscosity unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#KinematicViscosityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### kinetic energy
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#KineticEnergy`
Description | <p>Kinetic energy is energy due to motion.</p>
Super-classes |[om:Energy](http://opendata.caceres.es/def/ontomunicipio#Energy) (c)<br />
### Knudsen number
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#KnudsenNumber`
Description | <p>The Knudsen number is a dimensionless number defined as the ratio of the molecular mean free path length to a representative physical length scale.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### Knudsen number unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#KnudsenNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### label mass
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#LabelMass`
Super-classes |[om:Mass](http://opendata.caceres.es/def/ontomunicipio#Mass) (c)<br />
Sub-classes |[om:BodyLabelMass](http://opendata.caceres.es/def/ontomunicipio#BodyLabelMass) (c)<br />
### lactose mass fraction
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#LactoseMassFraction`
Description | <p>The fraction of the mass of lactose in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### length
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Length`
Description | <p>Length is the amount of space between two geographical points along a curve. It is a base quantity in the International System of Units and other systems of units. Length is speed times time. The metre, a base unit of length in the International System of Units, is defined in terms of speed of light during a certain time interval.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:length-Dimension](http://opendata.caceres.es/def/ontomunicipio#length-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:zRange](http://opendata.caceres.es/def/ontomunicipio#zRange) (c)<br />[om:xRange](http://opendata.caceres.es/def/ontomunicipio#xRange) (c)<br />[om:yRange](http://opendata.caceres.es/def/ontomunicipio#yRange) (c)<br />[om:Displacement](http://opendata.caceres.es/def/ontomunicipio#Displacement) (c)<br />[om:ScaleLength](http://opendata.caceres.es/def/ontomunicipio#ScaleLength) (c)<br />[om:Height](http://opendata.caceres.es/def/ontomunicipio#Height) (c)<br />[om:Distance](http://opendata.caceres.es/def/ontomunicipio#Distance) (c)<br />[om:Diameter](http://opendata.caceres.es/def/ontomunicipio#Diameter) (c)<br />[om:FontSize](http://opendata.caceres.es/def/ontomunicipio#FontSize) (c)<br />[om:Width](http://opendata.caceres.es/def/ontomunicipio#Width) (c)<br />[om:Radius](http://opendata.caceres.es/def/ontomunicipio#Radius) (c)<br />[om:Wavelength](http://opendata.caceres.es/def/ontomunicipio#Wavelength) (c)<br />[om:Depth](http://opendata.caceres.es/def/ontomunicipio#Depth) (c)<br />[om:ScaleHeight](http://opendata.caceres.es/def/ontomunicipio#ScaleHeight) (c)<br />[om:Circumference](http://opendata.caceres.es/def/ontomunicipio#Circumference) (c)<br />[om:Breadth](http://opendata.caceres.es/def/ontomunicipio#Breadth) (c)<br />[om:Thickness](http://opendata.caceres.es/def/ontomunicipio#Thickness) (c)<br />
Has members |[om:lengthOfThePathTravelledByLightInVacuumDuringATimeIntervalOf1299792458OfASecond](http://opendata.caceres.es/def/ontomunicipio#lengthOfThePathTravelledByLightInVacuumDuringATimeIntervalOf1299792458OfASecond)<br />
### length unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#LengthUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
Sub-classes |[om:FontSizeUnit](http://opendata.caceres.es/def/ontomunicipio#FontSizeUnit) (c)<br />
### Lewis number
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#LewisNumber`
Description | <p>The Lewis number is a dimensionless number defined as the ratio of thermal diffusivity to mass diffusivity.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
### Lewis number unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#LewisNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### light time
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#LightTime`
Description | <p>The time electromagnetic radiation takes to reach Earth from a distant source. Often the correction in light time is needed to accurately calculate the apparent position of solar system objects or to calculate the period of variable stars (different times are observed when the Earth is at a different position in its orbit).</p>
Super-classes |[om:Time](http://opendata.caceres.es/def/ontomunicipio#Time) (c)<br />
### limiting magnitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#LimitingMagnitude`
Description | <p>The magnitude of the faintest object (star) that can be detected by a telescope or other instrument. Depends not only on the telescope but also on the detector and on the observing method.</p>
Super-classes |[om:Magnitude](http://opendata.caceres.es/def/ontomunicipio#Magnitude) (c)<br />
### linear strain
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#LinearStrain`
Super-classes |[om:Strain](http://opendata.caceres.es/def/ontomunicipio#Strain) (c)<br />
### lipophilicity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Lipophilicity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### locust bean gum mass fraction
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#LocustBeanGumMassFraction`
Description | <p>The fraction of the mass of locust bean gum in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### loss modulus
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#LossModulus`
Super-classes |[om:DynamicModulus](http://opendata.caceres.es/def/ontomunicipio#DynamicModulus) (c)<br />
### luminance
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Luminance`
Description | <p>Luminous flux is the total visible energy emitted by a source per unit time.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:luminance-Dimension](http://opendata.caceres.es/def/ontomunicipio#luminance-Dimension) (c)<br />
### luminance unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#LuminanceUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### luminosity function
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#LuminosityFunction`
Description | <p>The number of stars of absolute magnitudes between Mv and Mv+ΔMv per cubic parsec.</p>
Super-classes |[om:NumberDensity](http://opendata.caceres.es/def/ontomunicipio#NumberDensity) (c)<br />
### luminous efficacy
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#LuminousEfficacy`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:luminousEfficacy-Dimension](http://opendata.caceres.es/def/ontomunicipio#luminousEfficacy-Dimension) (c)<br />
### luminous efficacy unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#LuminousEfficacyUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### luminous energy
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#LuminousEnergy`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:luminousEnergy-Dimension](http://opendata.caceres.es/def/ontomunicipio#luminousEnergy-Dimension) (c)<br />
### luminous energy unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#LuminousEnergyUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### luminous flux
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#LuminousFlux`
Description | <p>Luminous flux is the total visible energy emitted by a source per unit time.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:luminousFlux-Dimension](http://opendata.caceres.es/def/ontomunicipio#luminousFlux-Dimension) (c)<br />
### luminous flux unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#LuminousFluxUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### luminous intensity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#LuminousIntensity`
Description | <p>Luminous intensity is the wavelength-weighted power emitted by a light source in a particular direction per unit solid angle. It is a base quantity in the International System of Units. Luminous intensity is luminous flux divided by solid angle.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:luminousIntensity-Dimension](http://opendata.caceres.es/def/ontomunicipio#luminousIntensity-Dimension) (c)<br />
Has members |[om:luminousIntensityInAGivenDirectionOfASourceThatEmitsMonochromaticRadiationOfFrequency540e12HertzAndThatHasARadiantIntensityInThatDirectionOf1683WattPerSteradian](http://opendata.caceres.es/def/ontomunicipio#luminousIntensityInAGivenDirectionOfASourceThatEmitsMonochromaticRadiationOfFrequency540e12HertzAndThatHasARadiantIntensityInThatDirectionOf1683WattPerSteradian)<br />
### luminous intensity unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#LuminousIntensityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### Mach number
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MachNumber`
Description | <p>The Mach number is the speed of an object that moves through air, or any fluid substance, divided by the speed of sound as it is in that substance.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### Mach number unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MachNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### magnetic field
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MagneticField`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:MagneticField-Dimension](http://opendata.caceres.es/def/ontomunicipio#MagneticField-Dimension) (c)<br />
### magnetic field unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MagneticFieldUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### magnetic flux
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MagneticFlux`
Description | <p>Magnetic flux through any area perpendicular to a magnetic field is the product of the area by the field strength.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:magneticFlux-Dimension](http://opendata.caceres.es/def/ontomunicipio#magneticFlux-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### magnetic flux density
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MagneticFluxDensity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:magneticFluxDensity-Dimension](http://opendata.caceres.es/def/ontomunicipio#magneticFluxDensity-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### magnetic flux density unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MagneticFluxDensityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### magnetic flux unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MagneticFluxUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### magnetic Reynolds number
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MagneticReynoldsNumber`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### magnetic Reynolds number unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MagneticReynoldsNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### magnetomotive force
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MagnetomotiveForce`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:electricCurrent-Dimension](http://opendata.caceres.es/def/ontomunicipio#electricCurrent-Dimension) (c)<br />
### magnetomotive force unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MagnetomotiveForceUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### magnitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Magnitude`
Description | <p>Reverse logarithmic measure of the brightness of an object.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
Sub-classes |[om:LimitingMagnitude](http://opendata.caceres.es/def/ontomunicipio#LimitingMagnitude) (c)<br />[om:AbsoluteMagnitude](http://opendata.caceres.es/def/ontomunicipio#AbsoluteMagnitude) (c)<br />[om:MagnitudeAtMaximumBrightness](http://opendata.caceres.es/def/ontomunicipio#MagnitudeAtMaximumBrightness) (c)<br />[om:MagnitudeAtMinimumBrightness](http://opendata.caceres.es/def/ontomunicipio#MagnitudeAtMinimumBrightness) (c)<br />[om:BolometricMagnitude](http://opendata.caceres.es/def/ontomunicipio#BolometricMagnitude) (c)<br />[om:JohnsonMagnitude](http://opendata.caceres.es/def/ontomunicipio#JohnsonMagnitude) (c)<br />[om:PhotographicMagnitude](http://opendata.caceres.es/def/ontomunicipio#PhotographicMagnitude) (c)<br />[om:TychoBroadbandMagnitude](http://opendata.caceres.es/def/ontomunicipio#TychoBroadbandMagnitude) (c)<br />[om:ThuanAndGunnMagnitude](http://opendata.caceres.es/def/ontomunicipio#ThuanAndGunnMagnitude) (c)<br />[om:IntegratedMagnitude](http://opendata.caceres.es/def/ontomunicipio#IntegratedMagnitude) (c)<br />[om:RedMagnitude](http://opendata.caceres.es/def/ontomunicipio#RedMagnitude) (c)<br />[om:_1040NanometreLockwoodMagnitude](http://opendata.caceres.es/def/ontomunicipio#_1040NanometreLockwoodMagnitude) (c)<br />[om:CousinsMagnitude](http://opendata.caceres.es/def/ontomunicipio#CousinsMagnitude) (c)<br />[om:ApparentMagnitude](http://opendata.caceres.es/def/ontomunicipio#ApparentMagnitude) (c)<br />[om:StroemgrenMagnitude](http://opendata.caceres.es/def/ontomunicipio#StroemgrenMagnitude) (c)<br />[om:WhiteLightMagnitude](http://opendata.caceres.es/def/ontomunicipio#WhiteLightMagnitude) (c)<br />
### magnitude at maximum brightness
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MagnitudeAtMaximumBrightness`
Description | <p>The magnitude at maximum brightness of a variable star.</p>
Super-classes |[om:Magnitude](http://opendata.caceres.es/def/ontomunicipio#Magnitude) (c)<br />
Sub-classes |[om:VMagnitudeAtMaximumBrightness](http://opendata.caceres.es/def/ontomunicipio#VMagnitudeAtMaximumBrightness) (c)<br />[om:BMagnitudeAtMaximumBrightness](http://opendata.caceres.es/def/ontomunicipio#BMagnitudeAtMaximumBrightness) (c)<br />[om:WhiteLightMagnitudeAtMaximumBrightness](http://opendata.caceres.es/def/ontomunicipio#WhiteLightMagnitudeAtMaximumBrightness) (c)<br />[om:PhotographicMagnitudeAtMaximumBrightness](http://opendata.caceres.es/def/ontomunicipio#PhotographicMagnitudeAtMaximumBrightness) (c)<br />
### magnitude at minimum brightness
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MagnitudeAtMinimumBrightness`
Description | <p>The magnitude at minimum brightness of a variable star.</p>
Super-classes |[om:Magnitude](http://opendata.caceres.es/def/ontomunicipio#Magnitude) (c)<br />
Sub-classes |[om:VMagnitudeAtMinimumBrightness](http://opendata.caceres.es/def/ontomunicipio#VMagnitudeAtMinimumBrightness) (c)<br />[om:WhiteLightMagnitudeAtMinimumBrightness](http://opendata.caceres.es/def/ontomunicipio#WhiteLightMagnitudeAtMinimumBrightness) (c)<br />[om:PhotographicMagnitudeAtMinimumBrightness](http://opendata.caceres.es/def/ontomunicipio#PhotographicMagnitudeAtMinimumBrightness) (c)<br />[om:BMagnitudeAtMinimumBrightness](http://opendata.caceres.es/def/ontomunicipio#BMagnitudeAtMinimumBrightness) (c)<br />
### magnitude unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MagnitudeUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### manual firmness
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ManualFirmness`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### mass
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Mass`
Description | <p>Mass is the amount of matter of a phenomenon. It is a base quantity in the International System of Units. Mass is force divided by acceleration.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:mass-Dimension](http://opendata.caceres.es/def/ontomunicipio#mass-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:FlowpackMass](http://opendata.caceres.es/def/ontomunicipio#FlowpackMass) (c)<br />[om:CapMass](http://opendata.caceres.es/def/ontomunicipio#CapMass) (c)<br />[om:JeansMass](http://opendata.caceres.es/def/ontomunicipio#JeansMass) (c)<br />[om:VasePlusWaterPlusFlowerMass](http://opendata.caceres.es/def/ontomunicipio#VasePlusWaterPlusFlowerMass) (c)<br />[om:AtomicMass](http://opendata.caceres.es/def/ontomunicipio#AtomicMass) (c)<br />[om:TopMass](http://opendata.caceres.es/def/ontomunicipio#TopMass) (c)<br />[om:BodyMass](http://opendata.caceres.es/def/ontomunicipio#BodyMass) (c)<br />[om:CartonMass](http://opendata.caceres.es/def/ontomunicipio#CartonMass) (c)<br />[om:DryMass](http://opendata.caceres.es/def/ontomunicipio#DryMass) (c)<br />[om:LabelMass](http://opendata.caceres.es/def/ontomunicipio#LabelMass) (c)<br />[om:VasePlusWaterMass](http://opendata.caceres.es/def/ontomunicipio#VasePlusWaterMass) (c)<br />[om:NeckRingMass](http://opendata.caceres.es/def/ontomunicipio#NeckRingMass) (c)<br />[om:StrawMass](http://opendata.caceres.es/def/ontomunicipio#StrawMass) (c)<br />
Has members |[om:massOfTheInternationalPrototypeOfTheKilogram](http://opendata.caceres.es/def/ontomunicipio#massOfTheInternationalPrototypeOfTheKilogram)<br />
### mass flow
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MassFlow`
Description | <p>Mass flow is the movement of substances at equal rates or as a single body.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:massFlow-Dimension](http://opendata.caceres.es/def/ontomunicipio#massFlow-Dimension) (c)<br />
### mass flow unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MassFlowUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### mass fraction
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MassFraction`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:PotassiumSorbateMassFraction](http://opendata.caceres.es/def/ontomunicipio#PotassiumSorbateMassFraction) (c)<br />[om:SoyBeanMassFraction](http://opendata.caceres.es/def/ontomunicipio#SoyBeanMassFraction) (c)<br />[om:FatMassFraction](http://opendata.caceres.es/def/ontomunicipio#FatMassFraction) (c)<br />[om:StarchVA40MassFraction](http://opendata.caceres.es/def/ontomunicipio#StarchVA40MassFraction) (c)<br />[om:TweenMassFraction](http://opendata.caceres.es/def/ontomunicipio#TweenMassFraction) (c)<br />[om:WaterMassFraction](http://opendata.caceres.es/def/ontomunicipio#WaterMassFraction) (c)<br />[om:LocustBeanGumMassFraction](http://opendata.caceres.es/def/ontomunicipio#LocustBeanGumMassFraction) (c)<br />[om:DisodiumEthyleneDiamineTetreAcetateMassFraction](http://opendata.caceres.es/def/ontomunicipio#DisodiumEthyleneDiamineTetreAcetateMassFraction) (c)<br />[om:WheyProteinAggregateMassFraction](http://opendata.caceres.es/def/ontomunicipio#WheyProteinAggregateMassFraction) (c)<br />[om:LactoseMassFraction](http://opendata.caceres.es/def/ontomunicipio#LactoseMassFraction) (c)<br />[om:ColdGasMassFraction](http://opendata.caceres.es/def/ontomunicipio#ColdGasMassFraction) (c)<br />[om:AceticAcidMassFraction](http://opendata.caceres.es/def/ontomunicipio#AceticAcidMassFraction) (c)<br />[om:SaltMassFraction](http://opendata.caceres.es/def/ontomunicipio#SaltMassFraction) (c)<br />[om:SugarMassFraction](http://opendata.caceres.es/def/ontomunicipio#SugarMassFraction) (c)<br />[om:StarchMassFraction](http://opendata.caceres.es/def/ontomunicipio#StarchMassFraction) (c)<br />[om:MustardPowderMassFraction](http://opendata.caceres.es/def/ontomunicipio#MustardPowderMassFraction) (c)<br />[om:DryMatterMassFraction](http://opendata.caceres.es/def/ontomunicipio#DryMatterMassFraction) (c)<br />[om:GelatinMassFraction](http://opendata.caceres.es/def/ontomunicipio#GelatinMassFraction) (c)<br />[om:ModeratedStarchMassFraction](http://opendata.caceres.es/def/ontomunicipio#ModeratedStarchMassFraction) (c)<br />[om:StarchVA85MassFraction](http://opendata.caceres.es/def/ontomunicipio#StarchVA85MassFraction) (c)<br />[om:WheyProteinBeadsMassFraction](http://opendata.caceres.es/def/ontomunicipio#WheyProteinBeadsMassFraction) (c)<br />[om:GuarGumMassFraction](http://opendata.caceres.es/def/ontomunicipio#GuarGumMassFraction) (c)<br />[om:EggMassFraction](http://opendata.caceres.es/def/ontomunicipio#EggMassFraction) (c)<br />[om:XanthanMassFraction](http://opendata.caceres.es/def/ontomunicipio#XanthanMassFraction) (c)<br />[om:WheyProteinMassFraction](http://opendata.caceres.es/def/ontomunicipio#WheyProteinMassFraction) (c)<br />[om:ProteinMassFraction](http://opendata.caceres.es/def/ontomunicipio#ProteinMassFraction) (c)<br />
### mass fraction unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MassFractionUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### mass unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MassUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### measure
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Measure`
Description | <p>A measure combines a number to a unit of measure. For example, "3 m" is a measure.</p>
### metallicity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Metallicity`
Description | <p>The log of the ratio between the ratios of the observed Fe and H quantities in a star and the same ratio in the Sun. This is a very important quantity that is often used in astronomy as an indicator of the age of a star.</p>
Super-classes |[om:QuantityOfDimensionOne](http://opendata.caceres.es/def/ontomunicipio#QuantityOfDimensionOne) (c)<br />
### metre per prefixed second (time)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MetrePerPrefixedSecond-Time`
Super-classes |[om:UnitDivision](http://opendata.caceres.es/def/ontomunicipio#UnitDivision) (c)<br />
Has members |[om:metrePerCentisecond-Time](http://opendata.caceres.es/def/ontomunicipio#metrePerCentisecond-Time)<br />[om:metrePerExasecond-Time](http://opendata.caceres.es/def/ontomunicipio#metrePerExasecond-Time)<br />[om:metrePerYottasecond-Time](http://opendata.caceres.es/def/ontomunicipio#metrePerYottasecond-Time)<br />[om:metrePerAttosecond-Time](http://opendata.caceres.es/def/ontomunicipio#metrePerAttosecond-Time)<br />[om:metrePerZeptosecond-Time](http://opendata.caceres.es/def/ontomunicipio#metrePerZeptosecond-Time)<br />[om:metrePerFemtosecond-Time](http://opendata.caceres.es/def/ontomunicipio#metrePerFemtosecond-Time)<br />[om:metrePerGigasecond-Time](http://opendata.caceres.es/def/ontomunicipio#metrePerGigasecond-Time)<br />[om:metrePerMegasecond-Time](http://opendata.caceres.es/def/ontomunicipio#metrePerMegasecond-Time)<br />[om:metrePerKilosecond-Time](http://opendata.caceres.es/def/ontomunicipio#metrePerKilosecond-Time)<br />[om:metrePerHectosecond-Time](http://opendata.caceres.es/def/ontomunicipio#metrePerHectosecond-Time)<br />[om:metrePerPicosecond-Time](http://opendata.caceres.es/def/ontomunicipio#metrePerPicosecond-Time)<br />[om:metrePerTerasecond-Time](http://opendata.caceres.es/def/ontomunicipio#metrePerTerasecond-Time)<br />[om:metrePerMicrosecond-Time](http://opendata.caceres.es/def/ontomunicipio#metrePerMicrosecond-Time)<br />[om:metrePerDecisecond-Time](http://opendata.caceres.es/def/ontomunicipio#metrePerDecisecond-Time)<br />[om:metrePerZettasecond-Time](http://opendata.caceres.es/def/ontomunicipio#metrePerZettasecond-Time)<br />[om:metrePerMillisecond-Time](http://opendata.caceres.es/def/ontomunicipio#metrePerMillisecond-Time)<br />[om:metrePerYoctosecond-Time](http://opendata.caceres.es/def/ontomunicipio#metrePerYoctosecond-Time)<br />[om:metrePerDecasecond-Time](http://opendata.caceres.es/def/ontomunicipio#metrePerDecasecond-Time)<br />[om:metrePerPetasecond-Time](http://opendata.caceres.es/def/ontomunicipio#metrePerPetasecond-Time)<br />[om:metrePerNanosecond-Time](http://opendata.caceres.es/def/ontomunicipio#metrePerNanosecond-Time)<br />
### metre per prefixed second (time) squared
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MetrePerPrefixedSecond-TimeSquared`
Super-classes |[om:UnitDivision](http://opendata.caceres.es/def/ontomunicipio#UnitDivision) (c)<br />
Has members |[om:metrePerGigasecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#metrePerGigasecond-TimeSquared)<br />[om:metrePerKilosecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#metrePerKilosecond-TimeSquared)<br />[om:metrePerHectosecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#metrePerHectosecond-TimeSquared)<br />[om:metrePerZeptosecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#metrePerZeptosecond-TimeSquared)<br />[om:metrePerYoctosecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#metrePerYoctosecond-TimeSquared)<br />[om:metrePerExasecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#metrePerExasecond-TimeSquared)<br />[om:metrePerDecasecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#metrePerDecasecond-TimeSquared)<br />[om:metrePerTerasecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#metrePerTerasecond-TimeSquared)<br />[om:metrePerDecisecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#metrePerDecisecond-TimeSquared)<br />[om:metrePerAttosecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#metrePerAttosecond-TimeSquared)<br />[om:metrePerPicosecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#metrePerPicosecond-TimeSquared)<br />[om:metrePerMillisecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#metrePerMillisecond-TimeSquared)<br />[om:metrePerPetasecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#metrePerPetasecond-TimeSquared)<br />[om:metrePerZettasecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#metrePerZettasecond-TimeSquared)<br />[om:metrePerCentisecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#metrePerCentisecond-TimeSquared)<br />[om:metrePerNanosecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#metrePerNanosecond-TimeSquared)<br />[om:metrePerFemtosecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#metrePerFemtosecond-TimeSquared)<br />[om:metrePerMicrosecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#metrePerMicrosecond-TimeSquared)<br />[om:metrePerMegasecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#metrePerMegasecond-TimeSquared)<br />[om:metrePerYottasecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#metrePerYottasecond-TimeSquared)<br />
### moderated starch mass fraction
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ModeratedStarchMassFraction`
Description | <p>The fraction of the mass of moderated starch in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### modulus of elasticity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ModulusOfElasticity`
Super-classes |[om:DynamicModulus](http://opendata.caceres.es/def/ontomunicipio#DynamicModulus) (c)<br />
### molality
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Molality`
Description | <p>Molality is the number of moles of solute per kilogram of solvent.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### molality unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MolalityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### molar energy
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MolarEnergy`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:molarEnergy-Dimension](http://opendata.caceres.es/def/ontomunicipio#molarEnergy-Dimension) (c)<br />
Sub-classes |[om:ResonanceEnergy](http://opendata.caceres.es/def/ontomunicipio#ResonanceEnergy) (c)<br />
### molar energy unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MolarEnergyUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### molar entropy
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MolarEntropy`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:molarEntropyOrMolarHeatCapacityOrGasConstant-Dimension](http://opendata.caceres.es/def/ontomunicipio#molarEntropyOrMolarHeatCapacityOrGasConstant-Dimension) (c)<br />
### molar entropy unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MolarEntropyUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### molar heat capacity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MolarHeatCapacity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:molarEntropyOrMolarHeatCapacityOrGasConstant-Dimension](http://opendata.caceres.es/def/ontomunicipio#molarEntropyOrMolarHeatCapacityOrGasConstant-Dimension) (c)<br />
### molar heat capacity unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MolarHeatCapacityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### molar mass
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MolarMass`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### molar mass unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MolarMassUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### molar volume
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MolarVolume`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### molar volume unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MolarVolumeUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### mole per prefixed litre
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MolePerPrefixedLitre`
Super-classes |[om:UnitDivision](http://opendata.caceres.es/def/ontomunicipio#UnitDivision) (c)<br />
Has members |[om:molePerDecilitre](http://opendata.caceres.es/def/ontomunicipio#molePerDecilitre)<br />[om:molePerMegalitre](http://opendata.caceres.es/def/ontomunicipio#molePerMegalitre)<br />[om:molePerAttolitre](http://opendata.caceres.es/def/ontomunicipio#molePerAttolitre)<br />[om:molePerZeptolitre](http://opendata.caceres.es/def/ontomunicipio#molePerZeptolitre)<br />[om:molePerNanolitre](http://opendata.caceres.es/def/ontomunicipio#molePerNanolitre)<br />[om:molePerYottalitre](http://opendata.caceres.es/def/ontomunicipio#molePerYottalitre)<br />[om:molePerPetalitre](http://opendata.caceres.es/def/ontomunicipio#molePerPetalitre)<br />[om:molePerZettalitre](http://opendata.caceres.es/def/ontomunicipio#molePerZettalitre)<br />[om:molePerGigalitre](http://opendata.caceres.es/def/ontomunicipio#molePerGigalitre)<br />[om:molePerYoctolitre](http://opendata.caceres.es/def/ontomunicipio#molePerYoctolitre)<br />[om:molePerKilolitre](http://opendata.caceres.es/def/ontomunicipio#molePerKilolitre)<br />[om:molePerFemtolitre](http://opendata.caceres.es/def/ontomunicipio#molePerFemtolitre)<br />[om:molePerPicolitre](http://opendata.caceres.es/def/ontomunicipio#molePerPicolitre)<br />[om:molePerMicrolitre](http://opendata.caceres.es/def/ontomunicipio#molePerMicrolitre)<br />[om:molePerDecalitre](http://opendata.caceres.es/def/ontomunicipio#molePerDecalitre)<br />[om:molePerTeralitre](http://opendata.caceres.es/def/ontomunicipio#molePerTeralitre)<br />[om:molePerMillilitre](http://opendata.caceres.es/def/ontomunicipio#molePerMillilitre)<br />[om:molePerCentilitre](http://opendata.caceres.es/def/ontomunicipio#molePerCentilitre)<br />[om:molePerExalitre](http://opendata.caceres.es/def/ontomunicipio#molePerExalitre)<br />[om:molePerHectolitre](http://opendata.caceres.es/def/ontomunicipio#molePerHectolitre)<br />
### mole per prefixed metre
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MolePerPrefixedMetre`
Super-classes |[om:UnitDivision](http://opendata.caceres.es/def/ontomunicipio#UnitDivision) (c)<br />
Has members |[om:molePerDecametre](http://opendata.caceres.es/def/ontomunicipio#molePerDecametre)<br />[om:molePerPetametre](http://opendata.caceres.es/def/ontomunicipio#molePerPetametre)<br />[om:molePerGigametre](http://opendata.caceres.es/def/ontomunicipio#molePerGigametre)<br />[om:molePerHectometre](http://opendata.caceres.es/def/ontomunicipio#molePerHectometre)<br />[om:molePermegametre](http://opendata.caceres.es/def/ontomunicipio#molePermegametre)<br />[om:molePerFemtometre](http://opendata.caceres.es/def/ontomunicipio#molePerFemtometre)<br />[om:molePerMicrometre](http://opendata.caceres.es/def/ontomunicipio#molePerMicrometre)<br />[om:molePerCentimetre](http://opendata.caceres.es/def/ontomunicipio#molePerCentimetre)<br />[om:molePerZeptometre](http://opendata.caceres.es/def/ontomunicipio#molePerZeptometre)<br />[om:molePerZettametre](http://opendata.caceres.es/def/ontomunicipio#molePerZettametre)<br />[om:molePerDecimetre](http://opendata.caceres.es/def/ontomunicipio#molePerDecimetre)<br />[om:molePerYoctometre](http://opendata.caceres.es/def/ontomunicipio#molePerYoctometre)<br />[om:molePerAttometre](http://opendata.caceres.es/def/ontomunicipio#molePerAttometre)<br />[om:molePerPicometre](http://opendata.caceres.es/def/ontomunicipio#molePerPicometre)<br />[om:molePerKilometre](http://opendata.caceres.es/def/ontomunicipio#molePerKilometre)<br />[om:molePerYottametre](http://opendata.caceres.es/def/ontomunicipio#molePerYottametre)<br />[om:molePerExametre](http://opendata.caceres.es/def/ontomunicipio#molePerExametre)<br />[om:molePerNanometre](http://opendata.caceres.es/def/ontomunicipio#molePerNanometre)<br />[om:molePerMillimetre](http://opendata.caceres.es/def/ontomunicipio#molePerMillimetre)<br />[om:molePerTerametre](http://opendata.caceres.es/def/ontomunicipio#molePerTerametre)<br />
### moment of force
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MomentOfForce`
Description | <p>Moment of force is the effectiveness of a force to produce rotation about an axis measured by the product of the force and the perpendicular distance from the line of action of the force to the axis.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:energy-Dimension](http://opendata.caceres.es/def/ontomunicipio#energy-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### moment of force unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MomentOfForceUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### moment of inertia
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MomentOfInertia`
Description | <p>Moment of inertia is a measure of the effectiveness of mass in rotation.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### moment of inertia unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MomentOfInertiaUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### momentum
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Momentum`
Description | <p>Momentum is the product of mass and velocity of an object.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### momentum unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MomentumUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### mustard powder mass fraction
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#MustardPowderMassFraction`
Description | <p>The fraction of the mass of mustard powder in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### neck ring mass
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NeckRingMass`
Super-classes |[om:Mass](http://opendata.caceres.es/def/ontomunicipio#Mass) (c)<br />
### noise equivalent power
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NoiseEquivalentPower`
Description | <p>Radiative flux on a detector needed for a signal/noise ratio of 1 (Kitchin, Astrophysical Techniques, IoP, Table 1.1.2).</p>
Super-classes |[om:Power](http://opendata.caceres.es/def/ontomunicipio#Power) (c)<br />
### normal albedo
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NormalAlbedo`
Description | <p>Ratio between radiation falling vertically onto an object and the radiation radiated back vertically.</p>
Super-classes |[om:Albedo](http://opendata.caceres.es/def/ontomunicipio#Albedo) (c)<br />
### normal strain
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NormalStrain`
Super-classes |[om:Strain](http://opendata.caceres.es/def/ontomunicipio#Strain) (c)<br />
### normal stress
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NormalStress`
Super-classes |[om:Stress](http://opendata.caceres.es/def/ontomunicipio#Stress) (c)<br />
### normalised detectivity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NormalisedDetectivity`
Description | <p>The detectivity normalised by multiplying by the square root of the detector area, and by the electrical bandwidth. The units cm Hz(1/2)/W are commonly used and it then represents the signal-to-noise ratio when 1 W of radiation is incident on a detector with an area of 1 cm2, and the electrical bandwidth is 1 Hz.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### number
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Number`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
Sub-classes |[om:NumberPulpBrowning](http://opendata.caceres.es/def/ontomunicipio#NumberPulpBrowning) (c)<br />[om:NumberExternalBrowning](http://opendata.caceres.es/def/ontomunicipio#NumberExternalBrowning) (c)<br />[om:NumberManualFirmness](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness) (c)<br />[om:NumberBotrytis](http://opendata.caceres.es/def/ontomunicipio#NumberBotrytis) (c)<br />[om:NumberVascularBrowning](http://opendata.caceres.es/def/ontomunicipio#NumberVascularBrowning) (c)<br />[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />[om:NumberLeaves](http://opendata.caceres.es/def/ontomunicipio#NumberLeaves) (c)<br />[om:NumberBuds](http://opendata.caceres.es/def/ontomunicipio#NumberBuds) (c)<br />[om:NumberFlowers](http://opendata.caceres.es/def/ontomunicipio#NumberFlowers) (c)<br />[om:NumberBudStadium](http://opendata.caceres.es/def/ontomunicipio#NumberBudStadium) (c)<br />
### number abscised buds
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberAbscisedBuds`
Super-classes |[om:NumberBuds](http://opendata.caceres.es/def/ontomunicipio#NumberBuds) (c)<br />
### number abscised flowers
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberAbscisedFlowers`
Super-classes |[om:NumberFlowers](http://opendata.caceres.es/def/ontomunicipio#NumberFlowers) (c)<br />
### number abscised leaves
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberAbscisedLeaves`
Super-classes |[om:NumberLeaves](http://opendata.caceres.es/def/ontomunicipio#NumberLeaves) (c)<br />
### number blue-discolored flowers
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberBlue-DiscoloredFlowers`
Super-classes |[om:NumberFlowers](http://opendata.caceres.es/def/ontomunicipio#NumberFlowers) (c)<br />
### number Botrytis
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberBotrytis`
Super-classes |[om:Number](http://opendata.caceres.es/def/ontomunicipio#Number) (c)<br />
Sub-classes |[om:NumberBotrytis4](http://opendata.caceres.es/def/ontomunicipio#NumberBotrytis4) (c)<br />[om:NumberBotrytis1](http://opendata.caceres.es/def/ontomunicipio#NumberBotrytis1) (c)<br />[om:NumberBotrytis0](http://opendata.caceres.es/def/ontomunicipio#NumberBotrytis0) (c)<br />[om:NumberBotrytis2](http://opendata.caceres.es/def/ontomunicipio#NumberBotrytis2) (c)<br />[om:NumberBotrytis3](http://opendata.caceres.es/def/ontomunicipio#NumberBotrytis3) (c)<br />
### number Botrytis 0
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberBotrytis0`
Super-classes |[om:NumberBotrytis](http://opendata.caceres.es/def/ontomunicipio#NumberBotrytis) (c)<br />
### number Botrytis 1
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberBotrytis1`
Super-classes |[om:NumberBotrytis](http://opendata.caceres.es/def/ontomunicipio#NumberBotrytis) (c)<br />
### number Botrytis 2
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberBotrytis2`
Super-classes |[om:NumberBotrytis](http://opendata.caceres.es/def/ontomunicipio#NumberBotrytis) (c)<br />
### number Botrytis 3
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberBotrytis3`
Super-classes |[om:NumberBotrytis](http://opendata.caceres.es/def/ontomunicipio#NumberBotrytis) (c)<br />
### number Botrytis 4
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberBotrytis4`
Super-classes |[om:NumberBotrytis](http://opendata.caceres.es/def/ontomunicipio#NumberBotrytis) (c)<br />
### number bud stadium
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberBudStadium`
Super-classes |[om:Number](http://opendata.caceres.es/def/ontomunicipio#Number) (c)<br />
Sub-classes |[om:NumberBudStadium4](http://opendata.caceres.es/def/ontomunicipio#NumberBudStadium4) (c)<br />[om:NumberBudStadium5](http://opendata.caceres.es/def/ontomunicipio#NumberBudStadium5) (c)<br />[om:NumberBudStadium3](http://opendata.caceres.es/def/ontomunicipio#NumberBudStadium3) (c)<br />[om:NumberBudStadium1](http://opendata.caceres.es/def/ontomunicipio#NumberBudStadium1) (c)<br />[om:NumberBudStadium2](http://opendata.caceres.es/def/ontomunicipio#NumberBudStadium2) (c)<br />
### number bud stadium 1
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberBudStadium1`
Super-classes |[om:NumberBudStadium](http://opendata.caceres.es/def/ontomunicipio#NumberBudStadium) (c)<br />
### number bud stadium 2
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberBudStadium2`
Super-classes |[om:NumberBudStadium](http://opendata.caceres.es/def/ontomunicipio#NumberBudStadium) (c)<br />
### number bud stadium 3
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberBudStadium3`
Super-classes |[om:NumberBudStadium](http://opendata.caceres.es/def/ontomunicipio#NumberBudStadium) (c)<br />
### number bud stadium 4
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberBudStadium4`
Super-classes |[om:NumberBudStadium](http://opendata.caceres.es/def/ontomunicipio#NumberBudStadium) (c)<br />
### number bud stadium 5
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberBudStadium5`
Super-classes |[om:NumberBudStadium](http://opendata.caceres.es/def/ontomunicipio#NumberBudStadium) (c)<br />
### number buds
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberBuds`
Super-classes |[om:Number](http://opendata.caceres.es/def/ontomunicipio#Number) (c)<br />
Sub-classes |[om:NumberAbscisedBuds](http://opendata.caceres.es/def/ontomunicipio#NumberAbscisedBuds) (c)<br />[om:NumberMalformedBuds](http://opendata.caceres.es/def/ontomunicipio#NumberMalformedBuds) (c)<br />[om:TotalNumberBuds](http://opendata.caceres.es/def/ontomunicipio#TotalNumberBuds) (c)<br />[om:NumberDryBuds](http://opendata.caceres.es/def/ontomunicipio#NumberDryBuds) (c)<br />
### number color
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberColor`
Super-classes |[om:Number](http://opendata.caceres.es/def/ontomunicipio#Number) (c)<br />
Sub-classes |[om:NumberPulpBrowning3](http://opendata.caceres.es/def/ontomunicipio#NumberPulpBrowning3) (c)<br />[om:NumberExternalBrowning1](http://opendata.caceres.es/def/ontomunicipio#NumberExternalBrowning1) (c)<br />[om:NumberVascularBrowning4](http://opendata.caceres.es/def/ontomunicipio#NumberVascularBrowning4) (c)<br />[om:NumberVascularBrowning1](http://opendata.caceres.es/def/ontomunicipio#NumberVascularBrowning1) (c)<br />[om:NumberPulpBrowning4](http://opendata.caceres.es/def/ontomunicipio#NumberPulpBrowning4) (c)<br />[om:NumberColor5](http://opendata.caceres.es/def/ontomunicipio#NumberColor5) (c)<br />[om:NumberExternalBrowning4](http://opendata.caceres.es/def/ontomunicipio#NumberExternalBrowning4) (c)<br />[om:NumberPulpBrowning1](http://opendata.caceres.es/def/ontomunicipio#NumberPulpBrowning1) (c)<br />[om:NumberExternalBrowning3](http://opendata.caceres.es/def/ontomunicipio#NumberExternalBrowning3) (c)<br />[om:NumberPulpBrowning5](http://opendata.caceres.es/def/ontomunicipio#NumberPulpBrowning5) (c)<br />[om:NumberExternalBrowning5](http://opendata.caceres.es/def/ontomunicipio#NumberExternalBrowning5) (c)<br />[om:NumberVascularBrowning2](http://opendata.caceres.es/def/ontomunicipio#NumberVascularBrowning2) (c)<br />[om:NumberColor4](http://opendata.caceres.es/def/ontomunicipio#NumberColor4) (c)<br />[om:NumberColor2](http://opendata.caceres.es/def/ontomunicipio#NumberColor2) (c)<br />[om:NumberColor3](http://opendata.caceres.es/def/ontomunicipio#NumberColor3) (c)<br />[om:NumberVascularBrowning5](http://opendata.caceres.es/def/ontomunicipio#NumberVascularBrowning5) (c)<br />[om:NumberExternalBrowning2](http://opendata.caceres.es/def/ontomunicipio#NumberExternalBrowning2) (c)<br />[om:NumberPulpBrowning2](http://opendata.caceres.es/def/ontomunicipio#NumberPulpBrowning2) (c)<br />[om:NumberColor1](http://opendata.caceres.es/def/ontomunicipio#NumberColor1) (c)<br />[om:NumberVascularBrowning3](http://opendata.caceres.es/def/ontomunicipio#NumberVascularBrowning3) (c)<br />
### number color 1
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberColor1`
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### number color 2
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberColor2`
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### number color 3
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberColor3`
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### number color 4
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberColor4`
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### number color 5
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberColor5`
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### number density
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberDensity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:numberDensity-Dimension](http://opendata.caceres.es/def/ontomunicipio#numberDensity-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:InitialMassFunction](http://opendata.caceres.es/def/ontomunicipio#InitialMassFunction) (c)<br />[om:LuminosityFunction](http://opendata.caceres.es/def/ontomunicipio#LuminosityFunction) (c)<br />
### number density unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberDensityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### number dry buds
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberDryBuds`
Super-classes |[om:NumberBuds](http://opendata.caceres.es/def/ontomunicipio#NumberBuds) (c)<br />
### number dry flowers
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberDryFlowers`
Super-classes |[om:NumberFlowers](http://opendata.caceres.es/def/ontomunicipio#NumberFlowers) (c)<br />
### number dry leaves
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberDryLeaves`
Super-classes |[om:NumberLeaves](http://opendata.caceres.es/def/ontomunicipio#NumberLeaves) (c)<br />
### number external browning
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberExternalBrowning`
Super-classes |[om:Number](http://opendata.caceres.es/def/ontomunicipio#Number) (c)<br />
### number external browning 1
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberExternalBrowning1`
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### number external browning 2
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberExternalBrowning2`
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### number external browning 3
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberExternalBrowning3`
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### number external browning 4
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberExternalBrowning4`
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### number external browning 5
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberExternalBrowning5`
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### number flowers
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberFlowers`
Super-classes |[om:Number](http://opendata.caceres.es/def/ontomunicipio#Number) (c)<br />
Sub-classes |[om:TotalNumberFlowers](http://opendata.caceres.es/def/ontomunicipio#TotalNumberFlowers) (c)<br />[om:NumberDryFlowers](http://opendata.caceres.es/def/ontomunicipio#NumberDryFlowers) (c)<br />[om:NumberBlue-DiscoloredFlowers](http://opendata.caceres.es/def/ontomunicipio#NumberBlue-DiscoloredFlowers) (c)<br />[om:NumberWiltedFlowers](http://opendata.caceres.es/def/ontomunicipio#NumberWiltedFlowers) (c)<br />[om:NumberMalformedFlowers](http://opendata.caceres.es/def/ontomunicipio#NumberMalformedFlowers) (c)<br />[om:NumberNonturgidFlowers](http://opendata.caceres.es/def/ontomunicipio#NumberNonturgidFlowers) (c)<br />[om:NumberRottenFlowers](http://opendata.caceres.es/def/ontomunicipio#NumberRottenFlowers) (c)<br />[om:NumberAbscisedFlowers](http://opendata.caceres.es/def/ontomunicipio#NumberAbscisedFlowers) (c)<br />
### number leaves
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberLeaves`
Super-classes |[om:Number](http://opendata.caceres.es/def/ontomunicipio#Number) (c)<br />
Sub-classes |[om:NumberWiltedLeaves](http://opendata.caceres.es/def/ontomunicipio#NumberWiltedLeaves) (c)<br />[om:NumberNonturgidLeaves](http://opendata.caceres.es/def/ontomunicipio#NumberNonturgidLeaves) (c)<br />[om:NumberRottenLeaves](http://opendata.caceres.es/def/ontomunicipio#NumberRottenLeaves) (c)<br />[om:NumberYellowLeaves](http://opendata.caceres.es/def/ontomunicipio#NumberYellowLeaves) (c)<br />[om:NumberDryLeaves](http://opendata.caceres.es/def/ontomunicipio#NumberDryLeaves) (c)<br />[om:TotalNumberLeaves](http://opendata.caceres.es/def/ontomunicipio#TotalNumberLeaves) (c)<br />[om:NumberAbscisedLeaves](http://opendata.caceres.es/def/ontomunicipio#NumberAbscisedLeaves) (c)<br />
### number malformed buds
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberMalformedBuds`
Super-classes |[om:NumberBuds](http://opendata.caceres.es/def/ontomunicipio#NumberBuds) (c)<br />
### number malformed flowers
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberMalformedFlowers`
Super-classes |[om:NumberFlowers](http://opendata.caceres.es/def/ontomunicipio#NumberFlowers) (c)<br />
### number manual firmness
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness`
Super-classes |[om:Number](http://opendata.caceres.es/def/ontomunicipio#Number) (c)<br />
Sub-classes |[om:NumberManualFirmness3.5](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness3.5) (c)<br />[om:NumberManualFirmness0](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness0) (c)<br />[om:NumberManualFirmness1.5](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness1.5) (c)<br />[om:NumberManualFirmness1](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness1) (c)<br />[om:NumberManualFirmness3](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness3) (c)<br />[om:NumberManualFirmness2.5](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness2.5) (c)<br />[om:NumberManualFirmness4.5](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness4.5) (c)<br />[om:NumberManualFirmness4](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness4) (c)<br />[om:NumberManualFirmness5](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness5) (c)<br />[om:NumberManualFirmness2](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness2) (c)<br />[om:NumberManualFirmness0.5](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness0.5) (c)<br />
### number manual firmness 0
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness0`
Super-classes |[om:NumberManualFirmness](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness) (c)<br />
### number manual firmness 0.5
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness0.5`
Super-classes |[om:NumberManualFirmness](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness) (c)<br />
### number manual firmness 1
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness1`
Super-classes |[om:NumberManualFirmness](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness) (c)<br />
### number manual firmness 1.5
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness1.5`
Super-classes |[om:NumberManualFirmness](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness) (c)<br />
### number manual firmness 2
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness2`
Super-classes |[om:NumberManualFirmness](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness) (c)<br />
### number manual firmness 2.5
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness2.5`
Super-classes |[om:NumberManualFirmness](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness) (c)<br />
### number manual firmness 3
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness3`
Super-classes |[om:NumberManualFirmness](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness) (c)<br />
### number manual firmness 3.5
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness3.5`
Super-classes |[om:NumberManualFirmness](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness) (c)<br />
### number manual firmness 4
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness4`
Super-classes |[om:NumberManualFirmness](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness) (c)<br />
### number manual firmness 4.5
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness4.5`
Super-classes |[om:NumberManualFirmness](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness) (c)<br />
### number manual firmness 5
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness5`
Super-classes |[om:NumberManualFirmness](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness) (c)<br />
### number nonturgid flowers
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberNonturgidFlowers`
Super-classes |[om:NumberFlowers](http://opendata.caceres.es/def/ontomunicipio#NumberFlowers) (c)<br />
### number nonturgid leaves
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberNonturgidLeaves`
Super-classes |[om:NumberLeaves](http://opendata.caceres.es/def/ontomunicipio#NumberLeaves) (c)<br />
### number pulp browning
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberPulpBrowning`
Super-classes |[om:Number](http://opendata.caceres.es/def/ontomunicipio#Number) (c)<br />
### number pulp browning 1
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberPulpBrowning1`
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### number pulp browning 2
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberPulpBrowning2`
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### number pulp browning 3
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberPulpBrowning3`
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### number pulp browning 4
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberPulpBrowning4`
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### number pulp browning 5
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberPulpBrowning5`
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### number rotten flowers
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberRottenFlowers`
Super-classes |[om:NumberFlowers](http://opendata.caceres.es/def/ontomunicipio#NumberFlowers) (c)<br />
### number rotten leaves
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberRottenLeaves`
Super-classes |[om:NumberLeaves](http://opendata.caceres.es/def/ontomunicipio#NumberLeaves) (c)<br />
### number unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### number vascular browning
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberVascularBrowning`
Super-classes |[om:Number](http://opendata.caceres.es/def/ontomunicipio#Number) (c)<br />
### number vascular browning 1
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberVascularBrowning1`
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### number vascular browning 2
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberVascularBrowning2`
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### number vascular browning 3
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberVascularBrowning3`
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### number vascular browning 4
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberVascularBrowning4`
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### number vascular browning 5
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberVascularBrowning5`
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### number wilted flowers
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberWiltedFlowers`
Super-classes |[om:NumberFlowers](http://opendata.caceres.es/def/ontomunicipio#NumberFlowers) (c)<br />
### number wilted leaves
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberWiltedLeaves`
Super-classes |[om:NumberLeaves](http://opendata.caceres.es/def/ontomunicipio#NumberLeaves) (c)<br />
### number yellow leaves
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NumberYellowLeaves`
Super-classes |[om:NumberLeaves](http://opendata.caceres.es/def/ontomunicipio#NumberLeaves) (c)<br />
### Nusselt number
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NusseltNumber`
Description | <p>The Nusselt number is the ratio of convective to conductive heat transfer across (normal to) the boundary.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### Nusselt number for mass transfer
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NusseltNumberForMassTransfer`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### Nusselt number for mass transfer unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NusseltNumberForMassTransferUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### Nusselt number unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#NusseltNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### organ dose equivalent
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#OrganDoseEquivalent`
Super-classes |[om:DoseEquivalent](http://opendata.caceres.es/def/ontomunicipio#DoseEquivalent) (c)<br />
### overrun
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Overrun`
Super-classes |[om:VolumeFraction](http://opendata.caceres.es/def/ontomunicipio#VolumeFraction) (c)<br />
### peak wavelength
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PeakWavelength`
Description | <p>Wavelength for which the detectivity is at a maximum.</p>
Super-classes |[om:Wavelength](http://opendata.caceres.es/def/ontomunicipio#Wavelength) (c)<br />
### Péclet number
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PecletNumber`
Description | <p>The Péclet number is a dimensionless number that relates the rate of advection of a flow to its rate of diffusion, often thermal diffusion.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### Péclet number for mass transfer
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PecletNumberForMassTransfer`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
### Péclet number for mass transfer unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PecletNumberForMassTransferUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### Péclet number unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PecletNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### percentage
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Percentage`
Super-classes |[om:Ratio](http://opendata.caceres.es/def/ontomunicipio#Ratio) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### percentage unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PercentageUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### period
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Period`
Super-classes |[om:Time](http://opendata.caceres.es/def/ontomunicipio#Time) (c)<br />
### period of variability
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PeriodOfVariability`
Description | <p>The duration of one cycle in a (semi) periodical star.</p>
Super-classes |[om:Time](http://opendata.caceres.es/def/ontomunicipio#Time) (c)<br />
### permeability (earth science)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Permeability-EarthScience`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:area-Dimension](http://opendata.caceres.es/def/ontomunicipio#area-Dimension) (c)<br />
### permeability (earth science) unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Permeability-EarthScienceUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### permeability of free space
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PermeabilityOfFreeSpace`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:permeabilityOfFreeSpace-Dimension](http://opendata.caceres.es/def/ontomunicipio#permeabilityOfFreeSpace-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### permeability of free space unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PermeabilityOfFreeSpaceUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### permeance (electromagnetic)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Permeance-Electromagnetic`
Description | <p>Electromagnetic permeance is a measure of flux for a number of current-turns in magnetic circuit.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:inductanceOrPermeance-Electromagnetic-Dimension](http://opendata.caceres.es/def/ontomunicipio#inductanceOrPermeance-Electromagnetic-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### permeance (electromagnetic) unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Permeance-ElectromagneticUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### permeance (materials science)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Permeance-MaterialsScience`
Description | <p>Permeance is the degree to which a material transmits another substance.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:permeance-MaterialsScience-Dimension](http://opendata.caceres.es/def/ontomunicipio#permeance-MaterialsScience-Dimension) (c)<br />
### permeance (materials science) unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Permeance-MaterialsScienceUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### permittivity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Permittivity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:permittivity-Dimension](http://opendata.caceres.es/def/ontomunicipio#permittivity-Dimension) (c)<br />
### permittivity unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PermittivityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### personal dose equivalent
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PersonalDoseEquivalent`
Super-classes |[om:DoseEquivalent](http://opendata.caceres.es/def/ontomunicipio#DoseEquivalent) (c)<br />
### photographic amplitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PhotographicAmplitude`
Description | <p>Amplitude of the light variation in photographic magnitude.</p>
Super-classes |[om:Amplitude](http://opendata.caceres.es/def/ontomunicipio#Amplitude) (c)<br />
### photographic magnitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PhotographicMagnitude`
Super-classes |[om:Magnitude](http://opendata.caceres.es/def/ontomunicipio#Magnitude) (c)<br />
Sub-classes |[om:PhotographicMagnitudeAtMaximumBrightness](http://opendata.caceres.es/def/ontomunicipio#PhotographicMagnitudeAtMaximumBrightness) (c)<br />[om:PhotographicMagnitudeAtMinimumBrightness](http://opendata.caceres.es/def/ontomunicipio#PhotographicMagnitudeAtMinimumBrightness) (c)<br />
### photographic magnitude at maximum brightness
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PhotographicMagnitudeAtMaximumBrightness`
Super-classes |[om:PhotographicMagnitude](http://opendata.caceres.es/def/ontomunicipio#PhotographicMagnitude) (c)<br />[om:MagnitudeAtMaximumBrightness](http://opendata.caceres.es/def/ontomunicipio#MagnitudeAtMaximumBrightness) (c)<br />
### photographic magnitude at minimum brightness
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PhotographicMagnitudeAtMinimumBrightness`
Super-classes |[om:PhotographicMagnitude](http://opendata.caceres.es/def/ontomunicipio#PhotographicMagnitude) (c)<br />[om:MagnitudeAtMinimumBrightness](http://opendata.caceres.es/def/ontomunicipio#MagnitudeAtMinimumBrightness) (c)<br />
### planetary aberration
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PlanetaryAberration`
Description | <p>The apparent angular displacement of the observed position of a celestial object produced by the motion of the observer and the actual motion of the observed object.</p>
Super-classes |[om:Aberration](http://opendata.caceres.es/def/ontomunicipio#Aberration) (c)<br />
### point
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Point`
Description | <p>A point is an element of an interval scale or a ratio scale, for example, 273.16 on the Kelvin scale indicates the triple point of water thermodynamic temperature.</p>
Sub-classes |[om:FixedPoint](http://opendata.caceres.es/def/ontomunicipio#FixedPoint) (c)<br />
In range of |[om:hasPoint](http://opendata.caceres.es/def/ontomunicipio#hasPoint) (op)<br />
### potassium sorbate mass fraction
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PotassiumSorbateMassFraction`
Description | <p>The fraction of the mass of potassium sorbate in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### potential difference
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PotentialDifference`
Super-classes |[om:ElectricPotential](http://opendata.caceres.es/def/ontomunicipio#ElectricPotential) (c)<br />
### potential energy
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PotentialEnergy`
Description | <p>Potential energy is energy due to position of one body with respect to another or to the relative parts of the same body.</p>
Super-classes |[om:Energy](http://opendata.caceres.es/def/ontomunicipio#Energy) (c)<br />
### power
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Power`
Description | <p>Power is the time rate at which work is done. It is a derived quantity in the International System of Units. Power is energy divided by time.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:power-Dimension](http://opendata.caceres.es/def/ontomunicipio#power-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:NoiseEquivalentPower](http://opendata.caceres.es/def/ontomunicipio#NoiseEquivalentPower) (c)<br />[om:HeatFlowRate](http://opendata.caceres.es/def/ontomunicipio#HeatFlowRate) (c)<br />[om:RadiantFlux](http://opendata.caceres.es/def/ontomunicipio#RadiantFlux) (c)<br />
### power density
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PowerDensity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:powerDensity-Dimension](http://opendata.caceres.es/def/ontomunicipio#powerDensity-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:Irradiance](http://opendata.caceres.es/def/ontomunicipio#Irradiance) (c)<br />[om:HeatFluxDensity](http://opendata.caceres.es/def/ontomunicipio#HeatFluxDensity) (c)<br />
### power density unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PowerDensityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### power unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PowerUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### Prandtl number
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrandtlNumber`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
### Prandtl number unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrandtlNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### prefix
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Prefix`
Description | <p>A prefix is a name that precedes a basic unit of measure to indicate a decimal or binary multiple or fraction of the unit. Each prefix has a unique symbol that is prepended to the unit symbol. For example, an electric current of 0.000 000 001 ampere is written by using the SI-prefix nano as 1 nanoampere or 1 nA.</p>
Sub-classes |[om:BinaryPrefix](http://opendata.caceres.es/def/ontomunicipio#BinaryPrefix) (c)<br />[om:SIPrefix](http://opendata.caceres.es/def/ontomunicipio#SIPrefix) (c)<br />
In range of |[om:hasPrefix](http://opendata.caceres.es/def/ontomunicipio#hasPrefix) (op)<br />
### prefixed ampere
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedAmpere`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed are
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedAre`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed becquerel
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedBecquerel`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed bit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedBit`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed byte
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedByte`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed calorie (mean)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedCalorie-Mean`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed candela
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedCandela`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed coulomb
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedCoulomb`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed degree Celsius
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedDegreeCelsius`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed electronvolt
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedElectronvolt`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed farad
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedFarad`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed gram
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedGram`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed gram per litre
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedGramPerLitre`
Super-classes |[om:UnitDivision](http://opendata.caceres.es/def/ontomunicipio#UnitDivision) (c)<br />
Has members |[om:femtogramPerLitre](http://opendata.caceres.es/def/ontomunicipio#femtogramPerLitre)<br />[om:zeptogramPerLitre](http://opendata.caceres.es/def/ontomunicipio#zeptogramPerLitre)<br />[om:milligramPerLitre](http://opendata.caceres.es/def/ontomunicipio#milligramPerLitre)<br />[om:yottagramPerLitre](http://opendata.caceres.es/def/ontomunicipio#yottagramPerLitre)<br />[om:hectogramPerLitre](http://opendata.caceres.es/def/ontomunicipio#hectogramPerLitre)<br />[om:exagramPerLitre](http://opendata.caceres.es/def/ontomunicipio#exagramPerLitre)<br />[om:gigagramPerLitre](http://opendata.caceres.es/def/ontomunicipio#gigagramPerLitre)<br />[om:kilogramPerLitre](http://opendata.caceres.es/def/ontomunicipio#kilogramPerLitre)<br />[om:picogramPerLitre](http://opendata.caceres.es/def/ontomunicipio#picogramPerLitre)<br />[om:attogramPerLitre](http://opendata.caceres.es/def/ontomunicipio#attogramPerLitre)<br />[om:yoctogramPerLitre](http://opendata.caceres.es/def/ontomunicipio#yoctogramPerLitre)<br />[om:microgramPerLitre](http://opendata.caceres.es/def/ontomunicipio#microgramPerLitre)<br />[om:centigramPerLitre](http://opendata.caceres.es/def/ontomunicipio#centigramPerLitre)<br />[om:megagramPerLitre](http://opendata.caceres.es/def/ontomunicipio#megagramPerLitre)<br />[om:petagramPerLitre](http://opendata.caceres.es/def/ontomunicipio#petagramPerLitre)<br />[om:teragramPerLitre](http://opendata.caceres.es/def/ontomunicipio#teragramPerLitre)<br />[om:decagramPerLitre](http://opendata.caceres.es/def/ontomunicipio#decagramPerLitre)<br />[om:decigramPerLitre](http://opendata.caceres.es/def/ontomunicipio#decigramPerLitre)<br />[om:zettagramPerLitre](http://opendata.caceres.es/def/ontomunicipio#zettagramPerLitre)<br />[om:nanogramPerLitre](http://opendata.caceres.es/def/ontomunicipio#nanogramPerLitre)<br />
### prefixed gram per prefixed litre
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedGramPerPrefixedLitre`
Super-classes |[om:UnitDivision](http://opendata.caceres.es/def/ontomunicipio#UnitDivision) (c)<br />
### prefixed gray
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedGray`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed henry
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedHenry`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed hertz
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedHertz`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed joule
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedJoule`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed katal
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedKatal`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed kelvin
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedKelvin`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed litre
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedLitre`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed lumen
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedLumen`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed lux
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedLux`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed metre
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedMetre`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed metre per prefixed second (time)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedMetrePerPrefixedSecond-Time`
Super-classes |[om:UnitDivision](http://opendata.caceres.es/def/ontomunicipio#UnitDivision) (c)<br />
### prefixed metre per prefixed secon (time) squared
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedMetrePerPrefixedSecond-TimeSquared`
Super-classes |[om:UnitDivision](http://opendata.caceres.es/def/ontomunicipio#UnitDivision) (c)<br />
### prefixed metre per second (time)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedMetrePerSecond-Time`
Super-classes |[om:UnitDivision](http://opendata.caceres.es/def/ontomunicipio#UnitDivision) (c)<br />
Has members |[om:yottametrePerSecond-Time](http://opendata.caceres.es/def/ontomunicipio#yottametrePerSecond-Time)<br />[om:femtometrePerSecond-Time](http://opendata.caceres.es/def/ontomunicipio#femtometrePerSecond-Time)<br />[om:millimetrePerSecond-Time](http://opendata.caceres.es/def/ontomunicipio#millimetrePerSecond-Time)<br />[om:picometrePerSecond-Time](http://opendata.caceres.es/def/ontomunicipio#picometrePerSecond-Time)<br />[om:gigametrePerSecond-Time](http://opendata.caceres.es/def/ontomunicipio#gigametrePerSecond-Time)<br />[om:megametrePerSecond-Time](http://opendata.caceres.es/def/ontomunicipio#megametrePerSecond-Time)<br />[om:decimetrePerSecond-Time](http://opendata.caceres.es/def/ontomunicipio#decimetrePerSecond-Time)<br />[om:yoctometrePerSecond-Time](http://opendata.caceres.es/def/ontomunicipio#yoctometrePerSecond-Time)<br />[om:kilometrePerSecond-Time](http://opendata.caceres.es/def/ontomunicipio#kilometrePerSecond-Time)<br />[om:nanometrePerSecond-Time](http://opendata.caceres.es/def/ontomunicipio#nanometrePerSecond-Time)<br />[om:micrometrePerSecond-Time](http://opendata.caceres.es/def/ontomunicipio#micrometrePerSecond-Time)<br />[om:centimetrePerSecond-Time](http://opendata.caceres.es/def/ontomunicipio#centimetrePerSecond-Time)<br />[om:terametrePerSecond-Time](http://opendata.caceres.es/def/ontomunicipio#terametrePerSecond-Time)<br />[om:decametrePerSecond-Time](http://opendata.caceres.es/def/ontomunicipio#decametrePerSecond-Time)<br />[om:exametrePerSecond-Time](http://opendata.caceres.es/def/ontomunicipio#exametrePerSecond-Time)<br />[om:hectometrePerSecond-Time](http://opendata.caceres.es/def/ontomunicipio#hectometrePerSecond-Time)<br />[om:attometrePerSecond-Time](http://opendata.caceres.es/def/ontomunicipio#attometrePerSecond-Time)<br />[om:zettametrePerSecond-Time](http://opendata.caceres.es/def/ontomunicipio#zettametrePerSecond-Time)<br />[om:petametrePerSecond-Time](http://opendata.caceres.es/def/ontomunicipio#petametrePerSecond-Time)<br />[om:zeptometrePerSecond-Time](http://opendata.caceres.es/def/ontomunicipio#zeptometrePerSecond-Time)<br />
### prefixed metre per second (time) squared
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedMetrePerSecond-TimeSquared`
Super-classes |[om:UnitDivision](http://opendata.caceres.es/def/ontomunicipio#UnitDivision) (c)<br />
Has members |[om:kilometrePerSecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#kilometrePerSecond-TimeSquared)<br />[om:nanometrePerSecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#nanometrePerSecond-TimeSquared)<br />[om:gigametrePerSecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#gigametrePerSecond-TimeSquared)<br />[om:femtometrePerSecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#femtometrePerSecond-TimeSquared)<br />[om:zeptometrePerSecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#zeptometrePerSecond-TimeSquared)<br />[om:micrometrePerSecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#micrometrePerSecond-TimeSquared)<br />[om:centimetrePerSecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#centimetrePerSecond-TimeSquared)<br />[om:zettametrePerSecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#zettametrePerSecond-TimeSquared)<br />[om:yoctometrePerSecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#yoctometrePerSecond-TimeSquared)<br />[om:decametrePerSecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#decametrePerSecond-TimeSquared)<br />[om:exametrePerSecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#exametrePerSecond-TimeSquared)<br />[om:millimetrePerSecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#millimetrePerSecond-TimeSquared)<br />[om:decimetrePerSecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#decimetrePerSecond-TimeSquared)<br />[om:attometrePerSecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#attometrePerSecond-TimeSquared)<br />[om:hectometrePerSecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#hectometrePerSecond-TimeSquared)<br />[om:picometrePerSecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#picometrePerSecond-TimeSquared)<br />[om:yottametrePerSecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#yottametrePerSecond-TimeSquared)<br />[om:petametrePerSecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#petametrePerSecond-TimeSquared)<br />[om:megametrePerSecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#megametrePerSecond-TimeSquared)<br />[om:terametrePerSecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#terametrePerSecond-TimeSquared)<br />
### prefixed metre prefixed gram
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedMetrePrefixedGram`
Super-classes |[om:UnitMultiplication](http://opendata.caceres.es/def/ontomunicipio#UnitMultiplication) (c)<br />
### prefixed molair
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedMolair`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed mole
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedMole`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed mole per litre
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedMolePerLitre`
Super-classes |[om:UnitDivision](http://opendata.caceres.es/def/ontomunicipio#UnitDivision) (c)<br />
Has members |[om:micromolePerLitre](http://opendata.caceres.es/def/ontomunicipio#micromolePerLitre)<br />[om:decamolePerLitre](http://opendata.caceres.es/def/ontomunicipio#decamolePerLitre)<br />[om:teramolePerLitre](http://opendata.caceres.es/def/ontomunicipio#teramolePerLitre)<br />[om:decimolePerLitre](http://opendata.caceres.es/def/ontomunicipio#decimolePerLitre)<br />[om:zettamolePerLitre](http://opendata.caceres.es/def/ontomunicipio#zettamolePerLitre)<br />[om:picomolePerLitre](http://opendata.caceres.es/def/ontomunicipio#picomolePerLitre)<br />[om:millimolePerLitre](http://opendata.caceres.es/def/ontomunicipio#millimolePerLitre)<br />[om:yottamolePerLitre](http://opendata.caceres.es/def/ontomunicipio#yottamolePerLitre)<br />[om:megamolePerLitre](http://opendata.caceres.es/def/ontomunicipio#megamolePerLitre)<br />[om:gigamolePerLitre](http://opendata.caceres.es/def/ontomunicipio#gigamolePerLitre)<br />[om:kilomolePerLitre](http://opendata.caceres.es/def/ontomunicipio#kilomolePerLitre)<br />[om:hectomolePerLitre](http://opendata.caceres.es/def/ontomunicipio#hectomolePerLitre)<br />[om:examolePerLitre](http://opendata.caceres.es/def/ontomunicipio#examolePerLitre)<br />[om:petamolePerLitre](http://opendata.caceres.es/def/ontomunicipio#petamolePerLitre)<br />[om:centimolePerLitre](http://opendata.caceres.es/def/ontomunicipio#centimolePerLitre)<br />[om:femtomolePerLitre](http://opendata.caceres.es/def/ontomunicipio#femtomolePerLitre)<br />[om:yoctomolePerLitre](http://opendata.caceres.es/def/ontomunicipio#yoctomolePerLitre)<br />[om:attomolePerLitre](http://opendata.caceres.es/def/ontomunicipio#attomolePerLitre)<br />[om:nanomolePerLitre](http://opendata.caceres.es/def/ontomunicipio#nanomolePerLitre)<br />[om:zeptomolePerLitre](http://opendata.caceres.es/def/ontomunicipio#zeptomolePerLitre)<br />
### prefixed mole per metre
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedMolePerMetre`
Super-classes |[om:UnitDivision](http://opendata.caceres.es/def/ontomunicipio#UnitDivision) (c)<br />
Has members |[om:centimolePerMetre](http://opendata.caceres.es/def/ontomunicipio#centimolePerMetre)<br />[om:micromolePerMetre](http://opendata.caceres.es/def/ontomunicipio#micromolePerMetre)<br />[om:decimolePerMetre](http://opendata.caceres.es/def/ontomunicipio#decimolePerMetre)<br />[om:zeptomolePerMetre](http://opendata.caceres.es/def/ontomunicipio#zeptomolePerMetre)<br />[om:hectomolePerMetre](http://opendata.caceres.es/def/ontomunicipio#hectomolePerMetre)<br />[om:picomolePerMetre](http://opendata.caceres.es/def/ontomunicipio#picomolePerMetre)<br />[om:zettamolePerMetre](http://opendata.caceres.es/def/ontomunicipio#zettamolePerMetre)<br />[om:nanomolePerMetre](http://opendata.caceres.es/def/ontomunicipio#nanomolePerMetre)<br />[om:examolePerMetre](http://opendata.caceres.es/def/ontomunicipio#examolePerMetre)<br />[om:kilomolePerMetre](http://opendata.caceres.es/def/ontomunicipio#kilomolePerMetre)<br />[om:millimolePerMetre](http://opendata.caceres.es/def/ontomunicipio#millimolePerMetre)<br />[om:teramolePerMetre](http://opendata.caceres.es/def/ontomunicipio#teramolePerMetre)<br />[om:decamolePerMetre](http://opendata.caceres.es/def/ontomunicipio#decamolePerMetre)<br />[om:yottamolePerMetre](http://opendata.caceres.es/def/ontomunicipio#yottamolePerMetre)<br />[om:gigamolePerMetre](http://opendata.caceres.es/def/ontomunicipio#gigamolePerMetre)<br />[om:attomolePerMetre](http://opendata.caceres.es/def/ontomunicipio#attomolePerMetre)<br />[om:femtomolePerMetre](http://opendata.caceres.es/def/ontomunicipio#femtomolePerMetre)<br />[om:yoctomolePerMetre](http://opendata.caceres.es/def/ontomunicipio#yoctomolePerMetre)<br />[om:petamolePerMetre](http://opendata.caceres.es/def/ontomunicipio#petamolePerMetre)<br />[om:megamolePerMetre](http://opendata.caceres.es/def/ontomunicipio#megamolePerMetre)<br />
### prefixed mole per prefixed litre
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedMolePerPrefixedLitre`
Super-classes |[om:UnitDivision](http://opendata.caceres.es/def/ontomunicipio#UnitDivision) (c)<br />
### prefixed mole per prefixed metre
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedMolePerPrefixedMetre`
Super-classes |[om:UnitDivision](http://opendata.caceres.es/def/ontomunicipio#UnitDivision) (c)<br />
### prefixed newton
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedNewton`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed ohm
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedOhm`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed pascal
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedPascal`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed poise
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedPoise`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed radian
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedRadian`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed second (time)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedSecond-Time`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed second (time) squared
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedSecond-TimeSquared`
Super-classes |[om:UnitExponentiation](http://opendata.caceres.es/def/ontomunicipio#UnitExponentiation) (c)<br />
Has members |[om:picosecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#picosecond-TimeSquared)<br />[om:hectosecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#hectosecond-TimeSquared)<br />[om:yottasecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#yottasecond-TimeSquared)<br />[om:petasecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#petasecond-TimeSquared)<br />[om:exasecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#exasecond-TimeSquared)<br />[om:gigasecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#gigasecond-TimeSquared)<br />[om:decisecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#decisecond-TimeSquared)<br />[om:femtosecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#femtosecond-TimeSquared)<br />[om:nanosecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#nanosecond-TimeSquared)<br />[om:zettasecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#zettasecond-TimeSquared)<br />[om:yoctosecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#yoctosecond-TimeSquared)<br />[om:microsecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#microsecond-TimeSquared)<br />[om:decasecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#decasecond-TimeSquared)<br />[om:kilosecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#kilosecond-TimeSquared)<br />[om:zeptosecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#zeptosecond-TimeSquared)<br />[om:attosecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#attosecond-TimeSquared)<br />[om:centisecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#centisecond-TimeSquared)<br />[om:megasecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#megasecond-TimeSquared)<br />[om:terasecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#terasecond-TimeSquared)<br />[om:millisecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#millisecond-TimeSquared)<br />
### prefixed siemens
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedSiemens`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed sievert
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedSievert`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed steradian
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedSteradian`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed stokes
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedStokes`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed tesla
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedTesla`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed tonne
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedTonne`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed unified atomic mass unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedUnifiedAtomicMassUnit`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
Restrictions |[om:hasUnit](http://opendata.caceres.es/def/ontomunicipio#hasUnit) (op) **only** [om:SingularUnit](http://opendata.caceres.es/def/ontomunicipio#SingularUnit) (c)<br />
Sub-classes |[om:PrefixedElectronvolt](http://opendata.caceres.es/def/ontomunicipio#PrefixedElectronvolt) (c)<br />[om:PrefixedBit](http://opendata.caceres.es/def/ontomunicipio#PrefixedBit) (c)<br />[om:PrefixedGram](http://opendata.caceres.es/def/ontomunicipio#PrefixedGram) (c)<br />[om:PrefixedTesla](http://opendata.caceres.es/def/ontomunicipio#PrefixedTesla) (c)<br />[om:PrefixedWatt](http://opendata.caceres.es/def/ontomunicipio#PrefixedWatt) (c)<br />[om:PrefixedLux](http://opendata.caceres.es/def/ontomunicipio#PrefixedLux) (c)<br />[om:PrefixedSteradian](http://opendata.caceres.es/def/ontomunicipio#PrefixedSteradian) (c)<br />[om:PrefixedHertz](http://opendata.caceres.es/def/ontomunicipio#PrefixedHertz) (c)<br />[om:PrefixedPascal](http://opendata.caceres.es/def/ontomunicipio#PrefixedPascal) (c)<br />[om:PrefixedSiemens](http://opendata.caceres.es/def/ontomunicipio#PrefixedSiemens) (c)<br />[om:PrefixedStokes](http://opendata.caceres.es/def/ontomunicipio#PrefixedStokes) (c)<br />[om:PrefixedGray](http://opendata.caceres.es/def/ontomunicipio#PrefixedGray) (c)<br />[om:PrefixedFarad](http://opendata.caceres.es/def/ontomunicipio#PrefixedFarad) (c)<br />[om:PrefixedSecond-Time](http://opendata.caceres.es/def/ontomunicipio#PrefixedSecond-Time) (c)<br />[om:PrefixedOhm](http://opendata.caceres.es/def/ontomunicipio#PrefixedOhm) (c)<br />[om:PrefixedMole](http://opendata.caceres.es/def/ontomunicipio#PrefixedMole) (c)<br />[om:PrefixedLumen](http://opendata.caceres.es/def/ontomunicipio#PrefixedLumen) (c)<br />[om:PrefixedMetre](http://opendata.caceres.es/def/ontomunicipio#PrefixedMetre) (c)<br />[om:PrefixedCandela](http://opendata.caceres.es/def/ontomunicipio#PrefixedCandela) (c)<br />[om:PrefixedJoule](http://opendata.caceres.es/def/ontomunicipio#PrefixedJoule) (c)<br />[om:PrefixedWeber](http://opendata.caceres.es/def/ontomunicipio#PrefixedWeber) (c)<br />[om:PrefixedCoulomb](http://opendata.caceres.es/def/ontomunicipio#PrefixedCoulomb) (c)<br />[om:PrefixedVolt](http://opendata.caceres.es/def/ontomunicipio#PrefixedVolt) (c)<br />[om:PrefixedHenry](http://opendata.caceres.es/def/ontomunicipio#PrefixedHenry) (c)<br />[om:PrefixedAre](http://opendata.caceres.es/def/ontomunicipio#PrefixedAre) (c)<br />[om:PrefixedByte](http://opendata.caceres.es/def/ontomunicipio#PrefixedByte) (c)<br />[om:PrefixedMolair](http://opendata.caceres.es/def/ontomunicipio#PrefixedMolair) (c)<br />[om:PrefixedPoise](http://opendata.caceres.es/def/ontomunicipio#PrefixedPoise) (c)<br />[om:PrefixedDegreeCelsius](http://opendata.caceres.es/def/ontomunicipio#PrefixedDegreeCelsius) (c)<br />[om:PrefixedKatal](http://opendata.caceres.es/def/ontomunicipio#PrefixedKatal) (c)<br />[om:PrefixedTonne](http://opendata.caceres.es/def/ontomunicipio#PrefixedTonne) (c)<br />[om:PrefixedLitre](http://opendata.caceres.es/def/ontomunicipio#PrefixedLitre) (c)<br />[om:PrefixedNewton](http://opendata.caceres.es/def/ontomunicipio#PrefixedNewton) (c)<br />[om:PrefixedCalorie-Mean](http://opendata.caceres.es/def/ontomunicipio#PrefixedCalorie-Mean) (c)<br />[om:PrefixedBecquerel](http://opendata.caceres.es/def/ontomunicipio#PrefixedBecquerel) (c)<br />[om:PrefixedSievert](http://opendata.caceres.es/def/ontomunicipio#PrefixedSievert) (c)<br />[om:PrefixedUnifiedAtomicMassUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnifiedAtomicMassUnit) (c)<br />[om:PrefixedRadian](http://opendata.caceres.es/def/ontomunicipio#PrefixedRadian) (c)<br />[om:PrefixedKelvin](http://opendata.caceres.es/def/ontomunicipio#PrefixedKelvin) (c)<br />[om:PrefixedAmpere](http://opendata.caceres.es/def/ontomunicipio#PrefixedAmpere) (c)<br />
In domain of |[om:hasPrefix](http://opendata.caceres.es/def/ontomunicipio#hasPrefix) (op)<br />
Has members |[om:yottajoule](http://opendata.caceres.es/def/ontomunicipio#yottajoule)<br />[om:megajoule](http://opendata.caceres.es/def/ontomunicipio#megajoule)<br />[om:decimetre](http://opendata.caceres.es/def/ontomunicipio#decimetre)<br />[om:decahenry](http://opendata.caceres.es/def/ontomunicipio#decahenry)<br />[om:exawatt](http://opendata.caceres.es/def/ontomunicipio#exawatt)<br />[om:zeptokelvin](http://opendata.caceres.es/def/ontomunicipio#zeptokelvin)<br />[om:centiradian](http://opendata.caceres.es/def/ontomunicipio#centiradian)<br />[om:yottakelvin](http://opendata.caceres.es/def/ontomunicipio#yottakelvin)<br />[om:decametre](http://opendata.caceres.es/def/ontomunicipio#decametre)<br />[om:centijoule](http://opendata.caceres.es/def/ontomunicipio#centijoule)<br />[om:microdegreeCelsius](http://opendata.caceres.es/def/ontomunicipio#microdegreeCelsius)<br />[om:zeptocoulomb](http://opendata.caceres.es/def/ontomunicipio#zeptocoulomb)<br />[om:decasiemens](http://opendata.caceres.es/def/ontomunicipio#decasiemens)<br />[om:millisecond-Time](http://opendata.caceres.es/def/ontomunicipio#millisecond-Time)<br />[om:femtopascal](http://opendata.caceres.es/def/ontomunicipio#femtopascal)<br />[om:teramole](http://opendata.caceres.es/def/ontomunicipio#teramole)<br />[om:centimetre](http://opendata.caceres.es/def/ontomunicipio#centimetre)<br />[om:petavolt](http://opendata.caceres.es/def/ontomunicipio#petavolt)<br />[om:picokelvin](http://opendata.caceres.es/def/ontomunicipio#picokelvin)<br />[om:decibecquerel](http://opendata.caceres.es/def/ontomunicipio#decibecquerel)<br />[om:millibar](http://opendata.caceres.es/def/ontomunicipio#millibar)<br />[om:petacoulomb](http://opendata.caceres.es/def/ontomunicipio#petacoulomb)<br />[om:micronewton](http://opendata.caceres.es/def/ontomunicipio#micronewton)<br />[om:terakatal](http://opendata.caceres.es/def/ontomunicipio#terakatal)<br />[om:yoctowatt](http://opendata.caceres.es/def/ontomunicipio#yoctowatt)<br />[om:femtoampere](http://opendata.caceres.es/def/ontomunicipio#femtoampere)<br />[om:yoctodegreeCelsius](http://opendata.caceres.es/def/ontomunicipio#yoctodegreeCelsius)<br />[om:zeptolux](http://opendata.caceres.es/def/ontomunicipio#zeptolux)<br />[om:zeptofarad](http://opendata.caceres.es/def/ontomunicipio#zeptofarad)<br />[om:zettagray](http://opendata.caceres.es/def/ontomunicipio#zettagray)<br />[om:pebibit](http://opendata.caceres.es/def/ontomunicipio#pebibit)<br />[om:yoctotesla](http://opendata.caceres.es/def/ontomunicipio#yoctotesla)<br />[om:gigabyte](http://opendata.caceres.es/def/ontomunicipio#gigabyte)<br />[om:hectokatal](http://opendata.caceres.es/def/ontomunicipio#hectokatal)<br />[om:millivolt](http://opendata.caceres.es/def/ontomunicipio#millivolt)<br />[om:microtesla](http://opendata.caceres.es/def/ontomunicipio#microtesla)<br />[om:nanoweber](http://opendata.caceres.es/def/ontomunicipio#nanoweber)<br />[om:zeptovolt](http://opendata.caceres.es/def/ontomunicipio#zeptovolt)<br />[om:kilohertz](http://opendata.caceres.es/def/ontomunicipio#kilohertz)<br />[om:yoctoampere](http://opendata.caceres.es/def/ontomunicipio#yoctoampere)<br />[om:centilumen](http://opendata.caceres.es/def/ontomunicipio#centilumen)<br />[om:petafarad](http://opendata.caceres.es/def/ontomunicipio#petafarad)<br />[om:decaohm](http://opendata.caceres.es/def/ontomunicipio#decaohm)<br />[om:femtomolair](http://opendata.caceres.es/def/ontomunicipio#femtomolair)<br />[om:yoctokelvin](http://opendata.caceres.es/def/ontomunicipio#yoctokelvin)<br />[om:picosiemens](http://opendata.caceres.es/def/ontomunicipio#picosiemens)<br />[om:decasecond-Time](http://opendata.caceres.es/def/ontomunicipio#decasecond-Time)<br />[om:millimetreOfMercury](http://opendata.caceres.es/def/ontomunicipio#millimetreOfMercury)<br />[om:nanodegreeCelsius](http://opendata.caceres.es/def/ontomunicipio#nanodegreeCelsius)<br />[om:petatesla](http://opendata.caceres.es/def/ontomunicipio#petatesla)<br />[om:yoctogray](http://opendata.caceres.es/def/ontomunicipio#yoctogray)<br />[om:petakelvin](http://opendata.caceres.es/def/ontomunicipio#petakelvin)<br />[om:attolux](http://opendata.caceres.es/def/ontomunicipio#attolux)<br />[om:centimole](http://opendata.caceres.es/def/ontomunicipio#centimole)<br />[om:kilosievert](http://opendata.caceres.es/def/ontomunicipio#kilosievert)<br />[om:hectocandela](http://opendata.caceres.es/def/ontomunicipio#hectocandela)<br />[om:kilogray](http://opendata.caceres.es/def/ontomunicipio#kilogray)<br />[om:femtosievert](http://opendata.caceres.es/def/ontomunicipio#femtosievert)<br />[om:hectosecond-Time](http://opendata.caceres.es/def/ontomunicipio#hectosecond-Time)<br />[om:attomole](http://opendata.caceres.es/def/ontomunicipio#attomole)<br />[om:kilocalorie-Mean](http://opendata.caceres.es/def/ontomunicipio#kilocalorie-Mean)<br />[om:petahertz](http://opendata.caceres.es/def/ontomunicipio#petahertz)<br />[om:decatesla](http://opendata.caceres.es/def/ontomunicipio#decatesla)<br />[om:centipoise](http://opendata.caceres.es/def/ontomunicipio#centipoise)<br />[om:petabyte](http://opendata.caceres.es/def/ontomunicipio#petabyte)<br />[om:zettawatt](http://opendata.caceres.es/def/ontomunicipio#zettawatt)<br />[om:megahertz](http://opendata.caceres.es/def/ontomunicipio#megahertz)<br />[om:millilitre](http://opendata.caceres.es/def/ontomunicipio#millilitre)<br />[om:kilomole](http://opendata.caceres.es/def/ontomunicipio#kilomole)<br />[om:zeptomole](http://opendata.caceres.es/def/ontomunicipio#zeptomole)<br />[om:gigahenry](http://opendata.caceres.es/def/ontomunicipio#gigahenry)<br />[om:centistokes](http://opendata.caceres.es/def/ontomunicipio#centistokes)<br />[om:femtosecond-Time](http://opendata.caceres.es/def/ontomunicipio#femtosecond-Time)<br />[om:hectohertz](http://opendata.caceres.es/def/ontomunicipio#hectohertz)<br />[om:kilohm](http://opendata.caceres.es/def/ontomunicipio#kilohm)<br />[om:femtobecquerel](http://opendata.caceres.es/def/ontomunicipio#femtobecquerel)<br />[om:yoctoohm](http://opendata.caceres.es/def/ontomunicipio#yoctoohm)<br />[om:centihenry](http://opendata.caceres.es/def/ontomunicipio#centihenry)<br />[om:centiampere](http://opendata.caceres.es/def/ontomunicipio#centiampere)<br />[om:yoctohenry](http://opendata.caceres.es/def/ontomunicipio#yoctohenry)<br />[om:petasiemens](http://opendata.caceres.es/def/ontomunicipio#petasiemens)<br />[om:petaohm](http://opendata.caceres.es/def/ontomunicipio#petaohm)<br />[om:hectolitre](http://opendata.caceres.es/def/ontomunicipio#hectolitre)<br />[om:megalitre](http://opendata.caceres.es/def/ontomunicipio#megalitre)<br />[om:decabecquerel](http://opendata.caceres.es/def/ontomunicipio#decabecquerel)<br />[om:yottabit](http://opendata.caceres.es/def/ontomunicipio#yottabit)<br />[om:microgram](http://opendata.caceres.es/def/ontomunicipio#microgram)<br />[om:decagray](http://opendata.caceres.es/def/ontomunicipio#decagray)<br />[om:milligram](http://opendata.caceres.es/def/ontomunicipio#milligram)<br />[om:kilomolair](http://opendata.caceres.es/def/ontomunicipio#kilomolair)<br />[om:yoctosecond-Time](http://opendata.caceres.es/def/ontomunicipio#yoctosecond-Time)<br />[om:microsecond-Time](http://opendata.caceres.es/def/ontomunicipio#microsecond-Time)<br />[om:zettasiemens](http://opendata.caceres.es/def/ontomunicipio#zettasiemens)<br />[om:yoctokatal](http://opendata.caceres.es/def/ontomunicipio#yoctokatal)<br />[om:yoctojoule](http://opendata.caceres.es/def/ontomunicipio#yoctojoule)<br />[om:milliradian](http://opendata.caceres.es/def/ontomunicipio#milliradian)<br />[om:hectovolt](http://opendata.caceres.es/def/ontomunicipio#hectovolt)<br />[om:exakelvin](http://opendata.caceres.es/def/ontomunicipio#exakelvin)<br />[om:kilofarad](http://opendata.caceres.es/def/ontomunicipio#kilofarad)<br />[om:gigametre](http://opendata.caceres.es/def/ontomunicipio#gigametre)<br />[om:kibibit](http://opendata.caceres.es/def/ontomunicipio#kibibit)<br />[om:nanoampere](http://opendata.caceres.es/def/ontomunicipio#nanoampere)<br />[om:zeptoradian](http://opendata.caceres.es/def/ontomunicipio#zeptoradian)<br />[om:yobibyte](http://opendata.caceres.es/def/ontomunicipio#yobibyte)<br />[om:hectopascal](http://opendata.caceres.es/def/ontomunicipio#hectopascal)<br />[om:deciweber](http://opendata.caceres.es/def/ontomunicipio#deciweber)<br />[om:megabyte](http://opendata.caceres.es/def/ontomunicipio#megabyte)<br />[om:exatesla](http://opendata.caceres.es/def/ontomunicipio#exatesla)<br />[om:zeptodegreeCelsius](http://opendata.caceres.es/def/ontomunicipio#zeptodegreeCelsius)<br />[om:terahenry](http://opendata.caceres.es/def/ontomunicipio#terahenry)<br />[om:exasiemens](http://opendata.caceres.es/def/ontomunicipio#exasiemens)<br />[om:yottametre](http://opendata.caceres.es/def/ontomunicipio#yottametre)<br />[om:kiloparsec](http://opendata.caceres.es/def/ontomunicipio#kiloparsec)<br />[om:millimolair](http://opendata.caceres.es/def/ontomunicipio#millimolair)<br />[om:decisievert](http://opendata.caceres.es/def/ontomunicipio#decisievert)<br />[om:femtosteradian](http://opendata.caceres.es/def/ontomunicipio#femtosteradian)<br />[om:gigaparsec](http://opendata.caceres.es/def/ontomunicipio#gigaparsec)<br />[om:kilometre](http://opendata.caceres.es/def/ontomunicipio#kilometre)<br />[om:centikatal](http://opendata.caceres.es/def/ontomunicipio#centikatal)<br />[om:kilohenry](http://opendata.caceres.es/def/ontomunicipio#kilohenry)<br />[om:exaweber](http://opendata.caceres.es/def/ontomunicipio#exaweber)<br />[om:petakatal](http://opendata.caceres.es/def/ontomunicipio#petakatal)<br />[om:piconewton](http://opendata.caceres.es/def/ontomunicipio#piconewton)<br />[om:exacandela](http://opendata.caceres.es/def/ontomunicipio#exacandela)<br />[om:centivolt](http://opendata.caceres.es/def/ontomunicipio#centivolt)<br />[om:femtogram](http://opendata.caceres.es/def/ontomunicipio#femtogram)<br />[om:exabyte](http://opendata.caceres.es/def/ontomunicipio#exabyte)<br />[om:zeptomolair](http://opendata.caceres.es/def/ontomunicipio#zeptomolair)<br />[om:picosievert](http://opendata.caceres.es/def/ontomunicipio#picosievert)<br />[om:zettakelvin](http://opendata.caceres.es/def/ontomunicipio#zettakelvin)<br />[om:decakatal](http://opendata.caceres.es/def/ontomunicipio#decakatal)<br />[om:hectoweber](http://opendata.caceres.es/def/ontomunicipio#hectoweber)<br />[om:femtotesla](http://opendata.caceres.es/def/ontomunicipio#femtotesla)<br />[om:millinewton](http://opendata.caceres.es/def/ontomunicipio#millinewton)<br />[om:gigagram](http://opendata.caceres.es/def/ontomunicipio#gigagram)<br />[om:petawatt](http://opendata.caceres.es/def/ontomunicipio#petawatt)<br />[om:decaampere](http://opendata.caceres.es/def/ontomunicipio#decaampere)<br />[om:microjoule](http://opendata.caceres.es/def/ontomunicipio#microjoule)<br />[om:megaweber](http://opendata.caceres.es/def/ontomunicipio#megaweber)<br />[om:centisecond-Time](http://opendata.caceres.es/def/ontomunicipio#centisecond-Time)<br />[om:decavolt](http://opendata.caceres.es/def/ontomunicipio#decavolt)<br />[om:zettalitre](http://opendata.caceres.es/def/ontomunicipio#zettalitre)<br />[om:micromagnitude](http://opendata.caceres.es/def/ontomunicipio#micromagnitude)<br />[om:decihertz](http://opendata.caceres.es/def/ontomunicipio#decihertz)<br />[om:exbibit](http://opendata.caceres.es/def/ontomunicipio#exbibit)<br />[om:teralux](http://opendata.caceres.es/def/ontomunicipio#teralux)<br />[om:attokelvin](http://opendata.caceres.es/def/ontomunicipio#attokelvin)<br />[om:exaohm](http://opendata.caceres.es/def/ontomunicipio#exaohm)<br />[om:megahenry](http://opendata.caceres.es/def/ontomunicipio#megahenry)<br />[om:milliweber](http://opendata.caceres.es/def/ontomunicipio#milliweber)<br />[om:megagram](http://opendata.caceres.es/def/ontomunicipio#megagram)<br />[om:decimole](http://opendata.caceres.es/def/ontomunicipio#decimole)<br />[om:yottamolair](http://opendata.caceres.es/def/ontomunicipio#yottamolair)<br />[om:decanewton](http://opendata.caceres.es/def/ontomunicipio#decanewton)<br />[om:femtolitre](http://opendata.caceres.es/def/ontomunicipio#femtolitre)<br />[om:hectojoule](http://opendata.caceres.es/def/ontomunicipio#hectojoule)<br />[om:exahertz](http://opendata.caceres.es/def/ontomunicipio#exahertz)<br />[om:millilux](http://opendata.caceres.es/def/ontomunicipio#millilux)<br />[om:petabecquerel](http://opendata.caceres.es/def/ontomunicipio#petabecquerel)<br />[om:decikatal](http://opendata.caceres.es/def/ontomunicipio#decikatal)<br />[om:terabit](http://opendata.caceres.es/def/ontomunicipio#terabit)<br />[om:attotesla](http://opendata.caceres.es/def/ontomunicipio#attotesla)<br />[om:milligray](http://opendata.caceres.es/def/ontomunicipio#milligray)<br />[om:zeptohertz](http://opendata.caceres.es/def/ontomunicipio#zeptohertz)<br />[om:yottavolt](http://opendata.caceres.es/def/ontomunicipio#yottavolt)<br />[om:attopascal](http://opendata.caceres.es/def/ontomunicipio#attopascal)<br />[om:nanounifiedAtomicMassUnit](http://opendata.caceres.es/def/ontomunicipio#nanounifiedAtomicMassUnit)<br />[om:gigaampere](http://opendata.caceres.es/def/ontomunicipio#gigaampere)<br />[om:kiloelectronvolt](http://opendata.caceres.es/def/ontomunicipio#kiloelectronvolt)<br />[om:pebibyte](http://opendata.caceres.es/def/ontomunicipio#pebibyte)<br />[om:zettabyte](http://opendata.caceres.es/def/ontomunicipio#zettabyte)<br />[om:centikelvin](http://opendata.caceres.es/def/ontomunicipio#centikelvin)<br />[om:nanosiemens](http://opendata.caceres.es/def/ontomunicipio#nanosiemens)<br />[om:kilocoulomb](http://opendata.caceres.es/def/ontomunicipio#kilocoulomb)<br />[om:attomolair](http://opendata.caceres.es/def/ontomunicipio#attomolair)<br />[om:millifarad](http://opendata.caceres.es/def/ontomunicipio#millifarad)<br />[om:picofarad](http://opendata.caceres.es/def/ontomunicipio#picofarad)<br />[om:picogray](http://opendata.caceres.es/def/ontomunicipio#picogray)<br />[om:microsievert](http://opendata.caceres.es/def/ontomunicipio#microsievert)<br />[om:exasievert](http://opendata.caceres.es/def/ontomunicipio#exasievert)<br />[om:zettametre](http://opendata.caceres.es/def/ontomunicipio#zettametre)<br />[om:zeptoampere](http://opendata.caceres.es/def/ontomunicipio#zeptoampere)<br />[om:zettamole](http://opendata.caceres.es/def/ontomunicipio#zettamole)<br />[om:megamole](http://opendata.caceres.es/def/ontomunicipio#megamole)<br />[om:centitesla](http://opendata.caceres.es/def/ontomunicipio#centitesla)<br />[om:millikelvin](http://opendata.caceres.es/def/ontomunicipio#millikelvin)<br />[om:hectocoulomb](http://opendata.caceres.es/def/ontomunicipio#hectocoulomb)<br />[om:hectomole](http://opendata.caceres.es/def/ontomunicipio#hectomole)<br />[om:hectoampere](http://opendata.caceres.es/def/ontomunicipio#hectoampere)<br />[om:zeptokatal](http://opendata.caceres.es/def/ontomunicipio#zeptokatal)<br />[om:nanogray](http://opendata.caceres.es/def/ontomunicipio#nanogray)<br />[om:femtohertz](http://opendata.caceres.es/def/ontomunicipio#femtohertz)<br />[om:hectometre](http://opendata.caceres.es/def/ontomunicipio#hectometre)<br />[om:centilitre](http://opendata.caceres.es/def/ontomunicipio#centilitre)<br />[om:femtocandela](http://opendata.caceres.es/def/ontomunicipio#femtocandela)<br />[om:picopascal](http://opendata.caceres.es/def/ontomunicipio#picopascal)<br />[om:microcandela](http://opendata.caceres.es/def/ontomunicipio#microcandela)<br />[om:zebibyte](http://opendata.caceres.es/def/ontomunicipio#zebibyte)<br />[om:picovolt](http://opendata.caceres.es/def/ontomunicipio#picovolt)<br />[om:exanewton](http://opendata.caceres.es/def/ontomunicipio#exanewton)<br />[om:centilux](http://opendata.caceres.es/def/ontomunicipio#centilux)<br />[om:picoradian](http://opendata.caceres.es/def/ontomunicipio#picoradian)<br />[om:terajoule](http://opendata.caceres.es/def/ontomunicipio#terajoule)<br />[om:microkatal](http://opendata.caceres.es/def/ontomunicipio#microkatal)<br />[om:yoctogram](http://opendata.caceres.es/def/ontomunicipio#yoctogram)<br />[om:yottagray](http://opendata.caceres.es/def/ontomunicipio#yottagray)<br />[om:terasievert](http://opendata.caceres.es/def/ontomunicipio#terasievert)<br />[om:gigatesla](http://opendata.caceres.es/def/ontomunicipio#gigatesla)<br />[om:megasecond-Time](http://opendata.caceres.es/def/ontomunicipio#megasecond-Time)<br />[om:picocoulomb](http://opendata.caceres.es/def/ontomunicipio#picocoulomb)<br />[om:megavolt](http://opendata.caceres.es/def/ontomunicipio#megavolt)<br />[om:centiohm](http://opendata.caceres.es/def/ontomunicipio#centiohm)<br />[om:decimolair](http://opendata.caceres.es/def/ontomunicipio#decimolair)<br />[om:petabit](http://opendata.caceres.es/def/ontomunicipio#petabit)<br />[om:zettamolair](http://opendata.caceres.es/def/ontomunicipio#zettamolair)<br />[om:petaweber](http://opendata.caceres.es/def/ontomunicipio#petaweber)<br />[om:exakatal](http://opendata.caceres.es/def/ontomunicipio#exakatal)<br />[om:micromolair](http://opendata.caceres.es/def/ontomunicipio#micromolair)<br />[om:zettanewton](http://opendata.caceres.es/def/ontomunicipio#zettanewton)<br />[om:kiloweber](http://opendata.caceres.es/def/ontomunicipio#kiloweber)<br />[om:centigray](http://opendata.caceres.es/def/ontomunicipio#centigray)<br />[om:millimole](http://opendata.caceres.es/def/ontomunicipio#millimole)<br />[om:zeptolitre](http://opendata.caceres.es/def/ontomunicipio#zeptolitre)<br />[om:milligauss](http://opendata.caceres.es/def/ontomunicipio#milligauss)<br />[om:zettaweber](http://opendata.caceres.es/def/ontomunicipio#zettaweber)<br />[om:decafarad](http://opendata.caceres.es/def/ontomunicipio#decafarad)<br />[om:attoradian](http://opendata.caceres.es/def/ontomunicipio#attoradian)<br />[om:terabyte](http://opendata.caceres.es/def/ontomunicipio#terabyte)<br />[om:picodegreeCelsius](http://opendata.caceres.es/def/ontomunicipio#picodegreeCelsius)<br />[om:decisiemens](http://opendata.caceres.es/def/ontomunicipio#decisiemens)<br />[om:attoweber](http://opendata.caceres.es/def/ontomunicipio#attoweber)<br />[om:picolitre](http://opendata.caceres.es/def/ontomunicipio#picolitre)<br />[om:picomolair](http://opendata.caceres.es/def/ontomunicipio#picomolair)<br />[om:petalux](http://opendata.caceres.es/def/ontomunicipio#petalux)<br />[om:exahenry](http://opendata.caceres.es/def/ontomunicipio#exahenry)<br />[om:petamole](http://opendata.caceres.es/def/ontomunicipio#petamole)<br />[om:megalux](http://opendata.caceres.es/def/ontomunicipio#megalux)<br />[om:picogram](http://opendata.caceres.es/def/ontomunicipio#picogram)<br />[om:microweber](http://opendata.caceres.es/def/ontomunicipio#microweber)<br />[om:hectofarad](http://opendata.caceres.es/def/ontomunicipio#hectofarad)<br />[om:decalux](http://opendata.caceres.es/def/ontomunicipio#decalux)<br />[om:yottatesla](http://opendata.caceres.es/def/ontomunicipio#yottatesla)<br />[om:picobecquerel](http://opendata.caceres.es/def/ontomunicipio#picobecquerel)<br />[om:mebibit](http://opendata.caceres.es/def/ontomunicipio#mebibit)<br />[om:picoampere](http://opendata.caceres.es/def/ontomunicipio#picoampere)<br />[om:tebibyte](http://opendata.caceres.es/def/ontomunicipio#tebibyte)<br />[om:terapascal](http://opendata.caceres.es/def/ontomunicipio#terapascal)<br />[om:zettapascal](http://opendata.caceres.es/def/ontomunicipio#zettapascal)<br />[om:gigamolair](http://opendata.caceres.es/def/ontomunicipio#gigamolair)<br />[om:femtoradian](http://opendata.caceres.es/def/ontomunicipio#femtoradian)<br />[om:nanocandela](http://opendata.caceres.es/def/ontomunicipio#nanocandela)<br />[om:terafarad](http://opendata.caceres.es/def/ontomunicipio#terafarad)<br />[om:microsiemens](http://opendata.caceres.es/def/ontomunicipio#microsiemens)<br />[om:millitesla](http://opendata.caceres.es/def/ontomunicipio#millitesla)<br />[om:centibecquerel](http://opendata.caceres.es/def/ontomunicipio#centibecquerel)<br />[om:nanogram](http://opendata.caceres.es/def/ontomunicipio#nanogram)<br />[om:megaampere](http://opendata.caceres.es/def/ontomunicipio#megaampere)<br />[om:megakelvin](http://opendata.caceres.es/def/ontomunicipio#megakelvin)<br />[om:millidegreeCelsius](http://opendata.caceres.es/def/ontomunicipio#millidegreeCelsius)<br />[om:zeptohenry](http://opendata.caceres.es/def/ontomunicipio#zeptohenry)<br />[om:nanohertz](http://opendata.caceres.es/def/ontomunicipio#nanohertz)<br />[om:megaeuro](http://opendata.caceres.es/def/ontomunicipio#megaeuro)<br />[om:hectosiemens](http://opendata.caceres.es/def/ontomunicipio#hectosiemens)<br />[om:yottabyte](http://opendata.caceres.es/def/ontomunicipio#yottabyte)<br />[om:femtokelvin](http://opendata.caceres.es/def/ontomunicipio#femtokelvin)<br />[om:attonewton](http://opendata.caceres.es/def/ontomunicipio#attonewton)<br />[om:zeptobecquerel](http://opendata.caceres.es/def/ontomunicipio#zeptobecquerel)<br />[om:femtolumen](http://opendata.caceres.es/def/ontomunicipio#femtolumen)<br />[om:examole](http://opendata.caceres.es/def/ontomunicipio#examole)<br />[om:yoctosievert](http://opendata.caceres.es/def/ontomunicipio#yoctosievert)<br />[om:zebibit](http://opendata.caceres.es/def/ontomunicipio#zebibit)<br />[om:decilumen](http://opendata.caceres.es/def/ontomunicipio#decilumen)<br />[om:hectonewton](http://opendata.caceres.es/def/ontomunicipio#hectonewton)<br />[om:picometre](http://opendata.caceres.es/def/ontomunicipio#picometre)<br />[om:gibibyte](http://opendata.caceres.es/def/ontomunicipio#gibibyte)<br />[om:kilonewton](http://opendata.caceres.es/def/ontomunicipio#kilonewton)<br />[om:attosievert](http://opendata.caceres.es/def/ontomunicipio#attosievert)<br />[om:decisteradian](http://opendata.caceres.es/def/ontomunicipio#decisteradian)<br />[om:decaweber](http://opendata.caceres.es/def/ontomunicipio#decaweber)<br />[om:megacandela](http://opendata.caceres.es/def/ontomunicipio#megacandela)<br />[om:decicandela](http://opendata.caceres.es/def/ontomunicipio#decicandela)<br />[om:attogray](http://opendata.caceres.es/def/ontomunicipio#attogray)<br />[om:millikatal](http://opendata.caceres.es/def/ontomunicipio#millikatal)<br />[om:gigawatt](http://opendata.caceres.es/def/ontomunicipio#gigawatt)<br />[om:hectotesla](http://opendata.caceres.es/def/ontomunicipio#hectotesla)<br />[om:microgray](http://opendata.caceres.es/def/ontomunicipio#microgray)<br />[om:decalitre](http://opendata.caceres.es/def/ontomunicipio#decalitre)<br />[om:picowatt](http://opendata.caceres.es/def/ontomunicipio#picowatt)<br />[om:kilopascal](http://opendata.caceres.es/def/ontomunicipio#kilopascal)<br />[om:decitesla](http://opendata.caceres.es/def/ontomunicipio#decitesla)<br />[om:gigalux](http://opendata.caceres.es/def/ontomunicipio#gigalux)<br />[om:terakelvin](http://opendata.caceres.es/def/ontomunicipio#terakelvin)<br />[om:attolitre](http://opendata.caceres.es/def/ontomunicipio#attolitre)<br />[om:milliwatt](http://opendata.caceres.es/def/ontomunicipio#milliwatt)<br />[om:nanojoule](http://opendata.caceres.es/def/ontomunicipio#nanojoule)<br />[om:zettacoulomb](http://opendata.caceres.es/def/ontomunicipio#zettacoulomb)<br />[om:gigakelvin](http://opendata.caceres.es/def/ontomunicipio#gigakelvin)<br />[om:gigasiemens](http://opendata.caceres.es/def/ontomunicipio#gigasiemens)<br />[om:yoctofarad](http://opendata.caceres.es/def/ontomunicipio#yoctofarad)<br />[om:millihenry](http://opendata.caceres.es/def/ontomunicipio#millihenry)<br />[om:terabecquerel](http://opendata.caceres.es/def/ontomunicipio#terabecquerel)<br />[om:megaerg](http://opendata.caceres.es/def/ontomunicipio#megaerg)<br />[om:nanoradian](http://opendata.caceres.es/def/ontomunicipio#nanoradian)<br />[om:zettaampere](http://opendata.caceres.es/def/ontomunicipio#zettaampere)<br />[om:yottanewton](http://opendata.caceres.es/def/ontomunicipio#yottanewton)<br />[om:zettagram](http://opendata.caceres.es/def/ontomunicipio#zettagram)<br />[om:attosteradian](http://opendata.caceres.es/def/ontomunicipio#attosteradian)<br />[om:decagram](http://opendata.caceres.es/def/ontomunicipio#decagram)<br />[om:decamole](http://opendata.caceres.es/def/ontomunicipio#decamole)<br />[om:decifarad](http://opendata.caceres.es/def/ontomunicipio#decifarad)<br />[om:microradian](http://opendata.caceres.es/def/ontomunicipio#microradian)<br />[om:femtogray](http://opendata.caceres.es/def/ontomunicipio#femtogray)<br />[om:megakatal](http://opendata.caceres.es/def/ontomunicipio#megakatal)<br />[om:teralumen](http://opendata.caceres.es/def/ontomunicipio#teralumen)<br />[om:microbecquerel](http://opendata.caceres.es/def/ontomunicipio#microbecquerel)<br />[om:zettasecond-Time](http://opendata.caceres.es/def/ontomunicipio#zettasecond-Time)<br />[om:kilowatt](http://opendata.caceres.es/def/ontomunicipio#kilowatt)<br />[om:femtoohm](http://opendata.caceres.es/def/ontomunicipio#femtoohm)<br />[om:milliampere](http://opendata.caceres.es/def/ontomunicipio#milliampere)<br />[om:hectowatt](http://opendata.caceres.es/def/ontomunicipio#hectowatt)<br />[om:yottahenry](http://opendata.caceres.es/def/ontomunicipio#yottahenry)<br />[om:decigram](http://opendata.caceres.es/def/ontomunicipio#decigram)<br />[om:zettalux](http://opendata.caceres.es/def/ontomunicipio#zettalux)<br />[om:kilojoule](http://opendata.caceres.es/def/ontomunicipio#kilojoule)<br />[om:yoctosiemens](http://opendata.caceres.es/def/ontomunicipio#yoctosiemens)<br />[om:attofarad](http://opendata.caceres.es/def/ontomunicipio#attofarad)<br />[om:yoctoradian](http://opendata.caceres.es/def/ontomunicipio#yoctoradian)<br />[om:hectobecquerel](http://opendata.caceres.es/def/ontomunicipio#hectobecquerel)<br />[om:decalumen](http://opendata.caceres.es/def/ontomunicipio#decalumen)<br />[om:nanokatal](http://opendata.caceres.es/def/ontomunicipio#nanokatal)<br />[om:microfarad](http://opendata.caceres.es/def/ontomunicipio#microfarad)<br />[om:hectosievert](http://opendata.caceres.es/def/ontomunicipio#hectosievert)<br />[om:microlitre](http://opendata.caceres.es/def/ontomunicipio#microlitre)<br />[om:picokatal](http://opendata.caceres.es/def/ontomunicipio#picokatal)<br />[om:petasecond-Time](http://opendata.caceres.es/def/ontomunicipio#petasecond-Time)<br />[om:petalumen](http://opendata.caceres.es/def/ontomunicipio#petalumen)<br />[om:kilosiemens](http://opendata.caceres.es/def/ontomunicipio#kilosiemens)<br />[om:teranewton](http://opendata.caceres.es/def/ontomunicipio#teranewton)<br />[om:teraampere](http://opendata.caceres.es/def/ontomunicipio#teraampere)<br />[om:millisecond-Angle](http://opendata.caceres.es/def/ontomunicipio#millisecond-Angle)<br />[om:centiweber](http://opendata.caceres.es/def/ontomunicipio#centiweber)<br />[om:gigayear](http://opendata.caceres.es/def/ontomunicipio#gigayear)<br />[om:attogram](http://opendata.caceres.es/def/ontomunicipio#attogram)<br />[om:microohm](http://opendata.caceres.es/def/ontomunicipio#microohm)<br />[om:decibar](http://opendata.caceres.es/def/ontomunicipio#decibar)<br />[om:teracandela](http://opendata.caceres.es/def/ontomunicipio#teracandela)<br />[om:attowatt](http://opendata.caceres.es/def/ontomunicipio#attowatt)<br />[om:zeptosievert](http://opendata.caceres.es/def/ontomunicipio#zeptosievert)<br />[om:centicoulomb](http://opendata.caceres.es/def/ontomunicipio#centicoulomb)<br />[om:zettavolt](http://opendata.caceres.es/def/ontomunicipio#zettavolt)<br />[om:kilobit](http://opendata.caceres.es/def/ontomunicipio#kilobit)<br />[om:microbar](http://opendata.caceres.es/def/ontomunicipio#microbar)<br />[om:zeptoohm](http://opendata.caceres.es/def/ontomunicipio#zeptoohm)<br />[om:zettabit](http://opendata.caceres.es/def/ontomunicipio#zettabit)<br />[om:petaampere](http://opendata.caceres.es/def/ontomunicipio#petaampere)<br />[om:picolumen](http://opendata.caceres.es/def/ontomunicipio#picolumen)<br />[om:megawatt](http://opendata.caceres.es/def/ontomunicipio#megawatt)<br />[om:zettasievert](http://opendata.caceres.es/def/ontomunicipio#zettasievert)<br />[om:centisievert](http://opendata.caceres.es/def/ontomunicipio#centisievert)<br />[om:exalitre](http://opendata.caceres.es/def/ontomunicipio#exalitre)<br />[om:kilotesla](http://opendata.caceres.es/def/ontomunicipio#kilotesla)<br />[om:megasiemens](http://opendata.caceres.es/def/ontomunicipio#megasiemens)<br />[om:teramolair](http://opendata.caceres.es/def/ontomunicipio#teramolair)<br />[om:gigalumen](http://opendata.caceres.es/def/ontomunicipio#gigalumen)<br />[om:centisiemens](http://opendata.caceres.es/def/ontomunicipio#centisiemens)<br />[om:teratesla](http://opendata.caceres.es/def/ontomunicipio#teratesla)<br />[om:deciampere](http://opendata.caceres.es/def/ontomunicipio#deciampere)<br />[om:zeptogray](http://opendata.caceres.es/def/ontomunicipio#zeptogray)<br />[om:femtolux](http://opendata.caceres.es/def/ontomunicipio#femtolux)<br />[om:picosecond-Time](http://opendata.caceres.es/def/ontomunicipio#picosecond-Time)<br />[om:exalumen](http://opendata.caceres.es/def/ontomunicipio#exalumen)<br />[om:decahertz](http://opendata.caceres.es/def/ontomunicipio#decahertz)<br />[om:gigakatal](http://opendata.caceres.es/def/ontomunicipio#gigakatal)<br />[om:microlux](http://opendata.caceres.es/def/ontomunicipio#microlux)<br />[om:yoctopascal](http://opendata.caceres.es/def/ontomunicipio#yoctopascal)<br />[om:exabecquerel](http://opendata.caceres.es/def/ontomunicipio#exabecquerel)<br />[om:yobibit](http://opendata.caceres.es/def/ontomunicipio#yobibit)<br />[om:picojoule](http://opendata.caceres.es/def/ontomunicipio#picojoule)<br />[om:gigacandela](http://opendata.caceres.es/def/ontomunicipio#gigacandela)<br />[om:centidegreeCelsius](http://opendata.caceres.es/def/ontomunicipio#centidegreeCelsius)<br />[om:femtojoule](http://opendata.caceres.es/def/ontomunicipio#femtojoule)<br />[om:femtometre](http://opendata.caceres.es/def/ontomunicipio#femtometre)<br />[om:microhertz](http://opendata.caceres.es/def/ontomunicipio#microhertz)<br />[om:decikelvin](http://opendata.caceres.es/def/ontomunicipio#decikelvin)<br />[om:kilotonne](http://opendata.caceres.es/def/ontomunicipio#kilotonne)<br />[om:femtoweber](http://opendata.caceres.es/def/ontomunicipio#femtoweber)<br />[om:teravolt](http://opendata.caceres.es/def/ontomunicipio#teravolt)<br />[om:gigaweber](http://opendata.caceres.es/def/ontomunicipio#gigaweber)<br />[om:millicandela](http://opendata.caceres.es/def/ontomunicipio#millicandela)<br />[om:megalumen](http://opendata.caceres.es/def/ontomunicipio#megalumen)<br />[om:decicoulomb](http://opendata.caceres.es/def/ontomunicipio#decicoulomb)<br />[om:yottaampere](http://opendata.caceres.es/def/ontomunicipio#yottaampere)<br />[om:kilolitre](http://opendata.caceres.es/def/ontomunicipio#kilolitre)<br />[om:yottacoulomb](http://opendata.caceres.es/def/ontomunicipio#yottacoulomb)<br />[om:decijoule](http://opendata.caceres.es/def/ontomunicipio#decijoule)<br />[om:centisteradian](http://opendata.caceres.es/def/ontomunicipio#centisteradian)<br />[om:exametre](http://opendata.caceres.es/def/ontomunicipio#exametre)<br />[om:femtonewton](http://opendata.caceres.es/def/ontomunicipio#femtonewton)<br />[om:attosiemens](http://opendata.caceres.es/def/ontomunicipio#attosiemens)<br />[om:kilovolt](http://opendata.caceres.es/def/ontomunicipio#kilovolt)<br />[om:nanonewton](http://opendata.caceres.es/def/ontomunicipio#nanonewton)<br />[om:exaampere](http://opendata.caceres.es/def/ontomunicipio#exaampere)<br />[om:millisteradian](http://opendata.caceres.es/def/ontomunicipio#millisteradian)<br />[om:yottacandela](http://opendata.caceres.es/def/ontomunicipio#yottacandela)<br />[om:hectogram](http://opendata.caceres.es/def/ontomunicipio#hectogram)<br />[om:megatonne](http://opendata.caceres.es/def/ontomunicipio#megatonne)<br />[om:zettaohm](http://opendata.caceres.es/def/ontomunicipio#zettaohm)<br />[om:petamolair](http://opendata.caceres.es/def/ontomunicipio#petamolair)<br />[om:terahertz](http://opendata.caceres.es/def/ontomunicipio#terahertz)<br />[om:hectogray](http://opendata.caceres.es/def/ontomunicipio#hectogray)<br />[om:zeptoweber](http://opendata.caceres.es/def/ontomunicipio#zeptoweber)<br />[om:zeptometre](http://opendata.caceres.es/def/ontomunicipio#zeptometre)<br />[om:exagram](http://opendata.caceres.es/def/ontomunicipio#exagram)<br />[om:teracoulomb](http://opendata.caceres.es/def/ontomunicipio#teracoulomb)<br />[om:gigajoule](http://opendata.caceres.es/def/ontomunicipio#gigajoule)<br />[om:kilolux](http://opendata.caceres.es/def/ontomunicipio#kilolux)<br />[om:attobecquerel](http://opendata.caceres.es/def/ontomunicipio#attobecquerel)<br />[om:teraweber](http://opendata.caceres.es/def/ontomunicipio#teraweber)<br />[om:nanotesla](http://opendata.caceres.es/def/ontomunicipio#nanotesla)<br />[om:megatesla](http://opendata.caceres.es/def/ontomunicipio#megatesla)<br />[om:hectohenry](http://opendata.caceres.es/def/ontomunicipio#hectohenry)<br />[om:nanopascal](http://opendata.caceres.es/def/ontomunicipio#nanopascal)<br />[om:nanolitre](http://opendata.caceres.es/def/ontomunicipio#nanolitre)<br />[om:exajoule](http://opendata.caceres.es/def/ontomunicipio#exajoule)<br />[om:yoctomole](http://opendata.caceres.es/def/ontomunicipio#yoctomole)<br />[om:nanoohm](http://opendata.caceres.es/def/ontomunicipio#nanoohm)<br />[om:micromole](http://opendata.caceres.es/def/ontomunicipio#micromole)<br />[om:megaparsec](http://opendata.caceres.es/def/ontomunicipio#megaparsec)<br />[om:megapascal](http://opendata.caceres.es/def/ontomunicipio#megapascal)<br />[om:microsteradian](http://opendata.caceres.es/def/ontomunicipio#microsteradian)<br />[om:centicandela](http://opendata.caceres.es/def/ontomunicipio#centicandela)<br />[om:nanometre](http://opendata.caceres.es/def/ontomunicipio#nanometre)<br />[om:yoctosteradian](http://opendata.caceres.es/def/ontomunicipio#yoctosteradian)<br />[om:megagray](http://opendata.caceres.es/def/ontomunicipio#megagray)<br />[om:gibibit](http://opendata.caceres.es/def/ontomunicipio#gibibit)<br />[om:giganewton](http://opendata.caceres.es/def/ontomunicipio#giganewton)<br />[om:femtocoulomb](http://opendata.caceres.es/def/ontomunicipio#femtocoulomb)<br />[om:megafarad](http://opendata.caceres.es/def/ontomunicipio#megafarad)<br />[om:gigamole](http://opendata.caceres.es/def/ontomunicipio#gigamole)<br />[om:attojoule](http://opendata.caceres.es/def/ontomunicipio#attojoule)<br />[om:yoctonewton](http://opendata.caceres.es/def/ontomunicipio#yoctonewton)<br />[om:zettabecquerel](http://opendata.caceres.es/def/ontomunicipio#zettabecquerel)<br />[om:petametre](http://opendata.caceres.es/def/ontomunicipio#petametre)<br />[om:yottasecond-Time](http://opendata.caceres.es/def/ontomunicipio#yottasecond-Time)<br />[om:zeptosiemens](http://opendata.caceres.es/def/ontomunicipio#zeptosiemens)<br />[om:nanocoulomb](http://opendata.caceres.es/def/ontomunicipio#nanocoulomb)<br />[om:femtomole](http://opendata.caceres.es/def/ontomunicipio#femtomole)<br />[om:yottamole](http://opendata.caceres.es/def/ontomunicipio#yottamole)<br />[om:millimagnitude](http://opendata.caceres.es/def/ontomunicipio#millimagnitude)<br />[om:zettahertz](http://opendata.caceres.es/def/ontomunicipio#zettahertz)<br />[om:terametre](http://opendata.caceres.es/def/ontomunicipio#terametre)<br />[om:picomole](http://opendata.caceres.es/def/ontomunicipio#picomole)<br />[om:teraohm](http://opendata.caceres.es/def/ontomunicipio#teraohm)<br />[om:microvolt](http://opendata.caceres.es/def/ontomunicipio#microvolt)<br />[om:attosecond-Time](http://opendata.caceres.es/def/ontomunicipio#attosecond-Time)<br />[om:gigabecquerel](http://opendata.caceres.es/def/ontomunicipio#gigabecquerel)<br />[om:decilux](http://opendata.caceres.es/def/ontomunicipio#decilux)<br />[om:kilobecquerel](http://opendata.caceres.es/def/ontomunicipio#kilobecquerel)<br />[om:yottahertz](http://opendata.caceres.es/def/ontomunicipio#yottahertz)<br />[om:kiloampere](http://opendata.caceres.es/def/ontomunicipio#kiloampere)<br />[om:terawatt](http://opendata.caceres.es/def/ontomunicipio#terawatt)<br />[om:examolair](http://opendata.caceres.es/def/ontomunicipio#examolair)<br />[om:yottalumen](http://opendata.caceres.es/def/ontomunicipio#yottalumen)<br />[om:femtodegreeCelsius](http://opendata.caceres.es/def/ontomunicipio#femtodegreeCelsius)<br />[om:gigapascal](http://opendata.caceres.es/def/ontomunicipio#gigapascal)<br />[om:centifarad](http://opendata.caceres.es/def/ontomunicipio#centifarad)<br />[om:decipascal](http://opendata.caceres.es/def/ontomunicipio#decipascal)<br />[om:gigaelectronvolt](http://opendata.caceres.es/def/ontomunicipio#gigaelectronvolt)<br />[om:femtofarad](http://opendata.caceres.es/def/ontomunicipio#femtofarad)<br />[om:nanofarad](http://opendata.caceres.es/def/ontomunicipio#nanofarad)<br />[om:gigasecond-Time](http://opendata.caceres.es/def/ontomunicipio#gigasecond-Time)<br />[om:nanolumen](http://opendata.caceres.es/def/ontomunicipio#nanolumen)<br />[om:kilogram](http://opendata.caceres.es/def/ontomunicipio#kilogram)<br />[om:kilobyte](http://opendata.caceres.es/def/ontomunicipio#kilobyte)<br />[om:millisievert](http://opendata.caceres.es/def/ontomunicipio#millisievert)<br />[om:yottasiemens](http://opendata.caceres.es/def/ontomunicipio#yottasiemens)<br />[om:zeptotesla](http://opendata.caceres.es/def/ontomunicipio#zeptotesla)<br />[om:gigahertz](http://opendata.caceres.es/def/ontomunicipio#gigahertz)<br />[om:nanosecond-Time](http://opendata.caceres.es/def/ontomunicipio#nanosecond-Time)<br />[om:attolumen](http://opendata.caceres.es/def/ontomunicipio#attolumen)<br />[om:attoampere](http://opendata.caceres.es/def/ontomunicipio#attoampere)<br />[om:zettajoule](http://opendata.caceres.es/def/ontomunicipio#zettajoule)<br />[om:yottalitre](http://opendata.caceres.es/def/ontomunicipio#yottalitre)<br />[om:nanomolair](http://opendata.caceres.es/def/ontomunicipio#nanomolair)<br />[om:yottalux](http://opendata.caceres.es/def/ontomunicipio#yottalux)<br />[om:yoctoweber](http://opendata.caceres.es/def/ontomunicipio#yoctoweber)<br />[om:femtokatal](http://opendata.caceres.es/def/ontomunicipio#femtokatal)<br />[om:picotesla](http://opendata.caceres.es/def/ontomunicipio#picotesla)<br />[om:decigray](http://opendata.caceres.es/def/ontomunicipio#decigray)<br />[om:microkelvin](http://opendata.caceres.es/def/ontomunicipio#microkelvin)<br />[om:millicoulomb](http://opendata.caceres.es/def/ontomunicipio#millicoulomb)<br />[om:decinewton](http://opendata.caceres.es/def/ontomunicipio#decinewton)<br />[om:kilosecond-Time](http://opendata.caceres.es/def/ontomunicipio#kilosecond-Time)<br />[om:attocoulomb](http://opendata.caceres.es/def/ontomunicipio#attocoulomb)<br />[om:decilitre](http://opendata.caceres.es/def/ontomunicipio#decilitre)<br />[om:picohertz](http://opendata.caceres.es/def/ontomunicipio#picohertz)<br />[om:exalux](http://opendata.caceres.es/def/ontomunicipio#exalux)<br />[om:centipascal](http://opendata.caceres.es/def/ontomunicipio#centipascal)<br />[om:picocandela](http://opendata.caceres.es/def/ontomunicipio#picocandela)<br />[om:gigagray](http://opendata.caceres.es/def/ontomunicipio#gigagray)<br />[om:megasievert](http://opendata.caceres.es/def/ontomunicipio#megasievert)<br />[om:exavolt](http://opendata.caceres.es/def/ontomunicipio#exavolt)<br />[om:petanewton](http://opendata.caceres.es/def/ontomunicipio#petanewton)<br />[om:nanolux](http://opendata.caceres.es/def/ontomunicipio#nanolux)<br />[om:yottawatt](http://opendata.caceres.es/def/ontomunicipio#yottawatt)<br />[om:petajoule](http://opendata.caceres.es/def/ontomunicipio#petajoule)<br />[om:yottasievert](http://opendata.caceres.es/def/ontomunicipio#yottasievert)<br />[om:nanohenry](http://opendata.caceres.es/def/ontomunicipio#nanohenry)<br />[om:zeptowatt](http://opendata.caceres.es/def/ontomunicipio#zeptowatt)<br />[om:yoctobecquerel](http://opendata.caceres.es/def/ontomunicipio#yoctobecquerel)<br />[om:zeptosecond-Time](http://opendata.caceres.es/def/ontomunicipio#zeptosecond-Time)<br />[om:kilokelvin](http://opendata.caceres.es/def/ontomunicipio#kilokelvin)<br />[om:megamolair](http://opendata.caceres.es/def/ontomunicipio#megamolair)<br />[om:decawatt](http://opendata.caceres.es/def/ontomunicipio#decawatt)<br />[om:centimolair](http://opendata.caceres.es/def/ontomunicipio#centimolair)<br />[om:hectare](http://opendata.caceres.es/def/ontomunicipio#hectare)<br />[om:zeptojoule](http://opendata.caceres.es/def/ontomunicipio#zeptojoule)<br />[om:kilokatal](http://opendata.caceres.es/def/ontomunicipio#kilokatal)<br />[om:kilocandela](http://opendata.caceres.es/def/ontomunicipio#kilocandela)<br />[om:decisecond-Time](http://opendata.caceres.es/def/ontomunicipio#decisecond-Time)<br />[om:decapascal](http://opendata.caceres.es/def/ontomunicipio#decapascal)<br />[om:zettacandela](http://opendata.caceres.es/def/ontomunicipio#zettacandela)<br />[om:yoctolux](http://opendata.caceres.es/def/ontomunicipio#yoctolux)<br />[om:microcoulomb](http://opendata.caceres.es/def/ontomunicipio#microcoulomb)<br />[om:millijoule](http://opendata.caceres.es/def/ontomunicipio#millijoule)<br />[om:millipascal](http://opendata.caceres.es/def/ontomunicipio#millipascal)<br />[om:petapascal](http://opendata.caceres.es/def/ontomunicipio#petapascal)<br />[om:femtowatt](http://opendata.caceres.es/def/ontomunicipio#femtowatt)<br />[om:meganewton](http://opendata.caceres.es/def/ontomunicipio#meganewton)<br />[om:exabit](http://opendata.caceres.es/def/ontomunicipio#exabit)<br />[om:yoctovolt](http://opendata.caceres.es/def/ontomunicipio#yoctovolt)<br />[om:microhenry](http://opendata.caceres.es/def/ontomunicipio#microhenry)<br />[om:micrometre](http://opendata.caceres.es/def/ontomunicipio#micrometre)<br />[om:nanokelvin](http://opendata.caceres.es/def/ontomunicipio#nanokelvin)<br />[om:zeptosteradian](http://opendata.caceres.es/def/ontomunicipio#zeptosteradian)<br />[om:petagray](http://opendata.caceres.es/def/ontomunicipio#petagray)<br />[om:exagray](http://opendata.caceres.es/def/ontomunicipio#exagray)<br />[om:hectomolair](http://opendata.caceres.es/def/ontomunicipio#hectomolair)<br />[om:deciwatt](http://opendata.caceres.es/def/ontomunicipio#deciwatt)<br />[om:megohm](http://opendata.caceres.es/def/ontomunicipio#megohm)<br />[om:nanowatt](http://opendata.caceres.es/def/ontomunicipio#nanowatt)<br />[om:decihenry](http://opendata.caceres.es/def/ontomunicipio#decihenry)<br />[om:nanobecquerel](http://opendata.caceres.es/def/ontomunicipio#nanobecquerel)<br />[om:petasievert](http://opendata.caceres.es/def/ontomunicipio#petasievert)<br />[om:milliohm](http://opendata.caceres.es/def/ontomunicipio#milliohm)<br />[om:microampere](http://opendata.caceres.es/def/ontomunicipio#microampere)<br />[om:yoctohertz](http://opendata.caceres.es/def/ontomunicipio#yoctohertz)<br />[om:petagram](http://opendata.caceres.es/def/ontomunicipio#petagram)<br />[om:microlumen](http://opendata.caceres.es/def/ontomunicipio#microlumen)<br />[om:yottafarad](http://opendata.caceres.es/def/ontomunicipio#yottafarad)<br />[om:nanosteradian](http://opendata.caceres.es/def/ontomunicipio#nanosteradian)<br />[om:attometre](http://opendata.caceres.es/def/ontomunicipio#attometre)<br />[om:megacoulomb](http://opendata.caceres.es/def/ontomunicipio#megacoulomb)<br />[om:decidegreeCelsius](http://opendata.caceres.es/def/ontomunicipio#decidegreeCelsius)<br />[om:microwatt](http://opendata.caceres.es/def/ontomunicipio#microwatt)<br />[om:yoctomolair](http://opendata.caceres.es/def/ontomunicipio#yoctomolair)<br />[om:yottaweber](http://opendata.caceres.es/def/ontomunicipio#yottaweber)<br />[om:yottaohm](http://opendata.caceres.es/def/ontomunicipio#yottaohm)<br />[om:millihertz](http://opendata.caceres.es/def/ontomunicipio#millihertz)<br />[om:yottabecquerel](http://opendata.caceres.es/def/ontomunicipio#yottabecquerel)<br />[om:hectoohm](http://opendata.caceres.es/def/ontomunicipio#hectoohm)<br />[om:zeptopascal](http://opendata.caceres.es/def/ontomunicipio#zeptopascal)<br />[om:nanosievert](http://opendata.caceres.es/def/ontomunicipio#nanosievert)<br />[om:gigalitre](http://opendata.caceres.es/def/ontomunicipio#gigalitre)<br />[om:attohenry](http://opendata.caceres.es/def/ontomunicipio#attohenry)<br />[om:millisiemens](http://opendata.caceres.es/def/ontomunicipio#millisiemens)<br />[om:deciohm](http://opendata.caceres.es/def/ontomunicipio#deciohm)<br />[om:gigafarad](http://opendata.caceres.es/def/ontomunicipio#gigafarad)<br />[om:mebibyte](http://opendata.caceres.es/def/ontomunicipio#mebibyte)<br />[om:centiare](http://opendata.caceres.es/def/ontomunicipio#centiare)<br />[om:centinewton](http://opendata.caceres.es/def/ontomunicipio#centinewton)<br />[om:gigabit](http://opendata.caceres.es/def/ontomunicipio#gigabit)<br />[om:exbibyte](http://opendata.caceres.es/def/ontomunicipio#exbibyte)<br />[om:femtosiemens](http://opendata.caceres.es/def/ontomunicipio#femtosiemens)<br />[om:picolux](http://opendata.caceres.es/def/ontomunicipio#picolux)<br />[om:centihertz](http://opendata.caceres.es/def/ontomunicipio#centihertz)<br />[om:centigram](http://opendata.caceres.es/def/ontomunicipio#centigram)<br />[om:megametre](http://opendata.caceres.es/def/ontomunicipio#megametre)<br />[om:decamolair](http://opendata.caceres.es/def/ontomunicipio#decamolair)<br />[om:attoohm](http://opendata.caceres.es/def/ontomunicipio#attoohm)<br />[om:megaelectronvolt](http://opendata.caceres.es/def/ontomunicipio#megaelectronvolt)<br />[om:attodegreeCelsius](http://opendata.caceres.es/def/ontomunicipio#attodegreeCelsius)<br />[om:exasecond-Time](http://opendata.caceres.es/def/ontomunicipio#exasecond-Time)<br />[om:teragray](http://opendata.caceres.es/def/ontomunicipio#teragray)<br />[om:teragram](http://opendata.caceres.es/def/ontomunicipio#teragram)<br />[om:gigaohm](http://opendata.caceres.es/def/ontomunicipio#gigaohm)<br />[om:picoohm](http://opendata.caceres.es/def/ontomunicipio#picoohm)<br />[om:zettatesla](http://opendata.caceres.es/def/ontomunicipio#zettatesla)<br />[om:yottapascal](http://opendata.caceres.es/def/ontomunicipio#yottapascal)<br />[om:yoctometre](http://opendata.caceres.es/def/ontomunicipio#yoctometre)<br />[om:megabecquerel](http://opendata.caceres.es/def/ontomunicipio#megabecquerel)<br />[om:yottakatal](http://opendata.caceres.es/def/ontomunicipio#yottakatal)<br />[om:decivolt](http://opendata.caceres.es/def/ontomunicipio#decivolt)<br />[om:decakelvin](http://opendata.caceres.es/def/ontomunicipio#decakelvin)<br />[om:centiwatt](http://opendata.caceres.es/def/ontomunicipio#centiwatt)<br />[om:attocandela](http://opendata.caceres.es/def/ontomunicipio#attocandela)<br />[om:megabit](http://opendata.caceres.es/def/ontomunicipio#megabit)<br />[om:millibecquerel](http://opendata.caceres.es/def/ontomunicipio#millibecquerel)<br />[om:petalitre](http://opendata.caceres.es/def/ontomunicipio#petalitre)<br />[om:exafarad](http://opendata.caceres.es/def/ontomunicipio#exafarad)<br />[om:yottagram](http://opendata.caceres.es/def/ontomunicipio#yottagram)<br />[om:zettahenry](http://opendata.caceres.es/def/ontomunicipio#zettahenry)<br />[om:zeptolumen](http://opendata.caceres.es/def/ontomunicipio#zeptolumen)<br />[om:picohenry](http://opendata.caceres.es/def/ontomunicipio#picohenry)<br />[om:yoctolumen](http://opendata.caceres.es/def/ontomunicipio#yoctolumen)<br />[om:decajoule](http://opendata.caceres.es/def/ontomunicipio#decajoule)<br />[om:millimetre](http://opendata.caceres.es/def/ontomunicipio#millimetre)<br />[om:teralitre](http://opendata.caceres.es/def/ontomunicipio#teralitre)<br />[om:gigasievert](http://opendata.caceres.es/def/ontomunicipio#gigasievert)<br />[om:nanovolt](http://opendata.caceres.es/def/ontomunicipio#nanovolt)<br />[om:decacoulomb](http://opendata.caceres.es/def/ontomunicipio#decacoulomb)<br />[om:femtovolt](http://opendata.caceres.es/def/ontomunicipio#femtovolt)<br />[om:tebibit](http://opendata.caceres.es/def/ontomunicipio#tebibit)<br />[om:zeptogram](http://opendata.caceres.es/def/ontomunicipio#zeptogram)<br />[om:petacandela](http://opendata.caceres.es/def/ontomunicipio#petacandela)<br />[om:micropascal](http://opendata.caceres.es/def/ontomunicipio#micropascal)<br />[om:exapascal](http://opendata.caceres.es/def/ontomunicipio#exapascal)<br />[om:hectolumen](http://opendata.caceres.es/def/ontomunicipio#hectolumen)<br />[om:picosteradian](http://opendata.caceres.es/def/ontomunicipio#picosteradian)<br />[om:zeptocandela](http://opendata.caceres.es/def/ontomunicipio#zeptocandela)<br />[om:centimetreOfMercury](http://opendata.caceres.es/def/ontomunicipio#centimetreOfMercury)<br />[om:attovolt](http://opendata.caceres.es/def/ontomunicipio#attovolt)<br />[om:gigavolt](http://opendata.caceres.es/def/ontomunicipio#gigavolt)<br />[om:picoweber](http://opendata.caceres.es/def/ontomunicipio#picoweber)<br />[om:zettakatal](http://opendata.caceres.es/def/ontomunicipio#zettakatal)<br />[om:terasecond-Time](http://opendata.caceres.es/def/ontomunicipio#terasecond-Time)<br />[om:attohertz](http://opendata.caceres.es/def/ontomunicipio#attohertz)<br />[om:zeptonewton](http://opendata.caceres.es/def/ontomunicipio#zeptonewton)<br />[om:decasievert](http://opendata.caceres.es/def/ontomunicipio#decasievert)<br />[om:femtohenry](http://opendata.caceres.es/def/ontomunicipio#femtohenry)<br />[om:zettafarad](http://opendata.caceres.es/def/ontomunicipio#zettafarad)<br />[om:attokatal](http://opendata.caceres.es/def/ontomunicipio#attokatal)<br />[om:kibibyte](http://opendata.caceres.es/def/ontomunicipio#kibibyte)<br />[om:kilolumen](http://opendata.caceres.es/def/ontomunicipio#kilolumen)<br />[om:decacandela](http://opendata.caceres.es/def/ontomunicipio#decacandela)<br />[om:deciradian](http://opendata.caceres.es/def/ontomunicipio#deciradian)<br />[om:yoctocandela](http://opendata.caceres.es/def/ontomunicipio#yoctocandela)<br />[om:zettalumen](http://opendata.caceres.es/def/ontomunicipio#zettalumen)<br />[om:microsecond-Angle](http://opendata.caceres.es/def/ontomunicipio#microsecond-Angle)<br />[om:hectokelvin](http://opendata.caceres.es/def/ontomunicipio#hectokelvin)<br />[om:gigacoulomb](http://opendata.caceres.es/def/ontomunicipio#gigacoulomb)<br />[om:petahenry](http://opendata.caceres.es/def/ontomunicipio#petahenry)<br />[om:hectolux](http://opendata.caceres.es/def/ontomunicipio#hectolux)<br />[om:terasiemens](http://opendata.caceres.es/def/ontomunicipio#terasiemens)<br />[om:exacoulomb](http://opendata.caceres.es/def/ontomunicipio#exacoulomb)<br />[om:nanomole](http://opendata.caceres.es/def/ontomunicipio#nanomole)<br />[om:yoctolitre](http://opendata.caceres.es/def/ontomunicipio#yoctolitre)<br />[om:millilumen](http://opendata.caceres.es/def/ontomunicipio#millilumen)<br />[om:yoctocoulomb](http://opendata.caceres.es/def/ontomunicipio#yoctocoulomb)<br />
### prefixed volt
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedVolt`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed watt
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedWatt`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed weber
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedWeber`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### pressure
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Pressure`
Description | <p>Pressure is the force applied to or distributed over a surface. It is a derived quantity in the International System of Units. Pressure is force divided by area.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:pressure-Dimension](http://opendata.caceres.es/def/ontomunicipio#pressure-Dimension) (c)<br />
### pressure unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PressureUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### protein mass fraction
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ProteinMassFraction`
Description | <p>The fraction of the mass of protein in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### pulp browning
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#PulpBrowning`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### quality mark
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#QualityMark`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Sub-classes |[om:QualityMarkLeaf](http://opendata.caceres.es/def/ontomunicipio#QualityMarkLeaf) (c)<br />[om:QualityMarkFlower](http://opendata.caceres.es/def/ontomunicipio#QualityMarkFlower) (c)<br />[om:QualityMarkTotal](http://opendata.caceres.es/def/ontomunicipio#QualityMarkTotal) (c)<br />
### quality mark flower(s)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#QualityMarkFlower`
Super-classes |[om:QualityMark](http://opendata.caceres.es/def/ontomunicipio#QualityMark) (c)<br />
### quality mark leafs
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#QualityMarkLeaf`
Super-classes |[om:QualityMark](http://opendata.caceres.es/def/ontomunicipio#QualityMark) (c)<br />
### quality mark total
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#QualityMarkTotal`
Super-classes |[om:QualityMark](http://opendata.caceres.es/def/ontomunicipio#QualityMark) (c)<br />
### quantity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Quantity`
Description | <p>A quantity is a representation of a quantifiable (standardised) aspect (such as length, mass, and time) of a phenomenon (e.g., a star, a molecule, or a food product). Quantities are classified according to similarity in their (implicit) metrological aspect, e.g. the length of my table and the length of my chair are both classified as length.</p>
Sub-classes |[om:ElectricalResistivity](http://opendata.caceres.es/def/ontomunicipio#ElectricalResistivity) (c)<br />[om:CauseEndOfVaseLifeDryBuds](http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeDryBuds) (c)<br />[om:StemEndRot](http://opendata.caceres.es/def/ontomunicipio#StemEndRot) (c)<br />[om:MolarMass](http://opendata.caceres.es/def/ontomunicipio#MolarMass) (c)<br />[om:TemperatureRate](http://opendata.caceres.es/def/ontomunicipio#TemperatureRate) (c)<br />[om:FourierNumberForMassTransfer](http://opendata.caceres.es/def/ontomunicipio#FourierNumberForMassTransfer) (c)<br />[om:SpectralResponse](http://opendata.caceres.es/def/ontomunicipio#SpectralResponse) (c)<br />[om:DensityParameter](http://opendata.caceres.es/def/ontomunicipio#DensityParameter) (c)<br />[om:StantonNumberForMassTransfer](http://opendata.caceres.es/def/ontomunicipio#StantonNumberForMassTransfer) (c)<br />[om:CauseEndOfVaseLifeBlueFlowers](http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeBlueFlowers) (c)<br />[om:Volume](http://opendata.caceres.es/def/ontomunicipio#Volume) (c)<br />[om:ElectricFluxDensity](http://opendata.caceres.es/def/ontomunicipio#ElectricFluxDensity) (c)<br />[om:BolometricCorrection](http://opendata.caceres.es/def/ontomunicipio#BolometricCorrection) (c)<br />[om:AbsorbedDose](http://opendata.caceres.es/def/ontomunicipio#AbsorbedDose) (c)<br />[om:AlfvenNumber](http://opendata.caceres.es/def/ontomunicipio#AlfvenNumber) (c)<br />[om:Firmness-Penetrometer-Method1](http://opendata.caceres.es/def/ontomunicipio#Firmness-Penetrometer-Method1) (c)<br />[om:VolumetricViableCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCount) (c)<br />[om:Radiance](http://opendata.caceres.es/def/ontomunicipio#Radiance) (c)<br />[om:PecletNumberForMassTransfer](http://opendata.caceres.es/def/ontomunicipio#PecletNumberForMassTransfer) (c)<br />[om:Pressure](http://opendata.caceres.es/def/ontomunicipio#Pressure) (c)<br />[om:CauseEndOfVaseLifeRottenFlowers](http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeRottenFlowers) (c)<br />[om:Impulse](http://opendata.caceres.es/def/ontomunicipio#Impulse) (c)<br />[om:AreaDensity](http://opendata.caceres.es/def/ontomunicipio#AreaDensity) (c)<br />[om:DynamicModulus](http://opendata.caceres.es/def/ontomunicipio#DynamicModulus) (c)<br />[om:LuminousIntensity](http://opendata.caceres.es/def/ontomunicipio#LuminousIntensity) (c)<br />[om:AmountOfMoney](http://opendata.caceres.es/def/ontomunicipio#AmountOfMoney) (c)<br />[om:Strain](http://opendata.caceres.es/def/ontomunicipio#Strain) (c)<br />[om:CosmologicalConstant](http://opendata.caceres.es/def/ontomunicipio#CosmologicalConstant) (c)<br />[om:Number](http://opendata.caceres.es/def/ontomunicipio#Number) (c)<br />[om:CauseEndOfVaseLifeNonturgidLeaves](http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeNonturgidLeaves) (c)<br />[om:CurrentDensity](http://opendata.caceres.es/def/ontomunicipio#CurrentDensity) (c)<br />[om:PrandtlNumber](http://opendata.caceres.es/def/ontomunicipio#PrandtlNumber) (c)<br />[om:ExposureToXAndGammaRays](http://opendata.caceres.es/def/ontomunicipio#ExposureToXAndGammaRays) (c)<br />[om:Wavenumber](http://opendata.caceres.es/def/ontomunicipio#Wavenumber) (c)<br />[om:PermeabilityOfFreeSpace](http://opendata.caceres.es/def/ontomunicipio#PermeabilityOfFreeSpace) (c)<br />[om:Entropy](http://opendata.caceres.es/def/ontomunicipio#Entropy) (c)<br />[om:Acceleration](http://opendata.caceres.es/def/ontomunicipio#Acceleration) (c)<br />[om:Ratio](http://opendata.caceres.es/def/ontomunicipio#Ratio) (c)<br />[om:PulpBrowning](http://opendata.caceres.es/def/ontomunicipio#PulpBrowning) (c)<br />[om:EnergyDensity](http://opendata.caceres.es/def/ontomunicipio#EnergyDensity) (c)<br />[om:Hydrophobicity](http://opendata.caceres.es/def/ontomunicipio#Hydrophobicity) (c)<br />[om:FirstCowlingNumber](http://opendata.caceres.es/def/ontomunicipio#FirstCowlingNumber) (c)<br />[om:Area](http://opendata.caceres.es/def/ontomunicipio#Area) (c)<br />[om:ManualFirmness](http://opendata.caceres.es/def/ontomunicipio#ManualFirmness) (c)<br />[om:NusseltNumberForMassTransfer](http://opendata.caceres.es/def/ontomunicipio#NusseltNumberForMassTransfer) (c)<br />[om:Frequency](http://opendata.caceres.es/def/ontomunicipio#Frequency) (c)<br />[om:AreaDensityRate](http://opendata.caceres.es/def/ontomunicipio#AreaDensityRate) (c)<br />[om:Magnitude](http://opendata.caceres.es/def/ontomunicipio#Magnitude) (c)<br />[om:VascularBrowning](http://opendata.caceres.es/def/ontomunicipio#VascularBrowning) (c)<br />[om:MagneticFlux](http://opendata.caceres.es/def/ontomunicipio#MagneticFlux) (c)<br />[om:Time](http://opendata.caceres.es/def/ontomunicipio#Time) (c)<br />[om:ElectricDipoleMoment](http://opendata.caceres.es/def/ontomunicipio#ElectricDipoleMoment) (c)<br />[om:MassFlow](http://opendata.caceres.es/def/ontomunicipio#MassFlow) (c)<br />[om:Power](http://opendata.caceres.es/def/ontomunicipio#Power) (c)<br />[om:CatalyticActivityConcentration](http://opendata.caceres.es/def/ontomunicipio#CatalyticActivityConcentration) (c)<br />[om:Illuminance](http://opendata.caceres.es/def/ontomunicipio#Illuminance) (c)<br />[om:AreaFraction](http://opendata.caceres.es/def/ontomunicipio#AreaFraction) (c)<br />[om:LuminousFlux](http://opendata.caceres.es/def/ontomunicipio#LuminousFlux) (c)<br />[om:Torque](http://opendata.caceres.es/def/ontomunicipio#Torque) (c)<br />[om:CauseEndOfVaseLifeYellowLeaves](http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeYellowLeaves) (c)<br />[om:MolarEntropy](http://opendata.caceres.es/def/ontomunicipio#MolarEntropy) (c)<br />[om:Molality](http://opendata.caceres.es/def/ontomunicipio#Molality) (c)<br />[om:SpecificCatalyticActivity](http://opendata.caceres.es/def/ontomunicipio#SpecificCatalyticActivity) (c)<br />[om:AmountOfSubstance](http://opendata.caceres.es/def/ontomunicipio#AmountOfSubstance) (c)<br />[om:ElectricalResistance](http://opendata.caceres.es/def/ontomunicipio#ElectricalResistance) (c)<br />[om:SpecificEntropy](http://opendata.caceres.es/def/ontomunicipio#SpecificEntropy) (c)<br />[om:ReynoldsNumber](http://opendata.caceres.es/def/ontomunicipio#ReynoldsNumber) (c)<br />[om:CauseEndOfVaseLifeDryFlowers](http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeDryFlowers) (c)<br />[om:Reddening](http://opendata.caceres.es/def/ontomunicipio#Reddening) (c)<br />[om:QualityMark](http://opendata.caceres.es/def/ontomunicipio#QualityMark) (c)<br />[om:KinematicViscosity](http://opendata.caceres.es/def/ontomunicipio#KinematicViscosity) (c)<br />[om:Mass](http://opendata.caceres.es/def/ontomunicipio#Mass) (c)<br />[om:ScaleFactor](http://opendata.caceres.es/def/ontomunicipio#ScaleFactor) (c)<br />[om:Activity](http://opendata.caceres.es/def/ontomunicipio#Activity) (c)<br />[om:Length](http://opendata.caceres.es/def/ontomunicipio#Length) (c)<br />[om:Hydrophilicity](http://opendata.caceres.es/def/ontomunicipio#Hydrophilicity) (c)<br />[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />[om:Extinction](http://opendata.caceres.es/def/ontomunicipio#Extinction) (c)<br />[om:Reluctance](http://opendata.caceres.es/def/ontomunicipio#Reluctance) (c)<br />[om:CauseEndOfVaseLifeNonturgidFlowers](http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeNonturgidFlowers) (c)<br />[om:Admittance](http://opendata.caceres.es/def/ontomunicipio#Admittance) (c)<br />[om:RayleighNumber](http://opendata.caceres.es/def/ontomunicipio#RayleighNumber) (c)<br />[om:Permeance-Electromagnetic](http://opendata.caceres.es/def/ontomunicipio#Permeance-Electromagnetic) (c)<br />[om:AmountOfSubstanceFractionFlow](http://opendata.caceres.es/def/ontomunicipio#AmountOfSubstanceFractionFlow) (c)<br />[om:QuantumEfficiency](http://opendata.caceres.es/def/ontomunicipio#QuantumEfficiency) (c)<br />[om:CauseEndOfVaseLifeWiltedFlowers](http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeWiltedFlowers) (c)<br />[om:FourierNumber](http://opendata.caceres.es/def/ontomunicipio#FourierNumber) (c)<br />[om:StantonNumber](http://opendata.caceres.es/def/ontomunicipio#StantonNumber) (c)<br />[om:VolumeFraction](http://opendata.caceres.es/def/ontomunicipio#VolumeFraction) (c)<br />[om:CauseEndOfVaseLifeDryLeaves](http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeDryLeaves) (c)<br />[om:Exposure](http://opendata.caceres.es/def/ontomunicipio#Exposure) (c)<br />[om:SpecificHeatCapacity](http://opendata.caceres.es/def/ontomunicipio#SpecificHeatCapacity) (c)<br />[om:AngularMomentum](http://opendata.caceres.es/def/ontomunicipio#AngularMomentum) (c)<br />[om:MolarHeatCapacity](http://opendata.caceres.es/def/ontomunicipio#MolarHeatCapacity) (c)<br />[om:NumberDensity](http://opendata.caceres.es/def/ontomunicipio#NumberDensity) (c)<br />[om:CauseEndOfVaseLifeBotrytis](http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeBotrytis) (c)<br />[om:NusseltNumber](http://opendata.caceres.es/def/ontomunicipio#NusseltNumber) (c)<br />[om:Speed](http://opendata.caceres.es/def/ontomunicipio#Speed) (c)<br />[om:MomentOfInertia](http://opendata.caceres.es/def/ontomunicipio#MomentOfInertia) (c)<br />[om:ColourIndex](http://opendata.caceres.es/def/ontomunicipio#ColourIndex) (c)<br />[om:HeatTransferCoefficient](http://opendata.caceres.es/def/ontomunicipio#HeatTransferCoefficient) (c)<br />[om:Amphiphilicity](http://opendata.caceres.es/def/ontomunicipio#Amphiphilicity) (c)<br />[om:DarkNoise](http://opendata.caceres.es/def/ontomunicipio#DarkNoise) (c)<br />[om:RelativeHumidity](http://opendata.caceres.es/def/ontomunicipio#RelativeHumidity) (c)<br />[om:HartmannNumber](http://opendata.caceres.es/def/ontomunicipio#HartmannNumber) (c)<br />[om:DynamicViscosity](http://opendata.caceres.es/def/ontomunicipio#DynamicViscosity) (c)<br />[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />[om:ExternalBrowning](http://opendata.caceres.es/def/ontomunicipio#ExternalBrowning) (c)<br />[om:CauseEndOfVaseLifeAbscisedFlowers](http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeAbscisedFlowers) (c)<br />[om:MolarEnergy](http://opendata.caceres.es/def/ontomunicipio#MolarEnergy) (c)<br />[om:Luminance](http://opendata.caceres.es/def/ontomunicipio#Luminance) (c)<br />[om:SpecificViableCount](http://opendata.caceres.es/def/ontomunicipio#SpecificViableCount) (c)<br />[om:AmountOfSubstanceConcentration](http://opendata.caceres.es/def/ontomunicipio#AmountOfSubstanceConcentration) (c)<br />[om:MolarVolume](http://opendata.caceres.es/def/ontomunicipio#MolarVolume) (c)<br />[om:CowlingNumber](http://opendata.caceres.es/def/ontomunicipio#CowlingNumber) (c)<br />[om:KnudsenNumber](http://opendata.caceres.es/def/ontomunicipio#KnudsenNumber) (c)<br />[om:SaltStrength](http://opendata.caceres.es/def/ontomunicipio#SaltStrength) (c)<br />[om:MagneticField](http://opendata.caceres.es/def/ontomunicipio#MagneticField) (c)<br />[om:ColumnNumberDensity](http://opendata.caceres.es/def/ontomunicipio#ColumnNumberDensity) (c)<br />[om:WeberNumber](http://opendata.caceres.es/def/ontomunicipio#WeberNumber) (c)<br />[om:CurvatureConstant](http://opendata.caceres.es/def/ontomunicipio#CurvatureConstant) (c)<br />[om:Firmness-Penetrometer-Method2](http://opendata.caceres.es/def/ontomunicipio#Firmness-Penetrometer-Method2) (c)<br />[om:Stress](http://opendata.caceres.es/def/ontomunicipio#Stress) (c)<br />[om:CatalyticActivity](http://opendata.caceres.es/def/ontomunicipio#CatalyticActivity) (c)<br />[om:Acidity](http://opendata.caceres.es/def/ontomunicipio#Acidity) (c)<br />[om:SchmidtNumber](http://opendata.caceres.es/def/ontomunicipio#SchmidtNumber) (c)<br />[om:GrashofNumber](http://opendata.caceres.es/def/ontomunicipio#GrashofNumber) (c)<br />[om:BudStadium](http://opendata.caceres.es/def/ontomunicipio#BudStadium) (c)<br />[om:DecelerationParameter](http://opendata.caceres.es/def/ontomunicipio#DecelerationParameter) (c)<br />[om:ElectricPotential](http://opendata.caceres.es/def/ontomunicipio#ElectricPotential) (c)<br />[om:CauseEndOfVaseLifeWiltedLeaves](http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeWiltedLeaves) (c)<br />[om:ElectricalConductivity](http://opendata.caceres.es/def/ontomunicipio#ElectricalConductivity) (c)<br />[om:FroudeNumber](http://opendata.caceres.es/def/ontomunicipio#FroudeNumber) (c)<br />[om:ElectricalConductance](http://opendata.caceres.es/def/ontomunicipio#ElectricalConductance) (c)<br />[om:HeatCapacity](http://opendata.caceres.es/def/ontomunicipio#HeatCapacity) (c)<br />[om:Lipophilicity](http://opendata.caceres.es/def/ontomunicipio#Lipophilicity) (c)<br />[om:SurfaceTension](http://opendata.caceres.es/def/ontomunicipio#SurfaceTension) (c)<br />[om:Capacitance](http://opendata.caceres.es/def/ontomunicipio#Capacitance) (c)<br />[om:EulerNumber](http://opendata.caceres.es/def/ontomunicipio#EulerNumber) (c)<br />[om:Momentum](http://opendata.caceres.es/def/ontomunicipio#Momentum) (c)<br />[om:SymbolRate](http://opendata.caceres.es/def/ontomunicipio#SymbolRate) (c)<br />[om:ThermalResistance](http://opendata.caceres.es/def/ontomunicipio#ThermalResistance) (c)<br />[om:HubbleConstant](http://opendata.caceres.es/def/ontomunicipio#HubbleConstant) (c)<br />[om:Action](http://opendata.caceres.es/def/ontomunicipio#Action) (c)<br />[om:Density](http://opendata.caceres.es/def/ontomunicipio#Density) (c)<br />[om:CauseEndOfVaseLifeMalformedBuds](http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeMalformedBuds) (c)<br />[om:ShearRate](http://opendata.caceres.es/def/ontomunicipio#ShearRate) (c)<br />[om:ElectricField](http://opendata.caceres.es/def/ontomunicipio#ElectricField) (c)<br />[om:RadiantIntensity](http://opendata.caceres.es/def/ontomunicipio#RadiantIntensity) (c)<br />[om:Responsivity](http://opendata.caceres.es/def/ontomunicipio#Responsivity) (c)<br />[om:CauseEndOfVaseLifeRottenLeaves](http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeRottenLeaves) (c)<br />[om:ThermalConductivity](http://opendata.caceres.es/def/ontomunicipio#ThermalConductivity) (c)<br />[om:MagneticFluxDensity](http://opendata.caceres.es/def/ontomunicipio#MagneticFluxDensity) (c)<br />[om:QuantityOfDimensionOne](http://opendata.caceres.es/def/ontomunicipio#QuantityOfDimensionOne) (c)<br />[om:Permittivity](http://opendata.caceres.es/def/ontomunicipio#Permittivity) (c)<br />[om:ThermalDiffusivity](http://opendata.caceres.es/def/ontomunicipio#ThermalDiffusivity) (c)<br />[om:Inductance](http://opendata.caceres.es/def/ontomunicipio#Inductance) (c)<br />[om:ElectricCharge](http://opendata.caceres.es/def/ontomunicipio#ElectricCharge) (c)<br />[om:Energy](http://opendata.caceres.es/def/ontomunicipio#Energy) (c)<br />[om:Temperature](http://opendata.caceres.es/def/ontomunicipio#Temperature) (c)<br />[om:Permeability-EarthScience](http://opendata.caceres.es/def/ontomunicipio#Permeability-EarthScience) (c)<br />[om:AngularSpeed](http://opendata.caceres.es/def/ontomunicipio#AngularSpeed) (c)<br />[om:LuminousEnergy](http://opendata.caceres.es/def/ontomunicipio#LuminousEnergy) (c)<br />[om:AmountOfSubstanceFraction](http://opendata.caceres.es/def/ontomunicipio#AmountOfSubstanceFraction) (c)<br />[om:ElectricCurrent](http://opendata.caceres.es/def/ontomunicipio#ElectricCurrent) (c)<br />[om:Fluidity](http://opendata.caceres.es/def/ontomunicipio#Fluidity) (c)<br />[om:AcousticFirmness](http://opendata.caceres.es/def/ontomunicipio#AcousticFirmness) (c)<br />[om:MomentOfForce](http://opendata.caceres.es/def/ontomunicipio#MomentOfForce) (c)<br />[om:LuminousEfficacy](http://opendata.caceres.es/def/ontomunicipio#LuminousEfficacy) (c)<br />[om:AbsorbedDoseRate](http://opendata.caceres.es/def/ontomunicipio#AbsorbedDoseRate) (c)<br />[om:NormalisedDetectivity](http://opendata.caceres.es/def/ontomunicipio#NormalisedDetectivity) (c)<br />[om:CauseEndOfVaseLifeAbscisedLeaves](http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeAbscisedLeaves) (c)<br />[om:InformationCapacity](http://opendata.caceres.es/def/ontomunicipio#InformationCapacity) (c)<br />[om:AngularAcceleration](http://opendata.caceres.es/def/ontomunicipio#AngularAcceleration) (c)<br />[om:GrashofNumberForMassTransfer](http://opendata.caceres.es/def/ontomunicipio#GrashofNumberForMassTransfer) (c)<br />[om:VolumetricFlowRate](http://opendata.caceres.es/def/ontomunicipio#VolumetricFlowRate) (c)<br />[om:Detectivity](http://opendata.caceres.es/def/ontomunicipio#Detectivity) (c)<br />[om:GasConstant](http://opendata.caceres.es/def/ontomunicipio#GasConstant) (c)<br />[om:PecletNumber](http://opendata.caceres.es/def/ontomunicipio#PecletNumber) (c)<br />[om:SolidAngle](http://opendata.caceres.es/def/ontomunicipio#SolidAngle) (c)<br />[om:ThermalInsulance](http://opendata.caceres.es/def/ontomunicipio#ThermalInsulance) (c)<br />[om:ElectricChargeDensity](http://opendata.caceres.es/def/ontomunicipio#ElectricChargeDensity) (c)<br />[om:CauseEndOfVaseLifeMalformedFlowers](http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeMalformedFlowers) (c)<br />[om:StickStone](http://opendata.caceres.es/def/ontomunicipio#StickStone) (c)<br />[om:DynamicRange](http://opendata.caceres.es/def/ontomunicipio#DynamicRange) (c)<br />[om:Amplitude](http://opendata.caceres.es/def/ontomunicipio#Amplitude) (c)<br />[om:Permeance-MaterialsScience](http://opendata.caceres.es/def/ontomunicipio#Permeance-MaterialsScience) (c)<br />[om:DoseEquivalent](http://opendata.caceres.es/def/ontomunicipio#DoseEquivalent) (c)<br />[om:SpecificEnergy](http://opendata.caceres.es/def/ontomunicipio#SpecificEnergy) (c)<br />[om:MagnetomotiveForce](http://opendata.caceres.es/def/ontomunicipio#MagnetomotiveForce) (c)<br />[om:LewisNumber](http://opendata.caceres.es/def/ontomunicipio#LewisNumber) (c)<br />[om:Force](http://opendata.caceres.es/def/ontomunicipio#Force) (c)<br />[om:PowerDensity](http://opendata.caceres.es/def/ontomunicipio#PowerDensity) (c)<br />[om:MachNumber](http://opendata.caceres.es/def/ontomunicipio#MachNumber) (c)<br />[om:SpecificVolume](http://opendata.caceres.es/def/ontomunicipio#SpecificVolume) (c)<br />[om:StrouhalNumber](http://opendata.caceres.es/def/ontomunicipio#StrouhalNumber) (c)<br />[om:VolumetricHeatCapacity](http://opendata.caceres.es/def/ontomunicipio#VolumetricHeatCapacity) (c)<br />[om:AmountOfSubstanceFlow](http://opendata.caceres.es/def/ontomunicipio#AmountOfSubstanceFlow) (c)<br />[om:CauseEndOfVaseLifeAbscisedBuds](http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeAbscisedBuds) (c)<br />[om:MagneticReynoldsNumber](http://opendata.caceres.es/def/ontomunicipio#MagneticReynoldsNumber) (c)<br />
In domain of |[om:hasAggregateFunction](http://opendata.caceres.es/def/ontomunicipio#hasAggregateFunction) (op)<br />[om:hasContext](http://opendata.caceres.es/def/ontomunicipio#hasContext) (op)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op)<br />[om:hasPhenomenon](http://opendata.caceres.es/def/ontomunicipio#hasPhenomenon) (op)<br />
In range of |[om:hasQuantity](http://opendata.caceres.es/def/ontomunicipio#hasQuantity) (op)<br />[om:usesQuantity](http://opendata.caceres.es/def/ontomunicipio#usesQuantity) (op)<br />[om:hasBaseQuantity](http://opendata.caceres.es/def/ontomunicipio#hasBaseQuantity) (op)<br />[om:hasDerivedQuantity](http://opendata.caceres.es/def/ontomunicipio#hasDerivedQuantity) (op)<br />
### quantity of dimension one
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#QuantityOfDimensionOne`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:Ellipticity](http://opendata.caceres.es/def/ontomunicipio#Ellipticity) (c)<br />[om:Albedo](http://opendata.caceres.es/def/ontomunicipio#Albedo) (c)<br />[om:Eccentricity](http://opendata.caceres.es/def/ontomunicipio#Eccentricity) (c)<br />[om:Metallicity](http://opendata.caceres.es/def/ontomunicipio#Metallicity) (c)<br />
### quantity of dimension one unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#QuantityOfDimensionOneUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### quantum efficiency
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#QuantumEfficiency`
Description | <p>Ratio (of a detector such as a CCD) of actual number of detected photons and the number of incident photons.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
Sub-classes |[om:DetectiveQuantumEfficiency](http://opendata.caceres.es/def/ontomunicipio#DetectiveQuantumEfficiency) (c)<br />
### quantum efficiency unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#QuantumEfficiencyUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### R magnitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#RMagnitude`
Description | <p>R magnitude in the Cousins photometric system.</p>
Super-classes |[om:CousinsMagnitude](http://opendata.caceres.es/def/ontomunicipio#CousinsMagnitude) (c)<br />
### radiance
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Radiance`
Description | <p>Radiance is a radiometric measure that describes the amount of light that passes through or is emitted from a particular area and falls within a given solid angle in a specified direction.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:radiance-Dimension](http://opendata.caceres.es/def/ontomunicipio#radiance-Dimension) (c)<br />
### radiance unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#RadianceUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### radiant energy
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#RadiantEnergy`
Super-classes |[om:Energy](http://opendata.caceres.es/def/ontomunicipio#Energy) (c)<br />
### radiant flux
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#RadiantFlux`
Description | <p>Radiant flux is the measure of the total power of electromagnetic radiation.</p>
Super-classes |[om:Power](http://opendata.caceres.es/def/ontomunicipio#Power) (c)<br />
### radiant intensity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#RadiantIntensity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### radiant intensity unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#RadiantIntensityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### radius
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Radius`
Super-classes |[om:Length](http://opendata.caceres.es/def/ontomunicipio#Length) (c)<br />
Sub-classes |[om:Co-RotationRadius](http://opendata.caceres.es/def/ontomunicipio#Co-RotationRadius) (c)<br />
### radius (angle)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Radius-Angle`
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
### Rankine temperature
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#RankineTemperature`
Super-classes |[om:Temperature](http://opendata.caceres.es/def/ontomunicipio#Temperature) (c)<br />
Restrictions |[om:hasScale](http://opendata.caceres.es/def/ontomunicipio#hasScale) (op) **value** [om:RankineScale](http://opendata.caceres.es/def/ontomunicipio#RankineScale) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### Rankine temperature scale
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#RankineTemperatureScale`
Super-classes |[om:Scale](http://opendata.caceres.es/def/ontomunicipio#Scale) (c)<br />
### Rankine temperature unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#RankineTemperatureUnit`
Super-classes |[om:TemperatureUnit](http://opendata.caceres.es/def/ontomunicipio#TemperatureUnit) (c)<br />
### ratio
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Ratio`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
Sub-classes |[om:Percentage](http://opendata.caceres.es/def/ontomunicipio#Percentage) (c)<br />
### ratio scale
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#RatioScale`
Super-classes |[om:Scale](http://opendata.caceres.es/def/ontomunicipio#Scale) (c)<br />
Has members |[om:RankineScale](http://opendata.caceres.es/def/ontomunicipio#RankineScale)<br />[om:KelvinScale](http://opendata.caceres.es/def/ontomunicipio#KelvinScale)<br />
### ratio unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#RatioUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### Rayleigh number
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#RayleighNumber`
Description | <p>The Rayleigh number for a fluid is a dimensionless number associated with buoyancy driven flow.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### Rayleigh number unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#RayleighNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### Réaumur temperature
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ReaumurTemperature`
Super-classes |[om:Temperature](http://opendata.caceres.es/def/ontomunicipio#Temperature) (c)<br />
Restrictions |[om:hasScale](http://opendata.caceres.es/def/ontomunicipio#hasScale) (op) **value** [om:ReaumurScale](http://opendata.caceres.es/def/ontomunicipio#ReaumurScale) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### Réaumur temperature scale
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ReaumurTemperatureScale`
Super-classes |[om:Scale](http://opendata.caceres.es/def/ontomunicipio#Scale) (c)<br />
### Réaumur temperature unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ReaumurTemperatureUnit`
Super-classes |[om:TemperatureUnit](http://opendata.caceres.es/def/ontomunicipio#TemperatureUnit) (c)<br />
### red magnitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#RedMagnitude`
Description | <p>A red magnitude not specified for a specific photometric system.</p>
Super-classes |[om:Magnitude](http://opendata.caceres.es/def/ontomunicipio#Magnitude) (c)<br />
### reddening
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Reddening`
Description | <p>Reddening causes the star to appear redder if more dust or gas is between the star and the observer.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Sub-classes |[om:ReddeningB-V](http://opendata.caceres.es/def/ontomunicipio#ReddeningB-V) (c)<br />[om:ReddeningU-B](http://opendata.caceres.es/def/ontomunicipio#ReddeningU-B) (c)<br />
### reddening (B-V)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ReddeningB-V`
Description | <p>Reddening causes the star to appear redder if more dust or gas is between the star and the observer. The standard reddening is measured using the B and V passbands.</p>
Super-classes |[om:Reddening](http://opendata.caceres.es/def/ontomunicipio#Reddening) (c)<br />
### reddening (U-B)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ReddeningU-B`
Description | <p>Reddening measured with the U and B passbands.</p>
Super-classes |[om:Reddening](http://opendata.caceres.es/def/ontomunicipio#Reddening) (c)<br />
### relative humidity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#RelativeHumidity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### relative humidity unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#RelativeHumidityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### reluctance
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Reluctance`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:reluctance-Dimension](http://opendata.caceres.es/def/ontomunicipio#reluctance-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### reluctance unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ReluctanceUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### resonance energy
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ResonanceEnergy`
Super-classes |[om:MolarEnergy](http://opendata.caceres.es/def/ontomunicipio#MolarEnergy) (c)<br />
### responsivity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Responsivity`
Description | <p>Detector output for unit intensity input. Units are usually volts per watt or amps per watt.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### responsivity unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ResponsivityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### Reynolds number
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ReynoldsNumber`
Description | <p>The Reynolds number is a dimensionless number that gives a measure of the ratio of inertial forces to viscous forces and, consequently, quantifies the relative importance of these two types of forces for given flow conditions.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### Reynolds number unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ReynoldsNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### right ascension
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#RightAscension`
Description | <p>The angular distance on the celestial sphere measured eastward along the celestial equator from the equinox to the great circle passing through the celestial object and the celestial north pole.</p>
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
### SI prefix
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SIPrefix`
Super-classes |[om:Prefix](http://opendata.caceres.es/def/ontomunicipio#Prefix) (c)<br />
Has members |[om:nano](http://opendata.caceres.es/def/ontomunicipio#nano)<br />[om:peta](http://opendata.caceres.es/def/ontomunicipio#peta)<br />[om:micro](http://opendata.caceres.es/def/ontomunicipio#micro)<br />[om:centi](http://opendata.caceres.es/def/ontomunicipio#centi)<br />[om:zepto](http://opendata.caceres.es/def/ontomunicipio#zepto)<br />[om:femto](http://opendata.caceres.es/def/ontomunicipio#femto)<br />[om:deca](http://opendata.caceres.es/def/ontomunicipio#deca)<br />[om:tera](http://opendata.caceres.es/def/ontomunicipio#tera)<br />[om:yocto](http://opendata.caceres.es/def/ontomunicipio#yocto)<br />[om:exa](http://opendata.caceres.es/def/ontomunicipio#exa)<br />[om:zetta](http://opendata.caceres.es/def/ontomunicipio#zetta)<br />[om:mega](http://opendata.caceres.es/def/ontomunicipio#mega)<br />[om:hecto](http://opendata.caceres.es/def/ontomunicipio#hecto)<br />[om:yotta](http://opendata.caceres.es/def/ontomunicipio#yotta)<br />[om:kilo](http://opendata.caceres.es/def/ontomunicipio#kilo)<br />[om:giga](http://opendata.caceres.es/def/ontomunicipio#giga)<br />[om:milli](http://opendata.caceres.es/def/ontomunicipio#milli)<br />[om:atto](http://opendata.caceres.es/def/ontomunicipio#atto)<br />[om:pico](http://opendata.caceres.es/def/ontomunicipio#pico)<br />[om:deci](http://opendata.caceres.es/def/ontomunicipio#deci)<br />
### salt mass fraction
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SaltMassFraction`
Description | <p>The fraction of the mass of salt in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### salt strength
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SaltStrength`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### scale
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Scale`
Sub-classes |[om:CelsiusTemperatureScale](http://opendata.caceres.es/def/ontomunicipio#CelsiusTemperatureScale) (c)<br />[om:IntervalScale](http://opendata.caceres.es/def/ontomunicipio#IntervalScale) (c)<br />[om:ReaumurTemperatureScale](http://opendata.caceres.es/def/ontomunicipio#ReaumurTemperatureScale) (c)<br />[om:Temperature_scale](http://opendata.caceres.es/def/ontomunicipio#Temperature_scale) (c)<br />[om:FahrenheitTemperatureScale](http://opendata.caceres.es/def/ontomunicipio#FahrenheitTemperatureScale) (c)<br />[om:RatioScale](http://opendata.caceres.es/def/ontomunicipio#RatioScale) (c)<br />[om:ThermodynamicTemperatureScale](http://opendata.caceres.es/def/ontomunicipio#ThermodynamicTemperatureScale) (c)<br />[om:RankineTemperatureScale](http://opendata.caceres.es/def/ontomunicipio#RankineTemperatureScale) (c)<br />
In domain of |[om:hasOff-Set](http://opendata.caceres.es/def/ontomunicipio#hasOff-Set) (dp)<br />
In range of |[om:hasScale](http://opendata.caceres.es/def/ontomunicipio#hasScale) (op)<br />
### scale factor
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ScaleFactor`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### scale height
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ScaleHeight`
Description | <p>The scale height of a feature (such as the thin galactic disk) is the height (or position) at which the number density of the feature (for instance of the number of Population II stars) is equal to 1/e times the number density at the origin (for instance the Galactic Plane).</p>
Super-classes |[om:Length](http://opendata.caceres.es/def/ontomunicipio#Length) (c)<br />
### scale length
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ScaleLength`
Description | <p>The radial distance from a galaxy's core at which the average intensity has fallen to 1/e of the intensity at the centre of the galaxy.</p>
Super-classes |[om:Length](http://opendata.caceres.es/def/ontomunicipio#Length) (c)<br />
### Schmidt number
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SchmidtNumber`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
### Schmidt number unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SchmidtNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### secular aberration
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SecularAberration`
Description | <p>The component of the stellar abberation resulting from the motion of the solar system in space. This component is usually ignored. The abberation is the apparent angular displacement of the observed position of a celestial object from its geometric position, caused by the finite velocity of light in combination with the motions of the observer and of the observed object.</p>
Super-classes |[om:AngularDisplacement](http://opendata.caceres.es/def/ontomunicipio#AngularDisplacement) (c)<br />
### shear loss modulus
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ShearLossModulus`
Super-classes |[om:StorageModulus](http://opendata.caceres.es/def/ontomunicipio#StorageModulus) (c)<br />
### shear modulus
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ShearModulus`
Description | <p>Shear modulus is the ratio of shear stress to shear strain.</p>
Super-classes |[om:DynamicModulus](http://opendata.caceres.es/def/ontomunicipio#DynamicModulus) (c)<br />
### shear rate
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ShearRate`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### shear rate unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ShearRateUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### shear storage modulus
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ShearStorageModulus`
Super-classes |[om:StorageModulus](http://opendata.caceres.es/def/ontomunicipio#StorageModulus) (c)<br />
### shear strain
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ShearStrain`
Description | <p>Shear strain is a strain that acts parallel to the surface of a material that it acts on.</p>
Super-classes |[om:Strain](http://opendata.caceres.es/def/ontomunicipio#Strain) (c)<br />
### shear stress
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ShearStress`
Description | <p>Shear stress is a stress that is applied parallel or tangential to a face of a material.</p>
Super-classes |[om:Stress](http://opendata.caceres.es/def/ontomunicipio#Stress) (c)<br />
### singular unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SingularUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
Has members |[om:shannon](http://opendata.caceres.es/def/ontomunicipio#shannon)<br />[om:curie](http://opendata.caceres.es/def/ontomunicipio#curie)<br />[om:foot-USSurvey](http://opendata.caceres.es/def/ontomunicipio#foot-USSurvey)<br />[om:pint-Imperial](http://opendata.caceres.es/def/ontomunicipio#pint-Imperial)<br />[om:fluidOunce-US](http://opendata.caceres.es/def/ontomunicipio#fluidOunce-US)<br />[om:solarMass](http://opendata.caceres.es/def/ontomunicipio#solarMass)<br />[om:horsepower-British](http://opendata.caceres.es/def/ontomunicipio#horsepower-British)<br />[om:dryGallon-US](http://opendata.caceres.es/def/ontomunicipio#dryGallon-US)<br />[om:statweber](http://opendata.caceres.es/def/ontomunicipio#statweber)<br />[om:abohm](http://opendata.caceres.es/def/ontomunicipio#abohm)<br />[om:BritishThermalUnit-39F](http://opendata.caceres.es/def/ontomunicipio#BritishThermalUnit-39F)<br />[om:abcoulomb](http://opendata.caceres.es/def/ontomunicipio#abcoulomb)<br />[om:pascal](http://opendata.caceres.es/def/ontomunicipio#pascal)<br />[om:lambert](http://opendata.caceres.es/def/ontomunicipio#lambert)<br />[om:hour](http://opendata.caceres.es/def/ontomunicipio#hour)<br />[om:_1-10](http://opendata.caceres.es/def/ontomunicipio#_1-10)<br />[om:tonOfRefrigeration](http://opendata.caceres.es/def/ontomunicipio#tonOfRefrigeration)<br />[om:deltaA450](http://opendata.caceres.es/def/ontomunicipio#deltaA450)<br />[om:calorie-20C](http://opendata.caceres.es/def/ontomunicipio#calorie-20C)<br />[om:bushel-US](http://opendata.caceres.es/def/ontomunicipio#bushel-US)<br />[om:UnitedStatesDollar](http://opendata.caceres.es/def/ontomunicipio#UnitedStatesDollar)<br />[om:day-Sidereal](http://opendata.caceres.es/def/ontomunicipio#day-Sidereal)<br />[om:stathenry](http://opendata.caceres.es/def/ontomunicipio#stathenry)<br />[om:yard-International](http://opendata.caceres.es/def/ontomunicipio#yard-International)<br />[om:therm-EC](http://opendata.caceres.es/def/ontomunicipio#therm-EC)<br />[om:fathom-USSurvey](http://opendata.caceres.es/def/ontomunicipio#fathom-USSurvey)<br />[om:are](http://opendata.caceres.es/def/ontomunicipio#are)<br />[om:rem](http://opendata.caceres.es/def/ontomunicipio#rem)<br />[om:acreFoot](http://opendata.caceres.es/def/ontomunicipio#acreFoot)<br />[om:gauss](http://opendata.caceres.es/def/ontomunicipio#gauss)<br />[om:gamma](http://opendata.caceres.es/def/ontomunicipio#gamma)<br />[om:calorie-Thermochemical](http://opendata.caceres.es/def/ontomunicipio#calorie-Thermochemical)<br />[om:footPoundal](http://opendata.caceres.es/def/ontomunicipio#footPoundal)<br />[om:IndianRupee](http://opendata.caceres.es/def/ontomunicipio#IndianRupee)<br />[om:point-Postscript](http://opendata.caceres.es/def/ontomunicipio#point-Postscript)<br />[om:statfarad](http://opendata.caceres.es/def/ontomunicipio#statfarad)<br />[om:liquidQuart-US](http://opendata.caceres.es/def/ontomunicipio#liquidQuart-US)<br />[om:colonyFormingUnit](http://opendata.caceres.es/def/ontomunicipio#colonyFormingUnit)<br />[om:hertz](http://opendata.caceres.es/def/ontomunicipio#hertz)<br />[om:minute-Sidereal](http://opendata.caceres.es/def/ontomunicipio#minute-Sidereal)<br />[om:siemens](http://opendata.caceres.es/def/ontomunicipio#siemens)<br />[om:point-ATA](http://opendata.caceres.es/def/ontomunicipio#point-ATA)<br />[om:AFS](http://opendata.caceres.es/def/ontomunicipio#AFS)<br />[om:degree](http://opendata.caceres.es/def/ontomunicipio#degree)<br />[om:footcandle](http://opendata.caceres.es/def/ontomunicipio#footcandle)<br />[om:erg](http://opendata.caceres.es/def/ontomunicipio#erg)<br />[om:calorie-Mean](http://opendata.caceres.es/def/ontomunicipio#calorie-Mean)<br />[om:NewZealandDollar](http://opendata.caceres.es/def/ontomunicipio#NewZealandDollar)<br />[om:year](http://opendata.caceres.es/def/ontomunicipio#year)<br />[om:BritishThermalUnit-60F](http://opendata.caceres.es/def/ontomunicipio#BritishThermalUnit-60F)<br />[om:quart-Imperial](http://opendata.caceres.es/def/ontomunicipio#quart-Imperial)<br />[om:litre](http://opendata.caceres.es/def/ontomunicipio#litre)<br />[om:atmosphere-Standard](http://opendata.caceres.es/def/ontomunicipio#atmosphere-Standard)<br />[om:BritishThermalUnit-Mean](http://opendata.caceres.es/def/ontomunicipio#BritishThermalUnit-Mean)<br />[om:barrel-US](http://opendata.caceres.es/def/ontomunicipio#barrel-US)<br />[om:newton](http://opendata.caceres.es/def/ontomunicipio#newton)<br />[om:candela](http://opendata.caceres.es/def/ontomunicipio#candela)<br />[om:calorie-InternationalTable](http://opendata.caceres.es/def/ontomunicipio#calorie-InternationalTable)<br />[om:_1-0](http://opendata.caceres.es/def/ontomunicipio#_1-0)<br />[om:poundSterling](http://opendata.caceres.es/def/ontomunicipio#poundSterling)<br />[om:amylaseUnit](http://opendata.caceres.es/def/ontomunicipio#amylaseUnit)<br />[om:franklin](http://opendata.caceres.es/def/ontomunicipio#franklin)<br />[om:minute-Angle](http://opendata.caceres.es/def/ontomunicipio#minute-Angle)<br />[om:rhe](http://opendata.caceres.es/def/ontomunicipio#rhe)<br />[om:barye](http://opendata.caceres.es/def/ontomunicipio#barye)<br />[om:pennyweight-Troy](http://opendata.caceres.es/def/ontomunicipio#pennyweight-Troy)<br />[om:röntgen](http://opendata.caceres.es/def/ontomunicipio#röntgen)<br />[om:radian](http://opendata.caceres.es/def/ontomunicipio#radian)<br />[om:hour-Sidereal](http://opendata.caceres.es/def/ontomunicipio#hour-Sidereal)<br />[om:tonOfTNT](http://opendata.caceres.es/def/ontomunicipio#tonOfTNT)<br />[om:TurkishLira](http://opendata.caceres.es/def/ontomunicipio#TurkishLira)<br />[om:horsepower-Metric](http://opendata.caceres.es/def/ontomunicipio#horsepower-Metric)<br />[om:cord](http://opendata.caceres.es/def/ontomunicipio#cord)<br />[om:slug](http://opendata.caceres.es/def/ontomunicipio#slug)<br />[om:year-Tropical](http://opendata.caceres.es/def/ontomunicipio#year-Tropical)<br />[om:stere](http://opendata.caceres.es/def/ontomunicipio#stere)<br />[om:degreeReaumur](http://opendata.caceres.es/def/ontomunicipio#degreeReaumur)<br />[om:shake](http://opendata.caceres.es/def/ontomunicipio#shake)<br />[om:chain](http://opendata.caceres.es/def/ontomunicipio#chain)<br />[om:cicero](http://opendata.caceres.es/def/ontomunicipio#cicero)<br />[om:SouthKoreanWon](http://opendata.caceres.es/def/ontomunicipio#SouthKoreanWon)<br />[om:one](http://opendata.caceres.es/def/ontomunicipio#one)<br />[om:minute-HourAngle](http://opendata.caceres.es/def/ontomunicipio#minute-HourAngle)<br />[om:hundredweight-British](http://opendata.caceres.es/def/ontomunicipio#hundredweight-British)<br />[om:volt](http://opendata.caceres.es/def/ontomunicipio#volt)<br />[om:torr](http://opendata.caceres.es/def/ontomunicipio#torr)<br />[om:ampere](http://opendata.caceres.es/def/ontomunicipio#ampere)<br />[om:horsepower-Water](http://opendata.caceres.es/def/ontomunicipio#horsepower-Water)<br />[om:byte](http://opendata.caceres.es/def/ontomunicipio#byte)<br />[om:statvolt](http://opendata.caceres.es/def/ontomunicipio#statvolt)<br />[om:stattesla](http://opendata.caceres.es/def/ontomunicipio#stattesla)<br />[om:horsepower-Electric](http://opendata.caceres.es/def/ontomunicipio#horsepower-Electric)<br />[om:joule](http://opendata.caceres.es/def/ontomunicipio#joule)<br />[om:hundredweight-US](http://opendata.caceres.es/def/ontomunicipio#hundredweight-US)<br />[om:poundAvoirdupois](http://opendata.caceres.es/def/ontomunicipio#poundAvoirdupois)<br />[om:circularMil](http://opendata.caceres.es/def/ontomunicipio#circularMil)<br />[om:BritishThermalUnit-InternationalTable](http://opendata.caceres.es/def/ontomunicipio#BritishThermalUnit-InternationalTable)<br />[om:point-TeX](http://opendata.caceres.es/def/ontomunicipio#point-TeX)<br />[om:poundApothecaries](http://opendata.caceres.es/def/ontomunicipio#poundApothecaries)<br />[om:peck-US](http://opendata.caceres.es/def/ontomunicipio#peck-US)<br />[om:JapaneseYen](http://opendata.caceres.es/def/ontomunicipio#JapaneseYen)<br />[om:henry](http://opendata.caceres.es/def/ontomunicipio#henry)<br />[om:statampere](http://opendata.caceres.es/def/ontomunicipio#statampere)<br />[om:hartley](http://opendata.caceres.es/def/ontomunicipio#hartley)<br />[om:gram](http://opendata.caceres.es/def/ontomunicipio#gram)<br />[om:becquerel](http://opendata.caceres.es/def/ontomunicipio#becquerel)<br />[om:mil-Angle](http://opendata.caceres.es/def/ontomunicipio#mil-Angle)<br />[om:cup-USCustomary](http://opendata.caceres.es/def/ontomunicipio#cup-USCustomary)<br />[om:dessertspoon](http://opendata.caceres.es/def/ontomunicipio#dessertspoon)<br />[om:pica-ATA](http://opendata.caceres.es/def/ontomunicipio#pica-ATA)<br />[om:statmho](http://opendata.caceres.es/def/ontomunicipio#statmho)<br />[om:InternationalUnit](http://opendata.caceres.es/def/ontomunicipio#InternationalUnit)<br />[om:grain](http://opendata.caceres.es/def/ontomunicipio#grain)<br />[om:atmosphere-Technical](http://opendata.caceres.es/def/ontomunicipio#atmosphere-Technical)<br />[om:ounceApothecaries](http://opendata.caceres.es/def/ontomunicipio#ounceApothecaries)<br />[om:lux](http://opendata.caceres.es/def/ontomunicipio#lux)<br />[om:farad](http://opendata.caceres.es/def/ontomunicipio#farad)<br />[om:second-Sidereal](http://opendata.caceres.es/def/ontomunicipio#second-Sidereal)<br />[om:acre-International](http://opendata.caceres.es/def/ontomunicipio#acre-International)<br />[om:kayser](http://opendata.caceres.es/def/ontomunicipio#kayser)<br />[om:year-Sidereal](http://opendata.caceres.es/def/ontomunicipio#year-Sidereal)<br />[om:SwedishKrona](http://opendata.caceres.es/def/ontomunicipio#SwedishKrona)<br />[om:BrazilianReal](http://opendata.caceres.es/def/ontomunicipio#BrazilianReal)<br />[om:day](http://opendata.caceres.es/def/ontomunicipio#day)<br />[om:mho](http://opendata.caceres.es/def/ontomunicipio#mho)<br />[om:sievert](http://opendata.caceres.es/def/ontomunicipio#sievert)<br />[om:dyne](http://opendata.caceres.es/def/ontomunicipio#dyne)<br />[om:steradian](http://opendata.caceres.es/def/ontomunicipio#steradian)<br />[om:faraday](http://opendata.caceres.es/def/ontomunicipio#faraday)<br />[om:euro](http://opendata.caceres.es/def/ontomunicipio#euro)<br />[om:_1-5](http://opendata.caceres.es/def/ontomunicipio#_1-5)<br />[om:stokes](http://opendata.caceres.es/def/ontomunicipio#stokes)<br />[om:gilbert](http://opendata.caceres.es/def/ontomunicipio#gilbert)<br />[om:perm-0C](http://opendata.caceres.es/def/ontomunicipio#perm-0C)<br />[om:ton-Force-Short](http://opendata.caceres.es/def/ontomunicipio#ton-Force-Short)<br />[om:degreeCelsius](http://opendata.caceres.es/def/ontomunicipio#degreeCelsius)<br />[om:ton-ShortAssay](http://opendata.caceres.es/def/ontomunicipio#ton-ShortAssay)<br />[om:second-Angle](http://opendata.caceres.es/def/ontomunicipio#second-Angle)<br />[om:angstrom](http://opendata.caceres.es/def/ontomunicipio#angstrom)<br />[om:kelvin](http://opendata.caceres.es/def/ontomunicipio#kelvin)<br />[om:solarLuminosity](http://opendata.caceres.es/def/ontomunicipio#solarLuminosity)<br />[om:molair](http://opendata.caceres.es/def/ontomunicipio#molair)<br />[om:tonne](http://opendata.caceres.es/def/ontomunicipio#tonne)<br />[om:point-Didot](http://opendata.caceres.es/def/ontomunicipio#point-Didot)<br />[om:acre-USSurvey](http://opendata.caceres.es/def/ontomunicipio#acre-USSurvey)<br />[om:biot](http://opendata.caceres.es/def/ontomunicipio#biot)<br />[om:dryPint-US](http://opendata.caceres.es/def/ontomunicipio#dryPint-US)<br />[om:tesla](http://opendata.caceres.es/def/ontomunicipio#tesla)<br />[om:pica-Postscript](http://opendata.caceres.es/def/ontomunicipio#pica-Postscript)<br />[om:gallon-Imperial](http://opendata.caceres.es/def/ontomunicipio#gallon-Imperial)<br />[om:debye](http://opendata.caceres.es/def/ontomunicipio#debye)<br />[om:poise](http://opendata.caceres.es/def/ontomunicipio#poise)<br />[om:furlong-International](http://opendata.caceres.es/def/ontomunicipio#furlong-International)<br />[om:MexicanPeso](http://opendata.caceres.es/def/ontomunicipio#MexicanPeso)<br />[om:gon](http://opendata.caceres.es/def/ontomunicipio#gon)<br />[om:teaspoon-US](http://opendata.caceres.es/def/ontomunicipio#teaspoon-US)<br />[om:rad](http://opendata.caceres.es/def/ontomunicipio#rad)<br />[om:week](http://opendata.caceres.es/def/ontomunicipio#week)<br />[om:foot-International](http://opendata.caceres.es/def/ontomunicipio#foot-International)<br />[om:SingaporeDollar](http://opendata.caceres.es/def/ontomunicipio#SingaporeDollar)<br />[om:bit](http://opendata.caceres.es/def/ontomunicipio#bit)<br />[om:ton-Register](http://opendata.caceres.es/def/ontomunicipio#ton-Register)<br />[om:revolution](http://opendata.caceres.es/def/ontomunicipio#revolution)<br />[om:fermi](http://opendata.caceres.es/def/ontomunicipio#fermi)<br />[om:statcoulomb](http://opendata.caceres.es/def/ontomunicipio#statcoulomb)<br />[om:knot-International](http://opendata.caceres.es/def/ontomunicipio#knot-International)<br />[om:abhenry](http://opendata.caceres.es/def/ontomunicipio#abhenry)<br />[om:degreeFahrenheit](http://opendata.caceres.es/def/ontomunicipio#degreeFahrenheit)<br />[om:second-HourAngle](http://opendata.caceres.es/def/ontomunicipio#second-HourAngle)<br />[om:kip](http://opendata.caceres.es/def/ontomunicipio#kip)<br />[om:solarRadius](http://opendata.caceres.es/def/ontomunicipio#solarRadius)<br />[om:astronomicalUnit](http://opendata.caceres.es/def/ontomunicipio#astronomicalUnit)<br />[om:ton-Short](http://opendata.caceres.es/def/ontomunicipio#ton-Short)<br />[om:_0-5](http://opendata.caceres.es/def/ontomunicipio#_0-5)<br />[om:ounceAvoirdupois](http://opendata.caceres.es/def/ontomunicipio#ounceAvoirdupois)<br />[om:carat-Mass](http://opendata.caceres.es/def/ontomunicipio#carat-Mass)<br />[om:horsepower-Boiler](http://opendata.caceres.es/def/ontomunicipio#horsepower-Boiler)<br />[om:pica-TeX](http://opendata.caceres.es/def/ontomunicipio#pica-TeX)<br />[om:rod-US](http://opendata.caceres.es/def/ontomunicipio#rod-US)<br />[om:inch-International](http://opendata.caceres.es/def/ontomunicipio#inch-International)<br />[om:gill-Imperial](http://opendata.caceres.es/def/ontomunicipio#gill-Imperial)<br />[om:ChineseYuan](http://opendata.caceres.es/def/ontomunicipio#ChineseYuan)<br />[om:gill-US](http://opendata.caceres.es/def/ontomunicipio#gill-US)<br />[om:watt](http://opendata.caceres.es/def/ontomunicipio#watt)<br />[om:ohm](http://opendata.caceres.es/def/ontomunicipio#ohm)<br />[om:NorwegianKrone](http://opendata.caceres.es/def/ontomunicipio#NorwegianKrone)<br />[om:HongKongDollar](http://opendata.caceres.es/def/ontomunicipio#HongKongDollar)<br />[om:hour-HourAngle](http://opendata.caceres.es/def/ontomunicipio#hour-HourAngle)<br />[om:abampere](http://opendata.caceres.es/def/ontomunicipio#abampere)<br />[om:ton-Long](http://opendata.caceres.es/def/ontomunicipio#ton-Long)<br />[om:parsec](http://opendata.caceres.es/def/ontomunicipio#parsec)<br />[om:liquidPint-US](http://opendata.caceres.es/def/ontomunicipio#liquidPint-US)<br />[om:BritishThermalUnit-59F](http://opendata.caceres.es/def/ontomunicipio#BritishThermalUnit-59F)<br />[om:metre](http://opendata.caceres.es/def/ontomunicipio#metre)<br />[om:bar](http://opendata.caceres.es/def/ontomunicipio#bar)<br />[om:oersted](http://opendata.caceres.es/def/ontomunicipio#oersted)<br />[om:unifiedAtomicMassUnit](http://opendata.caceres.es/def/ontomunicipio#unifiedAtomicMassUnit)<br />[om:stilb](http://opendata.caceres.es/def/ontomunicipio#stilb)<br />[om:statohm](http://opendata.caceres.es/def/ontomunicipio#statohm)<br />[om:coulomb](http://opendata.caceres.es/def/ontomunicipio#coulomb)<br />[om:mole](http://opendata.caceres.es/def/ontomunicipio#mole)<br />[om:degreeRankine](http://opendata.caceres.es/def/ontomunicipio#degreeRankine)<br />[om:second-Time](http://opendata.caceres.es/def/ontomunicipio#second-Time)<br />[om:maxwell](http://opendata.caceres.es/def/ontomunicipio#maxwell)<br />[om:milligramRAE](http://opendata.caceres.es/def/ontomunicipio#milligramRAE)<br />[om:RussianRuble](http://opendata.caceres.es/def/ontomunicipio#RussianRuble)<br />[om:fluidOunce-Imperial](http://opendata.caceres.es/def/ontomunicipio#fluidOunce-Imperial)<br />[om:metreOfMercury](http://opendata.caceres.es/def/ontomunicipio#metreOfMercury)<br />[om:electronvolt](http://opendata.caceres.es/def/ontomunicipio#electronvolt)<br />[om:gallon-US](http://opendata.caceres.es/def/ontomunicipio#gallon-US)<br />[om:darcy](http://opendata.caceres.es/def/ontomunicipio#darcy)<br />[om:BritishThermalUnit-Thermochemical](http://opendata.caceres.es/def/ontomunicipio#BritishThermalUnit-Thermochemical)<br />[om:minute-Time](http://opendata.caceres.es/def/ontomunicipio#minute-Time)<br />[om:baud](http://opendata.caceres.es/def/ontomunicipio#baud)<br />[om:gal](http://opendata.caceres.es/def/ontomunicipio#gal)<br />[om:quad](http://opendata.caceres.es/def/ontomunicipio#quad)<br />[om:barn](http://opendata.caceres.es/def/ontomunicipio#barn)<br />[om:SouthAfricanRand](http://opendata.caceres.es/def/ontomunicipio#SouthAfricanRand)<br />[om:phot](http://opendata.caceres.es/def/ontomunicipio#phot)<br />[om:mile-Statute](http://opendata.caceres.es/def/ontomunicipio#mile-Statute)<br />[om:AustralianDollar](http://opendata.caceres.es/def/ontomunicipio#AustralianDollar)<br />[om:partsPerMillion](http://opendata.caceres.es/def/ontomunicipio#partsPerMillion)<br />[om:magnitude](http://opendata.caceres.es/def/ontomunicipio#magnitude)<br />[om:therm-US](http://opendata.caceres.es/def/ontomunicipio#therm-US)<br />[om:nauticalMile-International](http://opendata.caceres.es/def/ontomunicipio#nauticalMile-International)<br />[om:percent](http://opendata.caceres.es/def/ontomunicipio#percent)<br />[om:unitPole](http://opendata.caceres.es/def/ontomunicipio#unitPole)<br />[om:footlambert](http://opendata.caceres.es/def/ontomunicipio#footlambert)<br />[om:SwissFranc](http://opendata.caceres.es/def/ontomunicipio#SwissFranc)<br />[om:mil-Length](http://opendata.caceres.es/def/ontomunicipio#mil-Length)<br />[om:katal](http://opendata.caceres.es/def/ontomunicipio#katal)<br />[om:weber](http://opendata.caceres.es/def/ontomunicipio#weber)<br />[om:month](http://opendata.caceres.es/def/ontomunicipio#month)<br />[om:abmho](http://opendata.caceres.es/def/ontomunicipio#abmho)<br />[om:lumen](http://opendata.caceres.es/def/ontomunicipio#lumen)<br />[om:gray](http://opendata.caceres.es/def/ontomunicipio#gray)<br />[om:mile-USSurvey](http://opendata.caceres.es/def/ontomunicipio#mile-USSurvey)<br />[om:abfarad](http://opendata.caceres.es/def/ontomunicipio#abfarad)<br />[om:micron](http://opendata.caceres.es/def/ontomunicipio#micron)<br />[om:abvolt](http://opendata.caceres.es/def/ontomunicipio#abvolt)<br />[om:jansky](http://opendata.caceres.es/def/ontomunicipio#jansky)<br />[om:lightYear](http://opendata.caceres.es/def/ontomunicipio#lightYear)<br />[om:CanadianDollar](http://opendata.caceres.es/def/ontomunicipio#CanadianDollar)<br />[om:pound-Force](http://opendata.caceres.es/def/ontomunicipio#pound-Force)<br />[om:calorie-15C](http://opendata.caceres.es/def/ontomunicipio#calorie-15C)<br />[om:dryQuart-US](http://opendata.caceres.es/def/ontomunicipio#dryQuart-US)<br />[om:perm-23C](http://opendata.caceres.es/def/ontomunicipio#perm-23C)<br />[om:tablespoon-US](http://opendata.caceres.es/def/ontomunicipio#tablespoon-US)<br />[om:poundal](http://opendata.caceres.es/def/ontomunicipio#poundal)<br />
### solid angle
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SolidAngle`
Description | <p>Solid angle is the ratio of the surface of a portion of a sphere enclosed by the conical surface that forms an angle to the square of the radius of the sphere.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
Sub-classes |[om:AngularSize](http://opendata.caceres.es/def/ontomunicipio#AngularSize) (c)<br />
### solid angle unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SolidAngleUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### soy bean mass fraction
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SoyBeanMassFraction`
Description | <p>The fraction of the mass of soy bean oil in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### specific amylase activity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SpecificAmylaseActivity`
Super-classes |[om:SpecificCatalyticActivity](http://opendata.caceres.es/def/ontomunicipio#SpecificCatalyticActivity) (c)<br />
### specific catalytic activity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SpecificCatalyticActivity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:specificCatalyticActivity-Dimension](http://opendata.caceres.es/def/ontomunicipio#specificCatalyticActivity-Dimension) (c)<br />
Sub-classes |[om:SpecificAmylaseActivity](http://opendata.caceres.es/def/ontomunicipio#SpecificAmylaseActivity) (c)<br />[om:SpecificProteaseActivity](http://opendata.caceres.es/def/ontomunicipio#SpecificProteaseActivity) (c)<br />
### specific catalytic activity unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SpecificCatalyticActivityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### coliform bacteria count (specific)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SpecificColiformBacterieCount`
Super-classes |[om:SpecificViableCount](http://opendata.caceres.es/def/ontomunicipio#SpecificViableCount) (c)<br />
### Corynebacterium bovis count (specific)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SpecificCorynebacteriumBovisCount`
Super-classes |[om:SpecificViableCount](http://opendata.caceres.es/def/ontomunicipio#SpecificViableCount) (c)<br />
### Corynebacterium count (specific)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SpecificCorynebacteriumCount`
Super-classes |[om:SpecificViableCount](http://opendata.caceres.es/def/ontomunicipio#SpecificViableCount) (c)<br />
### specific energy
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SpecificEnergy`
Description | <p>Specific energy is energy per unit mass.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:specificEnergyOrAbsorbedDoseOrDoseEquivalent-Dimension](http://opendata.caceres.es/def/ontomunicipio#specificEnergyOrAbsorbedDoseOrDoseEquivalent-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### specific energy imparted
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SpecificEnergyImparted`
Super-classes |[om:AbsorbedDose](http://opendata.caceres.es/def/ontomunicipio#AbsorbedDose) (c)<br />
### specific energy unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SpecificEnergyUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### Enterobacteriaceae count (specific)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SpecificEnterobacteriaceaeCount`
Super-classes |[om:SpecificViableCount](http://opendata.caceres.es/def/ontomunicipio#SpecificViableCount) (c)<br />
### Enterococcus count (specific)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SpecificEnterococcusCount`
Super-classes |[om:SpecificViableCount](http://opendata.caceres.es/def/ontomunicipio#SpecificViableCount) (c)<br />
### specific entropy
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SpecificEntropy`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:specificEntropyOrSpecificHeatCapacity-Dimension](http://opendata.caceres.es/def/ontomunicipio#specificEntropyOrSpecificHeatCapacity-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### specific entropy unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SpecificEntropyUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### Escherichia coli count (specific)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SpecificEscherichiaColiCount`
Super-classes |[om:SpecificViableCount](http://opendata.caceres.es/def/ontomunicipio#SpecificViableCount) (c)<br />
### specific heat capacity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SpecificHeatCapacity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:specificEntropyOrSpecificHeatCapacity-Dimension](http://opendata.caceres.es/def/ontomunicipio#specificEntropyOrSpecificHeatCapacity-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### specific heat capacity unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SpecificHeatCapacityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### Klebsiella count (specific)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SpecificKlebsiellaCount`
Super-classes |[om:SpecificViableCount](http://opendata.caceres.es/def/ontomunicipio#SpecificViableCount) (c)<br />
### Listeria monocytogenes count (specific)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SpecificListeriaMonocytogenesCount`
Super-classes |[om:SpecificViableCount](http://opendata.caceres.es/def/ontomunicipio#SpecificViableCount) (c)<br />
### specific protease activity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SpecificProteaseActivity`
Super-classes |[om:SpecificCatalyticActivity](http://opendata.caceres.es/def/ontomunicipio#SpecificCatalyticActivity) (c)<br />
### Salmonella count (specific)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SpecificSalmonellaCount`
Super-classes |[om:SpecificViableCount](http://opendata.caceres.es/def/ontomunicipio#SpecificViableCount) (c)<br />
### Serratia marcescens count (specific)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SpecificSerratiaMarcescensCount`
Super-classes |[om:SpecificViableCount](http://opendata.caceres.es/def/ontomunicipio#SpecificViableCount) (c)<br />
### Staphylococcus aureus count (specific)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SpecificStaphylococcusAureusCount`
Super-classes |[om:SpecificViableCount](http://opendata.caceres.es/def/ontomunicipio#SpecificViableCount) (c)<br />
### Streptococcus agalactiae count (specific)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SpecificStreptococcusAgalactiaeCount`
Super-classes |[om:SpecificViableCount](http://opendata.caceres.es/def/ontomunicipio#SpecificViableCount) (c)<br />
### Streptococcus dysgalactiae count (specific)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SpecificStreptococcusDysgalactiaeCount`
Super-classes |[om:SpecificViableCount](http://opendata.caceres.es/def/ontomunicipio#SpecificViableCount) (c)<br />
### Streptococcus uberis count (specific)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SpecificStreptococcusUberisCount`
Super-classes |[om:SpecificViableCount](http://opendata.caceres.es/def/ontomunicipio#SpecificViableCount) (c)<br />
### viable count (specific)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SpecificViableCount`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:SpecificStaphylococcusAureusCount](http://opendata.caceres.es/def/ontomunicipio#SpecificStaphylococcusAureusCount) (c)<br />[om:SpecificSerratiaMarcescensCount](http://opendata.caceres.es/def/ontomunicipio#SpecificSerratiaMarcescensCount) (c)<br />[om:SpecificSalmonellaCount](http://opendata.caceres.es/def/ontomunicipio#SpecificSalmonellaCount) (c)<br />[om:SpecificYeastAndFungiCount](http://opendata.caceres.es/def/ontomunicipio#SpecificYeastAndFungiCount) (c)<br />[om:SpecificKlebsiellaCount](http://opendata.caceres.es/def/ontomunicipio#SpecificKlebsiellaCount) (c)<br />[om:SpecificEnterococcusCount](http://opendata.caceres.es/def/ontomunicipio#SpecificEnterococcusCount) (c)<br />[om:SpecificEnterobacteriaceaeCount](http://opendata.caceres.es/def/ontomunicipio#SpecificEnterobacteriaceaeCount) (c)<br />[om:SpecificCorynebacteriumBovisCount](http://opendata.caceres.es/def/ontomunicipio#SpecificCorynebacteriumBovisCount) (c)<br />[om:SpecificListeriaMonocytogenesCount](http://opendata.caceres.es/def/ontomunicipio#SpecificListeriaMonocytogenesCount) (c)<br />[om:SpecificStreptococcusDysgalactiaeCount](http://opendata.caceres.es/def/ontomunicipio#SpecificStreptococcusDysgalactiaeCount) (c)<br />[om:SpecificStreptococcusUberisCount](http://opendata.caceres.es/def/ontomunicipio#SpecificStreptococcusUberisCount) (c)<br />[om:SpecificEscherichiaColiCount](http://opendata.caceres.es/def/ontomunicipio#SpecificEscherichiaColiCount) (c)<br />[om:SpecificColiformBacterieCount](http://opendata.caceres.es/def/ontomunicipio#SpecificColiformBacterieCount) (c)<br />[om:SpecificCorynebacteriumCount](http://opendata.caceres.es/def/ontomunicipio#SpecificCorynebacteriumCount) (c)<br />[om:SpecificStreptococcusAgalactiaeCount](http://opendata.caceres.es/def/ontomunicipio#SpecificStreptococcusAgalactiaeCount) (c)<br />
### specific viable count unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SpecificViableCountUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### specific volume
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SpecificVolume`
Description | <p>Specific volume is volume per unit mass.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:specificVolume-Dimension](http://opendata.caceres.es/def/ontomunicipio#specificVolume-Dimension) (c)<br />
### specific volume unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SpecificVolumeUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### yeast and fungi count (specific)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SpecificYeastAndFungiCount`
Super-classes |[om:SpecificViableCount](http://opendata.caceres.es/def/ontomunicipio#SpecificViableCount) (c)<br />
### spectral response
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SpectralResponse`
Description | <p>The change in output signal as a function of changes in the wavelength of the input signal.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### speed
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Speed`
Description | <p>Speed is the time rate of motion measured by the distance moved over in unit time.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:speed-Dimension](http://opendata.caceres.es/def/ontomunicipio#speed-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:DrainageSpeed](http://opendata.caceres.es/def/ontomunicipio#DrainageSpeed) (c)<br />[om:Velocity](http://opendata.caceres.es/def/ontomunicipio#Velocity) (c)<br />
### speed unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SpeedUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### square prefixed metre
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SquarePrefixedMetre`
Super-classes |[om:UnitExponentiation](http://opendata.caceres.es/def/ontomunicipio#UnitExponentiation) (c)<br />
Has members |[om:squareMillimetre](http://opendata.caceres.es/def/ontomunicipio#squareMillimetre)<br />[om:squarePetametre](http://opendata.caceres.es/def/ontomunicipio#squarePetametre)<br />[om:squareMicrometre](http://opendata.caceres.es/def/ontomunicipio#squareMicrometre)<br />[om:squarePicometre](http://opendata.caceres.es/def/ontomunicipio#squarePicometre)<br />[om:squareKilometre](http://opendata.caceres.es/def/ontomunicipio#squareKilometre)<br />[om:squareZeptometre](http://opendata.caceres.es/def/ontomunicipio#squareZeptometre)<br />[om:squareDecimetre](http://opendata.caceres.es/def/ontomunicipio#squareDecimetre)<br />[om:squareMegametre](http://opendata.caceres.es/def/ontomunicipio#squareMegametre)<br />[om:squareNanometre](http://opendata.caceres.es/def/ontomunicipio#squareNanometre)<br />[om:squareZettametre](http://opendata.caceres.es/def/ontomunicipio#squareZettametre)<br />[om:squareYottametre](http://opendata.caceres.es/def/ontomunicipio#squareYottametre)<br />[om:squareHectometre](http://opendata.caceres.es/def/ontomunicipio#squareHectometre)<br />[om:squareFemtometre](http://opendata.caceres.es/def/ontomunicipio#squareFemtometre)<br />[om:squareYoctometre](http://opendata.caceres.es/def/ontomunicipio#squareYoctometre)<br />[om:squareCentimetre](http://opendata.caceres.es/def/ontomunicipio#squareCentimetre)<br />[om:squareDecametre](http://opendata.caceres.es/def/ontomunicipio#squareDecametre)<br />[om:squareTerametre](http://opendata.caceres.es/def/ontomunicipio#squareTerametre)<br />[om:squareGigametre](http://opendata.caceres.es/def/ontomunicipio#squareGigametre)<br />[om:squareAttometre](http://opendata.caceres.es/def/ontomunicipio#squareAttometre)<br />[om:squareExametre](http://opendata.caceres.es/def/ontomunicipio#squareExametre)<br />
### Stanton number
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#StantonNumber`
Description | <p>The Stanton number is a dimensionless number that measures the ratio of heat transferred into a fluid to the thermal capacity of fluid.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### Stanton number for mass transfer
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#StantonNumberForMassTransfer`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
### Stanton number for mass transfer unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#StantonNumberForMassTransferUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### Stanton number unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#StantonNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### starch mass fraction
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#StarchMassFraction`
Description | <p>The fraction of the mass of starch in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### starch VA40 mass fraction
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#StarchVA40MassFraction`
Description | <p>The fraction of the mass of starch VA40 in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### starch VA85 mass fraction
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#StarchVA85MassFraction`
Description | <p>The fraction of the mass of starch VA85 in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### stellar aberration
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#StellarAberration`
Description | <p>The apparent angular displacement of the observed position of a celestial object resulting from the motion of the observer. Stellar aberration is divided into diurnal, annual, and secular components.</p>
Super-classes |[om:Aberration](http://opendata.caceres.es/def/ontomunicipio#Aberration) (c)<br />
### stem end rot
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#StemEndRot`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### stem end rot area fraction
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#StemEndRotAreaFraction`
Super-classes |[om:AreaFraction](http://opendata.caceres.es/def/ontomunicipio#AreaFraction) (c)<br />
### stick stone
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#StickStone`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### storage modulus
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#StorageModulus`
Super-classes |[om:DynamicModulus](http://opendata.caceres.es/def/ontomunicipio#DynamicModulus) (c)<br />
Sub-classes |[om:ShearStorageModulus](http://opendata.caceres.es/def/ontomunicipio#ShearStorageModulus) (c)<br />[om:ShearLossModulus](http://opendata.caceres.es/def/ontomunicipio#ShearLossModulus) (c)<br />
### strain
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Strain`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
Sub-classes |[om:StrainTensor](http://opendata.caceres.es/def/ontomunicipio#StrainTensor) (c)<br />[om:VolumeStrain](http://opendata.caceres.es/def/ontomunicipio#VolumeStrain) (c)<br />[om:LinearStrain](http://opendata.caceres.es/def/ontomunicipio#LinearStrain) (c)<br />[om:NormalStrain](http://opendata.caceres.es/def/ontomunicipio#NormalStrain) (c)<br />[om:ShearStrain](http://opendata.caceres.es/def/ontomunicipio#ShearStrain) (c)<br />
### strain tensor
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#StrainTensor`
Super-classes |[om:Strain](http://opendata.caceres.es/def/ontomunicipio#Strain) (c)<br />
### strain unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#StrainUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### straw mass
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#StrawMass`
Super-classes |[om:Mass](http://opendata.caceres.es/def/ontomunicipio#Mass) (c)<br />
### stress
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Stress`
Description | <p>Stress is a force that produces or tends to produce deformation in a body measured by the force applied per unit area.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:pressure-Dimension](http://opendata.caceres.es/def/ontomunicipio#pressure-Dimension) (c)<br />
Sub-classes |[om:ShearStress](http://opendata.caceres.es/def/ontomunicipio#ShearStress) (c)<br />[om:NormalStress](http://opendata.caceres.es/def/ontomunicipio#NormalStress) (c)<br />[om:CompressiveStress](http://opendata.caceres.es/def/ontomunicipio#CompressiveStress) (c)<br />[om:StressTensor](http://opendata.caceres.es/def/ontomunicipio#StressTensor) (c)<br />
### stress tensor
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#StressTensor`
Super-classes |[om:Stress](http://opendata.caceres.es/def/ontomunicipio#Stress) (c)<br />
### stress unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#StressUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### Strömgren magnitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#StroemgrenMagnitude`
Description | <p>A magnitude measured in one of Strömgren's standard passbands (using a standard filter, u, b, v, or y) or in the passbands defined by Crawford (β_narrow or β_wide).</p>
Super-classes |[om:Magnitude](http://opendata.caceres.es/def/ontomunicipio#Magnitude) (c)<br />
Sub-classes |[om:uMagnitude](http://opendata.caceres.es/def/ontomunicipio#uMagnitude) (c)<br />[om:yMagnitude](http://opendata.caceres.es/def/ontomunicipio#yMagnitude) (c)<br />[om:bMagnitude](http://opendata.caceres.es/def/ontomunicipio#bMagnitude) (c)<br />[om:vMagnitude](http://opendata.caceres.es/def/ontomunicipio#vMagnitude) (c)<br />[om:BetaNarrowMagnitude](http://opendata.caceres.es/def/ontomunicipio#BetaNarrowMagnitude) (c)<br />[om:BetaWideMagnitude](http://opendata.caceres.es/def/ontomunicipio#BetaWideMagnitude) (c)<br />
### Strouhal number
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#StrouhalNumber`
Description | <p>The Strouhal number is a dimensionless number that describes oscillating flow mechanisms.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
### Strouhal number unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#StrouhalNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### sugar mass fraction
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SugarMassFraction`
Description | <p>The fraction of the mass of sugar in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### supergalactic latitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SupergalacticLatitude`
Description | <p>The angular distance on the celestial sphere north or south of the supergalactic equator. It is measured along the great circle passing through the object and the supergalactic poles and perpendicular to the supergalactic equator.</p>
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
### supergalactic longitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SupergalacticLongitude`
Description | <p>The angular distance on the celestial sphere measured clockwise from the supergalactic centre (as defined by the International Astronomical Union (IAU)) along the supergalactic equator to the intersection with the great circle drawn from the supergalactic north pole through the object.</p>
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
### surface tension
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SurfaceTension`
Description | <p>Surface tension is an attractive property of the surface of a liquid.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:surfaceTension-Dimension](http://opendata.caceres.es/def/ontomunicipio#surfaceTension-Dimension) (c)<br />
### surface tension unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SurfaceTensionUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### symbol rate
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SymbolRate`
Description | <p>Symbol rate is the number of symbol changes (signalling events) made to the transmission medium per second using a digitally modulated signal or a line code.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Has members |[om:oneDistinctSymbolChangeOrSignallingEventMadeToTheTransmissionMediumPerSecondInADigitallyModulatedSignalOrALineCode](http://opendata.caceres.es/def/ontomunicipio#oneDistinctSymbolChangeOrSignallingEventMadeToTheTransmissionMediumPerSecondInADigitallyModulatedSignalOrALineCode)<br />
### symbol rate unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SymbolRateUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### system of units
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#SystemOfUnits`
Description | <p>In order to achieve a coherent, interdependent set of units of measure in the wide variety of units that exist, units are organised in systems of units. A system of units is based on a set of units chosen by convention to be the system’s base units, units that are considered to be mutually independent (i.e., can’t be expressed in terms of each other).</p>
In domain of |[om:hasBaseQuantity](http://opendata.caceres.es/def/ontomunicipio#hasBaseQuantity) (op)<br />[om:hasBaseUnit](http://opendata.caceres.es/def/ontomunicipio#hasBaseUnit) (op)<br />[om:hasDerivedUnit](http://opendata.caceres.es/def/ontomunicipio#hasDerivedUnit) (op)<br />[om:hasDerivedQuantity](http://opendata.caceres.es/def/ontomunicipio#hasDerivedQuantity) (op)<br />
Has members |[om:InternationalSystemOfUnits](http://opendata.caceres.es/def/ontomunicipio#InternationalSystemOfUnits)<br />[om:centimetre-Gram-SecondElectromagneticSystemOfUnits](http://opendata.caceres.es/def/ontomunicipio#centimetre-Gram-SecondElectromagneticSystemOfUnits)<br />[om:metre-Kilogram-Second-AmpereSystemOfUnits](http://opendata.caceres.es/def/ontomunicipio#metre-Kilogram-Second-AmpereSystemOfUnits)<br />[om:centimetre-Gram-Second-FranklinSystemOfUnits](http://opendata.caceres.es/def/ontomunicipio#centimetre-Gram-Second-FranklinSystemOfUnits)<br />[om:centimetre-Gram-SecondSystemOfUnits](http://opendata.caceres.es/def/ontomunicipio#centimetre-Gram-SecondSystemOfUnits)<br />[om:centimetre-Gram-Second-BiotSystemOfUnits](http://opendata.caceres.es/def/ontomunicipio#centimetre-Gram-Second-BiotSystemOfUnits)<br />[om:centimetre-Gram-SecondElectrostaticSystemOfUnits](http://opendata.caceres.es/def/ontomunicipio#centimetre-Gram-SecondElectrostaticSystemOfUnits)<br />[om:GaussianSystemOfUnits](http://opendata.caceres.es/def/ontomunicipio#GaussianSystemOfUnits)<br />
### temperature
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Temperature`
Description | <p>Temperature is the extent to which an object is hot.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasScale](http://opendata.caceres.es/def/ontomunicipio#hasScale) (op) **only** ()<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:thermodynamicTemperature-Dimension](http://opendata.caceres.es/def/ontomunicipio#thermodynamicTemperature-Dimension) (c)<br />
Sub-classes |[om:FahrenheitTemperature](http://opendata.caceres.es/def/ontomunicipio#FahrenheitTemperature) (c)<br />[om:RankineTemperature](http://opendata.caceres.es/def/ontomunicipio#RankineTemperature) (c)<br />[om:ReaumurTemperature](http://opendata.caceres.es/def/ontomunicipio#ReaumurTemperature) (c)<br />[om:CelsiusTemperature](http://opendata.caceres.es/def/ontomunicipio#CelsiusTemperature) (c)<br />[om:ThermodynamicTemperature](http://opendata.caceres.es/def/ontomunicipio#ThermodynamicTemperature) (c)<br />
### temperature rate
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#TemperatureRate`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### temperature rate unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#TemperatureRateUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### temperature unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#TemperatureUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
Sub-classes |[om:ThermodynamicTemperatureUnit](http://opendata.caceres.es/def/ontomunicipio#ThermodynamicTemperatureUnit) (c)<br />[om:RankineTemperatureUnit](http://opendata.caceres.es/def/ontomunicipio#RankineTemperatureUnit) (c)<br />[om:CelsiusTemperatureUnit](http://opendata.caceres.es/def/ontomunicipio#CelsiusTemperatureUnit) (c)<br />[om:FahrenheitTemperatureUnit](http://opendata.caceres.es/def/ontomunicipio#FahrenheitTemperatureUnit) (c)<br />[om:ReaumurTemperatureUnit](http://opendata.caceres.es/def/ontomunicipio#ReaumurTemperatureUnit) (c)<br />
### Temperature_scale
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Temperature_scale`
Super-classes |[om:Scale](http://opendata.caceres.es/def/ontomunicipio#Scale) (c)<br />
### thermal conductivity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ThermalConductivity`
Description | <p>Termal conductivity indicates the ability of a material to conduct heat.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:thermalConductivity-Dimension](http://opendata.caceres.es/def/ontomunicipio#thermalConductivity-Dimension) (c)<br />
### thermal conductivity unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ThermalConductivityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### thermal diffusivity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ThermalDiffusivity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### thermal diffusivity unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ThermalDiffusivityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### thermal insulance
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ThermalInsulance`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:thermalInsulance-Dimension](http://opendata.caceres.es/def/ontomunicipio#thermalInsulance-Dimension) (c)<br />
### thermal insulance unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ThermalInsulanceUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### thermal resistance
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ThermalResistance`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:thermalResistance-Dimension](http://opendata.caceres.es/def/ontomunicipio#thermalResistance-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### thermal resistance unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ThermalResistanceUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### thermodynamic temperature
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ThermodynamicTemperature`
Description | <p>Thermodynamic temperature is the absolute measure of temperature. Its zero point is the temperature at which the particle constituents of matter have minimal motion and can be no colder. Thermodynamic temperature is a base quantity in the International System of Units.</p>
Super-classes |[om:Temperature](http://opendata.caceres.es/def/ontomunicipio#Temperature) (c)<br />
Restrictions |[om:hasScale](http://opendata.caceres.es/def/ontomunicipio#hasScale) (op) **value** [om:KelvinScale](http://opendata.caceres.es/def/ontomunicipio#KelvinScale) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:BrightnessTemperature](http://opendata.caceres.es/def/ontomunicipio#BrightnessTemperature) (c)<br />[om:IonizationTemperature](http://opendata.caceres.es/def/ontomunicipio#IonizationTemperature) (c)<br />[om:ColourTemperature](http://opendata.caceres.es/def/ontomunicipio#ColourTemperature) (c)<br />[om:ElectronTemperature](http://opendata.caceres.es/def/ontomunicipio#ElectronTemperature) (c)<br />
Has members |[om:_127316OfTheThermodynamicTemperatureOfTheTriplePointOfWater](http://opendata.caceres.es/def/ontomunicipio#_127316OfTheThermodynamicTemperatureOfTheTriplePointOfWater)<br />[om:thermodynamicTemperatureOfTheTriplePointOfWater](http://opendata.caceres.es/def/ontomunicipio#thermodynamicTemperatureOfTheTriplePointOfWater)<br />
### thermodynamic temperature scale
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ThermodynamicTemperatureScale`
Super-classes |[om:Scale](http://opendata.caceres.es/def/ontomunicipio#Scale) (c)<br />
### thermodynamic temperature unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ThermodynamicTemperatureUnit`
Super-classes |[om:TemperatureUnit](http://opendata.caceres.es/def/ontomunicipio#TemperatureUnit) (c)<br />
### thickness
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Thickness`
Super-classes |[om:Length](http://opendata.caceres.es/def/ontomunicipio#Length) (c)<br />
### thrust
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Thrust`
Description | <p>Thrust is a reaction force that is caused by an accelerated mass expelled by a system in one direction.</p>
Super-classes |[om:Force](http://opendata.caceres.es/def/ontomunicipio#Force) (c)<br />
### Thuan and Gunn magnitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ThuanAndGunnMagnitude`
Description | <p>A magnitude measured in one of Thuan and Gunn's standard passbands (using a standard filter, i.e. g).</p>
Super-classes |[om:Magnitude](http://opendata.caceres.es/def/ontomunicipio#Magnitude) (c)<br />
Sub-classes |[om:gMagnitude](http://opendata.caceres.es/def/ontomunicipio#gMagnitude) (c)<br />
### time
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Time`
Description | <p>Time is a base quantity in the International System of Units and other systems of units. It is measured by numbers of repetitions of cyclical events.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:time-Dimension](http://opendata.caceres.es/def/ontomunicipio#time-Dimension) (c)<br />
Sub-classes |[om:VaseLife](http://opendata.caceres.es/def/ontomunicipio#VaseLife) (c)<br />[om:Date](http://opendata.caceres.es/def/ontomunicipio#Date) (c)<br />[om:Period](http://opendata.caceres.es/def/ontomunicipio#Period) (c)<br />[om:PeriodOfVariability](http://opendata.caceres.es/def/ontomunicipio#PeriodOfVariability) (c)<br />[om:LightTime](http://opendata.caceres.es/def/ontomunicipio#LightTime) (c)<br />[om:TimeConstant](http://opendata.caceres.es/def/ontomunicipio#TimeConstant) (c)<br />[om:Duration](http://opendata.caceres.es/def/ontomunicipio#Duration) (c)<br />[om:Half-Life](http://opendata.caceres.es/def/ontomunicipio#Half-Life) (c)<br />
### time constant
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#TimeConstant`
Description | <p>Time required to approach (1-1/e) of the final output value of a detector (about 63%) (Kitchin, Astrophysical Techniques, IoP, Table 1.1.2).</p>
Super-classes |[om:Time](http://opendata.caceres.es/def/ontomunicipio#Time) (c)<br />
### time unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#TimeUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### top mass
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#TopMass`
Super-classes |[om:Mass](http://opendata.caceres.es/def/ontomunicipio#Mass) (c)<br />
### torque
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Torque`
Description | <p>Torque is the effectiveness of a force to produce rotation about an axis, measured by the product of the force and the perpendicular distance from the line of action of the force to the axis.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:energy-Dimension](http://opendata.caceres.es/def/ontomunicipio#energy-Dimension) (c)<br />
### torque unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#TorqueUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### total 3D start-end distance
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Total3DStartEndDistance`
Super-classes |[om:Distance](http://opendata.caceres.es/def/ontomunicipio#Distance) (c)<br />
### total density parameter
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#TotalDensityParameter`
Description | <p>The total density parameter.</p>
Super-classes |[om:DensityParameter](http://opendata.caceres.es/def/ontomunicipio#DensityParameter) (c)<br />
### total distance travelled
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#TotalDistanceTravelled`
Super-classes |[om:Distance](http://opendata.caceres.es/def/ontomunicipio#Distance) (c)<br />
### total number buds
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#TotalNumberBuds`
Super-classes |[om:NumberBuds](http://opendata.caceres.es/def/ontomunicipio#NumberBuds) (c)<br />
### total number flowers
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#TotalNumberFlowers`
Super-classes |[om:NumberFlowers](http://opendata.caceres.es/def/ontomunicipio#NumberFlowers) (c)<br />
### total number leaves
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#TotalNumberLeaves`
Super-classes |[om:NumberLeaves](http://opendata.caceres.es/def/ontomunicipio#NumberLeaves) (c)<br />
### true distance modulus
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#TrueDistanceModulus`
Super-classes |[om:DistanceModulus](http://opendata.caceres.es/def/ontomunicipio#DistanceModulus) (c)<br />
### tween mass fraction
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#TweenMassFraction`
Description | <p>The fraction of the mass of tween in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### Tycho broadband magnitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#TychoBroadbandMagnitude`
Description | <p>Broadband Tycho magnitude (formed from B and V magintude measurements.</p>
Super-classes |[om:Magnitude](http://opendata.caceres.es/def/ontomunicipio#Magnitude) (c)<br />
### U magnitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#UMagnitude`
Description | <p>Johnson U magnitude. The Johnson U band is a standard passband in the ultraviolet area. The central wavelength is 365nm and the bandwidth is 70nm.  The filter to be used is the Corning 9863 filter.</p>
Super-classes |[om:JohnsonMagnitude](http://opendata.caceres.es/def/ontomunicipio#JohnsonMagnitude) (c)<br />
### unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Unit`
Description | <p>A unit of measure is a definite magnitude of a quantity, defined and adopted by convention or by law. It is used as a standard for measurement of the same quantity, where any other value of the quantity can be expressed as a simple multiple of the unit. For example, length is a quantity; the metre is a unit of length that represents a definite predetermined length. When we say 10 metre (or 10 m), we actually mean 10 times the definite predetermined length called "metre".</p>
Sub-classes |[om:SpecificVolumeUnit](http://opendata.caceres.es/def/ontomunicipio#SpecificVolumeUnit) (c)<br />[om:AngularAccelerationUnit](http://opendata.caceres.es/def/ontomunicipio#AngularAccelerationUnit) (c)<br />[om:ElectricChargeUnit](http://opendata.caceres.es/def/ontomunicipio#ElectricChargeUnit) (c)<br />[om:SpecificHeatCapacityUnit](http://opendata.caceres.es/def/ontomunicipio#SpecificHeatCapacityUnit) (c)<br />[om:AreaDensityRateUnit](http://opendata.caceres.es/def/ontomunicipio#AreaDensityRateUnit) (c)<br />[om:RatioUnit](http://opendata.caceres.es/def/ontomunicipio#RatioUnit) (c)<br />[om:TorqueUnit](http://opendata.caceres.es/def/ontomunicipio#TorqueUnit) (c)<br />[om:SpecificViableCountUnit](http://opendata.caceres.es/def/ontomunicipio#SpecificViableCountUnit) (c)<br />[om:EnergyUnit](http://opendata.caceres.es/def/ontomunicipio#EnergyUnit) (c)<br />[om:TemperatureRateUnit](http://opendata.caceres.es/def/ontomunicipio#TemperatureRateUnit) (c)<br />[om:Permeance-MaterialsScienceUnit](http://opendata.caceres.es/def/ontomunicipio#Permeance-MaterialsScienceUnit) (c)<br />[om:CowlingNumberUnit](http://opendata.caceres.es/def/ontomunicipio#CowlingNumberUnit) (c)<br />[om:CurvatureConstantUnit](http://opendata.caceres.es/def/ontomunicipio#CurvatureConstantUnit) (c)<br />[om:ElectricalConductivityUnit](http://opendata.caceres.es/def/ontomunicipio#ElectricalConductivityUnit) (c)<br />[om:AngularMomentumUnit](http://opendata.caceres.es/def/ontomunicipio#AngularMomentumUnit) (c)<br />[om:ExposureToXAndGammaRaysUnit](http://opendata.caceres.es/def/ontomunicipio#ExposureToXAndGammaRaysUnit) (c)<br />[om:KnudsenNumberUnit](http://opendata.caceres.es/def/ontomunicipio#KnudsenNumberUnit) (c)<br />[om:RadianceUnit](http://opendata.caceres.es/def/ontomunicipio#RadianceUnit) (c)<br />[om:HeatCapacityUnit](http://opendata.caceres.es/def/ontomunicipio#HeatCapacityUnit) (c)<br />[om:ForceUnit](http://opendata.caceres.es/def/ontomunicipio#ForceUnit) (c)<br />[om:SpecificCatalyticActivityUnit](http://opendata.caceres.es/def/ontomunicipio#SpecificCatalyticActivityUnit) (c)<br />[om:StrainUnit](http://opendata.caceres.es/def/ontomunicipio#StrainUnit) (c)<br />[om:ElectricCurrentUnit](http://opendata.caceres.es/def/ontomunicipio#ElectricCurrentUnit) (c)<br />[om:ThermalResistanceUnit](http://opendata.caceres.es/def/ontomunicipio#ThermalResistanceUnit) (c)<br />[om:NumberDensityUnit](http://opendata.caceres.es/def/ontomunicipio#NumberDensityUnit) (c)<br />[om:AmountOfSubstanceConcentrationUnit](http://opendata.caceres.es/def/ontomunicipio#AmountOfSubstanceConcentrationUnit) (c)<br />[om:ElectricalResistanceUnit](http://opendata.caceres.es/def/ontomunicipio#ElectricalResistanceUnit) (c)<br />[om:AreaFractionUnit](http://opendata.caceres.es/def/ontomunicipio#AreaFractionUnit) (c)<br />[om:NumberUnit](http://opendata.caceres.es/def/ontomunicipio#NumberUnit) (c)<br />[om:MolarVolumeUnit](http://opendata.caceres.es/def/ontomunicipio#MolarVolumeUnit) (c)<br />[om:ElectricalResistivityUnit](http://opendata.caceres.es/def/ontomunicipio#ElectricalResistivityUnit) (c)<br />[om:SpecificEntropyUnit](http://opendata.caceres.es/def/ontomunicipio#SpecificEntropyUnit) (c)<br />[om:CompoundUnit](http://opendata.caceres.es/def/ontomunicipio#CompoundUnit) (c)<br />[om:EulerNumberUnit](http://opendata.caceres.es/def/ontomunicipio#EulerNumberUnit) (c)<br />[om:LuminousFluxUnit](http://opendata.caceres.es/def/ontomunicipio#LuminousFluxUnit) (c)<br />[om:VolumeFractionUnit](http://opendata.caceres.es/def/ontomunicipio#VolumeFractionUnit) (c)<br />[om:GasConstantUnit](http://opendata.caceres.es/def/ontomunicipio#GasConstantUnit) (c)<br />[om:AreaDensityUnit](http://opendata.caceres.es/def/ontomunicipio#AreaDensityUnit) (c)<br />[om:AmountOfMoneyUnit](http://opendata.caceres.es/def/ontomunicipio#AmountOfMoneyUnit) (c)<br />[om:SurfaceTensionUnit](http://opendata.caceres.es/def/ontomunicipio#SurfaceTensionUnit) (c)<br />[om:InformationCapacityUnit](http://opendata.caceres.es/def/ontomunicipio#InformationCapacityUnit) (c)<br />[om:StrouhalNumberUnit](http://opendata.caceres.es/def/ontomunicipio#StrouhalNumberUnit) (c)<br />[om:ColumnNumberDensityUnit](http://opendata.caceres.es/def/ontomunicipio#ColumnNumberDensityUnit) (c)<br />[om:GrashofNumberUnit](http://opendata.caceres.es/def/ontomunicipio#GrashofNumberUnit) (c)<br />[om:SpecificEnergyUnit](http://opendata.caceres.es/def/ontomunicipio#SpecificEnergyUnit) (c)<br />[om:CatalyticActivityUnit](http://opendata.caceres.es/def/ontomunicipio#CatalyticActivityUnit) (c)<br />[om:MachNumberUnit](http://opendata.caceres.es/def/ontomunicipio#MachNumberUnit) (c)<br />[om:TimeUnit](http://opendata.caceres.es/def/ontomunicipio#TimeUnit) (c)<br />[om:FourierNumberForMassTransferUnit](http://opendata.caceres.es/def/ontomunicipio#FourierNumberForMassTransferUnit) (c)<br />[om:FirstCowlingNumberUnit](http://opendata.caceres.es/def/ontomunicipio#FirstCowlingNumberUnit) (c)<br />[om:Permeance-ElectromagneticUnit](http://opendata.caceres.es/def/ontomunicipio#Permeance-ElectromagneticUnit) (c)<br />[om:ThermalDiffusivityUnit](http://opendata.caceres.es/def/ontomunicipio#ThermalDiffusivityUnit) (c)<br />[om:DynamicViscosityUnit](http://opendata.caceres.es/def/ontomunicipio#DynamicViscosityUnit) (c)<br />[om:AccelerationUnit](http://opendata.caceres.es/def/ontomunicipio#AccelerationUnit) (c)<br />[om:DensityParameterUnit](http://opendata.caceres.es/def/ontomunicipio#DensityParameterUnit) (c)<br />[om:QuantityOfDimensionOneUnit](http://opendata.caceres.es/def/ontomunicipio#QuantityOfDimensionOneUnit) (c)<br />[om:ShearRateUnit](http://opendata.caceres.es/def/ontomunicipio#ShearRateUnit) (c)<br />[om:VolumeUnit](http://opendata.caceres.es/def/ontomunicipio#VolumeUnit) (c)<br />[om:HubbleConstantUnit](http://opendata.caceres.es/def/ontomunicipio#HubbleConstantUnit) (c)<br />[om:AngularSpeedUnit](http://opendata.caceres.es/def/ontomunicipio#AngularSpeedUnit) (c)<br />[om:RelativeHumidityUnit](http://opendata.caceres.es/def/ontomunicipio#RelativeHumidityUnit) (c)<br />[om:WavenumberUnit](http://opendata.caceres.es/def/ontomunicipio#WavenumberUnit) (c)<br />[om:AmountOfSubstanceFractionUnit](http://opendata.caceres.es/def/ontomunicipio#AmountOfSubstanceFractionUnit) (c)<br />[om:StressUnit](http://opendata.caceres.es/def/ontomunicipio#StressUnit) (c)<br />[om:FluidityUnit](http://opendata.caceres.es/def/ontomunicipio#FluidityUnit) (c)<br />[om:MassFractionUnit](http://opendata.caceres.es/def/ontomunicipio#MassFractionUnit) (c)<br />[om:DynamicRangeUnit](http://opendata.caceres.es/def/ontomunicipio#DynamicRangeUnit) (c)<br />[om:HartmannNumberUnit](http://opendata.caceres.es/def/ontomunicipio#HartmannNumberUnit) (c)<br />[om:PecletNumberUnit](http://opendata.caceres.es/def/ontomunicipio#PecletNumberUnit) (c)<br />[om:EnergyDensityUnit](http://opendata.caceres.es/def/ontomunicipio#EnergyDensityUnit) (c)<br />[om:ElectricDipoleMomentUnit](http://opendata.caceres.es/def/ontomunicipio#ElectricDipoleMomentUnit) (c)<br />[om:PermittivityUnit](http://opendata.caceres.es/def/ontomunicipio#PermittivityUnit) (c)<br />[om:PecletNumberForMassTransferUnit](http://opendata.caceres.es/def/ontomunicipio#PecletNumberForMassTransferUnit) (c)<br />[om:IlluminanceUnit](http://opendata.caceres.es/def/ontomunicipio#IlluminanceUnit) (c)<br />[om:TemperatureUnit](http://opendata.caceres.es/def/ontomunicipio#TemperatureUnit) (c)<br />[om:PowerDensityUnit](http://opendata.caceres.es/def/ontomunicipio#PowerDensityUnit) (c)<br />[om:ElectricPotentialUnit](http://opendata.caceres.es/def/ontomunicipio#ElectricPotentialUnit) (c)<br />[om:MassFlowUnit](http://opendata.caceres.es/def/ontomunicipio#MassFlowUnit) (c)<br />[om:SpeedUnit](http://opendata.caceres.es/def/ontomunicipio#SpeedUnit) (c)<br />[om:DecelerationParameterUnit](http://opendata.caceres.es/def/ontomunicipio#DecelerationParameterUnit) (c)<br />[om:KinematicViscosityUnit](http://opendata.caceres.es/def/ontomunicipio#KinematicViscosityUnit) (c)<br />[om:ElectricFluxDensityUnit](http://opendata.caceres.es/def/ontomunicipio#ElectricFluxDensityUnit) (c)<br />[om:MomentOfForceUnit](http://opendata.caceres.es/def/ontomunicipio#MomentOfForceUnit) (c)<br />[om:CatalyticActivityConcentrationUnit](http://opendata.caceres.es/def/ontomunicipio#CatalyticActivityConcentrationUnit) (c)<br />[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />[om:CapacitanceUnit](http://opendata.caceres.es/def/ontomunicipio#CapacitanceUnit) (c)<br />[om:MagneticFieldUnit](http://opendata.caceres.es/def/ontomunicipio#MagneticFieldUnit) (c)<br />[om:ThermalInsulanceUnit](http://opendata.caceres.es/def/ontomunicipio#ThermalInsulanceUnit) (c)<br />[om:MagneticReynoldsNumberUnit](http://opendata.caceres.es/def/ontomunicipio#MagneticReynoldsNumberUnit) (c)<br />[om:HeatTransferCoefficientUnit](http://opendata.caceres.es/def/ontomunicipio#HeatTransferCoefficientUnit) (c)<br />[om:LuminousEnergyUnit](http://opendata.caceres.es/def/ontomunicipio#LuminousEnergyUnit) (c)<br />[om:EntropyUnit](http://opendata.caceres.es/def/ontomunicipio#EntropyUnit) (c)<br />[om:VolumetricViableCountUnit](http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCountUnit) (c)<br />[om:AmountOfSubstanceFlowUnit](http://opendata.caceres.es/def/ontomunicipio#AmountOfSubstanceFlowUnit) (c)<br />[om:FrequencyUnit](http://opendata.caceres.es/def/ontomunicipio#FrequencyUnit) (c)<br />[om:LewisNumberUnit](http://opendata.caceres.es/def/ontomunicipio#LewisNumberUnit) (c)<br />[om:MassUnit](http://opendata.caceres.es/def/ontomunicipio#MassUnit) (c)<br />[om:WeberNumberUnit](http://opendata.caceres.es/def/ontomunicipio#WeberNumberUnit) (c)<br />[om:SolidAngleUnit](http://opendata.caceres.es/def/ontomunicipio#SolidAngleUnit) (c)<br />[om:MolarMassUnit](http://opendata.caceres.es/def/ontomunicipio#MolarMassUnit) (c)<br />[om:MomentumUnit](http://opendata.caceres.es/def/ontomunicipio#MomentumUnit) (c)<br />[om:ActionUnit](http://opendata.caceres.es/def/ontomunicipio#ActionUnit) (c)<br />[om:PermeabilityOfFreeSpaceUnit](http://opendata.caceres.es/def/ontomunicipio#PermeabilityOfFreeSpaceUnit) (c)<br />[om:LengthUnit](http://opendata.caceres.es/def/ontomunicipio#LengthUnit) (c)<br />[om:SchmidtNumberUnit](http://opendata.caceres.es/def/ontomunicipio#SchmidtNumberUnit) (c)<br />[om:ActivityUnit](http://opendata.caceres.es/def/ontomunicipio#ActivityUnit) (c)<br />[om:PowerUnit](http://opendata.caceres.es/def/ontomunicipio#PowerUnit) (c)<br />[om:FroudeNumberUnit](http://opendata.caceres.es/def/ontomunicipio#FroudeNumberUnit) (c)<br />[om:MagnetomotiveForceUnit](http://opendata.caceres.es/def/ontomunicipio#MagnetomotiveForceUnit) (c)<br />[om:CurrentDensityUnit](http://opendata.caceres.es/def/ontomunicipio#CurrentDensityUnit) (c)<br />[om:LuminousIntensityUnit](http://opendata.caceres.es/def/ontomunicipio#LuminousIntensityUnit) (c)<br />[om:StantonNumberUnit](http://opendata.caceres.es/def/ontomunicipio#StantonNumberUnit) (c)<br />[om:DetectivityUnit](http://opendata.caceres.es/def/ontomunicipio#DetectivityUnit) (c)<br />[om:Permeability-EarthScienceUnit](http://opendata.caceres.es/def/ontomunicipio#Permeability-EarthScienceUnit) (c)<br />[om:FourierNumberUnit](http://opendata.caceres.es/def/ontomunicipio#FourierNumberUnit) (c)<br />[om:AmountOfSubstanceUnit](http://opendata.caceres.es/def/ontomunicipio#AmountOfSubstanceUnit) (c)<br />[om:AbsorbedDoseUnit](http://opendata.caceres.es/def/ontomunicipio#AbsorbedDoseUnit) (c)<br />[om:DoseEquivalentUnit](http://opendata.caceres.es/def/ontomunicipio#DoseEquivalentUnit) (c)<br />[om:ExposureUnit](http://opendata.caceres.es/def/ontomunicipio#ExposureUnit) (c)<br />[om:LuminousEfficacyUnit](http://opendata.caceres.es/def/ontomunicipio#LuminousEfficacyUnit) (c)<br />[om:LuminanceUnit](http://opendata.caceres.es/def/ontomunicipio#LuminanceUnit) (c)<br />[om:AbsorbedDoseRateUnit](http://opendata.caceres.es/def/ontomunicipio#AbsorbedDoseRateUnit) (c)<br />[om:MolarHeatCapacityUnit](http://opendata.caceres.es/def/ontomunicipio#MolarHeatCapacityUnit) (c)<br />[om:ThermalConductivityUnit](http://opendata.caceres.es/def/ontomunicipio#ThermalConductivityUnit) (c)<br />[om:InductanceUnit](http://opendata.caceres.es/def/ontomunicipio#InductanceUnit) (c)<br />[om:SymbolRateUnit](http://opendata.caceres.es/def/ontomunicipio#SymbolRateUnit) (c)<br />[om:StantonNumberForMassTransferUnit](http://opendata.caceres.es/def/ontomunicipio#StantonNumberForMassTransferUnit) (c)<br />[om:ResponsivityUnit](http://opendata.caceres.es/def/ontomunicipio#ResponsivityUnit) (c)<br />[om:ElectricChargeDensityUnit](http://opendata.caceres.es/def/ontomunicipio#ElectricChargeDensityUnit) (c)<br />[om:MolalityUnit](http://opendata.caceres.es/def/ontomunicipio#MolalityUnit) (c)<br />[om:MolarEnergyUnit](http://opendata.caceres.es/def/ontomunicipio#MolarEnergyUnit) (c)<br />[om:QuantumEfficiencyUnit](http://opendata.caceres.es/def/ontomunicipio#QuantumEfficiencyUnit) (c)<br />[om:SingularUnit](http://opendata.caceres.es/def/ontomunicipio#SingularUnit) (c)<br />[om:ReluctanceUnit](http://opendata.caceres.es/def/ontomunicipio#ReluctanceUnit) (c)<br />[om:ReynoldsNumberUnit](http://opendata.caceres.es/def/ontomunicipio#ReynoldsNumberUnit) (c)<br />[om:UnitMultiple](http://opendata.caceres.es/def/ontomunicipio#UnitMultiple) (c)<br />[om:DensityUnit](http://opendata.caceres.es/def/ontomunicipio#DensityUnit) (c)<br />[om:NusseltNumberForMassTransferUnit](http://opendata.caceres.es/def/ontomunicipio#NusseltNumberForMassTransferUnit) (c)<br />[om:VolumetricFlowRateUnit](http://opendata.caceres.es/def/ontomunicipio#VolumetricFlowRateUnit) (c)<br />[om:AreaUnit](http://opendata.caceres.es/def/ontomunicipio#AreaUnit) (c)<br />[om:VolumetricHeatCapacityUnit](http://opendata.caceres.es/def/ontomunicipio#VolumetricHeatCapacityUnit) (c)<br />[om:ElectricalConductanceUnit](http://opendata.caceres.es/def/ontomunicipio#ElectricalConductanceUnit) (c)<br />[om:MagnitudeUnit](http://opendata.caceres.es/def/ontomunicipio#MagnitudeUnit) (c)<br />[om:NusseltNumberUnit](http://opendata.caceres.es/def/ontomunicipio#NusseltNumberUnit) (c)<br />[om:MolarEntropyUnit](http://opendata.caceres.es/def/ontomunicipio#MolarEntropyUnit) (c)<br />[om:ElectricFieldUnit](http://opendata.caceres.es/def/ontomunicipio#ElectricFieldUnit) (c)<br />[om:MagneticFluxUnit](http://opendata.caceres.es/def/ontomunicipio#MagneticFluxUnit) (c)<br />[om:RayleighNumberUnit](http://opendata.caceres.es/def/ontomunicipio#RayleighNumberUnit) (c)<br />[om:PressureUnit](http://opendata.caceres.es/def/ontomunicipio#PressureUnit) (c)<br />[om:PercentageUnit](http://opendata.caceres.es/def/ontomunicipio#PercentageUnit) (c)<br />[om:GrashofNumberForMassTransferUnit](http://opendata.caceres.es/def/ontomunicipio#GrashofNumberForMassTransferUnit) (c)<br />[om:AlfvenNumberUnit](http://opendata.caceres.es/def/ontomunicipio#AlfvenNumberUnit) (c)<br />[om:RadiantIntensityUnit](http://opendata.caceres.es/def/ontomunicipio#RadiantIntensityUnit) (c)<br />[om:AngleUnit](http://opendata.caceres.es/def/ontomunicipio#AngleUnit) (c)<br />[om:MomentOfInertiaUnit](http://opendata.caceres.es/def/ontomunicipio#MomentOfInertiaUnit) (c)<br />[om:PrandtlNumberUnit](http://opendata.caceres.es/def/ontomunicipio#PrandtlNumberUnit) (c)<br />[om:MagneticFluxDensityUnit](http://opendata.caceres.es/def/ontomunicipio#MagneticFluxDensityUnit) (c)<br />
In range of |[om:hasUnit](http://opendata.caceres.es/def/ontomunicipio#hasUnit) (op)<br />[om:hasDerivedUnit](http://opendata.caceres.es/def/ontomunicipio#hasDerivedUnit) (op)<br />[om:hasBaseUnit](http://opendata.caceres.es/def/ontomunicipio#hasBaseUnit) (op)<br />[om:commonlyHasUnit](http://opendata.caceres.es/def/ontomunicipio#commonlyHasUnit) (op)<br />[om:usesUnit](http://opendata.caceres.es/def/ontomunicipio#usesUnit) (op)<br />
Has members |[om:euro](http://opendata.caceres.es/def/ontomunicipio#euro)<br />[om:stokes](http://opendata.caceres.es/def/ontomunicipio#stokes)<br />[om:poundApothecaries](http://opendata.caceres.es/def/ontomunicipio#poundApothecaries)<br />[om:peck-US](http://opendata.caceres.es/def/ontomunicipio#peck-US)<br />[om:JapaneseYen](http://opendata.caceres.es/def/ontomunicipio#JapaneseYen)<br />[om:_1-5](http://opendata.caceres.es/def/ontomunicipio#_1-5)<br />[om:sievert](http://opendata.caceres.es/def/ontomunicipio#sievert)<br />[om:gram](http://opendata.caceres.es/def/ontomunicipio#gram)<br />[om:ton-ShortAssay](http://opendata.caceres.es/def/ontomunicipio#ton-ShortAssay)<br />[om:mho](http://opendata.caceres.es/def/ontomunicipio#mho)<br />[om:dyne](http://opendata.caceres.es/def/ontomunicipio#dyne)<br />[om:tonne](http://opendata.caceres.es/def/ontomunicipio#tonne)<br />[om:poundAvoirdupois](http://opendata.caceres.es/def/ontomunicipio#poundAvoirdupois)<br />[om:acre-International](http://opendata.caceres.es/def/ontomunicipio#acre-International)<br />[om:day](http://opendata.caceres.es/def/ontomunicipio#day)<br />[om:byte](http://opendata.caceres.es/def/ontomunicipio#byte)<br />[om:stattesla](http://opendata.caceres.es/def/ontomunicipio#stattesla)<br />[om:statvolt](http://opendata.caceres.es/def/ontomunicipio#statvolt)<br />[om:SwedishKrona](http://opendata.caceres.es/def/ontomunicipio#SwedishKrona)<br />[om:BrazilianReal](http://opendata.caceres.es/def/ontomunicipio#BrazilianReal)<br />[om:hundredweight-US](http://opendata.caceres.es/def/ontomunicipio#hundredweight-US)<br />[om:volt](http://opendata.caceres.es/def/ontomunicipio#volt)<br />[om:second-Sidereal](http://opendata.caceres.es/def/ontomunicipio#second-Sidereal)<br />[om:cup-USCustomary](http://opendata.caceres.es/def/ontomunicipio#cup-USCustomary)<br />[om:chain](http://opendata.caceres.es/def/ontomunicipio#chain)<br />[om:torr](http://opendata.caceres.es/def/ontomunicipio#torr)<br />[om:SouthKoreanWon](http://opendata.caceres.es/def/ontomunicipio#SouthKoreanWon)<br />[om:shake](http://opendata.caceres.es/def/ontomunicipio#shake)<br />[om:becquerel](http://opendata.caceres.es/def/ontomunicipio#becquerel)<br />[om:stere](http://opendata.caceres.es/def/ontomunicipio#stere)<br />[om:hartley](http://opendata.caceres.es/def/ontomunicipio#hartley)<br />[om:cicero](http://opendata.caceres.es/def/ontomunicipio#cicero)<br />[om:statampere](http://opendata.caceres.es/def/ontomunicipio#statampere)<br />[om:radian](http://opendata.caceres.es/def/ontomunicipio#radian)<br />[om:henry](http://opendata.caceres.es/def/ontomunicipio#henry)<br />[om:BritishThermalUnit-InternationalTable](http://opendata.caceres.es/def/ontomunicipio#BritishThermalUnit-InternationalTable)<br />[om:circularMil](http://opendata.caceres.es/def/ontomunicipio#circularMil)<br />[om:rhe](http://opendata.caceres.es/def/ontomunicipio#rhe)<br />[om:point-TeX](http://opendata.caceres.es/def/ontomunicipio#point-TeX)<br />[om:franklin](http://opendata.caceres.es/def/ontomunicipio#franklin)<br />[om:_1-0](http://opendata.caceres.es/def/ontomunicipio#_1-0)<br />[om:candela](http://opendata.caceres.es/def/ontomunicipio#candela)<br />[om:calorie-InternationalTable](http://opendata.caceres.es/def/ontomunicipio#calorie-InternationalTable)<br />[om:horsepower-Water](http://opendata.caceres.es/def/ontomunicipio#horsepower-Water)<br />[om:ampere](http://opendata.caceres.es/def/ontomunicipio#ampere)<br />[om:minute-Angle](http://opendata.caceres.es/def/ontomunicipio#minute-Angle)<br />[om:horsepower-Electric](http://opendata.caceres.es/def/ontomunicipio#horsepower-Electric)<br />[om:joule](http://opendata.caceres.es/def/ontomunicipio#joule)<br />[om:litre](http://opendata.caceres.es/def/ontomunicipio#litre)<br />[om:poundSterling](http://opendata.caceres.es/def/ontomunicipio#poundSterling)<br />[om:quart-Imperial](http://opendata.caceres.es/def/ontomunicipio#quart-Imperial)<br />[om:newton](http://opendata.caceres.es/def/ontomunicipio#newton)<br />[om:minute-HourAngle](http://opendata.caceres.es/def/ontomunicipio#minute-HourAngle)<br />[om:hundredweight-British](http://opendata.caceres.es/def/ontomunicipio#hundredweight-British)<br />[om:one](http://opendata.caceres.es/def/ontomunicipio#one)<br />[om:BritishThermalUnit-60F](http://opendata.caceres.es/def/ontomunicipio#BritishThermalUnit-60F)<br />[om:calorie-Mean](http://opendata.caceres.es/def/ontomunicipio#calorie-Mean)<br />[om:degreeReaumur](http://opendata.caceres.es/def/ontomunicipio#degreeReaumur)<br />[om:AFS](http://opendata.caceres.es/def/ontomunicipio#AFS)<br />[om:footcandle](http://opendata.caceres.es/def/ontomunicipio#footcandle)<br />[om:point-ATA](http://opendata.caceres.es/def/ontomunicipio#point-ATA)<br />[om:year-Tropical](http://opendata.caceres.es/def/ontomunicipio#year-Tropical)<br />[om:NewZealandDollar](http://opendata.caceres.es/def/ontomunicipio#NewZealandDollar)<br />[om:colonyFormingUnit](http://opendata.caceres.es/def/ontomunicipio#colonyFormingUnit)<br />[om:liquidQuart-US](http://opendata.caceres.es/def/ontomunicipio#liquidQuart-US)<br />[om:siemens](http://opendata.caceres.es/def/ontomunicipio#siemens)<br />[om:TurkishLira](http://opendata.caceres.es/def/ontomunicipio#TurkishLira)<br />[om:tonOfTNT](http://opendata.caceres.es/def/ontomunicipio#tonOfTNT)<br />[om:slug](http://opendata.caceres.es/def/ontomunicipio#slug)<br />[om:cord](http://opendata.caceres.es/def/ontomunicipio#cord)<br />[om:horsepower-Metric](http://opendata.caceres.es/def/ontomunicipio#horsepower-Metric)<br />[om:barye](http://opendata.caceres.es/def/ontomunicipio#barye)<br />[om:point-Postscript](http://opendata.caceres.es/def/ontomunicipio#point-Postscript)<br />[om:amylaseUnit](http://opendata.caceres.es/def/ontomunicipio#amylaseUnit)<br />[om:hour-Sidereal](http://opendata.caceres.es/def/ontomunicipio#hour-Sidereal)<br />[om:röntgen](http://opendata.caceres.es/def/ontomunicipio#röntgen)<br />[om:pennyweight-Troy](http://opendata.caceres.es/def/ontomunicipio#pennyweight-Troy)<br />[om:BritishThermalUnit-Mean](http://opendata.caceres.es/def/ontomunicipio#BritishThermalUnit-Mean)<br />[om:IndianRupee](http://opendata.caceres.es/def/ontomunicipio#IndianRupee)<br />[om:yard-International](http://opendata.caceres.es/def/ontomunicipio#yard-International)<br />[om:therm-EC](http://opendata.caceres.es/def/ontomunicipio#therm-EC)<br />[om:calorie-Thermochemical](http://opendata.caceres.es/def/ontomunicipio#calorie-Thermochemical)<br />[om:fathom-USSurvey](http://opendata.caceres.es/def/ontomunicipio#fathom-USSurvey)<br />[om:stathenry](http://opendata.caceres.es/def/ontomunicipio#stathenry)<br />[om:footPoundal](http://opendata.caceres.es/def/ontomunicipio#footPoundal)<br />[om:barrel-US](http://opendata.caceres.es/def/ontomunicipio#barrel-US)<br />[om:are](http://opendata.caceres.es/def/ontomunicipio#are)<br />[om:atmosphere-Standard](http://opendata.caceres.es/def/ontomunicipio#atmosphere-Standard)<br />[om:deltaA450](http://opendata.caceres.es/def/ontomunicipio#deltaA450)<br />[om:day-Sidereal](http://opendata.caceres.es/def/ontomunicipio#day-Sidereal)<br />[om:tonOfRefrigeration](http://opendata.caceres.es/def/ontomunicipio#tonOfRefrigeration)<br />[om:UnitedStatesDollar](http://opendata.caceres.es/def/ontomunicipio#UnitedStatesDollar)<br />[om:minute-Sidereal](http://opendata.caceres.es/def/ontomunicipio#minute-Sidereal)<br />[om:calorie-20C](http://opendata.caceres.es/def/ontomunicipio#calorie-20C)<br />[om:abcoulomb](http://opendata.caceres.es/def/ontomunicipio#abcoulomb)<br />[om:erg](http://opendata.caceres.es/def/ontomunicipio#erg)<br />[om:year](http://opendata.caceres.es/def/ontomunicipio#year)<br />[om:degree](http://opendata.caceres.es/def/ontomunicipio#degree)<br />[om:statfarad](http://opendata.caceres.es/def/ontomunicipio#statfarad)<br />[om:hertz](http://opendata.caceres.es/def/ontomunicipio#hertz)<br />[om:pascal](http://opendata.caceres.es/def/ontomunicipio#pascal)<br />[om:lambert](http://opendata.caceres.es/def/ontomunicipio#lambert)<br />[om:pint-Imperial](http://opendata.caceres.es/def/ontomunicipio#pint-Imperial)<br />[om:solarMass](http://opendata.caceres.es/def/ontomunicipio#solarMass)<br />[om:fluidOunce-US](http://opendata.caceres.es/def/ontomunicipio#fluidOunce-US)<br />[om:tablespoon-US](http://opendata.caceres.es/def/ontomunicipio#tablespoon-US)<br />[om:rem](http://opendata.caceres.es/def/ontomunicipio#rem)<br />[om:calorie-15C](http://opendata.caceres.es/def/ontomunicipio#calorie-15C)<br />[om:CanadianDollar](http://opendata.caceres.es/def/ontomunicipio#CanadianDollar)<br />[om:gauss](http://opendata.caceres.es/def/ontomunicipio#gauss)<br />[om:gamma](http://opendata.caceres.es/def/ontomunicipio#gamma)<br />[om:acreFoot](http://opendata.caceres.es/def/ontomunicipio#acreFoot)<br />[om:perm-23C](http://opendata.caceres.es/def/ontomunicipio#perm-23C)<br />[om:bushel-US](http://opendata.caceres.es/def/ontomunicipio#bushel-US)<br />[om:dryQuart-US](http://opendata.caceres.es/def/ontomunicipio#dryQuart-US)<br />[om:micron](http://opendata.caceres.es/def/ontomunicipio#micron)<br />[om:pound-Force](http://opendata.caceres.es/def/ontomunicipio#pound-Force)<br />[om:gray](http://opendata.caceres.es/def/ontomunicipio#gray)<br />[om:jansky](http://opendata.caceres.es/def/ontomunicipio#jansky)<br />[om:abmho](http://opendata.caceres.es/def/ontomunicipio#abmho)<br />[om:_1-10](http://opendata.caceres.es/def/ontomunicipio#_1-10)<br />[om:hour](http://opendata.caceres.es/def/ontomunicipio#hour)<br />[om:abfarad](http://opendata.caceres.es/def/ontomunicipio#abfarad)<br />[om:weber](http://opendata.caceres.es/def/ontomunicipio#weber)<br />[om:abohm](http://opendata.caceres.es/def/ontomunicipio#abohm)<br />[om:lumen](http://opendata.caceres.es/def/ontomunicipio#lumen)<br />[om:statweber](http://opendata.caceres.es/def/ontomunicipio#statweber)<br />[om:horsepower-British](http://opendata.caceres.es/def/ontomunicipio#horsepower-British)<br />[om:foot-USSurvey](http://opendata.caceres.es/def/ontomunicipio#foot-USSurvey)<br />[om:BritishThermalUnit-39F](http://opendata.caceres.es/def/ontomunicipio#BritishThermalUnit-39F)<br />[om:SwissFranc](http://opendata.caceres.es/def/ontomunicipio#SwissFranc)<br />[om:footlambert](http://opendata.caceres.es/def/ontomunicipio#footlambert)<br />[om:percent](http://opendata.caceres.es/def/ontomunicipio#percent)<br />[om:unitPole](http://opendata.caceres.es/def/ontomunicipio#unitPole)<br />[om:dryGallon-US](http://opendata.caceres.es/def/ontomunicipio#dryGallon-US)<br />[om:AustralianDollar](http://opendata.caceres.es/def/ontomunicipio#AustralianDollar)<br />[om:barn](http://opendata.caceres.es/def/ontomunicipio#barn)<br />[om:partsPerMillion](http://opendata.caceres.es/def/ontomunicipio#partsPerMillion)<br />[om:phot](http://opendata.caceres.es/def/ontomunicipio#phot)<br />[om:darcy](http://opendata.caceres.es/def/ontomunicipio#darcy)<br />[om:SouthAfricanRand](http://opendata.caceres.es/def/ontomunicipio#SouthAfricanRand)<br />[om:shannon](http://opendata.caceres.es/def/ontomunicipio#shannon)<br />[om:curie](http://opendata.caceres.es/def/ontomunicipio#curie)<br />[om:abvolt](http://opendata.caceres.es/def/ontomunicipio#abvolt)<br />[om:poundal](http://opendata.caceres.es/def/ontomunicipio#poundal)<br />[om:quad](http://opendata.caceres.es/def/ontomunicipio#quad)<br />[om:BritishThermalUnit-Thermochemical](http://opendata.caceres.es/def/ontomunicipio#BritishThermalUnit-Thermochemical)<br />[om:milligramRAE](http://opendata.caceres.es/def/ontomunicipio#milligramRAE)<br />[om:second-Time](http://opendata.caceres.es/def/ontomunicipio#second-Time)<br />[om:lightYear](http://opendata.caceres.es/def/ontomunicipio#lightYear)<br />[om:coulomb](http://opendata.caceres.es/def/ontomunicipio#coulomb)<br />[om:electronvolt](http://opendata.caceres.es/def/ontomunicipio#electronvolt)<br />[om:statohm](http://opendata.caceres.es/def/ontomunicipio#statohm)<br />[om:stilb](http://opendata.caceres.es/def/ontomunicipio#stilb)<br />[om:maxwell](http://opendata.caceres.es/def/ontomunicipio#maxwell)<br />[om:metre](http://opendata.caceres.es/def/ontomunicipio#metre)<br />[om:katal](http://opendata.caceres.es/def/ontomunicipio#katal)<br />[om:mile-USSurvey](http://opendata.caceres.es/def/ontomunicipio#mile-USSurvey)<br />[om:liquidPint-US](http://opendata.caceres.es/def/ontomunicipio#liquidPint-US)<br />[om:nauticalMile-International](http://opendata.caceres.es/def/ontomunicipio#nauticalMile-International)<br />[om:therm-US](http://opendata.caceres.es/def/ontomunicipio#therm-US)<br />[om:month](http://opendata.caceres.es/def/ontomunicipio#month)<br />[om:HongKongDollar](http://opendata.caceres.es/def/ontomunicipio#HongKongDollar)<br />[om:bar](http://opendata.caceres.es/def/ontomunicipio#bar)<br />[om:mil-Length](http://opendata.caceres.es/def/ontomunicipio#mil-Length)<br />[om:magnitude](http://opendata.caceres.es/def/ontomunicipio#magnitude)<br />[om:NorwegianKrone](http://opendata.caceres.es/def/ontomunicipio#NorwegianKrone)<br />[om:pica-TeX](http://opendata.caceres.es/def/ontomunicipio#pica-TeX)<br />[om:mile-Statute](http://opendata.caceres.es/def/ontomunicipio#mile-Statute)<br />[om:gal](http://opendata.caceres.es/def/ontomunicipio#gal)<br />[om:minute-Time](http://opendata.caceres.es/def/ontomunicipio#minute-Time)<br />[om:ounceAvoirdupois](http://opendata.caceres.es/def/ontomunicipio#ounceAvoirdupois)<br />[om:gill-US](http://opendata.caceres.es/def/ontomunicipio#gill-US)<br />[om:_0-5](http://opendata.caceres.es/def/ontomunicipio#_0-5)<br />[om:gallon-US](http://opendata.caceres.es/def/ontomunicipio#gallon-US)<br />[om:fluidOunce-Imperial](http://opendata.caceres.es/def/ontomunicipio#fluidOunce-Imperial)<br />[om:baud](http://opendata.caceres.es/def/ontomunicipio#baud)<br />[om:RussianRuble](http://opendata.caceres.es/def/ontomunicipio#RussianRuble)<br />[om:carat-Mass](http://opendata.caceres.es/def/ontomunicipio#carat-Mass)<br />[om:metreOfMercury](http://opendata.caceres.es/def/ontomunicipio#metreOfMercury)<br />[om:kip](http://opendata.caceres.es/def/ontomunicipio#kip)<br />[om:degreeRankine](http://opendata.caceres.es/def/ontomunicipio#degreeRankine)<br />[om:ton-Short](http://opendata.caceres.es/def/ontomunicipio#ton-Short)<br />[om:astronomicalUnit](http://opendata.caceres.es/def/ontomunicipio#astronomicalUnit)<br />[om:unifiedAtomicMassUnit](http://opendata.caceres.es/def/ontomunicipio#unifiedAtomicMassUnit)<br />[om:oersted](http://opendata.caceres.es/def/ontomunicipio#oersted)<br />[om:mole](http://opendata.caceres.es/def/ontomunicipio#mole)<br />[om:degreeFahrenheit](http://opendata.caceres.es/def/ontomunicipio#degreeFahrenheit)<br />[om:parsec](http://opendata.caceres.es/def/ontomunicipio#parsec)<br />[om:SingaporeDollar](http://opendata.caceres.es/def/ontomunicipio#SingaporeDollar)<br />[om:fermi](http://opendata.caceres.es/def/ontomunicipio#fermi)<br />[om:BritishThermalUnit-59F](http://opendata.caceres.es/def/ontomunicipio#BritishThermalUnit-59F)<br />[om:ohm](http://opendata.caceres.es/def/ontomunicipio#ohm)<br />[om:revolution](http://opendata.caceres.es/def/ontomunicipio#revolution)<br />[om:foot-International](http://opendata.caceres.es/def/ontomunicipio#foot-International)<br />[om:ChineseYuan](http://opendata.caceres.es/def/ontomunicipio#ChineseYuan)<br />[om:ton-Long](http://opendata.caceres.es/def/ontomunicipio#ton-Long)<br />[om:inch-International](http://opendata.caceres.es/def/ontomunicipio#inch-International)<br />[om:abampere](http://opendata.caceres.es/def/ontomunicipio#abampere)<br />[om:hour-HourAngle](http://opendata.caceres.es/def/ontomunicipio#hour-HourAngle)<br />[om:teaspoon-US](http://opendata.caceres.es/def/ontomunicipio#teaspoon-US)<br />[om:furlong-International](http://opendata.caceres.es/def/ontomunicipio#furlong-International)<br />[om:rad](http://opendata.caceres.es/def/ontomunicipio#rad)<br />[om:horsepower-Boiler](http://opendata.caceres.es/def/ontomunicipio#horsepower-Boiler)<br />[om:gon](http://opendata.caceres.es/def/ontomunicipio#gon)<br />[om:MexicanPeso](http://opendata.caceres.es/def/ontomunicipio#MexicanPeso)<br />[om:watt](http://opendata.caceres.es/def/ontomunicipio#watt)<br />[om:pica-Postscript](http://opendata.caceres.es/def/ontomunicipio#pica-Postscript)<br />[om:gill-Imperial](http://opendata.caceres.es/def/ontomunicipio#gill-Imperial)<br />[om:rod-US](http://opendata.caceres.es/def/ontomunicipio#rod-US)<br />[om:poise](http://opendata.caceres.es/def/ontomunicipio#poise)<br />[om:solarRadius](http://opendata.caceres.es/def/ontomunicipio#solarRadius)<br />[om:gallon-Imperial](http://opendata.caceres.es/def/ontomunicipio#gallon-Imperial)<br />[om:tesla](http://opendata.caceres.es/def/ontomunicipio#tesla)<br />[om:dryPint-US](http://opendata.caceres.es/def/ontomunicipio#dryPint-US)<br />[om:second-HourAngle](http://opendata.caceres.es/def/ontomunicipio#second-HourAngle)<br />[om:molair](http://opendata.caceres.es/def/ontomunicipio#molair)<br />[om:kelvin](http://opendata.caceres.es/def/ontomunicipio#kelvin)<br />[om:abhenry](http://opendata.caceres.es/def/ontomunicipio#abhenry)<br />[om:statcoulomb](http://opendata.caceres.es/def/ontomunicipio#statcoulomb)<br />[om:knot-International](http://opendata.caceres.es/def/ontomunicipio#knot-International)<br />[om:perm-0C](http://opendata.caceres.es/def/ontomunicipio#perm-0C)<br />[om:biot](http://opendata.caceres.es/def/ontomunicipio#biot)<br />[om:degreeCelsius](http://opendata.caceres.es/def/ontomunicipio#degreeCelsius)<br />[om:solarLuminosity](http://opendata.caceres.es/def/ontomunicipio#solarLuminosity)<br />[om:ton-Register](http://opendata.caceres.es/def/ontomunicipio#ton-Register)<br />[om:ton-Force-Short](http://opendata.caceres.es/def/ontomunicipio#ton-Force-Short)<br />[om:angstrom](http://opendata.caceres.es/def/ontomunicipio#angstrom)<br />[om:second-Angle](http://opendata.caceres.es/def/ontomunicipio#second-Angle)<br />[om:gilbert](http://opendata.caceres.es/def/ontomunicipio#gilbert)<br />[om:faraday](http://opendata.caceres.es/def/ontomunicipio#faraday)<br />[om:kayser](http://opendata.caceres.es/def/ontomunicipio#kayser)<br />[om:steradian](http://opendata.caceres.es/def/ontomunicipio#steradian)<br />[om:week](http://opendata.caceres.es/def/ontomunicipio#week)<br />[om:bit](http://opendata.caceres.es/def/ontomunicipio#bit)<br />[om:farad](http://opendata.caceres.es/def/ontomunicipio#farad)<br />[om:debye](http://opendata.caceres.es/def/ontomunicipio#debye)<br />[om:year-Sidereal](http://opendata.caceres.es/def/ontomunicipio#year-Sidereal)<br />[om:atmosphere-Technical](http://opendata.caceres.es/def/ontomunicipio#atmosphere-Technical)<br />[om:grain](http://opendata.caceres.es/def/ontomunicipio#grain)<br />[om:lux](http://opendata.caceres.es/def/ontomunicipio#lux)<br />[om:ounceApothecaries](http://opendata.caceres.es/def/ontomunicipio#ounceApothecaries)<br />[om:InternationalUnit](http://opendata.caceres.es/def/ontomunicipio#InternationalUnit)<br />[om:pica-ATA](http://opendata.caceres.es/def/ontomunicipio#pica-ATA)<br />[om:statmho](http://opendata.caceres.es/def/ontomunicipio#statmho)<br />[om:mil-Angle](http://opendata.caceres.es/def/ontomunicipio#mil-Angle)<br />[om:point-Didot](http://opendata.caceres.es/def/ontomunicipio#point-Didot)<br />[om:dessertspoon](http://opendata.caceres.es/def/ontomunicipio#dessertspoon)<br />[om:acre-USSurvey](http://opendata.caceres.es/def/ontomunicipio#acre-USSurvey)<br />
### unit division
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#UnitDivision`
Super-classes |[om:CompoundUnit](http://opendata.caceres.es/def/ontomunicipio#CompoundUnit) (c)<br />
Sub-classes |[om:PrefixedMolePerLitre](http://opendata.caceres.es/def/ontomunicipio#PrefixedMolePerLitre) (c)<br />[om:PrefixedMetrePerSecond-Time](http://opendata.caceres.es/def/ontomunicipio#PrefixedMetrePerSecond-Time) (c)<br />[om:MetrePerPrefixedSecond-Time](http://opendata.caceres.es/def/ontomunicipio#MetrePerPrefixedSecond-Time) (c)<br />[om:PrefixedMolePerPrefixedMetre](http://opendata.caceres.es/def/ontomunicipio#PrefixedMolePerPrefixedMetre) (c)<br />[om:PrefixedGramPerPrefixedLitre](http://opendata.caceres.es/def/ontomunicipio#PrefixedGramPerPrefixedLitre) (c)<br />[om:PrefixedMetrePerSecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#PrefixedMetrePerSecond-TimeSquared) (c)<br />[om:GramPerPrefixedLitre](http://opendata.caceres.es/def/ontomunicipio#GramPerPrefixedLitre) (c)<br />[om:PrefixedMetrePerPrefixedSecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#PrefixedMetrePerPrefixedSecond-TimeSquared) (c)<br />[om:PrefixedMetrePerPrefixedSecond-Time](http://opendata.caceres.es/def/ontomunicipio#PrefixedMetrePerPrefixedSecond-Time) (c)<br />[om:PrefixedMolePerPrefixedLitre](http://opendata.caceres.es/def/ontomunicipio#PrefixedMolePerPrefixedLitre) (c)<br />[om:PrefixedMolePerMetre](http://opendata.caceres.es/def/ontomunicipio#PrefixedMolePerMetre) (c)<br />[om:PrefixedGramPerLitre](http://opendata.caceres.es/def/ontomunicipio#PrefixedGramPerLitre) (c)<br />[om:MetrePerPrefixedSecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#MetrePerPrefixedSecond-TimeSquared) (c)<br />[om:MolePerPrefixedMetre](http://opendata.caceres.es/def/ontomunicipio#MolePerPrefixedMetre) (c)<br />[om:MolePerPrefixedLitre](http://opendata.caceres.es/def/ontomunicipio#MolePerPrefixedLitre) (c)<br />
Has members |[om:squareMetrePerSecond-Time](http://opendata.caceres.es/def/ontomunicipio#squareMetrePerSecond-Time)<br />[om:squareMetrePerGram](http://opendata.caceres.es/def/ontomunicipio#squareMetrePerGram)<br />[om:newtonPerCoulomb](http://opendata.caceres.es/def/ontomunicipio#newtonPerCoulomb)<br />[om:gramPerSquareMetreMetre](http://opendata.caceres.es/def/ontomunicipio#gramPerSquareMetreMetre)<br />[om:metrePerMetre](http://opendata.caceres.es/def/ontomunicipio#metrePerMetre)<br />[om:lumenPerSquareMetre](http://opendata.caceres.es/def/ontomunicipio#lumenPerSquareMetre)<br />[om:cubicMillimetrePerCubicMillimetre](http://opendata.caceres.es/def/ontomunicipio#cubicMillimetrePerCubicMillimetre)<br />[om:millimetrePerHour](http://opendata.caceres.es/def/ontomunicipio#millimetrePerHour)<br />[om:joulePerCubicMetreKelvin](http://opendata.caceres.es/def/ontomunicipio#joulePerCubicMetreKelvin)<br />[om:colonyFormingUnitPerMillilitre](http://opendata.caceres.es/def/ontomunicipio#colonyFormingUnitPerMillilitre)<br />[om:nanokatalPerMilligram](http://opendata.caceres.es/def/ontomunicipio#nanokatalPerMilligram)<br />[om:micromolePerSecond-Time](http://opendata.caceres.es/def/ontomunicipio#micromolePerSecond-Time)<br />[om:gramPerGram](http://opendata.caceres.es/def/ontomunicipio#gramPerGram)<br />[om:gramPerSquareMetreDay](http://opendata.caceres.es/def/ontomunicipio#gramPerSquareMetreDay)<br />[om:deltaA450PerSecond-Time](http://opendata.caceres.es/def/ontomunicipio#deltaA450PerSecond-Time)<br />[om:gramPerSquareMetreCentimetre](http://opendata.caceres.es/def/ontomunicipio#gramPerSquareMetreCentimetre)<br />[om:metrePerDay](http://opendata.caceres.es/def/ontomunicipio#metrePerDay)<br />[om:second-TimePerSquareMetre](http://opendata.caceres.es/def/ontomunicipio#second-TimePerSquareMetre)<br />[om:voltPerMetre](http://opendata.caceres.es/def/ontomunicipio#voltPerMetre)<br />[om:millisecond-AnglePerYear](http://opendata.caceres.es/def/ontomunicipio#millisecond-AnglePerYear)<br />[om:squareMetrePerSquareMetreDay](http://opendata.caceres.es/def/ontomunicipio#squareMetrePerSquareMetreDay)<br />[om:kilometrePerHour](http://opendata.caceres.es/def/ontomunicipio#kilometrePerHour)<br />[om:solarMassPerCubicParsec](http://opendata.caceres.es/def/ontomunicipio#solarMassPerCubicParsec)<br />[om:kilogramPerMole](http://opendata.caceres.es/def/ontomunicipio#kilogramPerMole)<br />[om:kilogramPerSecond-Time](http://opendata.caceres.es/def/ontomunicipio#kilogramPerSecond-Time)<br />[om:amperePerVolt](http://opendata.caceres.es/def/ontomunicipio#amperePerVolt)<br />[om:voltPerAmpere](http://opendata.caceres.es/def/ontomunicipio#voltPerAmpere)<br />[om:joulePerSecond-Time](http://opendata.caceres.es/def/ontomunicipio#joulePerSecond-Time)<br />[om:candelaPerSquareCentimetre](http://opendata.caceres.es/def/ontomunicipio#candelaPerSquareCentimetre)<br />[om:kilogramPerHectare](http://opendata.caceres.es/def/ontomunicipio#kilogramPerHectare)<br />[om:wattPerSquareMetreSteradian](http://opendata.caceres.es/def/ontomunicipio#wattPerSquareMetreSteradian)<br />[om:cubicMetrePerMole](http://opendata.caceres.es/def/ontomunicipio#cubicMetrePerMole)<br />[om:kilogramPerCubicmetre](http://opendata.caceres.es/def/ontomunicipio#kilogramPerCubicmetre)<br />[om:voltPerWatt](http://opendata.caceres.es/def/ontomunicipio#voltPerWatt)<br />[om:cubicMetrePerYear](http://opendata.caceres.es/def/ontomunicipio#cubicMetrePerYear)<br />[om:squareMetreKelvinPerWatt](http://opendata.caceres.es/def/ontomunicipio#squareMetreKelvinPerWatt)<br />[om:megaeuroPerPetajoule](http://opendata.caceres.es/def/ontomunicipio#megaeuroPerPetajoule)<br />[om:litrePerHour](http://opendata.caceres.es/def/ontomunicipio#litrePerHour)<br />[om:second-TimePerDay](http://opendata.caceres.es/def/ontomunicipio#second-TimePerDay)<br />[om:kelvinPerWatt](http://opendata.caceres.es/def/ontomunicipio#kelvinPerWatt)<br />[om:metrePerSecond-Time](http://opendata.caceres.es/def/ontomunicipio#metrePerSecond-Time)<br />[om:kilogramPerPascalSecond-TimeSquareMetre](http://opendata.caceres.es/def/ontomunicipio#kilogramPerPascalSecond-TimeSquareMetre)<br />[om:wattPerAmpere](http://opendata.caceres.es/def/ontomunicipio#wattPerAmpere)<br />[om:amperePerWatt](http://opendata.caceres.es/def/ontomunicipio#amperePerWatt)<br />[om:amperePerSquareMetre](http://opendata.caceres.es/def/ontomunicipio#amperePerSquareMetre)<br />[om:henryPerMetre](http://opendata.caceres.es/def/ontomunicipio#henryPerMetre)<br />[om:weberPerAmpere](http://opendata.caceres.es/def/ontomunicipio#weberPerAmpere)<br />[om:millimetrePerDay](http://opendata.caceres.es/def/ontomunicipio#millimetrePerDay)<br />[om:metreKilogramPerSecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#metreKilogramPerSecond-TimeSquared)<br />[om:gramPerCubicCentimetre](http://opendata.caceres.es/def/ontomunicipio#gramPerCubicCentimetre)<br />[om:molePerKilogram](http://opendata.caceres.es/def/ontomunicipio#molePerKilogram)<br />[om:kilojoulePerHectogram](http://opendata.caceres.es/def/ontomunicipio#kilojoulePerHectogram)<br />[om:degreeCelsiusPerHour](http://opendata.caceres.es/def/ontomunicipio#degreeCelsiusPerHour)<br />[om:megaeuroPerMegawatt](http://opendata.caceres.es/def/ontomunicipio#megaeuroPerMegawatt)<br />[om:degreeCelsiusPerSecond-Time](http://opendata.caceres.es/def/ontomunicipio#degreeCelsiusPerSecond-Time)<br />[om:cubicCentimetrePerCubicCentimetre](http://opendata.caceres.es/def/ontomunicipio#cubicCentimetrePerCubicCentimetre)<br />[om:molePerSecond-Time](http://opendata.caceres.es/def/ontomunicipio#molePerSecond-Time)<br />[om:gramPerMegajoule](http://opendata.caceres.es/def/ontomunicipio#gramPerMegajoule)<br />[om:joulePerKelvin](http://opendata.caceres.es/def/ontomunicipio#joulePerKelvin)<br />[om:gramPerSquareMetreSecond-Time](http://opendata.caceres.es/def/ontomunicipio#gramPerSquareMetreSecond-Time)<br />[om:lumenPerWatt](http://opendata.caceres.es/def/ontomunicipio#lumenPerWatt)<br />[om:gramPerLitre](http://opendata.caceres.es/def/ontomunicipio#gramPerLitre)<br />[om:molePerMole](http://opendata.caceres.es/def/ontomunicipio#molePerMole)<br />[om:degreeCelsiusPerMinute-Time](http://opendata.caceres.es/def/ontomunicipio#degreeCelsiusPerMinute-Time)<br />[om:faradPerMetre](http://opendata.caceres.es/def/ontomunicipio#faradPerMetre)<br />[om:amperePerMetre](http://opendata.caceres.es/def/ontomunicipio#amperePerMetre)<br />[om:tonnePerHectare](http://opendata.caceres.es/def/ontomunicipio#tonnePerHectare)<br />[om:_1000ColonyFormingUnitPerMillilitre](http://opendata.caceres.es/def/ontomunicipio#_1000ColonyFormingUnitPerMillilitre)<br />[om:newtonPerSquareMetre](http://opendata.caceres.es/def/ontomunicipio#newtonPerSquareMetre)<br />[om:candelaPerSquareMetre](http://opendata.caceres.es/def/ontomunicipio#candelaPerSquareMetre)<br />[om:molePerCubicmetre](http://opendata.caceres.es/def/ontomunicipio#molePerCubicmetre)<br />[om:gramPerJoule](http://opendata.caceres.es/def/ontomunicipio#gramPerJoule)<br />[om:katalPerCubicmetre](http://opendata.caceres.es/def/ontomunicipio#katalPerCubicmetre)<br />[om:megajoulePerSquareMetre](http://opendata.caceres.es/def/ontomunicipio#megajoulePerSquareMetre)<br />[om:wattPerSquareMetreKelvin](http://opendata.caceres.es/def/ontomunicipio#wattPerSquareMetreKelvin)<br />[om:cubicMetrePerKilogram](http://opendata.caceres.es/def/ontomunicipio#cubicMetrePerKilogram)<br />[om:radianPerSecond-Time](http://opendata.caceres.es/def/ontomunicipio#radianPerSecond-Time)<br />[om:colonyFormingUnitPerGram](http://opendata.caceres.es/def/ontomunicipio#colonyFormingUnitPerGram)<br />[om:centimetrePerCubicCentimetre](http://opendata.caceres.es/def/ontomunicipio#centimetrePerCubicCentimetre)<br />[om:gramPerHectogram](http://opendata.caceres.es/def/ontomunicipio#gramPerHectogram)<br />[om:litrePerMole](http://opendata.caceres.es/def/ontomunicipio#litrePerMole)<br />[om:mile-StatutePerHour](http://opendata.caceres.es/def/ontomunicipio#mile-StatutePerHour)<br />[om:tonnePerCubicmetre](http://opendata.caceres.es/def/ontomunicipio#tonnePerCubicmetre)<br />[om:cubicMetrePerSecond-Time](http://opendata.caceres.es/def/ontomunicipio#cubicMetrePerSecond-Time)<br />[om:joulePerKelvinKilogram](http://opendata.caceres.es/def/ontomunicipio#joulePerKelvinKilogram)<br />[om:kilogramPerCubicDecimetre](http://opendata.caceres.es/def/ontomunicipio#kilogramPerCubicDecimetre)<br />[om:grayPerSecond-Time](http://opendata.caceres.es/def/ontomunicipio#grayPerSecond-Time)<br />[om:coulombPerKilogram](http://opendata.caceres.es/def/ontomunicipio#coulombPerKilogram)<br />[om:wattPerSquareMetre](http://opendata.caceres.es/def/ontomunicipio#wattPerSquareMetre)<br />[om:metreKilogramPerSecond-Time](http://opendata.caceres.es/def/ontomunicipio#metreKilogramPerSecond-Time)<br />[om:microgramPerCubicCentimetre](http://opendata.caceres.es/def/ontomunicipio#microgramPerCubicCentimetre)<br />[om:megajoulePerSquareMetreDay](http://opendata.caceres.es/def/ontomunicipio#megajoulePerSquareMetreDay)<br />[om:nauticalMile-InternationalPerHour](http://opendata.caceres.es/def/ontomunicipio#nauticalMile-InternationalPerHour)<br />[om:wattPerCubicmetre](http://opendata.caceres.es/def/ontomunicipio#wattPerCubicmetre)<br />[om:milligramPerKilometre](http://opendata.caceres.es/def/ontomunicipio#milligramPerKilometre)<br />[om:joulePerCubicmetre](http://opendata.caceres.es/def/ontomunicipio#joulePerCubicmetre)<br />[om:kilogramPerGigajoule](http://opendata.caceres.es/def/ontomunicipio#kilogramPerGigajoule)<br />[om:milligramPerKilogram](http://opendata.caceres.es/def/ontomunicipio#milligramPerKilogram)<br />[om:solarMassPerGigayearCubicKiloparsec](http://opendata.caceres.es/def/ontomunicipio#solarMassPerGigayearCubicKiloparsec)<br />[om:megametrePerKilojoule](http://opendata.caceres.es/def/ontomunicipio#megametrePerKilojoule)<br />[om:wattPerSteradianSquareMetreHertz](http://opendata.caceres.es/def/ontomunicipio#wattPerSteradianSquareMetreHertz)<br />[om:magnitudePerSecond-AngleSquared](http://opendata.caceres.es/def/ontomunicipio#magnitudePerSecond-AngleSquared)<br />[om:newtonPerMetre](http://opendata.caceres.es/def/ontomunicipio#newtonPerMetre)<br />[om:metrePerSecond-TimePerMetre](http://opendata.caceres.es/def/ontomunicipio#metrePerSecond-TimePerMetre)<br />[om:siemensPerMetre](http://opendata.caceres.es/def/ontomunicipio#siemensPerMetre)<br />[om:radianPerSecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#radianPerSecond-TimeSquared)<br />[om:wattPerHertz](http://opendata.caceres.es/def/ontomunicipio#wattPerHertz)<br />[om:weberPerSquareMetre](http://opendata.caceres.es/def/ontomunicipio#weberPerSquareMetre)<br />[om:microgramPerJoule](http://opendata.caceres.es/def/ontomunicipio#microgramPerJoule)<br />[om:wattPerSquareMetreHertz](http://opendata.caceres.es/def/ontomunicipio#wattPerSquareMetreHertz)<br />[om:coulombPerCubicmetre](http://opendata.caceres.es/def/ontomunicipio#coulombPerCubicmetre)<br />[om:solarMassPerGigayearCubicParsec](http://opendata.caceres.es/def/ontomunicipio#solarMassPerGigayearCubicParsec)<br />[om:wattPerMetreKelvin](http://opendata.caceres.es/def/ontomunicipio#wattPerMetreKelvin)<br />[om:joulePerKelvinMole](http://opendata.caceres.es/def/ontomunicipio#joulePerKelvinMole)<br />[om:metrePerSecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#metrePerSecond-TimeSquared)<br />[om:coulombPerSquareMetre](http://opendata.caceres.es/def/ontomunicipio#coulombPerSquareMetre)<br />[om:squareMetrePerSquareMetre](http://opendata.caceres.es/def/ontomunicipio#squareMetrePerSquareMetre)<br />[om:wattPerNanometre](http://opendata.caceres.es/def/ontomunicipio#wattPerNanometre)<br />[om:deltaA450PerSecond-TimePerMilligram](http://opendata.caceres.es/def/ontomunicipio#deltaA450PerSecond-TimePerMilligram)<br />[om:wattPerSecond-AngleSquared](http://opendata.caceres.es/def/ontomunicipio#wattPerSecond-AngleSquared)<br />[om:wattPerSteradian](http://opendata.caceres.es/def/ontomunicipio#wattPerSteradian)<br />[om:molePerMetre](http://opendata.caceres.es/def/ontomunicipio#molePerMetre)<br />[om:centimetrePerDay](http://opendata.caceres.es/def/ontomunicipio#centimetrePerDay)<br />[om:milligramPerHectogram](http://opendata.caceres.es/def/ontomunicipio#milligramPerHectogram)<br />[om:joulePerSquareMetreDay](http://opendata.caceres.es/def/ontomunicipio#joulePerSquareMetreDay)<br />[om:gramPerKilogram](http://opendata.caceres.es/def/ontomunicipio#gramPerKilogram)<br />[om:joulePerSquareMetre](http://opendata.caceres.es/def/ontomunicipio#joulePerSquareMetre)<br />[om:microgramPerSquareMetreSecond-Time](http://opendata.caceres.es/def/ontomunicipio#microgramPerSquareMetreSecond-Time)<br />[om:metrePerCubicMetre](http://opendata.caceres.es/def/ontomunicipio#metrePerCubicMetre)<br />[om:micromolePerSecond-TimeGram](http://opendata.caceres.es/def/ontomunicipio#micromolePerSecond-TimeGram)<br />[om:molePerLitre](http://opendata.caceres.es/def/ontomunicipio#molePerLitre)<br />[om:megaeuroPerMegatonne](http://opendata.caceres.es/def/ontomunicipio#megaeuroPerMegatonne)<br />[om:joulePerMole](http://opendata.caceres.es/def/ontomunicipio#joulePerMole)<br />[om:gramPerMetre](http://opendata.caceres.es/def/ontomunicipio#gramPerMetre)<br />[om:wattPerSteradianSquareMetre](http://opendata.caceres.es/def/ontomunicipio#wattPerSteradianSquareMetre)<br />[om:joulePerSquareMetreSecond-Time](http://opendata.caceres.es/def/ontomunicipio#joulePerSquareMetreSecond-Time)<br />[om:wattPerSquareMetreNanometre](http://opendata.caceres.es/def/ontomunicipio#wattPerSquareMetreNanometre)<br />[om:colonyFormingUnitPer25Millilitre](http://opendata.caceres.es/def/ontomunicipio#colonyFormingUnitPer25Millilitre)<br />[om:coulombPerVolt](http://opendata.caceres.es/def/ontomunicipio#coulombPerVolt)<br />[om:gramPerCubicmetre](http://opendata.caceres.es/def/ontomunicipio#gramPerCubicmetre)<br />[om:partsPerMillionPerYear](http://opendata.caceres.es/def/ontomunicipio#partsPerMillionPerYear)<br />[om:joulePerKilogram](http://opendata.caceres.es/def/ontomunicipio#joulePerKilogram)<br />[om:milligramPerCubicmetre](http://opendata.caceres.es/def/ontomunicipio#milligramPerCubicmetre)<br />[om:micromolePerMole](http://opendata.caceres.es/def/ontomunicipio#micromolePerMole)<br />[om:kilogramPerKilogram](http://opendata.caceres.es/def/ontomunicipio#kilogramPerKilogram)<br />[om:kilogramPerHectareDay](http://opendata.caceres.es/def/ontomunicipio#kilogramPerHectareDay)<br />[om:kilojoulePerSquareMetreDay](http://opendata.caceres.es/def/ontomunicipio#kilojoulePerSquareMetreDay)<br />[om:kilogramPerSquareMetre](http://opendata.caceres.es/def/ontomunicipio#kilogramPerSquareMetre)<br />[om:gramPerSquareMetre](http://opendata.caceres.es/def/ontomunicipio#gramPerSquareMetre)<br />[om:bitPerSecond-Time](http://opendata.caceres.es/def/ontomunicipio#bitPerSecond-Time)<br />[om:litrePer100Kilometre](http://opendata.caceres.es/def/ontomunicipio#litrePer100Kilometre)<br />[om:cubicMetrePerCubicmetre](http://opendata.caceres.es/def/ontomunicipio#cubicMetrePerCubicmetre)<br />[om:kilometrePerSecond-TimePerMegaparsec](http://opendata.caceres.es/def/ontomunicipio#kilometrePerSecond-TimePerMegaparsec)<br />
### unit exponentiation
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#UnitExponentiation`
Super-classes |[om:CompoundUnit](http://opendata.caceres.es/def/ontomunicipio#CompoundUnit) (c)<br />
Sub-classes |[om:CubicPrefixedMetre](http://opendata.caceres.es/def/ontomunicipio#CubicPrefixedMetre) (c)<br />[om:SquarePrefixedMetre](http://opendata.caceres.es/def/ontomunicipio#SquarePrefixedMetre) (c)<br />[om:PrefixedSecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#PrefixedSecond-TimeSquared) (c)<br />
Has members |[om:reciprocalDegreeCelsiusDay](http://opendata.caceres.es/def/ontomunicipio#reciprocalDegreeCelsiusDay)<br />[om:squareMetre](http://opendata.caceres.es/def/ontomunicipio#squareMetre)<br />[om:reciprocalPascalSecond-Time](http://opendata.caceres.es/def/ontomunicipio#reciprocalPascalSecond-Time)<br />[om:cubicParsec](http://opendata.caceres.es/def/ontomunicipio#cubicParsec)<br />[om:second-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#second-TimeSquared)<br />[om:reciprocalCubicCentimetre](http://opendata.caceres.es/def/ontomunicipio#reciprocalCubicCentimetre)<br />[om:reciprocalCubicParsec](http://opendata.caceres.es/def/ontomunicipio#reciprocalCubicParsec)<br />[om:reciprocalHenry](http://opendata.caceres.es/def/ontomunicipio#reciprocalHenry)<br />[om:reciprocalCubicMetre](http://opendata.caceres.es/def/ontomunicipio#reciprocalCubicMetre)<br />[om:reciprocalWatt](http://opendata.caceres.es/def/ontomunicipio#reciprocalWatt)<br />[om:reciprocalKelvin](http://opendata.caceres.es/def/ontomunicipio#reciprocalKelvin)<br />[om:reciprocalDegreeCelsius](http://opendata.caceres.es/def/ontomunicipio#reciprocalDegreeCelsius)<br />[om:reciprocalHour](http://opendata.caceres.es/def/ontomunicipio#reciprocalHour)<br />[om:second-TimeToThePower-2](http://opendata.caceres.es/def/ontomunicipio#second-TimeToThePower-2)<br />[om:reciprocalMetre](http://opendata.caceres.es/def/ontomunicipio#reciprocalMetre)<br />[om:reciprocalAtmosphere-Standard](http://opendata.caceres.es/def/ontomunicipio#reciprocalAtmosphere-Standard)<br />[om:reciprocalDay](http://opendata.caceres.es/def/ontomunicipio#reciprocalDay)<br />[om:reciprocalSecond-Time](http://opendata.caceres.es/def/ontomunicipio#reciprocalSecond-Time)<br />[om:degreeSquared](http://opendata.caceres.es/def/ontomunicipio#degreeSquared)<br />[om:cubicKiloparsec](http://opendata.caceres.es/def/ontomunicipio#cubicKiloparsec)<br />[om:reciprocalYear](http://opendata.caceres.es/def/ontomunicipio#reciprocalYear)<br />[om:second-AngleSquared](http://opendata.caceres.es/def/ontomunicipio#second-AngleSquared)<br />[om:reciprocalSquareMetre](http://opendata.caceres.es/def/ontomunicipio#reciprocalSquareMetre)<br />[om:reciprocalGram](http://opendata.caceres.es/def/ontomunicipio#reciprocalGram)<br />[om:reciprocalSquareCentimetre](http://opendata.caceres.es/def/ontomunicipio#reciprocalSquareCentimetre)<br />[om:cubicMetre](http://opendata.caceres.es/def/ontomunicipio#cubicMetre)<br />[om:reciprocalPartsPerMillionPerYear](http://opendata.caceres.es/def/ontomunicipio#reciprocalPartsPerMillionPerYear)<br />
### unit multiple
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#UnitMultiple`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
Has members |[om:_1000ColonyFormingUnit](http://opendata.caceres.es/def/ontomunicipio#_1000ColonyFormingUnit)<br />[om:_25Millilitre](http://opendata.caceres.es/def/ontomunicipio#_25Millilitre)<br />[om:_100Kilometre](http://opendata.caceres.es/def/ontomunicipio#_100Kilometre)<br />
### unit multiplication
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#UnitMultiplication`
Super-classes |[om:CompoundUnit](http://opendata.caceres.es/def/ontomunicipio#CompoundUnit) (c)<br />
Sub-classes |[om:PrefixedMetrePrefixedGram](http://opendata.caceres.es/def/ontomunicipio#PrefixedMetrePrefixedGram) (c)<br />
Has members |[om:steradianSquareMetreHertz](http://opendata.caceres.es/def/ontomunicipio#steradianSquareMetreHertz)<br />[om:second-TimeAmpere](http://opendata.caceres.es/def/ontomunicipio#second-TimeAmpere)<br />[om:newtonMetre](http://opendata.caceres.es/def/ontomunicipio#newtonMetre)<br />[om:pascalSecond-TimeSquareMetre](http://opendata.caceres.es/def/ontomunicipio#pascalSecond-TimeSquareMetre)<br />[om:kelvinKilogram](http://opendata.caceres.es/def/ontomunicipio#kelvinKilogram)<br />[om:moleMicrometre](http://opendata.caceres.es/def/ontomunicipio#moleMicrometre)<br />[om:pascalSecond-Time](http://opendata.caceres.es/def/ontomunicipio#pascalSecond-Time)<br />[om:degreeCelsiusDay](http://opendata.caceres.es/def/ontomunicipio#degreeCelsiusDay)<br />[om:micronewtonMetre](http://opendata.caceres.es/def/ontomunicipio#micronewtonMetre)<br />[om:squareMetreKelvin](http://opendata.caceres.es/def/ontomunicipio#squareMetreKelvin)<br />[om:squareMetreSteradian](http://opendata.caceres.es/def/ontomunicipio#squareMetreSteradian)<br />[om:squareMetreSecond-Time](http://opendata.caceres.es/def/ontomunicipio#squareMetreSecond-Time)<br />[om:reciprocalSquareMetreReciprocalMetre](http://opendata.caceres.es/def/ontomunicipio#reciprocalSquareMetreReciprocalMetre)<br />[om:kilogramSquareMetre](http://opendata.caceres.es/def/ontomunicipio#kilogramSquareMetre)<br />[om:moleMicrometreReciprocalSquareCentimetreReciprocalSecond-Time](http://opendata.caceres.es/def/ontomunicipio#moleMicrometreReciprocalSquareCentimetreReciprocalSecond-Time)<br />[om:metreKelvin](http://opendata.caceres.es/def/ontomunicipio#metreKelvin)<br />[om:gigayearCubicParsec](http://opendata.caceres.es/def/ontomunicipio#gigayearCubicParsec)<br />[om:kilogramSecond-TimeToThePower-2ReciprocalMetre](http://opendata.caceres.es/def/ontomunicipio#kilogramSecond-TimeToThePower-2ReciprocalMetre)<br />[om:candelaSteradian](http://opendata.caceres.es/def/ontomunicipio#candelaSteradian)<br />[om:reciprocalSquareMetreReciprocalGram](http://opendata.caceres.es/def/ontomunicipio#reciprocalSquareMetreReciprocalGram)<br />[om:hectareDay](http://opendata.caceres.es/def/ontomunicipio#hectareDay)<br />[om:terawattHour](http://opendata.caceres.es/def/ontomunicipio#terawattHour)<br />[om:moleMicrometreReciprocalSquareCentimetre](http://opendata.caceres.es/def/ontomunicipio#moleMicrometreReciprocalSquareCentimetre)<br />[om:voltSecond-Time](http://opendata.caceres.es/def/ontomunicipio#voltSecond-Time)<br />[om:millinewtonMetre](http://opendata.caceres.es/def/ontomunicipio#millinewtonMetre)<br />[om:ergSecond-Time](http://opendata.caceres.es/def/ontomunicipio#ergSecond-Time)<br />[om:wattSquareMetre](http://opendata.caceres.es/def/ontomunicipio#wattSquareMetre)<br />[om:jouleSecond-Time](http://opendata.caceres.es/def/ontomunicipio#jouleSecond-Time)<br />[om:kilogramSecond-TimeToThePower-2](http://opendata.caceres.es/def/ontomunicipio#kilogramSecond-TimeToThePower-2)<br />[om:steradianSquareMetre](http://opendata.caceres.es/def/ontomunicipio#steradianSquareMetre)<br />[om:kelvinMole](http://opendata.caceres.es/def/ontomunicipio#kelvinMole)<br />[om:coulombMetre](http://opendata.caceres.es/def/ontomunicipio#coulombMetre)<br />[om:squareMetreNanometre](http://opendata.caceres.es/def/ontomunicipio#squareMetreNanometre)<br />[om:gigayearCubicKiloparsec](http://opendata.caceres.es/def/ontomunicipio#gigayearCubicKiloparsec)<br />[om:kilowattHour](http://opendata.caceres.es/def/ontomunicipio#kilowattHour)<br />[om:luxSecond-Time](http://opendata.caceres.es/def/ontomunicipio#luxSecond-Time)<br />[om:metreKilogram](http://opendata.caceres.es/def/ontomunicipio#metreKilogram)<br />[om:ohmMetre](http://opendata.caceres.es/def/ontomunicipio#ohmMetre)<br />[om:squareMetreDay](http://opendata.caceres.es/def/ontomunicipio#squareMetreDay)<br />[om:cubicMetreKelvin](http://opendata.caceres.es/def/ontomunicipio#cubicMetreKelvin)<br />[om:squareMetreHertz](http://opendata.caceres.es/def/ontomunicipio#squareMetreHertz)<br />[om:lumenSecond-Time](http://opendata.caceres.es/def/ontomunicipio#lumenSecond-Time)<br />
### V amplitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#VAmplitude`
Description | <p>Amplitude of the light variation in Johnson V magnitude. The Johnson V band is a standard passband in the visual area, matching the response curve of the human eye. The central wavelength is 550nm and the bandwidth is 90nm.  The filter to be used is the Corning 3384 filter.</p>
Super-classes |[om:Amplitude](http://opendata.caceres.es/def/ontomunicipio#Amplitude) (c)<br />
### V magnitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#VMagnitude`
Description | <p>Johnson V magnitude. The Johnson V band is a standard passband in the visual area, matching the response curve of the human eye. The central wavelength is 550nm and the bandwidth is 90nm.  The filter to be used is the Corning 3384 filter.</p>
Super-classes |[om:JohnsonMagnitude](http://opendata.caceres.es/def/ontomunicipio#JohnsonMagnitude) (c)<br />
Sub-classes |[om:VMagnitudeAtMinimumBrightness](http://opendata.caceres.es/def/ontomunicipio#VMagnitudeAtMinimumBrightness) (c)<br />[om:VMagnitudeAtMaximumBrightness](http://opendata.caceres.es/def/ontomunicipio#VMagnitudeAtMaximumBrightness) (c)<br />
### V magnitude at maximum brightness
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#VMagnitudeAtMaximumBrightness`
Description | <p>Johnson V magnitude (apparent) at maximum brightness (i.e. for a variable star). The Johnson V band is a standard filter in the visual area, matching the response curve of the human eye. The central wavelength is 550nm and the bandwidth is 90nm.  The filter to be used is the Corning 3384 filter.</p>
Super-classes |[om:MagnitudeAtMaximumBrightness](http://opendata.caceres.es/def/ontomunicipio#MagnitudeAtMaximumBrightness) (c)<br />[om:VMagnitude](http://opendata.caceres.es/def/ontomunicipio#VMagnitude) (c)<br />
### V magnitude at minimum brightness
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#VMagnitudeAtMinimumBrightness`
Description | <p>Johnson V magnitude (apparent) at minimum brightness (i.e. for a variable star). The Johnson V band is a standard filter in the visual area, matching the response curve of the human eye. The central wavelength is 550nm and the bandwidth is 90nm.  The filter to be used is the Corning 3384 filter.</p>
Super-classes |[om:MagnitudeAtMinimumBrightness](http://opendata.caceres.es/def/ontomunicipio#MagnitudeAtMinimumBrightness) (c)<br />[om:VMagnitude](http://opendata.caceres.es/def/ontomunicipio#VMagnitude) (c)<br />
### vascular browning
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#VascularBrowning`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### vase life
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#VaseLife`
Super-classes |[om:Time](http://opendata.caceres.es/def/ontomunicipio#Time) (c)<br />
### vase plus water mass
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#VasePlusWaterMass`
Super-classes |[om:Mass](http://opendata.caceres.es/def/ontomunicipio#Mass) (c)<br />
### vase plus water plus flower mass
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#VasePlusWaterPlusFlowerMass`
Super-classes |[om:Mass](http://opendata.caceres.es/def/ontomunicipio#Mass) (c)<br />
### velocity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Velocity`
Description | <p>Velocity is the rate of change of position.</p>
Super-classes |[om:Speed](http://opendata.caceres.es/def/ontomunicipio#Speed) (c)<br />
### visual albedo
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#VisualAlbedo`
Description | <p>The albedo only for radiation in the visual part of the spectrum.</p>
Super-classes |[om:Albedo](http://opendata.caceres.es/def/ontomunicipio#Albedo) (c)<br />
### volume
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Volume`
Description | <p>Volume is a measure of how much three-dimensional space any phenomenon occupies. It is a derived quantity in the International System of Units. Volume is length to the power 3.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:volume-Dimension](http://opendata.caceres.es/def/ontomunicipio#volume-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### volume fraction
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#VolumeFraction`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:Overrun](http://opendata.caceres.es/def/ontomunicipio#Overrun) (c)<br />
### volume fraction unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#VolumeFractionUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### volume strain
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#VolumeStrain`
Super-classes |[om:Strain](http://opendata.caceres.es/def/ontomunicipio#Strain) (c)<br />
### volume unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#VolumeUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### coliform bacteria count (volumetric)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricColiformBacterieCount`
Super-classes |[om:VolumetricViableCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCount) (c)<br />
### Corynebacterium bovis count (volumetric)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricCorynebacteriumBovisCount`
Super-classes |[om:VolumetricViableCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCount) (c)<br />
### Corynebacterium count (volumetric)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricCorynebacteriumCount`
Super-classes |[om:VolumetricViableCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCount) (c)<br />
### Enterobacteriaceae count (volumetric)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricEnterobacteriaceaeCount`
Super-classes |[om:VolumetricViableCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCount) (c)<br />
### Enterococcus count (volumetric)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricEnterococcusCount`
Super-classes |[om:VolumetricViableCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCount) (c)<br />
### Escherichia coli count (volumetric)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricEscherichiaColiCount`
Super-classes |[om:VolumetricViableCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCount) (c)<br />
### volumetric flow rate
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricFlowRate`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:volumetricFlowRate-Dimension](http://opendata.caceres.es/def/ontomunicipio#volumetricFlowRate-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### volumetric flow rate unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricFlowRateUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### volumetric heat capacity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricHeatCapacity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:volumetricHeatCapacity-Dimension](http://opendata.caceres.es/def/ontomunicipio#volumetricHeatCapacity-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### volumetric heat capacity unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricHeatCapacityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### Klebsiella count (volumetric)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricKlebsiellaCount`
Super-classes |[om:VolumetricViableCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCount) (c)<br />
### Listeria monocytogenes count (volumetric)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricListeriaMonocytogenesCount`
Super-classes |[om:VolumetricViableCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCount) (c)<br />
### Salmonella count (volumetric)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricSalmonellaCount`
Super-classes |[om:VolumetricViableCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCount) (c)<br />
### Serratia marcescens count (volumetric)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricSerratiaMarcescensCount`
Super-classes |[om:VolumetricViableCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCount) (c)<br />
### Staphylococcus aureus count (volumetric)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricStaphylococcusAureusCount`
Super-classes |[om:VolumetricViableCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCount) (c)<br />
### Streptococcus agalactiae count (volumetric)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricStreptococcusAgalactiaeCount`
Super-classes |[om:VolumetricViableCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCount) (c)<br />
### Streptococcus dysgalactiae count (volumetric)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricStreptococcusDysgalactiaeCount`
Super-classes |[om:VolumetricViableCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCount) (c)<br />
### Streptococcus uberis count (volumetric)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricStreptococcusUberisCount`
Super-classes |[om:VolumetricViableCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCount) (c)<br />
### viable count (volumetric)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCount`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:VolumetricStreptococcusUberisCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricStreptococcusUberisCount) (c)<br />[om:VolumetricEscherichiaColiCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricEscherichiaColiCount) (c)<br />[om:VolumetricCorynebacteriumCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricCorynebacteriumCount) (c)<br />[om:VolumetricYeastAndFungiCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricYeastAndFungiCount) (c)<br />[om:VolumetricEnterococcusCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricEnterococcusCount) (c)<br />[om:VolumetricStreptococcusDysgalactiaeCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricStreptococcusDysgalactiaeCount) (c)<br />[om:VolumetricStreptococcusAgalactiaeCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricStreptococcusAgalactiaeCount) (c)<br />[om:VolumetricListeriaMonocytogenesCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricListeriaMonocytogenesCount) (c)<br />[om:VolumetricSalmonellaCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricSalmonellaCount) (c)<br />[om:VolumetricCorynebacteriumBovisCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricCorynebacteriumBovisCount) (c)<br />[om:VolumetricSerratiaMarcescensCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricSerratiaMarcescensCount) (c)<br />[om:VolumetricColiformBacterieCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricColiformBacterieCount) (c)<br />[om:VolumetricEnterobacteriaceaeCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricEnterobacteriaceaeCount) (c)<br />[om:VolumetricKlebsiellaCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricKlebsiellaCount) (c)<br />[om:VolumetricStaphylococcusAureusCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricStaphylococcusAureusCount) (c)<br />
### volumetric viable count unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCountUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### yeast and fungi count (volumetric)
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricYeastAndFungiCount`
Super-classes |[om:VolumetricViableCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCount) (c)<br />
### water mass fraction
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#WaterMassFraction`
Description | <p>The fraction of the mass of water in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### wavelength
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Wavelength`
Super-classes |[om:Length](http://opendata.caceres.es/def/ontomunicipio#Length) (c)<br />
Sub-classes |[om:Cut-OffWavelength](http://opendata.caceres.es/def/ontomunicipio#Cut-OffWavelength) (c)<br />[om:PeakWavelength](http://opendata.caceres.es/def/ontomunicipio#PeakWavelength) (c)<br />
### wavenumber
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Wavenumber`
Description | <p>Wavenumber is the number of repeating units of a propagating wave (the number of times a wave has the same phase) per unit of space.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:wavenumber-Dimension](http://opendata.caceres.es/def/ontomunicipio#wavenumber-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### wave number unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#WavenumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### Weber number
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#WeberNumber`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### Weber number unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#WeberNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### weight
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Weight`
Description | <p>Weight is a force that attracts a body towards another (reference) body.</p>
Super-classes |[om:Force](http://opendata.caceres.es/def/ontomunicipio#Force) (c)<br />
### wetting angle
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#WettingAngle`
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
### whey protein aggregate mass fraction
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#WheyProteinAggregateMassFraction`
Description | <p>The fraction of the mass of whey protein aggregate in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### whey protein beads mass fraction
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#WheyProteinBeadsMassFraction`
Description | <p>The fraction of the mass of whey protein beads in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### whey protein mass fraction
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#WheyProteinMassFraction`
Description | <p>The fraction of the mass of whey protein in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### white light magnitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#WhiteLightMagnitude`
Super-classes |[om:Magnitude](http://opendata.caceres.es/def/ontomunicipio#Magnitude) (c)<br />
Sub-classes |[om:WhiteLightMagnitudeAtMaximumBrightness](http://opendata.caceres.es/def/ontomunicipio#WhiteLightMagnitudeAtMaximumBrightness) (c)<br />[om:WhiteLightMagnitudeAtMinimumBrightness](http://opendata.caceres.es/def/ontomunicipio#WhiteLightMagnitudeAtMinimumBrightness) (c)<br />
### white light magnitude at maximum brightness
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#WhiteLightMagnitudeAtMaximumBrightness`
Super-classes |[om:WhiteLightMagnitude](http://opendata.caceres.es/def/ontomunicipio#WhiteLightMagnitude) (c)<br />[om:MagnitudeAtMaximumBrightness](http://opendata.caceres.es/def/ontomunicipio#MagnitudeAtMaximumBrightness) (c)<br />
### white light magnitude at minimum brightness
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#WhiteLightMagnitudeAtMinimumBrightness`
Super-classes |[om:MagnitudeAtMinimumBrightness](http://opendata.caceres.es/def/ontomunicipio#MagnitudeAtMinimumBrightness) (c)<br />[om:WhiteLightMagnitude](http://opendata.caceres.es/def/ontomunicipio#WhiteLightMagnitude) (c)<br />
### width
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Width`
Super-classes |[om:Length](http://opendata.caceres.es/def/ontomunicipio#Length) (c)<br />
### work
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#Work`
Description | <p>Work is the energy when a force acts against resistance to produce motion in a body.</p>
Super-classes |[om:Energy](http://opendata.caceres.es/def/ontomunicipio#Energy) (c)<br />
### xanthan mass fraction
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#XanthanMassFraction`
Description | <p>The fraction of the mass of xanthan in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### zenith distance
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#ZenithDistance`
Description | <p>The angular distance on the celestial sphere measured along the great circle from the zenith to the celestial object. z = 90° - h.</p>
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
### 1040 nm Lockwood magnitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#_1040NanometreLockwoodMagnitude`
Description | <p>A magnitude in the 1.04 micrometre band of the photometric system introduced by G.W. Lockwood.</p>
Super-classes |[om:Magnitude](http://opendata.caceres.es/def/ontomunicipio#Magnitude) (c)<br />
### b magnitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#bMagnitude`
Description | <p>b Magnitude in the Strömgren photometric system with a peak wavelength at 467 nm and a peak-half-width of 18 nm.</p>
Super-classes |[om:StroemgrenMagnitude](http://opendata.caceres.es/def/ontomunicipio#StroemgrenMagnitude) (c)<br />
### g magnitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#gMagnitude`
Description | <p>g Magnitude in the Thuan and Gunn photometric system.</p>
Super-classes |[om:ThuanAndGunnMagnitude](http://opendata.caceres.es/def/ontomunicipio#ThuanAndGunnMagnitude) (c)<br />
### u magnitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#uMagnitude`
Description | <p>u Magnitude in the Strömgren photometric system with a peak wavelength at 350 nm and a peak-half-width of 30 nm.</p>
Super-classes |[om:StroemgrenMagnitude](http://opendata.caceres.es/def/ontomunicipio#StroemgrenMagnitude) (c)<br />
### v magnitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#vMagnitude`
Description | <p>v Magnitude in the Strömgren photometric system with a peak wavelength at 411 nm and a peak-half-width of 19 nm.</p>
Super-classes |[om:StroemgrenMagnitude](http://opendata.caceres.es/def/ontomunicipio#StroemgrenMagnitude) (c)<br />
### x range
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#xRange`
Super-classes |[om:Length](http://opendata.caceres.es/def/ontomunicipio#Length) (c)<br />
### xy 2D start-end distance
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#xy2DStartEndDistance`
Super-classes |[om:Distance](http://opendata.caceres.es/def/ontomunicipio#Distance) (c)<br />
### xy distance travelled
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#xyDistanceTravelled`
Super-classes |[om:Distance](http://opendata.caceres.es/def/ontomunicipio#Distance) (c)<br />
### y magnitude
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#yMagnitude`
Description | <p>y Magnitude in the Strömgren photometric system with a peak wavelength at 547 nm and a peak-half-width of 23 nm.</p>
Super-classes |[om:StroemgrenMagnitude](http://opendata.caceres.es/def/ontomunicipio#StroemgrenMagnitude) (c)<br />
### y range
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#yRange`
Super-classes |[om:Length](http://opendata.caceres.es/def/ontomunicipio#Length) (c)<br />
### z range
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#zRange`
Super-classes |[om:Length](http://opendata.caceres.es/def/ontomunicipio#Length) (c)<br />

## Object Properties
[commonly has unit](#commonlyhasunit),
[has aggregate function](#hasaggregatefunction),
[has base](#hasbase),
[has base quantity](#hasbasequantity),
[has base unit](#hasbaseunit),
[has context](#hascontext),
[has denominator](#hasdenominator),
[has derived quantity](#hasderivedquantity),
[has derived unit](#hasderivedunit),
[has dimension](#hasdimension),
[has numerator](#hasnumerator),
[has phenomenon](#hasphenomenon),
[has point](#haspoint),
[has prefix](#hasprefix),
[has quantity](#hasquantity),
[has scale](#hasscale),
[has term 1](#hasterm1),
[has term 2](#hasterm2),
[has unit](#hasunit),
[has value](#hasvalue),
[uses quantity](#usesquantity),
[uses unit](#usesunit),
[reference](#reference),
[](commonlyhasunit)
### commonly has unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#commonlyHasUnit`
Description | This property indicates a commonly-used unit.
Domain(s) |([om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c))<br />
Range(s) |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
[](hasaggregatefunction)
### has aggregate function
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#hasAggregateFunction`
Domain(s) |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Range(s) |[om:Function](http://opendata.caceres.es/def/ontomunicipio#Function) (c)<br />
[](hasbase)
### has base
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#hasBase`
Domain(s) |([om:UnitExponentiation](http://opendata.caceres.es/def/ontomunicipio#UnitExponentiation) (c))<br />
Range(s) |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
[](hasbasequantity)
### has base quantity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#hasBaseQuantity`
Domain(s) |[om:SystemOfUnits](http://opendata.caceres.es/def/ontomunicipio#SystemOfUnits) (c)<br />
Range(s) |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
[](hasbaseunit)
### has base unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#hasBaseUnit`
Domain(s) |[om:SystemOfUnits](http://opendata.caceres.es/def/ontomunicipio#SystemOfUnits) (c)<br />
Range(s) |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
[](hascontext)
### has context
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#hasContext`
Domain(s) |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
[](hasdenominator)
### has denominator
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#hasDenominator`
Domain(s) |([om:UnitDivision](http://opendata.caceres.es/def/ontomunicipio#UnitDivision) (c))<br />
Range(s) |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
[](hasderivedquantity)
### has derived quantity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#hasDerivedQuantity`
Domain(s) |[om:SystemOfUnits](http://opendata.caceres.es/def/ontomunicipio#SystemOfUnits) (c)<br />
Range(s) |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
[](hasderivedunit)
### has derived unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#hasDerivedUnit`
Domain(s) |[om:SystemOfUnits](http://opendata.caceres.es/def/ontomunicipio#SystemOfUnits) (c)<br />
Range(s) |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
[](hasdimension)
### has dimension
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#hasDimension`
Domain(s) |([om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c) or [om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c) or [om:Scale](http://opendata.caceres.es/def/ontomunicipio#Scale) (c))<br />
Range(s) |[om:Dimension](http://opendata.caceres.es/def/ontomunicipio#Dimension) (c)<br />
[](hasnumerator)
### has numerator
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#hasNumerator`
Domain(s) |([om:UnitDivision](http://opendata.caceres.es/def/ontomunicipio#UnitDivision) (c))<br />
Range(s) |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
[](hasphenomenon)
### has phenomenon
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#hasPhenomenon`
Domain(s) |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
[](haspoint)
### has point
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#hasPoint`
Domain(s) |([om:IntervalScale](http://opendata.caceres.es/def/ontomunicipio#IntervalScale) (c) or [om:RatioScale](http://opendata.caceres.es/def/ontomunicipio#RatioScale) (c) or [om:FixedPoint](http://opendata.caceres.es/def/ontomunicipio#FixedPoint) (c))<br />
Range(s) |[om:Point](http://opendata.caceres.es/def/ontomunicipio#Point) (c)<br />
[](hasprefix)
### has prefix
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#hasPrefix`
Domain(s) |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
Range(s) |[om:Prefix](http://opendata.caceres.es/def/ontomunicipio#Prefix) (c)<br />
[](hasquantity)
### has quantity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#hasQuantity`
Domain(s) |([om:SingularUnit](http://opendata.caceres.es/def/ontomunicipio#SingularUnit) (c) or [om:FixedPoint](http://opendata.caceres.es/def/ontomunicipio#FixedPoint) (c))<br />
Range(s) |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
[](hasscale)
### has scale
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#hasScale`
Domain(s) |([om:Scale](http://opendata.caceres.es/def/ontomunicipio#Scale) (c) or [om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c) or [om:ApplicationArea](http://opendata.caceres.es/def/ontomunicipio#ApplicationArea) (c))<br />
Range(s) |[om:Scale](http://opendata.caceres.es/def/ontomunicipio#Scale) (c)<br />
[](hasterm1)
### has term 1
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#hasTerm1`
Domain(s) |([om:UnitMultiplication](http://opendata.caceres.es/def/ontomunicipio#UnitMultiplication) (c))<br />
Range(s) |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
[](hasterm2)
### has term 2
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#hasTerm2`
Domain(s) |([om:UnitMultiplication](http://opendata.caceres.es/def/ontomunicipio#UnitMultiplication) (c))<br />
Range(s) |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
[](hasunit)
### has unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#hasUnit`
Domain(s) |([om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c) or [om:UnitMultiple](http://opendata.caceres.es/def/ontomunicipio#UnitMultiple) (c) or [om:SingularUnit](http://opendata.caceres.es/def/ontomunicipio#SingularUnit) (c) or [om:IntervalScale](http://opendata.caceres.es/def/ontomunicipio#IntervalScale) (c) or [om:RatioScale](http://opendata.caceres.es/def/ontomunicipio#RatioScale) (c) or [om:Measure](http://opendata.caceres.es/def/ontomunicipio#Measure) (c))<br />
Range(s) |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
[](hasvalue)
### has value
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#hasValue`
Domain(s) |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Range(s) |[om:Measure](http://opendata.caceres.es/def/ontomunicipio#Measure) (c)<br />[om:Point](http://opendata.caceres.es/def/ontomunicipio#Point) (c)<br />
[](usesquantity)
### uses quantity
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#usesQuantity`
Domain(s) |[om:ApplicationArea](http://opendata.caceres.es/def/ontomunicipio#ApplicationArea) (c)<br />
Range(s) |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
[](usesunit)
### uses unit
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#usesUnit`
Domain(s) |[om:ApplicationArea](http://opendata.caceres.es/def/ontomunicipio#ApplicationArea) (c)<br />
Range(s) |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
[](reference)
### reference
Property | Value
--- | ---
URI | `http://www.wurvoc.org/bibliography/om-2/reference`
Domain(s) |[bibo:Document](http://purl.org/ontology/bibo/Document) (c)<br />

## Functional Properties
[has factor](#hasfactor),
[](hasfactor)
### has factor
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#hasFactor`
Domain(s) |([om:UnitMultiple](http://opendata.caceres.es/def/ontomunicipio#UnitMultiple) (c) or [om:SingularUnit](http://opendata.caceres.es/def/ontomunicipio#SingularUnit) (c) or [om:Prefix](http://opendata.caceres.es/def/ontomunicipio#Prefix) (c) or [om:Scale](http://opendata.caceres.es/def/ontomunicipio#Scale) (c))<br />
Range(s) |[xsd:float](http://www.w3.org/2001/XMLSchema#float) (c)<br />

## Datatype Properties
[has exponent](#hasexponent),
[has numerical value](#hasnumericalvalue),
[has off-set](#hasoff-set),
[has SI amount of substance dimension exponent](#hasSIamountofsubstancedimensionexponent),
[has SI electric current dimension exponent](#hasSIelectriccurrentdimensionexponent),
[has SI length dimension exponent](#hasSIlengthdimensionexponent),
[has SI luminous intensity dimension exponent](#hasSIluminousintensitydimensionexponent),
[has SI mass dimension exponent](#hasSImassdimensionexponent),
[has SI thermodynamic temperature dimension exponent](#hasSIthermodynamictemperaturedimensionexponent),
[has SI time dimension exponent](#hasSItimedimensionexponent),
[](hasexponent)
### has exponent
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#hasExponent`
Domain(s) |([om:UnitExponentiation](http://opendata.caceres.es/def/ontomunicipio#UnitExponentiation) (c))<br />
Range(s) |[xsd:integer](http://www.w3.org/2001/XMLSchema#integer) (c)<br />
[](hasnumericalvalue)
### has numerical value
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#hasNumericalValue`
Domain(s) |([om:Measure](http://opendata.caceres.es/def/ontomunicipio#Measure) (c) or [om:Point](http://opendata.caceres.es/def/ontomunicipio#Point) (c))<br />
[](hasoff-set)
### has off-set
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#hasOff-Set`
Domain(s) |[om:Scale](http://opendata.caceres.es/def/ontomunicipio#Scale) (c)<br />
Range(s) |[xsd:float](http://www.w3.org/2001/XMLSchema#float) (c)<br />
[](hasSIamountofsubstancedimensionexponent)
### has SI amount of substance dimension exponent
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#hasSIAmountOfSubstanceDimensionExponent`
Domain(s) |[om:Dimension](http://opendata.caceres.es/def/ontomunicipio#Dimension) (c)<br />
Range(s) |[xsd:integer](http://www.w3.org/2001/XMLSchema#integer) (c)<br />
[](hasSIelectriccurrentdimensionexponent)
### has SI electric current dimension exponent
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#hasSIElectricCurrentDimensionExponent`
Domain(s) |[om:Dimension](http://opendata.caceres.es/def/ontomunicipio#Dimension) (c)<br />
Range(s) |[xsd:integer](http://www.w3.org/2001/XMLSchema#integer) (c)<br />
[](hasSIlengthdimensionexponent)
### has SI length dimension exponent
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#hasSILengthDimensionExponent`
Domain(s) |[om:Dimension](http://opendata.caceres.es/def/ontomunicipio#Dimension) (c)<br />
Range(s) |[xsd:integer](http://www.w3.org/2001/XMLSchema#integer) (c)<br />
[](hasSIluminousintensitydimensionexponent)
### has SI luminous intensity dimension exponent
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#hasSILuminousIntensityDimensionExponent`
Domain(s) |[om:Dimension](http://opendata.caceres.es/def/ontomunicipio#Dimension) (c)<br />
Range(s) |[xsd:integer](http://www.w3.org/2001/XMLSchema#integer) (c)<br />
[](hasSImassdimensionexponent)
### has SI mass dimension exponent
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#hasSIMassDimensionExponent`
Domain(s) |[om:Dimension](http://opendata.caceres.es/def/ontomunicipio#Dimension) (c)<br />
Range(s) |[xsd:integer](http://www.w3.org/2001/XMLSchema#integer) (c)<br />
[](hasSIthermodynamictemperaturedimensionexponent)
### has SI thermodynamic temperature dimension exponent
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#hasSIThermodynamicTemperatureDimensionExponent`
Domain(s) |[om:Dimension](http://opendata.caceres.es/def/ontomunicipio#Dimension) (c)<br />
Range(s) |[xsd:integer](http://www.w3.org/2001/XMLSchema#integer) (c)<br />
[](hasSItimedimensionexponent)
### has SI time dimension exponent
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#hasSITimeDimensionExponent`
Domain(s) |[om:Dimension](http://opendata.caceres.es/def/ontomunicipio#Dimension) (c)<br />
Range(s) |[xsd:integer](http://www.w3.org/2001/XMLSchema#integer) (c)<br />

## Annotation Properties
[LaTeX command](#LaTeXcommand),
[LaTeX symbol](#LaTeXsymbol),
[abbreviation](#abbreviation),
[alternative LaTeX symbol](#alternativeLaTeXsymbol),
[alternative label](#alternativelabel),
[alternative symbol](#alternativesymbol),
[longcomment](#longcomment),
[symbol](#symbol),
[unofficial abbreviation](#unofficialabbreviation),
[unofficial label](#unofficiallabel),
[creator](#creator),
[date](#date),
[identifier](#identifier),
[hiddenLabel](#hiddenLabel),
[illustration](#illustration),
[logo](#logo),
[](LaTeXcommand)
### LaTeX command
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#LaTeXCommand`
Description | OMLaTeX command that can be used to render this quantity or unit.
[](LaTeXsymbol)
### LaTeX symbol
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#LaTeXSymbol`
Description | OMLaTeX formatted symbol may include commands such as \unit and \E as defined in OMLaTeX.
[](abbreviation)
### abbreviation
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#abbreviation`
[](alternativeLaTeXsymbol)
### alternative LaTeX symbol
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#alternativeLaTeXSymbol`
Description | An alternative OMLaTeX formatted symbol, which may include commands such as \unit and \E as defined in OMLaTeX.
[](alternativelabel)
### alternative label
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#alternativeLabel`
[](alternativesymbol)
### alternative symbol
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#alternativeSymbol`
[](longcomment)
### longcomment
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#longcomment`
[](symbol)
### symbol
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#symbol`
[](unofficialabbreviation)
### unofficial abbreviation
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#unofficialAbbreviation`
Description | Used to specify abbreviations that are used in e.g. every day speech but are not defined in any standard.
Super-properties |[skos:hiddenLabel](http://www.w3.org/2004/02/skos/core#hiddenLabel) (ap)<br />
[](unofficiallabel)
### unofficial label
Property | Value
--- | ---
URI | `http://opendata.caceres.es/def/ontomunicipio#unofficialLabel`
Description | Used to specify labels that are used in e.g. every day speech but are not defined in any standard.
Super-properties |[skos:hiddenLabel](http://www.w3.org/2004/02/skos/core#hiddenLabel) (ap)<br />
[](creator)
### creator
Property | Value
--- | ---
URI | `http://purl.org/dc/elements/1.1/creator`
[](date)
### date
Property | Value
--- | ---
URI | `http://purl.org/dc/elements/1.1/date`
[](identifier)
### identifier
Property | Value
--- | ---
URI | `http://purl.org/dc/elements/1.1/identifier`
[](hiddenLabel)
### hiddenLabel
Property | Value
--- | ---
URI | `http://www.w3.org/2004/02/skos/core#hiddenLabel`
[](illustration)
### illustration
Property | Value
--- | ---
URI | `http://www.wurvoc.org/vocabularies/WV/illustration`
[](logo)
### logo
Property | Value
--- | ---
URI | `http://www.wurvoc.org/vocabularies/WV/logo`

## Named Individuals
## Namespaces
* **bibo**
  * `http://purl.org/ontology/bibo/`
* **dc**
  * `http://purl.org/dc/elements/1.1/`
* **dct**
  * `http://purl.org/dc/terms/`
* **foaf**
  * `http://xmlns.com/foaf/0.1/`
* **om**
  * `http://opendata.caceres.es/def/ontomunicipio#`
* **owl**
  * `http://www.w3.org/2002/07/owl#`
* **prov**
  * `http://www.w3.org/ns/prov#`
* **rdf**
  * `http://www.w3.org/1999/02/22-rdf-syntax-ns#`
* **rdfs**
  * `http://www.w3.org/2000/01/rdf-schema#`
* **sdo**
  * `https://schema.org/`
* **skos**
  * `http://www.w3.org/2004/02/skos/core#`
* **xsd**
  * `http://www.w3.org/2001/XMLSchema#`

## Legend
* Classes: c
* Object Properties: op
* Functional Properties: fp
* Data Properties: dp
* Annotation Properties: dp
* Properties: p
* Named Individuals: ni