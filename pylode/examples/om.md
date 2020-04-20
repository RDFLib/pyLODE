# Ontology of units of Measure (OM)
Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE)


## Metadata
* **IRI**
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
[Fahrenheit temperature scale](#Fahrenheittemperaturescale),
[Fahrenheit temperature unit](#Fahrenheittemperatureunit),
[Fahrenheittemperatuur](#Fahrenheittemperatuur),
[Fourier number for mass transfer](#Fouriernumberformasstransfer),
[Fourier number for mass transfer unit](#Fouriernumberformasstransferunit),
[Fourier number unit](#Fouriernumberunit),
[Froude number](#Froudenumber),
[Froude number unit](#Froudenumberunit),
[Grashof number for mass transfer](#Grashofnumberformasstransfer),
[Grashof number for mass transfer unit](#Grashofnumberformasstransferunit),
[Grashof number unit](#Grashofnumberunit),
[Hartmann number unit](#Hartmannnumberunit),
[Hubble constant unit](#Hubbleconstantunit),
[I magnitude](#Imagnitude),
[Jeans mass](#Jeansmass),
[Johnson magnitude](#Johnsonmagnitude),
[Klebsiella count (specific)](#Klebsiellacount(specific)),
[Klebsiella count (volumetric)](#Klebsiellacount(volumetric)),
[Knudsen number](#Knudsennumber),
[Knudsen number unit](#Knudsennumberunit),
[Lewis number unit](#Lewisnumberunit),
[Listeria monocytogenes count (specific)](#Listeriamonocytogenescount(specific)),
[Listeria monocytogenes count (volumetric)](#Listeriamonocytogenescount(volumetric)),
[Mach number](#Machnumber),
[Mach number unit](#Machnumberunit),
[Nusselt number](#Nusseltnumber),
[Nusselt number for mass transfer](#Nusseltnumberformasstransfer),
[Nusselt number for mass transfer unit](#Nusseltnumberformasstransferunit),
[Nusselt number unit](#Nusseltnumberunit),
[Prandtl number unit](#Prandtlnumberunit),
[Péclet number](#Pcletnumber),
[Péclet number for mass transfer](#Pcletnumberformasstransfer),
[Péclet number for mass transfer unit](#Pcletnumberformasstransferunit),
[Péclet number unit](#Pcletnumberunit),
[R magnitude](#Rmagnitude),
[Rankine temperature scale](#Rankinetemperaturescale),
[Rankine temperature unit](#Rankinetemperatureunit),
[Rankinetemperatuur](#Rankinetemperatuur),
[Rayleigh number](#Rayleighnumber),
[Rayleigh number unit](#Rayleighnumberunit),
[Reynolds number unit](#Reynoldsnumberunit),
[Réaumur temperature scale](#Raumurtemperaturescale),
[Réaumur temperature unit](#Raumurtemperatureunit),
[Réaumurtemperatuur](#Raumurtemperatuur),
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
[aantal Botrytis 0](#aantalBotrytis0),
[aantal Botrytis 2](#aantalBotrytis2),
[aantal Botrytis 4](#aantalBotrytis4),
[aantal bladeren](#aantalbladeren),
[aantal bloemen](#aantalbloemen),
[aantal gevallen bloemen](#aantalgevallenbloemen),
[aantal kleur 1](#aantalkleur1),
[aantal kleur 2](#aantalkleur2),
[aantal kleur 3](#aantalkleur3),
[aantal knopstadium](#aantalknopstadium),
[aantal knopstadium 2](#aantalknopstadium2),
[aantal knopstadium 4](#aantalknopstadium4),
[aantal manuele stevigheid 0](#aantalmanuelestevigheid0),
[aantal manuele stevigheid 1](#aantalmanuelestevigheid1),
[aantal manuele stevigheid 1.5](#aantalmanuelestevigheid1.5),
[aantal manuele stevigheid 2.5](#aantalmanuelestevigheid2.5),
[aantal manuele stevigheid 3.5](#aantalmanuelestevigheid3.5),
[aantal manuele stevigheid 4](#aantalmanuelestevigheid4),
[aantal manuele stevigheid 4.5](#aantalmanuelestevigheid4.5),
[aantal manuele stevigheid 5](#aantalmanuelestevigheid5),
[aantal misvormde knoppen](#aantalmisvormdeknoppen),
[aantal rotte bladeren](#aantalrottebladeren),
[aantal vergeelde bladeren](#aantalvergeeldebladeren),
[aantal verwelkte bladeren](#aantalverwelktebladeren),
[aantal verwelkte bloemen](#aantalverwelktebloemen),
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
[actie](#actie),
[action unit](#actionunit),
[activiteit](#activiteit),
[activity unit](#activityunit),
[admittance](#admittance),
[albedo](#albedo),
[altitude](#altitude),
[ambient dose equivalent](#ambientdoseequivalent),
[amfifiliciteit](#amfifiliciteit),
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
[amplitude](#amplitude),
[angle](#angle),
[angle unit](#angleunit),
[angular acceleration](#angularacceleration),
[angular acceleration unit](#angularaccelerationunit),
[angular displacement](#angulardisplacement),
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
[area density](#areadensity),
[area density rate](#areadensityrate),
[area density rate unit](#areadensityrateunit),
[area density unit](#areadensityunit),
[area fraction](#areafraction),
[area fraction unit](#areafractionunit),
[area unit](#areaunit),
[atomic mass](#atomicmass),
[azimut](#azimut),
[b magnitude](#bmagnitude),
[binary prefix](#binaryprefix),
[body label mass](#bodylabelmass),
[body mass](#bodymass),
[bolometric correction](#bolometriccorrection),
[bolometric magnitude](#bolometricmagnitude),
[bond albedo](#bondalbedo),
[breadth](#breadth),
[breedte](#breedte),
[brightness temperature](#brightnesstemperature),
[bud stadium day 0](#budstadiumday0),
[cap mass](#capmass),
[capacitance unit](#capacitanceunit),
[capaciteit](#capaciteit),
[carton mass](#cartonmass),
[catalytic activity](#catalyticactivity),
[catalytic activity concentration](#catalyticactivityconcentration),
[catalytic activity concentration unit](#catalyticactivityconcentrationunit),
[catalytic activity unit](#catalyticactivityunit),
[cause end of vase life Botrytis](#causeendofvaselifeBotrytis),
[cause end of vase life abscised leaves](#causeendofvaselifeabscisedleaves),
[cause end of vase life blue flowers](#causeendofvaselifeblueflowers),
[cause end of vase life dry flowers](#causeendofvaselifedryflowers),
[cause end of vase life malformed buds](#causeendofvaselifemalformedbuds),
[cause end of vase life nonturgid flowers](#causeendofvaselifenonturgidflowers),
[cause end of vase life nonturgid leaves](#causeendofvaselifenonturgidleaves),
[co-rotation radius](#co-rotationradius),
[cold gas mass fraction](#coldgasmassfraction),
[coliform bacteria count (specific)](#coliformbacteriacount(specific)),
[coliform bacteria count (volumetric)](#coliformbacteriacount(volumetric)),
[collision frequency](#collisionfrequency),
[color area fraction](#colorareafraction),
[colour temperature](#colourtemperature),
[column number density](#columnnumberdensity),
[column number density unit](#columnnumberdensityunit),
[compound unit](#compoundunit),
[compressiemodulus](#compressiemodulus),
[compressive stress](#compressivestress),
[constante van Hubble](#constantevanHubble),
[constante van Hubble tijdens het huidige epoch](#constantevanHubbletijdenshethuidigeepoch),
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
[datum](#datum),
[deceleration parameter](#decelerationparameter),
[deceleration parameter unit](#decelerationparameterunit),
[declinatie](#declinatie),
[density parameter](#densityparameter),
[density parameter for baryonic matter](#densityparameterforbaryonicmatter),
[density parameter for matter](#densityparameterformatter),
[density parameter for radiation](#densityparameterforradiation),
[density parameter for vacuum](#densityparameterforvacuum),
[density parameter unit](#densityparameterunit),
[density unit](#densityunit),
[detective quantum efficiency](#detectivequantumefficiency),
[detectivity](#detectivity),
[detectivity unit](#detectivityunit),
[diameter (hoek)](#diameter(hoek)),
[diepte](#diepte),
[dikte](#dikte),
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
[druk](#druk),
[dry body mass](#drybodymass),
[dry mass](#drymass),
[dry matter mass fraction](#drymattermassfraction),
[duur](#duur),
[dynamic modulus](#dynamicmodulus),
[dynamic range](#dynamicrange),
[dynamic range unit](#dynamicrangeunit),
[dynamic viscosity unit](#dynamicviscosityunit),
[dynamische viscositeit](#dynamischeviscositeit),
[eccentriciteit](#eccentriciteit),
[ecliptic latitude](#eclipticlatitude),
[ecliptic longitude](#eclipticlongitude),
[egg mass fraction](#eggmassfraction),
[elasticiteitsmodulus](#elasticiteitsmodulus),
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
[energy density](#energydensity),
[energy density unit](#energydensityunit),
[energy unit](#energyunit),
[entropy unit](#entropyunit),
[epoch](#epoch),
[epoch at maximum brightness](#epochatmaximumbrightness),
[exposure](#exposure),
[exposure to x and γ rays](#exposuretoxandrays),
[exposure to x and γ rays unit](#exposuretoxandraysunit),
[exposure unit](#exposureunit),
[external browning](#externalbrowning),
[extinctie](#extinctie),
[extinction at waveband](#extinctionatwaveband),
[extinction at wavelength](#extinctionatwavelength),
[extinction in B](#extinctioninB),
[extinction in U](#extinctioninU),
[extinction in V](#extinctioninV),
[fat mass fraction](#fatmassfraction),
[first Cowling number](#firstCowlingnumber),
[first Cowling number unit](#firstCowlingnumberunit),
[fixed point](#fixedpoint),
[fixed zero point](#fixedzeropoint),
[flowpack mass](#flowpackmass),
[fluidity](#fluidity),
[fluidity unit](#fluidityunit),
[font size unit](#fontsizeunit),
[fontgrootte](#fontgrootte),
[force](#force),
[force unit](#forceunit),
[frequency unit](#frequencyunit),
[frequentie](#frequentie),
[friction](#friction),
[function](#function),
[g magnitude](#gmagnitude),
[galactic cylindrical polar angle coordinate](#galacticcylindricalpolaranglecoordinate),
[galactic latitude](#galacticlatitude),
[galactic longitude](#galacticlongitude),
[gas constant unit](#gasconstantunit),
[gasconstante](#gasconstante),
[gelatin mass fraction](#gelatinmassfraction),
[geometrical albedo](#geometricalalbedo),
[getal van Fourier](#getalvanFourier),
[getal van Grashof](#getalvanGrashof),
[getal van Hartmann](#getalvanHartmann),
[getal van Lewis](#getalvanLewis),
[getal van Prandtl](#getalvanPrandtl),
[getal van Reynolds](#getalvanReynolds),
[golflengte](#golflengte),
[gram per prefixed litre](#gramperprefixedlitre),
[guar gum mass fraction](#guargummassfraction),
[half-life](#half-life),
[heat capacity](#heatcapacity),
[heat capacity unit](#heatcapacityunit),
[heat flow rate](#heatflowrate),
[heat flux density](#heatfluxdensity),
[heat transfer coefficient](#heattransfercoefficient),
[heat transfer coefficient unit](#heattransfercoefficientunit),
[height](#height),
[hour angle](#hourangle),
[hydrofobiciteit](#hydrofobiciteit),
[hydrophilicity](#hydrophilicity),
[illuminance](#illuminance),
[illuminance unit](#illuminanceunit),
[impulsmoment](#impulsmoment),
[inductance](#inductance),
[inductance unit](#inductanceunit),
[information capacity](#informationcapacity),
[information capacity unit](#informationcapacityunit),
[initial mass function](#initialmassfunction),
[integrated magnitude](#integratedmagnitude),
[interval scale](#intervalscale),
[intrinsic colour index](#intrinsiccolourindex),
[inwendige energie](#inwendigeenergie),
[ionization temperature](#ionizationtemperature),
[irradiance](#irradiance),
[kerma](#kerma),
[kinematic viscosity](#kinematicviscosity),
[kinematic viscosity unit](#kinematicviscosityunit),
[kinetic energy](#kineticenergy),
[kleurindex](#kleurindex),
[knopstadium](#knopstadium),
[knopstadium dag 4](#knopstadiumdag4),
[knopstadium dag 7](#knopstadiumdag7),
[kwaliteitscijfer bloem(en)](#kwaliteitscijferbloem(en)),
[kwaliteitscijfer total](#kwaliteitscijfertotal),
[label mass](#labelmass),
[lactose mass fraction](#lactosemassfraction),
[length unit](#lengthunit),
[lichtsterkte](#lichtsterkte),
[light time](#lighttime),
[limiting magnitude](#limitingmagnitude),
[lineaire vervorming](#lineairevervorming),
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
[luminous intensity unit](#luminousintensityunit),
[magnetic Reynolds number unit](#magneticReynoldsnumberunit),
[magnetic field](#magneticfield),
[magnetic field unit](#magneticfieldunit),
[magnetic flux](#magneticflux),
[magnetic flux density](#magneticfluxdensity),
[magnetic flux density unit](#magneticfluxdensityunit),
[magnetic flux unit](#magneticfluxunit),
[magnetisch getal van Reynolds](#magnetischgetalvanReynolds),
[magnetomotive force](#magnetomotiveforce),
[magnetomotive force unit](#magnetomotiveforceunit),
[magnitude](#magnitude),
[magnitude at maximum brightness](#magnitudeatmaximumbrightness),
[magnitude at minimum brightness](#magnitudeatminimumbrightness),
[magnitude unit](#magnitudeunit),
[manual firmness](#manualfirmness),
[mass flow](#massflow),
[mass flow unit](#massflowunit),
[mass fraction](#massfraction),
[mass fraction unit](#massfractionunit),
[mass unit](#massunit),
[massa](#massa),
[measure](#measure),
[mechanische spanning](#mechanischespanning),
[metallicity](#metallicity),
[metre per prefixed second (time)](#metreperprefixedsecond(time)),
[metre per prefixed second (time) squared](#metreperprefixedsecond(time)squared),
[moderated starch mass fraction](#moderatedstarchmassfraction),
[molair volume](#molairvolume),
[molaire energie](#molaireenergie),
[molaire warmtecapaciteit](#molairewarmtecapaciteit),
[molality](#molality),
[molality unit](#molalityunit),
[molar energy unit](#molarenergyunit),
[molar entropy](#molarentropy),
[molar entropy unit](#molarentropyunit),
[molar heat capacity unit](#molarheatcapacityunit),
[molar mass](#molarmass),
[molar mass unit](#molarmassunit),
[molar volume unit](#molarvolumeunit),
[mole per prefixed litre](#moleperprefixedlitre),
[mole per prefixed metre](#moleperprefixedmetre),
[moment of force](#momentofforce),
[moment of force unit](#momentofforceunit),
[moment of inertia unit](#momentofinertiaunit),
[momentum](#momentum),
[momentum unit](#momentumunit),
[mustard powder mass fraction](#mustardpowdermassfraction),
[neck ring mass](#neckringmass),
[noise equivalent power](#noiseequivalentpower),
[normaalspanning](#normaalspanning),
[normaalvervorming](#normaalvervorming),
[normal albedo](#normalalbedo),
[normalised detectivity](#normaliseddetectivity),
[number](#number),
[number Botrytis](#numberBotrytis),
[number Botrytis 1](#numberBotrytis1),
[number Botrytis 3](#numberBotrytis3),
[number abscised buds](#numberabscisedbuds),
[number abscised leaves](#numberabscisedleaves),
[number blue-discolored flowers](#numberblue-discoloredflowers),
[number bud stadium 1](#numberbudstadium1),
[number bud stadium 3](#numberbudstadium3),
[number bud stadium 5](#numberbudstadium5),
[number buds](#numberbuds),
[number color](#numbercolor),
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
[number malformed flowers](#numbermalformedflowers),
[number manual firmness](#numbermanualfirmness),
[number manual firmness 0.5](#numbermanualfirmness0.5),
[number manual firmness 2](#numbermanualfirmness2),
[number manual firmness 3](#numbermanualfirmness3),
[number nonturgid flowers](#numbernonturgidflowers),
[number nonturgid leaves](#numbernonturgidleaves),
[number pulp browning](#numberpulpbrowning),
[number pulp browning 1](#numberpulpbrowning1),
[number pulp browning 2](#numberpulpbrowning2),
[number pulp browning 3](#numberpulpbrowning3),
[number pulp browning 4](#numberpulpbrowning4),
[number pulp browning 5](#numberpulpbrowning5),
[number rotten flowers](#numberrottenflowers),
[number unit](#numberunit),
[number vascular browning](#numbervascularbrowning),
[number vascular browning 1](#numbervascularbrowning1),
[number vascular browning 2](#numbervascularbrowning2),
[number vascular browning 3](#numbervascularbrowning3),
[number vascular browning 4](#numbervascularbrowning4),
[number vascular browning 5](#numbervascularbrowning5),
[oorzaak einde vaasleven bladverdroging](#oorzaakeindevaaslevenbladverdroging),
[oorzaak einde vaasleven bladvergeling](#oorzaakeindevaaslevenbladvergeling),
[oorzaak einde vaasleven bladverwelking](#oorzaakeindevaaslevenbladverwelking),
[oorzaak einde vaasleven bloemrot](#oorzaakeindevaaslevenbloemrot),
[oorzaak einde vaasleven bloemval](#oorzaakeindevaaslevenbloemval),
[oorzaak einde vaasleven bloemverwelking](#oorzaakeindevaaslevenbloemverwelking),
[oorzaak einde vaasleven knopval](#oorzaakeindevaaslevenknopval),
[oorzaak einde vaasleven knopverdroging](#oorzaakeindevaaslevenknopverdroging),
[oorzaak einde vaasleven misvormde bloemen](#oorzaakeindevaaslevenmisvormdebloemen),
[oorzaak einde vaasleven rotte bladeren](#oorzaakeindevaaslevenrottebladeren),
[oppervlakte](#oppervlakte),
[oppervlaktespanning](#oppervlaktespanning),
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
[potentiële energie](#potentileenergie),
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
[pressure unit](#pressureunit),
[protein mass fraction](#proteinmassfraction),
[pulp browning](#pulpbrowning),
[quality mark](#qualitymark),
[quality mark leafs](#qualitymarkleafs),
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
[radius (angle)](#radius(angle)),
[ratio](#ratio),
[ratio scale](#ratioscale),
[ratio unit](#ratiounit),
[rechte klimming](#rechteklimming),
[red magnitude](#redmagnitude),
[reddening](#reddening),
[reddening (B-V)](#reddening(B-V)),
[reddening (U-B)](#reddening(U-B)),
[relatieve luchtvochtigheid](#relatieveluchtvochtigheid),
[relative humidity unit](#relativehumidityunit),
[reluctance](#reluctance),
[reluctance unit](#reluctanceunit),
[resonance energy](#resonanceenergy),
[responsivity](#responsivity),
[responsivity unit](#responsivityunit),
[salt mass fraction](#saltmassfraction),
[scale](#scale),
[scale height](#scaleheight),
[scale length](#scalelength),
[schaalfactor](#schaalfactor),
[secular aberration](#secularaberration),
[shear loss modulus](#shearlossmodulus),
[shear modulus](#shearmodulus),
[shear rate](#shearrate),
[shear rate unit](#shearrateunit),
[shear storage modulus](#shearstoragemodulus),
[shear strain](#shearstrain),
[shear stress](#shearstress),
[singular unit](#singularunit),
[snelheid (vector)](#snelheid(vector)),
[solid angle unit](#solidangleunit),
[soortelijke warmte](#soortelijkewarmte),
[soy bean mass fraction](#soybeanmassfraction),
[specific amylase activity](#specificamylaseactivity),
[specific catalytic activity](#specificcatalyticactivity),
[specific catalytic activity unit](#specificcatalyticactivityunit),
[specific energy](#specificenergy),
[specific energy imparted](#specificenergyimparted),
[specific energy unit](#specificenergyunit),
[specific entropy](#specificentropy),
[specific entropy unit](#specificentropyunit),
[specific heat capacity unit](#specificheatcapacityunit),
[specific protease activity](#specificproteaseactivity),
[specific viable count unit](#specificviablecountunit),
[specific volume](#specificvolume),
[specific volume unit](#specificvolumeunit),
[spectral response](#spectralresponse),
[speed unit](#speedunit),
[square prefixed metre](#squareprefixedmetre),
[starch VA40 mass fraction](#starchVA40massfraction),
[starch VA85 mass fraction](#starchVA85massfraction),
[starch mass fraction](#starchmassfraction),
[stellar aberration](#stellaraberration),
[stem end rot](#stemendrot),
[stem-end-rot-oppervlaktefractie](#stem-end-rot-oppervlaktefractie),
[stevigheid (penetrometer) (methode 1)](#stevigheid(penetrometer)(methode1)),
[stevigheid (penetrometer) (methode 2)](#stevigheid(penetrometer)(methode2)),
[stick stone](#stickstone),
[stoot](#stoot),
[storage modulus](#storagemodulus),
[straal](#straal),
[strain](#strain),
[strain tensor](#straintensor),
[strain unit](#strainunit),
[straw mass](#strawmass),
[stress tensor](#stresstensor),
[stress unit](#stressunit),
[sugar mass fraction](#sugarmassfraction),
[supergalactic latitude](#supergalacticlatitude),
[supergalactic longitude](#supergalacticlongitude),
[surface tension unit](#surfacetensionunit),
[symbol rate](#symbolrate),
[symbol rate unit](#symbolrateunit),
[system of units](#systemofunits),
[temperature rate unit](#temperaturerateunit),
[temperature unit](#temperatureunit),
[temperatuur](#temperatuur),
[temperatuur-rate](#temperatuur-rate),
[thermal conductivity unit](#thermalconductivityunit),
[thermal diffusivity](#thermaldiffusivity),
[thermal diffusivity unit](#thermaldiffusivityunit),
[thermal insulance](#thermalinsulance),
[thermal insulance unit](#thermalinsulanceunit),
[thermal resistance](#thermalresistance),
[thermal resistance unit](#thermalresistanceunit),
[thermische geleidbaarheid](#thermischegeleidbaarheid),
[thermodynamic temperature](#thermodynamictemperature),
[thermodynamic temperature scale](#thermodynamictemperaturescale),
[thermodynamic temperature unit](#thermodynamictemperatureunit),
[thrust](#thrust),
[time](#time),
[time constant](#timeconstant),
[time unit](#timeunit),
[top mass](#topmass),
[torque unit](#torqueunit),
[totaal aantal bladeren](#totaalaantalbladeren),
[totaal aantal knoppen](#totaalaantalknoppen),
[total 3D start-end distance](#total3Dstart-enddistance),
[total density parameter](#totaldensityparameter),
[total distance travelled](#totaldistancetravelled),
[total number flowers](#totalnumberflowers),
[traagheidsmoment](#traagheidsmoment),
[true distance modulus](#truedistancemodulus),
[tween mass fraction](#tweenmassfraction),
[u magnitude](#umagnitude),
[unit](#unit),
[unit division](#unitdivision),
[unit exponentiation](#unitexponentiation),
[unit multiple](#unitmultiple),
[unit multiplication](#unitmultiplication),
[v magnitude](#vmagnitude),
[vaas- plus water- plus bloemmassa](#vaas-pluswater-plusbloemmassa),
[vaas- plus watermassa](#vaas-pluswatermassa),
[vaasleven](#vaasleven),
[valversnelling](#valversnelling),
[vascular browning](#vascularbrowning),
[viable count (specific)](#viablecount(specific)),
[viable count (volumetric)](#viablecount(volumetric)),
[visual albedo](#visualalbedo),
[volume](#volume),
[volume fraction unit](#volumefractionunit),
[volume strain](#volumestrain),
[volume unit](#volumeunit),
[volumefractie](#volumefractie),
[volumetric flow rate](#volumetricflowrate),
[volumetric flow rate unit](#volumetricflowrateunit),
[volumetric heat capacity](#volumetricheatcapacity),
[volumetric heat capacity unit](#volumetricheatcapacityunit),
[volumetric viable count unit](#volumetricviablecountunit),
[warmte](#warmte),
[water mass fraction](#watermassfraction),
[wave number unit](#wavenumberunit),
[wavenumber](#wavenumber),
[weight](#weight),
[wetting angle](#wettingangle),
[whey protein aggregate mass fraction](#wheyproteinaggregatemassfraction),
[whey protein beads mass fraction](#wheyproteinbeadsmassfraction),
[whey protein mass fraction](#wheyproteinmassfraction),
[white light magnitude](#whitelightmagnitude),
[white light magnitude at maximum brightness](#whitelightmagnitudeatmaximumbrightness),
[white light magnitude at minimum brightness](#whitelightmagnitudeatminimumbrightness),
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
[zenitafstand](#zenitafstand),
[zoutsterkte](#zoutsterkte),
[β_narrow magnitude](#_narrowmagnitude),
[β_wide magnitude](#_widemagnitude),
[功率](#Power),
[圆周](#),
[密度](#Density),
[扭矩](#Torque),
[焓](#Enthalpy),
[熵单位](#Entropy),
[直径](#Diameter),
[立体角](#SolidAngle),
[能量](#Energy),
[速度](#Speed),
[长度](#Length),
### aberration
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Aberration`
Description | <p>The apparent angular displacement of the observed position of a celestial object from its geometric position, caused by the finite velocity of light in combination with the motions of the observer and of the observed object.</p>
Super-classes |[om:AngularDisplacement](http://opendata.caceres.es/def/ontomunicipio#AngularDisplacement) (c)<br />
Sub-classes |[om:PlanetaryAberration](http://opendata.caceres.es/def/ontomunicipio#PlanetaryAberration) (c)<br />[om:StellarAberration](http://opendata.caceres.es/def/ontomunicipio#StellarAberration) (c)<br />
### aberration in latitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AberrationInLatitude`
Description | <p>The apparent angular displacement in ecliptical latitude of the observed position of a celestial object from its geometric position, caused by the finite velocity of light in combination with the motions of the observer and of the observed object.</p>
Super-classes |[om:AngularDisplacement](http://opendata.caceres.es/def/ontomunicipio#AngularDisplacement) (c)<br />
### aberration in longitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AberrationInLongitude`
Description | <p>The apparent angular displacement in ecliptical longitude of the observed position of a celestial object from its geometric position, caused by the finite velocity of light in combination with the motions of the observer and of the observed object.</p>
Super-classes |[om:AngularDisplacement](http://opendata.caceres.es/def/ontomunicipio#AngularDisplacement) (c)<br />
### absolute bolometric magnitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AbsoluteBolometricMagnitude`
Description | <p>The absolute magnitude (see absolute magnitude) of a star is a measure of its total energy emission per second, or luminosity, i.e., the bolometric magnitude from a standard distance (10 pc).</p>
Super-classes |[om:BolometricMagnitude](http://opendata.caceres.es/def/ontomunicipio#BolometricMagnitude) (c)<br />
### absolute magnitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AbsoluteMagnitude`
Description | <p>Logarithmic measure of the brightness of an object as seen from a standard distance of 10 pc. Units usually not indicated (http://en.wikipedia.org/wiki/Magnitude_(astronomy).</p>
Super-classes |[om:Magnitude](http://opendata.caceres.es/def/ontomunicipio#Magnitude) (c)<br />
### absorbed dose
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AbsorbedDose`
Description | <p>Absorbed dose is the energy deposited in a medium by ionizing radiation. It is a derived quantity in the International System of Units. Absorbed dose is energy divided by mass.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:specificEnergyOrAbsorbedDoseOrDoseEquivalent-Dimension](http://opendata.caceres.es/def/ontomunicipio#specificEnergyOrAbsorbedDoseOrDoseEquivalent-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:Kerma](http://opendata.caceres.es/def/ontomunicipio#Kerma) (c)<br />[om:SpecificEnergyImparted](http://opendata.caceres.es/def/ontomunicipio#SpecificEnergyImparted) (c)<br />
### absorbed dose rate
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AbsorbedDoseRate`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:absorbedDoseRate-Dimension](http://opendata.caceres.es/def/ontomunicipio#absorbedDoseRate-Dimension) (c)<br />
### absorbed dose rate unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AbsorbedDoseRateUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### absorbed dose unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AbsorbedDoseUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### acceleration
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Acceleration`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:acceleration-Dmension](http://opendata.caceres.es/def/ontomunicipio#acceleration-Dmension) (c)<br />
Sub-classes |[om:GravitationalAcceleration](http://opendata.caceres.es/def/ontomunicipio#GravitationalAcceleration) (c)<br />
### acceleration unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AccelerationUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### acetic acid mass fraction
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AceticAcidMassFraction`
Description | <p>The fraction of the mass of acetic acid in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### acidity
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Acidity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### acoustic firmness
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AcousticFirmness`
Description | <p>Stevigheid gemeten met AWETA (acoustic firmness value). AFS value.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### actie
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Action`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:actionOrAngularMomentum-Dimension](http://opendata.caceres.es/def/ontomunicipio#actionOrAngularMomentum-Dimension) (c)<br />
### action unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ActionUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### activiteit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Activity`
Description | <p>Activity is the decay rate of a radioactive substance. It is a derived quantity in the International System of Units. Activity is 1 divided by time.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:frequency-Dimension](http://opendata.caceres.es/def/ontomunicipio#frequency-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### activity unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ActivityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### admittance
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Admittance`
Description | <p>Admittance is a measure of how easily a circuit or device will allow a current to flow. It is electric current divided by electric potential.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### albedo
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Albedo`
Description | <p>Ratio between radiation falling onto an object and the radiation reflected or scattered back. Or the ratio between the illumination and observed brightness.</p>
Super-classes |[om:QuantityOfDimensionOne](http://opendata.caceres.es/def/ontomunicipio#QuantityOfDimensionOne) (c)<br />
Sub-classes |[om:NormalAlbedo](http://opendata.caceres.es/def/ontomunicipio#NormalAlbedo) (c)<br />[om:VisualAlbedo](http://opendata.caceres.es/def/ontomunicipio#VisualAlbedo) (c)<br />[om:GeometricalAlbedo](http://opendata.caceres.es/def/ontomunicipio#GeometricalAlbedo) (c)<br />[om:BondAlbedo](http://opendata.caceres.es/def/ontomunicipio#BondAlbedo) (c)<br />
### Alfvén number
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AlfvenNumber`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
### Alfvén number unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AlfvenNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### altitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Altitude`
Description | <p>The angular distance of a celestial body above or below the horizon, measured along the great circle passing through the body and the zenith.</p>
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
### ambient dose equivalent
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AmbientDoseEquivalent`
Super-classes |[om:DoseEquivalent](http://opendata.caceres.es/def/ontomunicipio#DoseEquivalent) (c)<br />
### amount of money
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AmountOfMoney`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:Cost](http://opendata.caceres.es/def/ontomunicipio#Cost) (c)<br />
### amount of money unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AmountOfMoneyUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### amount of substance
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AmountOfSubstance`
Description | <p>Amount of substance is the number of elementary entities such as atoms, molecules, electrons, particles, etc. present in a phenomenon. It is a base quantity in the International System of Units.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:amountOfSubstance-Dimension](http://opendata.caceres.es/def/ontomunicipio#amountOfSubstance-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### amount of substance concentration
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AmountOfSubstanceConcentration`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:amountOfSubstanceConcentration-Dimension](http://opendata.caceres.es/def/ontomunicipio#amountOfSubstanceConcentration-Dimension) (c)<br />
### amount of substance concentration unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AmountOfSubstanceConcentrationUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### amount of substance flow
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AmountOfSubstanceFlow`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### amount of substance flow unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AmountOfSubstanceFlowUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### amount of substance fraction
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AmountOfSubstanceFraction`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### amount of substance fraction flow
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AmountOfSubstanceFractionFlow`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### amount of substance fraction unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AmountOfSubstanceFractionUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### amount of substance unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AmountOfSubstanceUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### amfifiliciteit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Amphiphilicity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### amplitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Amplitude`
Description | <p>The difference between the maximum and minimum magnitudes of a variable star, i.e., the total range of its brightness.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Sub-classes |[om:VAmplitude](http://opendata.caceres.es/def/ontomunicipio#VAmplitude) (c)<br />[om:PhotographicAmplitude](http://opendata.caceres.es/def/ontomunicipio#PhotographicAmplitude) (c)<br />
### angle
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Angle`
Description | <p>Angle is the ratio between an arc and its radius.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:Diameter-Angle](http://opendata.caceres.es/def/ontomunicipio#Diameter-Angle) (c)<br />[om:ContactAngle](http://opendata.caceres.es/def/ontomunicipio#ContactAngle) (c)<br />[om:Radius-Angle](http://opendata.caceres.es/def/ontomunicipio#Radius-Angle) (c)<br />[om:SupergalacticLongitude](http://opendata.caceres.es/def/ontomunicipio#SupergalacticLongitude) (c)<br />[om:EclipticLatitude](http://opendata.caceres.es/def/ontomunicipio#EclipticLatitude) (c)<br />[om:GalacticLongitude](http://opendata.caceres.es/def/ontomunicipio#GalacticLongitude) (c)<br />[om:ZenithDistance](http://opendata.caceres.es/def/ontomunicipio#ZenithDistance) (c)<br />[om:WettingAngle](http://opendata.caceres.es/def/ontomunicipio#WettingAngle) (c)<br />[om:Declination](http://opendata.caceres.es/def/ontomunicipio#Declination) (c)<br />[om:GalacticCylindricalPolarAngleCoordinate](http://opendata.caceres.es/def/ontomunicipio#GalacticCylindricalPolarAngleCoordinate) (c)<br />[om:Altitude](http://opendata.caceres.es/def/ontomunicipio#Altitude) (c)<br />[om:HourAngle](http://opendata.caceres.es/def/ontomunicipio#HourAngle) (c)<br />[om:RightAscension](http://opendata.caceres.es/def/ontomunicipio#RightAscension) (c)<br />[om:ApparentDiameter](http://opendata.caceres.es/def/ontomunicipio#ApparentDiameter) (c)<br />[om:Azimuth](http://opendata.caceres.es/def/ontomunicipio#Azimuth) (c)<br />[om:EclipticLongitude](http://opendata.caceres.es/def/ontomunicipio#EclipticLongitude) (c)<br />[om:AngularDisplacement](http://opendata.caceres.es/def/ontomunicipio#AngularDisplacement) (c)<br />[om:SupergalacticLatitude](http://opendata.caceres.es/def/ontomunicipio#SupergalacticLatitude) (c)<br />[om:GalacticLatitude](http://opendata.caceres.es/def/ontomunicipio#GalacticLatitude) (c)<br />
### angle unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AngleUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### angular acceleration
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AngularAcceleration`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:angularAcceleration-Dmension](http://opendata.caceres.es/def/ontomunicipio#angularAcceleration-Dmension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### angular acceleration unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AngularAccelerationUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### angular displacement
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AngularDisplacement`
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
Sub-classes |[om:Aberration](http://opendata.caceres.es/def/ontomunicipio#Aberration) (c)<br />[om:AnnualAberration](http://opendata.caceres.es/def/ontomunicipio#AnnualAberration) (c)<br />[om:AberrationInLatitude](http://opendata.caceres.es/def/ontomunicipio#AberrationInLatitude) (c)<br />[om:SecularAberration](http://opendata.caceres.es/def/ontomunicipio#SecularAberration) (c)<br />[om:AberrationInLongitude](http://opendata.caceres.es/def/ontomunicipio#AberrationInLongitude) (c)<br />[om:DiurnalAberration](http://opendata.caceres.es/def/ontomunicipio#DiurnalAberration) (c)<br />
### impulsmoment
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AngularMomentum`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:actionOrAngularMomentum-Dimension](http://opendata.caceres.es/def/ontomunicipio#actionOrAngularMomentum-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### angular momentum unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AngularMomentumUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### angular size
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AngularSize`
Super-classes |[om:SolidAngle](http://opendata.caceres.es/def/ontomunicipio#SolidAngle) (c)<br />
### angular speed
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AngularSpeed`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:angularSpeed-Dimension](http://opendata.caceres.es/def/ontomunicipio#angularSpeed-Dimension) (c)<br />
Sub-classes |[om:AngularVelocity](http://opendata.caceres.es/def/ontomunicipio#AngularVelocity) (c)<br />
### angular speed unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AngularSpeedUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### angular velocity
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AngularVelocity`
Super-classes |[om:AngularSpeed](http://opendata.caceres.es/def/ontomunicipio#AngularSpeed) (c)<br />
### annual aberration
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AnnualAberration`
Description | <p>The component of the stellar abberation resulting from the motion of the Earth about the Sun. The abberation is the apparent angular displacement of the observed position of a celestial object from its geometric position, caused by the finite velocity of light in combination with the motions of the observer and of the observed object.</p>
Super-classes |[om:AngularDisplacement](http://opendata.caceres.es/def/ontomunicipio#AngularDisplacement) (c)<br />
### apparent diameter
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ApparentDiameter`
Description | <p>The angle that the actual diameter of an object makes in the sky; also known as angular size. Most often small, so units are mostly arcminutes, arcseconds, or even milli- or microarcseconds.</p>
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
### apparent distance modulus
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ApparentDistanceModulus`
Super-classes |[om:DistanceModulus](http://opendata.caceres.es/def/ontomunicipio#DistanceModulus) (c)<br />
### apparent magnitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ApparentMagnitude`
Description | <p>Logarithmic measure of the apparent brightness of an object. Units usually not indicated(http://en.wikipedia.org/wiki/Magnitude_(astronomy).</p>
Super-classes |[om:Magnitude](http://opendata.caceres.es/def/ontomunicipio#Magnitude) (c)<br />
### application area
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ApplicationArea`
Description | <p>An application area groups quantities and units of measure for application areas such as scientific disciplines (e.g., thermodynamics, mechanics).</p>
In domain of |[om:usesQuantity](http://opendata.caceres.es/def/ontomunicipio#usesQuantity) (op)<br />[om:usesUnit](http://opendata.caceres.es/def/ontomunicipio#usesUnit) (op)<br />
### oppervlakte
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Area`
Description | <p>Area expresses the two-dimensional size of a defined part of a surface, typically a region bounded by a closed curve. It is a derived quantity in the International System of Units. Area is length squared.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:area-Dimension](http://opendata.caceres.es/def/ontomunicipio#area-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### area density
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AreaDensity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### area density rate
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AreaDensityRate`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### area density rate unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AreaDensityRateUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### area density unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AreaDensityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### area fraction
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AreaFraction`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
Sub-classes |[om:ColorAreaFraction](http://opendata.caceres.es/def/ontomunicipio#ColorAreaFraction) (c)<br />[om:Coverage](http://opendata.caceres.es/def/ontomunicipio#Coverage) (c)<br />[om:StemEndRotAreaFraction](http://opendata.caceres.es/def/ontomunicipio#StemEndRotAreaFraction) (c)<br />
### area fraction unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AreaFractionUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### area unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AreaUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### atomic mass
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#AtomicMass`
Super-classes |[om:Mass](http://opendata.caceres.es/def/ontomunicipio#Mass) (c)<br />
### azimut
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Azimuth`
Description | <p>The angular distance measured clockwise along the horizon from a specified reference point (usually north) to the intersection with the great circle drawn from the zenith through a body on the celestial sphere.</p>
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
### B magnitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#BMagnitude`
Description | <p>Johnson B magnitude. The Johnson B band is a standard filter in the blue area. The central wavelength is 440nm and the bandwidth is 100nm.  The filter to be used is the Corning 5030 filter plus the Schott GG13 filter.</p>
Super-classes |[om:JohnsonMagnitude](http://opendata.caceres.es/def/ontomunicipio#JohnsonMagnitude) (c)<br />
Sub-classes |[om:BMagnitudeAtMaximumBrightness](http://opendata.caceres.es/def/ontomunicipio#BMagnitudeAtMaximumBrightness) (c)<br />[om:BMagnitudeAtMinimumBrightness](http://opendata.caceres.es/def/ontomunicipio#BMagnitudeAtMinimumBrightness) (c)<br />
### B magnitude at maximum brightness
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#BMagnitudeAtMaximumBrightness`
Description | <p>Johnson B magnitude at maximum brightness (i.e. for a variable star). The Johnson B band is a standard filter in the blue area. The central wavelength is 440nm and the bandwidth is 100nm.  The filter to be used is the Corning 5030 filter plus the Schott GG13 filter.</p>
Super-classes |[om:MagnitudeAtMaximumBrightness](http://opendata.caceres.es/def/ontomunicipio#MagnitudeAtMaximumBrightness) (c)<br />[om:BMagnitude](http://opendata.caceres.es/def/ontomunicipio#BMagnitude) (c)<br />
### B magnitude at minimum brightness
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#BMagnitudeAtMinimumBrightness`
Description | <p>Johnson B magnitude at minimum brightness (i.e. for a variable star). The Johnson B band is a standard filter in the blue area. The central wavelength is 440nm and the bandwidth is 100nm.  The filter to be used is the Corning 5030 filter plus the Schott GG13 filter.</p>
Super-classes |[om:MagnitudeAtMinimumBrightness](http://opendata.caceres.es/def/ontomunicipio#MagnitudeAtMinimumBrightness) (c)<br />[om:BMagnitude](http://opendata.caceres.es/def/ontomunicipio#BMagnitude) (c)<br />
### β_narrow magnitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#BetaNarrowMagnitude`
Description | <p>β_narrow  Magnitude in the Strömgren-Crawford photometric system with a peak wavelength at 485.8 nm and a peak-half-width of 2.9 nm.</p>
Super-classes |[om:StroemgrenMagnitude](http://opendata.caceres.es/def/ontomunicipio#StroemgrenMagnitude) (c)<br />
### β_wide magnitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#BetaWideMagnitude`
Description | <p>β_wide  Magnitude in the Strömgren-Crawford photometric system with a peak wavelength at 485 nm and a peak-half-width of 12.9 nm.</p>
Super-classes |[om:StroemgrenMagnitude](http://opendata.caceres.es/def/ontomunicipio#StroemgrenMagnitude) (c)<br />
### binary prefix
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#BinaryPrefix`
Description | <p>IEC prefix</p>
Super-classes |[om:Prefix](http://opendata.caceres.es/def/ontomunicipio#Prefix) (c)<br />
### body label mass
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#BodyLabelMass`
Super-classes |[om:LabelMass](http://opendata.caceres.es/def/ontomunicipio#LabelMass) (c)<br />
### body mass
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#BodyMass`
Super-classes |[om:Mass](http://opendata.caceres.es/def/ontomunicipio#Mass) (c)<br />
### bolometric correction
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#BolometricCorrection`
Description | <p>The visual magnitude of an object minus its bolometric magnitude.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### bolometric magnitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#BolometricMagnitude`
Description | <p>The magnitude of a star measured across all wavelengths, so that it takes into account the total amount of energy radiated. If a star is a strong infrared or ultraviolet emitter, its bolometric magnitude  will differ greatly from its visual magnitude.</p>
Super-classes |[om:Magnitude](http://opendata.caceres.es/def/ontomunicipio#Magnitude) (c)<br />
Sub-classes |[om:AbsoluteBolometricMagnitude](http://opendata.caceres.es/def/ontomunicipio#AbsoluteBolometricMagnitude) (c)<br />
### bond albedo
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#BondAlbedo`
Description | <p>Is the fraction of the total incident solar radiation - the radiation at all wavelengths - that is reflected or scattered by an object in all directions.</p>
Super-classes |[om:Albedo](http://opendata.caceres.es/def/ontomunicipio#Albedo) (c)<br />
### breadth
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Breadth`
Super-classes |[om:Length](http://opendata.caceres.es/def/ontomunicipio#Length) (c)<br />
### brightness temperature
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#BrightnessTemperature`
Description | <p>The temperature that a blackbody would need to have in order to emit radiation of the observed intensity at a given wavelength (mostly used in radio astronomy).</p>
Super-classes |[om:ThermodynamicTemperature](http://opendata.caceres.es/def/ontomunicipio#ThermodynamicTemperature) (c)<br />
### knopstadium
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#BudStadium`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Sub-classes |[om:BudStadiumDay4](http://opendata.caceres.es/def/ontomunicipio#BudStadiumDay4) (c)<br />[om:BudStadiumDay7](http://opendata.caceres.es/def/ontomunicipio#BudStadiumDay7) (c)<br />[om:BudStadiumDay0](http://opendata.caceres.es/def/ontomunicipio#BudStadiumDay0) (c)<br />
### bud stadium day 0
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#BudStadiumDay0`
Description | <p>Knopstadium vaasdag 0 (start vaasleven) (code).</p>
Super-classes |[om:BudStadium](http://opendata.caceres.es/def/ontomunicipio#BudStadium) (c)<br />
### knopstadium dag 4
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#BudStadiumDay4`
Description | <p>Knopstadium vaasdag 4 (code).</p>
Super-classes |[om:BudStadium](http://opendata.caceres.es/def/ontomunicipio#BudStadium) (c)<br />
### knopstadium dag 7
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#BudStadiumDay7`
Description | <p>Knopstadium vaasdag 7 (code).</p>
Super-classes |[om:BudStadium](http://opendata.caceres.es/def/ontomunicipio#BudStadium) (c)<br />
### compressiemodulus
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#BulkModulus`
Description | <p>Bulk modulus is a substance's resistance to uniform compression.</p>
Super-classes |[om:DynamicModulus](http://opendata.caceres.es/def/ontomunicipio#DynamicModulus) (c)<br />
### cap mass
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CapMass`
Super-classes |[om:Mass](http://opendata.caceres.es/def/ontomunicipio#Mass) (c)<br />
### capaciteit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Capacitance`
Description | <p>Capacitance is the ability to hold electrical charge. It is a derived quantity in the International System of Units. Capacitance is electric charge divided by electric potential.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:capacitance-Dimension](http://opendata.caceres.es/def/ontomunicipio#capacitance-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### capacitance unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CapacitanceUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### carton mass
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CartonMass`
Super-classes |[om:Mass](http://opendata.caceres.es/def/ontomunicipio#Mass) (c)<br />
### catalytic activity
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CatalyticActivity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:catalyticActivity-Dimension](http://opendata.caceres.es/def/ontomunicipio#catalyticActivity-Dimension) (c)<br />
### catalytic activity concentration
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CatalyticActivityConcentration`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:catalyticActivityConcentration-Dimension](http://opendata.caceres.es/def/ontomunicipio#catalyticActivityConcentration-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### catalytic activity concentration unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CatalyticActivityConcentrationUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### catalytic activity unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CatalyticActivityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### oorzaak einde vaasleven knopval
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeAbscisedBuds`
Description | <p>Oorzaak einde vaasleven knopval (1/0).</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### oorzaak einde vaasleven bloemval
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeAbscisedFlowers`
Description | <p>Oorzaak einde vaasleven bloemval (1/0).</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### cause end of vase life abscised leaves
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeAbscisedLeaves`
Description | <p>Oorzaak einde vaasleven bladval (1/0).</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### cause end of vase life blue flowers
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeBlueFlowers`
Description | <p>Oorzaak einde vaasleven blauwe bloemen (1/0).</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### cause end of vase life Botrytis
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeBotrytis`
Description | <p>Oorzaak einde vaasleven Botrytis (b3 of b4) (1/0).</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### oorzaak einde vaasleven knopverdroging
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeDryBuds`
Description | <p>Oorzaak einde vaasleven knopverdroging (1/0).</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### cause end of vase life dry flowers
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeDryFlowers`
Description | <p>Oorzaak einde vaasleven bloemverdroging (1/0).</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### oorzaak einde vaasleven bladverdroging
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeDryLeaves`
Description | <p>Oorzaak einde vaasleven bladverdroging (1/0).</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### cause end of vase life malformed buds
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeMalformedBuds`
Description | <p>Oorzaak einde vaasleven misvormde knoppen (1/0).</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### oorzaak einde vaasleven misvormde bloemen
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeMalformedFlowers`
Description | <p>Oorzaak einde vaasleven misvormde bloemen (1/0).</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### cause end of vase life nonturgid flowers
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeNonturgidFlowers`
Description | <p>Oorzaak einde vaasleven slappe bloemen (1/0).</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### cause end of vase life nonturgid leaves
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeNonturgidLeaves`
Description | <p>Oorzaak einde vaasleven slappe bladeren (1/0).</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### oorzaak einde vaasleven bloemrot
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeRottenFlowers`
Description | <p>Oorzaak einde vaasleven bloemrot (1/0).</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### oorzaak einde vaasleven rotte bladeren
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeRottenLeaves`
Description | <p>Oorzaak einde vaasleven rotte bladeren (1/0).</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### oorzaak einde vaasleven bloemverwelking
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeWiltedFlowers`
Description | <p>Oorzaak einde vaasleven bloemverwelking (1/0).</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### oorzaak einde vaasleven bladverwelking
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeWiltedLeaves`
Description | <p>Oorzaak einde vaasleven bladverwelking (1/0).</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### oorzaak einde vaasleven bladvergeling
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeYellowLeaves`
Description | <p>Oorzaak einde vaasleven bladvergeling (1/0).</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### Celsius temperature
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CelsiusTemperature`
Super-classes |[om:Temperature](http://opendata.caceres.es/def/ontomunicipio#Temperature) (c)<br />
Restrictions |[om:hasScale](http://opendata.caceres.es/def/ontomunicipio#hasScale) (op) **value** [om:CelsiusScale](http://opendata.caceres.es/def/ontomunicipio#CelsiusScale) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### Celsius temperature scale
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CelsiusTemperatureScale`
Super-classes |[om:Scale](http://opendata.caceres.es/def/ontomunicipio#Scale) (c)<br />
### Celsius temperature unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CelsiusTemperatureUnit`
Super-classes |[om:TemperatureUnit](http://opendata.caceres.es/def/ontomunicipio#TemperatureUnit) (c)<br />
### 圆周
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Circumference`
Super-classes |[om:Length](http://opendata.caceres.es/def/ontomunicipio#Length) (c)<br />
### co-rotation radius
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Co-RotationRadius`
Description | <p>The radius (distance from the galaxy's centre) at which the stars move at the same speed as the spiral pattern or bar in a galaxy.</p>
Super-classes |[om:Radius](http://opendata.caceres.es/def/ontomunicipio#Radius) (c)<br />
### cold gas mass fraction
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ColdGasMassFraction`
Description | <p>The fraction of the mass of a galaxy that is in the form of cold gas ~10s K.</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### collision frequency
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CollisionFrequency`
Description | <p>Collision frequency is the average number of collisions between reacting molecules per unit time.</p>
Super-classes |[om:Frequency](http://opendata.caceres.es/def/ontomunicipio#Frequency) (c)<br />
### color area fraction
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ColorAreaFraction`
Description | <p>Voorbeeld avocado Hass: percentage oppervlak donker.</p>
Super-classes |[om:AreaFraction](http://opendata.caceres.es/def/ontomunicipio#AreaFraction) (c)<br />
### kleurindex
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ColourIndex`
Description | <p>The difference between the apparent magnitude of a star at two different wavelengths (always the shorter-wavelength magnitude minus the longer-wavelength magnitude) to give a quantification of the star's colour. The magnitude of an object at different wavelengths are measured by using different filters before the detector. Often the Johnson system with UBV passbands are used. Other passbands may also be used (for instance g-r).</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Sub-classes |[om:IntrinsicColourIndex](http://opendata.caceres.es/def/ontomunicipio#IntrinsicColourIndex) (c)<br />
### colour temperature
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ColourTemperature`
Description | <p>The temperature of a blackbody that has the same colour index as a given star.</p>
Super-classes |[om:ThermodynamicTemperature](http://opendata.caceres.es/def/ontomunicipio#ThermodynamicTemperature) (c)<br />
### column number density
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ColumnNumberDensity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:columnNumberDensity-Dimension](http://opendata.caceres.es/def/ontomunicipio#columnNumberDensity-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### column number density unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ColumnNumberDensityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### compound unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CompoundUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
Sub-classes |[om:UnitExponentiation](http://opendata.caceres.es/def/ontomunicipio#UnitExponentiation) (c)<br />[om:UnitMultiplication](http://opendata.caceres.es/def/ontomunicipio#UnitMultiplication) (c)<br />[om:UnitDivision](http://opendata.caceres.es/def/ontomunicipio#UnitDivision) (c)<br />
### compressive stress
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CompressiveStress`
Description | <p>Compressive stress is a stress that, when applied, acts towards the center of a material.</p>
Super-classes |[om:Stress](http://opendata.caceres.es/def/ontomunicipio#Stress) (c)<br />
### contact angle
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ContactAngle`
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
### cosmological constant
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CosmologicalConstant`
Description | <p>The cosmological constant.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### cost
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Cost`
Super-classes |[om:AmountOfMoney](http://opendata.caceres.es/def/ontomunicipio#AmountOfMoney) (c)<br />
### Cousins magnitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CousinsMagnitude`
Description | <p>A magnitude measured in one of Cousins standard passbands (using a standard filter, i.e. I or R).</p>
Super-classes |[om:Magnitude](http://opendata.caceres.es/def/ontomunicipio#Magnitude) (c)<br />
Sub-classes |[om:IMagnitude](http://opendata.caceres.es/def/ontomunicipio#IMagnitude) (c)<br />[om:RMagnitude](http://opendata.caceres.es/def/ontomunicipio#RMagnitude) (c)<br />
### coverage
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Coverage`
Super-classes |[om:AreaFraction](http://opendata.caceres.es/def/ontomunicipio#AreaFraction) (c)<br />
### Cowling number
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CowlingNumber`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
### Cowling number unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CowlingNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### critical density
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CriticalDensity`
Description | <p>The density needed for a closed universe.</p>
Super-classes |[om:Density](http://opendata.caceres.es/def/ontomunicipio#Density) (c)<br />
### cubic prefixed metre
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CubicPrefixedMetre`
Super-classes |[om:UnitExponentiation](http://opendata.caceres.es/def/ontomunicipio#UnitExponentiation) (c)<br />
### current density
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CurrentDensity`
Description | <p>Current density is the density of flow of a conserved charge. It is a derived quantity in the International System of Units. Current density is electric current divided by area.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:currentDensity-Dimension](http://opendata.caceres.es/def/ontomunicipio#currentDensity-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### current density unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CurrentDensityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### curvature constant
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CurvatureConstant`
Description | <p>The curvature constant k=-1, 0, or 1.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### curvature constant unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#CurvatureConstantUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### cut-off wavelength
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Cut-OffWavelength`
Description | <p>Either: wavelengths at which the detectivity (D) falls to 0, or the wavelengths at which the detectivity falls to 1% of the peak value, or the wavelengths at which the normalised detectivity (D*) has fallen to half its peak value.</p>
Super-classes |[om:Wavelength](http://opendata.caceres.es/def/ontomunicipio#Wavelength) (c)<br />
### dark noise
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#DarkNoise`
Description | <p>Output from a detector when unilluminated - usually as RMS voltage or current (Kitchin, Astrophysical Techniques, IoP, Table 1.1.2).</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### datum
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Date`
Super-classes |[om:Time](http://opendata.caceres.es/def/ontomunicipio#Time) (c)<br />
Sub-classes |[om:Epoch](http://opendata.caceres.es/def/ontomunicipio#Epoch) (c)<br />
### deceleration parameter
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#DecelerationParameter`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### deceleration parameter unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#DecelerationParameterUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### declinatie
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Declination`
Description | <p>The angular distance on the celestial sphere north or south of the celestial equator. It is measured along the hour circle passing through the celestial object. Declination is usually given in combination with right ascension or hour angle.</p>
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
### 密度
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Density`
Description | <p>Density is the concentration of matter. It is a derived quantity in the International System of Units. Density is mass divided by volume.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:density-Dimension](http://opendata.caceres.es/def/ontomunicipio#density-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:CriticalDensity](http://opendata.caceres.es/def/ontomunicipio#CriticalDensity) (c)<br />
### density parameter
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#DensityParameter`
Description | <p>Ratio of the average density and the critical density.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
Sub-classes |[om:DensityParameterForMatter](http://opendata.caceres.es/def/ontomunicipio#DensityParameterForMatter) (c)<br />[om:DensityParameterForRadiation](http://opendata.caceres.es/def/ontomunicipio#DensityParameterForRadiation) (c)<br />[om:DensityParameterForVacuum](http://opendata.caceres.es/def/ontomunicipio#DensityParameterForVacuum) (c)<br />[om:DensityParameterForBaryonicMatter](http://opendata.caceres.es/def/ontomunicipio#DensityParameterForBaryonicMatter) (c)<br />[om:TotalDensityParameter](http://opendata.caceres.es/def/ontomunicipio#TotalDensityParameter) (c)<br />
### density parameter for baryonic matter
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#DensityParameterForBaryonicMatter`
Description | <p>The density parameter for baryonic (oridnary) matter.</p>
Super-classes |[om:DensityParameter](http://opendata.caceres.es/def/ontomunicipio#DensityParameter) (c)<br />
### density parameter for matter
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#DensityParameterForMatter`
Description | <p>The density parameter for matter (either baryonic or dark).</p>
Super-classes |[om:DensityParameter](http://opendata.caceres.es/def/ontomunicipio#DensityParameter) (c)<br />
### density parameter for radiation
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#DensityParameterForRadiation`
Description | <p>The density parameter for radiation.</p>
Super-classes |[om:DensityParameter](http://opendata.caceres.es/def/ontomunicipio#DensityParameter) (c)<br />
### density parameter for vacuum
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#DensityParameterForVacuum`
Description | <p>The density parameter for vacuum.</p>
Super-classes |[om:DensityParameter](http://opendata.caceres.es/def/ontomunicipio#DensityParameter) (c)<br />
### density parameter unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#DensityParameterUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### density unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#DensityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### diepte
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Depth`
Super-classes |[om:Length](http://opendata.caceres.es/def/ontomunicipio#Length) (c)<br />
### detective quantum efficiency
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#DetectiveQuantumEfficiency`
Description | <p>Square of ratio between the output signal noise ratio and the input signal noise ratio.</p>
Super-classes |[om:QuantumEfficiency](http://opendata.caceres.es/def/ontomunicipio#QuantumEfficiency) (c)<br />
### detectivity
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Detectivity`
Description | <p>Reciprocal of Noise equivalent power. The signal-to-noise ratio for incident radiation of unit intensity.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### detectivity unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#DetectivityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### 直径
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Diameter`
Super-classes |[om:Length](http://opendata.caceres.es/def/ontomunicipio#Length) (c)<br />
### diameter (hoek)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Diameter-Angle`
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
### dimension
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Dimension`
Description | <p>Dimensions are abstract properties of units and quantities neglecting their vectorial or tensorial character and all numerical factors including their sign.</p>
In domain of |[om:hasSIThermodynamicTemperatureDimensionExponent](http://opendata.caceres.es/def/ontomunicipio#hasSIThermodynamicTemperatureDimensionExponent) (dp)<br />[om:hasSIAmountOfSubstanceDimensionExponent](http://opendata.caceres.es/def/ontomunicipio#hasSIAmountOfSubstanceDimensionExponent) (dp)<br />[om:hasSITimeDimensionExponent](http://opendata.caceres.es/def/ontomunicipio#hasSITimeDimensionExponent) (dp)<br />[om:hasSILuminousIntensityDimensionExponent](http://opendata.caceres.es/def/ontomunicipio#hasSILuminousIntensityDimensionExponent) (dp)<br />[om:hasSILengthDimensionExponent](http://opendata.caceres.es/def/ontomunicipio#hasSILengthDimensionExponent) (dp)<br />[om:hasSIMassDimensionExponent](http://opendata.caceres.es/def/ontomunicipio#hasSIMassDimensionExponent) (dp)<br />[om:hasSIElectricCurrentDimensionExponent](http://opendata.caceres.es/def/ontomunicipio#hasSIElectricCurrentDimensionExponent) (dp)<br />
In range of |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op)<br />
### directional dose equivalent
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#DirectionalDoseEquivalent`
Super-classes |[om:DoseEquivalent](http://opendata.caceres.es/def/ontomunicipio#DoseEquivalent) (c)<br />
### disodium ethylene diamine tetra acetate mass fraction
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#DisodiumEthyleneDiamineTetreAcetateMassFraction`
Description | <p>The fraction of the mass of disodium ethylene diamine tetra acetate in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### displacement
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Displacement`
Super-classes |[om:Length](http://opendata.caceres.es/def/ontomunicipio#Length) (c)<br />
### distance
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Distance`
Super-classes |[om:Length](http://opendata.caceres.es/def/ontomunicipio#Length) (c)<br />
Sub-classes |[om:TotalDistanceTravelled](http://opendata.caceres.es/def/ontomunicipio#TotalDistanceTravelled) (c)<br />[om:xyDistanceTravelled](http://opendata.caceres.es/def/ontomunicipio#xyDistanceTravelled) (c)<br />[om:xy2DStartEndDistance](http://opendata.caceres.es/def/ontomunicipio#xy2DStartEndDistance) (c)<br />[om:DistanceModulus](http://opendata.caceres.es/def/ontomunicipio#DistanceModulus) (c)<br />[om:Total3DStartEndDistance](http://opendata.caceres.es/def/ontomunicipio#Total3DStartEndDistance) (c)<br />
### distance modulus
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#DistanceModulus`
Description | <p>The difference between the apparent magnitude (m) of an astronomical object, such as a star, and its absolute magnitude (M), used as a distance measurement. Distances can be expressed in distance modulii as $$m-M = 5\log d + 10 = 10-5 log \varpi$$ where (d) is the distance in kiloparsec and (\varpi) is the parallax in milliarcseconds.</p>
Super-classes |[om:Distance](http://opendata.caceres.es/def/ontomunicipio#Distance) (c)<br />
Sub-classes |[om:ApparentDistanceModulus](http://opendata.caceres.es/def/ontomunicipio#ApparentDistanceModulus) (c)<br />[om:TrueDistanceModulus](http://opendata.caceres.es/def/ontomunicipio#TrueDistanceModulus) (c)<br />
### diurnal aberration
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#DiurnalAberration`
Description | <p>The component of the stellar abberation resulting from the diurnal motion of the observer around the centre of the Earth. The abberation is the apparent angular displacement of the observed position of a celestial object from its geometric position, caused by the finite velocity of light in combination with the motions of the observer and of the observed object.</p>
Super-classes |[om:AngularDisplacement](http://opendata.caceres.es/def/ontomunicipio#AngularDisplacement) (c)<br />
### dose equivalent
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#DoseEquivalent`
Description | <p>Dose equivalent is a measure of the radiation dose to tissue where an attempt has been made to allow for the different relative biological effects of different types of ionizing radiation.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:specificEnergyOrAbsorbedDoseOrDoseEquivalent-Dimension](http://opendata.caceres.es/def/ontomunicipio#specificEnergyOrAbsorbedDoseOrDoseEquivalent-Dimension) (c)<br />
Sub-classes |[om:PersonalDoseEquivalent](http://opendata.caceres.es/def/ontomunicipio#PersonalDoseEquivalent) (c)<br />[om:AmbientDoseEquivalent](http://opendata.caceres.es/def/ontomunicipio#AmbientDoseEquivalent) (c)<br />[om:DirectionalDoseEquivalent](http://opendata.caceres.es/def/ontomunicipio#DirectionalDoseEquivalent) (c)<br />[om:OrganDoseEquivalent](http://opendata.caceres.es/def/ontomunicipio#OrganDoseEquivalent) (c)<br />
### dose equivalent unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#DoseEquivalentUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### drainage speed
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#DrainageSpeed`
Super-classes |[om:Speed](http://opendata.caceres.es/def/ontomunicipio#Speed) (c)<br />
### dry body mass
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#DryBodyMass`
Super-classes |[om:DryMass](http://opendata.caceres.es/def/ontomunicipio#DryMass) (c)<br />
### dry mass
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#DryMass`
Super-classes |[om:Mass](http://opendata.caceres.es/def/ontomunicipio#Mass) (c)<br />
Sub-classes |[om:DryBodyMass](http://opendata.caceres.es/def/ontomunicipio#DryBodyMass) (c)<br />
### dry matter mass fraction
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#DryMatterMassFraction`
Description | <p>The fraction of the mass of dry matter in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### duur
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Duration`
Super-classes |[om:Time](http://opendata.caceres.es/def/ontomunicipio#Time) (c)<br />
### dynamic modulus
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#DynamicModulus`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:pressure-Dimension](http://opendata.caceres.es/def/ontomunicipio#pressure-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:ShearModulus](http://opendata.caceres.es/def/ontomunicipio#ShearModulus) (c)<br />[om:ModulusOfElasticity](http://opendata.caceres.es/def/ontomunicipio#ModulusOfElasticity) (c)<br />[om:LossModulus](http://opendata.caceres.es/def/ontomunicipio#LossModulus) (c)<br />[om:ElasticityTensor](http://opendata.caceres.es/def/ontomunicipio#ElasticityTensor) (c)<br />[om:BulkModulus](http://opendata.caceres.es/def/ontomunicipio#BulkModulus) (c)<br />[om:StorageModulus](http://opendata.caceres.es/def/ontomunicipio#StorageModulus) (c)<br />
### dynamic range
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#DynamicRange`
Description | <p>Ratio between the saturation output and the dark signal, sometimes only over the region of linearity.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
### dynamic range unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#DynamicRangeUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### dynamische viscositeit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#DynamicViscosity`
Description | <p>Viscosity is the definite resistance to change of form of many materials.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dynamicViscosity-Dimension](http://opendata.caceres.es/def/ontomunicipio#dynamicViscosity-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### dynamic viscosity unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#DynamicViscosityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### eccentriciteit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Eccentricity`
Description | <p>A measure of the deviation from a circle for an orbit.</p>
Super-classes |[om:QuantityOfDimensionOne](http://opendata.caceres.es/def/ontomunicipio#QuantityOfDimensionOne) (c)<br />
### ecliptic latitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#EclipticLatitude`
Description | <p>The angular distance on the celestial sphere north or south of the ecliptic (the path of the Sun on the celestial sphere during one year). It is measured along the great circle passing through the object and the ecliptic poles and perpendicular to the ecliptic.</p>
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
### ecliptic longitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#EclipticLongitude`
Description | <p>The angular distance on the celestial sphere measured clockwise from the vernal equinox along the ecliptic (the path of the Sun on the celestial sphere during one year) to the intersection with the great circle drawn from the ecliptical north pole through the object.</p>
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
### egg mass fraction
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#EggMassFraction`
Description | <p>The fraction of the mass of egg in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### elasticity tensor
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ElasticityTensor`
Super-classes |[om:DynamicModulus](http://opendata.caceres.es/def/ontomunicipio#DynamicModulus) (c)<br />
### electric charge
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ElectricCharge`
Description | <p>Electric charge is a conserved property of some subatomic particles, which determines their electromagnetic interaction. It is a derived quantity in the International System of Units. Electric charge is electric current times time.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:electricCharge-Dimension](http://opendata.caceres.es/def/ontomunicipio#electricCharge-Dimension) (c)<br />
### electric charge density
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ElectricChargeDensity`
Description | <p>Electric charge density is the amount of electric charge in a volume. It is a derived quantity in the International System of Units. Electric charge density is electric charge divided by volume.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:electricChargeDensity-Dimension](http://opendata.caceres.es/def/ontomunicipio#electricChargeDensity-Dimension) (c)<br />
### electric charge density unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ElectricChargeDensityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### electric charge unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ElectricChargeUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### electric current
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ElectricCurrent`
Description | <p>Electric current is the flow of electric charge. It is a base quantity in the International System of Units. Electric current is electric charge divided by time.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:electricCurrent-Dimension](http://opendata.caceres.es/def/ontomunicipio#electricCurrent-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### electric current unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ElectricCurrentUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### electric dipole moment
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ElectricDipoleMoment`
Description | <p>Electric dipole moment is a measure of the polarity of a system of electric charges.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:electricDipoleMoment-Dimension](http://opendata.caceres.es/def/ontomunicipio#electricDipoleMoment-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### electric dipole moment unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ElectricDipoleMomentUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### electric field
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ElectricField`
Description | <p>Electric field is a property of the space surrounding an electric charge or in the presence of a time-varying magnetic field which exerts a forceon other electrically charged objects.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:electricField-Dimension](http://opendata.caceres.es/def/ontomunicipio#electricField-Dimension) (c)<br />
### electric field unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ElectricFieldUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### electric flux density
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ElectricFluxDensity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:electricFluxDensity-Dimension](http://opendata.caceres.es/def/ontomunicipio#electricFluxDensity-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### electric flux density unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ElectricFluxDensityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### electric potential
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ElectricPotential`
Description | <p>Electric potential is the potential energy per unit charge associated with static (time-invariant) electric field.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:electricPotential-Dimension](http://opendata.caceres.es/def/ontomunicipio#electricPotential-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:PotentialDifference](http://opendata.caceres.es/def/ontomunicipio#PotentialDifference) (c)<br />[om:ElectromotiveForce](http://opendata.caceres.es/def/ontomunicipio#ElectromotiveForce) (c)<br />
### electric potential unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ElectricPotentialUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### electrical conductance
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ElectricalConductance`
Description | <p>Electrical conductance is a measure of how easily electricity flows along a certain path through an electrical element.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:electricalConductance-Dimension](http://opendata.caceres.es/def/ontomunicipio#electricalConductance-Dimension) (c)<br />
### electrical conductance unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ElectricalConductanceUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### electrical conductivity
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ElectricalConductivity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:electricalConductivity-Dimension](http://opendata.caceres.es/def/ontomunicipio#electricalConductivity-Dimension) (c)<br />
### electrical conductivity unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ElectricalConductivityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### electrical resistance
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ElectricalResistance`
Description | <p>Electrical resistance is the degree to which an object opposes an electric current through it. It is a derived quantity in the International System of Units.  Electrical resistance is electric potential divided by electric current.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:electricalResistance-Dimension](http://opendata.caceres.es/def/ontomunicipio#electricalResistance-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### electrical resistance unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ElectricalResistanceUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### electrical resistivity
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ElectricalResistivity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:electricalResistivity-Dimension](http://opendata.caceres.es/def/ontomunicipio#electricalResistivity-Dimension) (c)<br />
### electrical resistivity unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ElectricalResistivityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### electromotive force
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ElectromotiveForce`
Description | <p>Electromotive force is that which causes a flow of current.</p>
Super-classes |[om:ElectricPotential](http://opendata.caceres.es/def/ontomunicipio#ElectricPotential) (c)<br />
### electron temperature
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ElectronTemperature`
Description | <p>The temperature determined by the mean kinetic energy of free electrons in a plasma; also known as kinetic temperature.</p>
Super-classes |[om:ThermodynamicTemperature](http://opendata.caceres.es/def/ontomunicipio#ThermodynamicTemperature) (c)<br />
### ellipticity
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Ellipticity`
Description | <p>A measure of the amount by which an object, such as a planet or a galaxy, deviates from a perfect sphere.</p>
Super-classes |[om:QuantityOfDimensionOne](http://opendata.caceres.es/def/ontomunicipio#QuantityOfDimensionOne) (c)<br />
### 能量
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Energy`
Description | <p>Energy can be defined as the ability to do work. It is a derived quantity in the International System of Units.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:energy-Dimension](http://opendata.caceres.es/def/ontomunicipio#energy-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:Work](http://opendata.caceres.es/def/ontomunicipio#Work) (c)<br />[om:Heat](http://opendata.caceres.es/def/ontomunicipio#Heat) (c)<br />[om:KineticEnergy](http://opendata.caceres.es/def/ontomunicipio#KineticEnergy) (c)<br />[om:InternalEnergy](http://opendata.caceres.es/def/ontomunicipio#InternalEnergy) (c)<br />[om:Enthalpy](http://opendata.caceres.es/def/ontomunicipio#Enthalpy) (c)<br />[om:RadiantEnergy](http://opendata.caceres.es/def/ontomunicipio#RadiantEnergy) (c)<br />[om:PotentialEnergy](http://opendata.caceres.es/def/ontomunicipio#PotentialEnergy) (c)<br />
### energy density
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#EnergyDensity`
Description | <p>Energy density is the amount of energy stored in a given system or region of space per unit volume.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:energyDensity-Dimension](http://opendata.caceres.es/def/ontomunicipio#energyDensity-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### energy density unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#EnergyDensityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### energy unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#EnergyUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### 焓
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Enthalpy`
Description | <p>Enthalpy is the sum of the internal energy of a system plus the product of the pressure-volume work done on the system.</p>
Super-classes |[om:Energy](http://opendata.caceres.es/def/ontomunicipio#Energy) (c)<br />
### 熵单位
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Entropy`
Description | <p>Entropy is a measure of the unavailability of a system’s energy to do work.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:entropyOrHeatCapacity-Dimension](http://opendata.caceres.es/def/ontomunicipio#entropyOrHeatCapacity-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### entropy unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#EntropyUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### epoch
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Epoch`
Super-classes |[om:Date](http://opendata.caceres.es/def/ontomunicipio#Date) (c)<br />
Sub-classes |[om:EpochAtMaximumBrightness](http://opendata.caceres.es/def/ontomunicipio#EpochAtMaximumBrightness) (c)<br />
### epoch at maximum brightness
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#EpochAtMaximumBrightness`
Description | <p>A moment when the object (i.e. a variable star) was at maximum brightness.</p>
Super-classes |[om:Epoch](http://opendata.caceres.es/def/ontomunicipio#Epoch) (c)<br />
### Euler number
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#EulerNumber`
Description | <p>The Euler number is a dimensionless number that expresses the relationship between a local pressure drop e.g. over a restriction and the kinetic energy per unit volume.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### Euler number unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#EulerNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### exposure
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Exposure`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:exposure-Dimension](http://opendata.caceres.es/def/ontomunicipio#exposure-Dimension) (c)<br />
### exposure to x and γ rays
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ExposureToXAndGammaRays`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:exposureToXAndGammaRays-Dimension](http://opendata.caceres.es/def/ontomunicipio#exposureToXAndGammaRays-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### exposure to x and γ rays unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ExposureToXAndGammaRaysUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### exposure unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ExposureUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### external browning
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ExternalBrowning`
Description | <p>Voorbeeld avocado Hass: poster (code).</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### extinctie
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Extinction`
Description | <p>Total extinction at a specific wavelength. The extinction is caused by dust and gas between a star and the observer. It is the difference between the observed magnitude and the magnitude the source would have had if no extinction had taken place.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Sub-classes |[om:ExtinctionAtWavelength](http://opendata.caceres.es/def/ontomunicipio#ExtinctionAtWavelength) (c)<br />[om:ExtinctionAtWaveband](http://opendata.caceres.es/def/ontomunicipio#ExtinctionAtWaveband) (c)<br />
### extinction at waveband
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ExtinctionAtWaveband`
Super-classes |[om:Extinction](http://opendata.caceres.es/def/ontomunicipio#Extinction) (c)<br />
Sub-classes |[om:ExtinctionInU](http://opendata.caceres.es/def/ontomunicipio#ExtinctionInU) (c)<br />[om:ExtinctionInB](http://opendata.caceres.es/def/ontomunicipio#ExtinctionInB) (c)<br />[om:ExtinctionInV](http://opendata.caceres.es/def/ontomunicipio#ExtinctionInV) (c)<br />
### extinction at wavelength
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ExtinctionAtWavelength`
Super-classes |[om:Extinction](http://opendata.caceres.es/def/ontomunicipio#Extinction) (c)<br />
### extinction in B
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ExtinctionInB`
Super-classes |[om:ExtinctionAtWaveband](http://opendata.caceres.es/def/ontomunicipio#ExtinctionAtWaveband) (c)<br />
### extinction in U
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ExtinctionInU`
Super-classes |[om:ExtinctionAtWaveband](http://opendata.caceres.es/def/ontomunicipio#ExtinctionAtWaveband) (c)<br />
### extinction in V
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ExtinctionInV`
Super-classes |[om:ExtinctionAtWaveband](http://opendata.caceres.es/def/ontomunicipio#ExtinctionAtWaveband) (c)<br />
### Fahrenheittemperatuur
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#FahrenheitTemperature`
Super-classes |[om:Temperature](http://opendata.caceres.es/def/ontomunicipio#Temperature) (c)<br />
Restrictions |[om:hasScale](http://opendata.caceres.es/def/ontomunicipio#hasScale) (op) **value** [om:FahrenheitScale](http://opendata.caceres.es/def/ontomunicipio#FahrenheitScale) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### Fahrenheit temperature scale
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#FahrenheitTemperatureScale`
Super-classes |[om:Scale](http://opendata.caceres.es/def/ontomunicipio#Scale) (c)<br />
### Fahrenheit temperature unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#FahrenheitTemperatureUnit`
Super-classes |[om:TemperatureUnit](http://opendata.caceres.es/def/ontomunicipio#TemperatureUnit) (c)<br />
### fat mass fraction
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#FatMassFraction`
Description | <p>The fraction of the mass of fat in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### stevigheid (penetrometer) (methode 1)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Firmness-Penetrometer-Method1`
Description | <p>Stevigheid gemeten met penetrometer methode 1.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### stevigheid (penetrometer) (methode 2)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Firmness-Penetrometer-Method2`
Description | <p>Stevigheid gemeten met penetrometer methode 2.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### first Cowling number
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#FirstCowlingNumber`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### first Cowling number unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#FirstCowlingNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### fixed point
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#FixedPoint`
Super-classes |[om:Point](http://opendata.caceres.es/def/ontomunicipio#Point) (c)<br />
Restrictions |[om:hasPoint](http://opendata.caceres.es/def/ontomunicipio#hasPoint) (op) **only** ([om:FixedPoint](http://opendata.caceres.es/def/ontomunicipio#FixedPoint) (c))<br />
Sub-classes |[om:FixedZeroPoint](http://opendata.caceres.es/def/ontomunicipio#FixedZeroPoint) (c)<br />
### fixed zero point
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#FixedZeroPoint`
Super-classes |[om:FixedPoint](http://opendata.caceres.es/def/ontomunicipio#FixedPoint) (c)<br />
### flowpack mass
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#FlowpackMass`
Super-classes |[om:Mass](http://opendata.caceres.es/def/ontomunicipio#Mass) (c)<br />
### fluidity
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Fluidity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:fluidity-Dimension](http://opendata.caceres.es/def/ontomunicipio#fluidity-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### fluidity unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#FluidityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### fontgrootte
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#FontSize`
Super-classes |[om:Length](http://opendata.caceres.es/def/ontomunicipio#Length) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### font size unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#FontSizeUnit`
Super-classes |[om:LengthUnit](http://opendata.caceres.es/def/ontomunicipio#LengthUnit) (c)<br />
### force
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Force`
Description | <p>Force is the extent to which an object with mass can be caused to accelerate. It is a derived quantity in the International System of Units. Force is mass times acceleration.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:force-Dimension](http://opendata.caceres.es/def/ontomunicipio#force-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:Friction](http://opendata.caceres.es/def/ontomunicipio#Friction) (c)<br />[om:Weight](http://opendata.caceres.es/def/ontomunicipio#Weight) (c)<br />[om:Thrust](http://opendata.caceres.es/def/ontomunicipio#Thrust) (c)<br />
### force unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ForceUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### getal van Fourier
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#FourierNumber`
Description | <p>The Fourier number is a dimensionless number that characterises heat conduction. It is the ratio of heat conduction rate to rate of thermal energy storage. The Fourier number is a dimensionless time.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
### Fourier number for mass transfer
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#FourierNumberForMassTransfer`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
### Fourier number for mass transfer unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#FourierNumberForMassTransferUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### Fourier number unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#FourierNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### frequentie
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Frequency`
Description | <p>Frequency is a measure of the number of occurrences of a repeating event per unit time.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:frequency-Dimension](http://opendata.caceres.es/def/ontomunicipio#frequency-Dimension) (c)<br />
Sub-classes |[om:CollisionFrequency](http://opendata.caceres.es/def/ontomunicipio#CollisionFrequency) (c)<br />
### frequency unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#FrequencyUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### friction
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Friction`
Description | <p>Friction is a force that resists the relative motion of solid surfaces, fluid layers, or material elements sliding against each other.</p>
Super-classes |[om:Force](http://opendata.caceres.es/def/ontomunicipio#Force) (c)<br />
### Froude number
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#FroudeNumber`
Description | <p>The Froude number is a dimensionless number that compares inertial and gravitational forces. It may be used to quantify the resistance of an object moving through water, and compare objects of different sizes.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### Froude number unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#FroudeNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### function
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Function`
In range of |[om:hasAggregateFunction](http://opendata.caceres.es/def/ontomunicipio#hasAggregateFunction) (op)<br />
### galactic cylindrical polar angle coordinate
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#GalacticCylindricalPolarAngleCoordinate`
Description | <p>The angle from the Galactic centre between the perpendicular projection of the Sun on the Galactic plane and the projection of the object. This is one of the three Galactic Cylindrical Polar Coordinates.</p>
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
### galactic latitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#GalacticLatitude`
Description | <p>The angular distance on the celestial sphere north or south of the galactic equator. It is measured along the great circle passing through the object and the galactic poles and perpendicular to the galactic equator.</p>
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
### galactic longitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#GalacticLongitude`
Description | <p>The angular distance on the celestial sphere measured clockwise from the galactic centre (as defined by the International Astronomical Union (IAU)) along the galactic equator to the intersection with the great circle drawn from the galactic north pole through the object.</p>
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
### gasconstante
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#GasConstant`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:molarEntropyOrMolarHeatCapacityOrGasConstant-Dimension](http://opendata.caceres.es/def/ontomunicipio#molarEntropyOrMolarHeatCapacityOrGasConstant-Dimension) (c)<br />
### gas constant unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#GasConstantUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### gelatin mass fraction
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#GelatinMassFraction`
Description | <p>The fraction of the mass of gelatin in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### geometrical albedo
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#GeometricalAlbedo`
Description | <p>Ratio between the brightness of an object as seen from the direction of a hypothetical white, diffusely reflecting sphere of the same size and at the same distance.</p>
Super-classes |[om:Albedo](http://opendata.caceres.es/def/ontomunicipio#Albedo) (c)<br />
### gram per prefixed litre
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#GramPerPrefixedLitre`
Super-classes |[om:UnitDivision](http://opendata.caceres.es/def/ontomunicipio#UnitDivision) (c)<br />
### getal van Grashof
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#GrashofNumber`
Description | <p>The Grashof number is a dimensionless number that approximates the ratio of buoyancy to viscous force that acts on a fluid.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
### Grashof number for mass transfer
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#GrashofNumberForMassTransfer`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
### Grashof number for mass transfer unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#GrashofNumberForMassTransferUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### Grashof number unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#GrashofNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### valversnelling
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#GravitationalAcceleration`
Super-classes |[om:Acceleration](http://opendata.caceres.es/def/ontomunicipio#Acceleration) (c)<br />
### guar gum mass fraction
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#GuarGumMassFraction`
Description | <p>The fraction of the mass of guar gum in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### half-life
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Half-Life`
Super-classes |[om:Time](http://opendata.caceres.es/def/ontomunicipio#Time) (c)<br />
### getal van Hartmann
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#HartmannNumber`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
### Hartmann number unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#HartmannNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### warmte
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Heat`
Description | <p>Heat is any flow of energy from one body or system to another due to a difference in temperature.</p>
Super-classes |[om:Energy](http://opendata.caceres.es/def/ontomunicipio#Energy) (c)<br />
### heat capacity
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#HeatCapacity`
Description | <p>Heat capacity is the heat required to increase the temperature of a system or substance one unit temperature.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:entropyOrHeatCapacity-Dimension](http://opendata.caceres.es/def/ontomunicipio#entropyOrHeatCapacity-Dimension) (c)<br />
### heat capacity unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#HeatCapacityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### heat flow rate
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#HeatFlowRate`
Super-classes |[om:Power](http://opendata.caceres.es/def/ontomunicipio#Power) (c)<br />
### heat flux density
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#HeatFluxDensity`
Super-classes |[om:PowerDensity](http://opendata.caceres.es/def/ontomunicipio#PowerDensity) (c)<br />
### heat transfer coefficient
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#HeatTransferCoefficient`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:heatTransferCoefficient-Dimension](http://opendata.caceres.es/def/ontomunicipio#heatTransferCoefficient-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### heat transfer coefficient unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#HeatTransferCoefficientUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### height
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Height`
Super-classes |[om:Length](http://opendata.caceres.es/def/ontomunicipio#Length) (c)<br />
### hour angle
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#HourAngle`
Description | <p>The angular distance on the celestial sphere measured westward along the celestial equator from the meridian to the hour circle that passes through the celestial object.</p>
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
### constante van Hubble
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#HubbleConstant`
Description | <p>The Hubble constant (NOT a constant over time).</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:HubbleConstantAtPresentEpoch](http://opendata.caceres.es/def/ontomunicipio#HubbleConstantAtPresentEpoch) (c)<br />
### constante van Hubble tijdens het huidige epoch
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#HubbleConstantAtPresentEpoch`
Description | <p>The Hubble constant at the present epoch (a constant).</p>
Super-classes |[om:HubbleConstant](http://opendata.caceres.es/def/ontomunicipio#HubbleConstant) (c)<br />
### Hubble constant unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#HubbleConstantUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### hydrophilicity
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Hydrophilicity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### hydrofobiciteit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Hydrophobicity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### I magnitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#IMagnitude`
Description | <p>I magnitude in the Cousins photometric system.</p>
Super-classes |[om:CousinsMagnitude](http://opendata.caceres.es/def/ontomunicipio#CousinsMagnitude) (c)<br />
### illuminance
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Illuminance`
Description | <p>Illuminance is the total luminous flux incident on a surface per unit area.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:illuminance-Dimension](http://opendata.caceres.es/def/ontomunicipio#illuminance-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### illuminance unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#IlluminanceUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### stoot
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Impulse`
Description | <p>Impulse is the integral of a force with respect to time.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### inductance
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Inductance`
Description | <p>Inductance is that property in an electrical circuit where a change in the current flowing through that circuit induces an electromotive force that opposes the change in current.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:inductanceOrPermeance-Electromagnetic-Dimension](http://opendata.caceres.es/def/ontomunicipio#inductanceOrPermeance-Electromagnetic-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### inductance unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#InductanceUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### information capacity
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#InformationCapacity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### information capacity unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#InformationCapacityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### initial mass function
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#InitialMassFunction`
Description | <p>The number of stars in mass fraction dM around mass M. Used in Salpeter's Initial Mass Function (IMF).</p>
Super-classes |[om:NumberDensity](http://opendata.caceres.es/def/ontomunicipio#NumberDensity) (c)<br />
### integrated magnitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#IntegratedMagnitude`
Description | <p>The apparent magnitude that an extended object, such as a nebula or galaxy, would have if all its light were concentrated at a starlike point.</p>
Super-classes |[om:Magnitude](http://opendata.caceres.es/def/ontomunicipio#Magnitude) (c)<br />
### inwendige energie
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#InternalEnergy`
Description | <p>The internal energy of a thermodynamic system, or a body with well-defined boundaries is the total of the kinetic energy due to the motion of molecules (translational, rotational, vibrational) and the potential energy associated with the vibrational and electric energy of atoms within molecules or crystals.</p>
Super-classes |[om:Energy](http://opendata.caceres.es/def/ontomunicipio#Energy) (c)<br />
### interval scale
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#IntervalScale`
Super-classes |[om:Scale](http://opendata.caceres.es/def/ontomunicipio#Scale) (c)<br />
### intrinsic colour index
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#IntrinsicColourIndex`
Description | <p>The colour index a star would have in the absence of interstellar extinction (reddening). It is assumed that all stars of the same spectral type and luminosity class have the same colour index.</p>
Super-classes |[om:ColourIndex](http://opendata.caceres.es/def/ontomunicipio#ColourIndex) (c)<br />
### ionization temperature
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#IonizationTemperature`
Description | <p>The temperature of a gas or plasma derived from the relative numbers of neutral atoms and ions. Specifically, it is the temperature for which the Saha equations would predict these relative numbers, assuming the atoms and ions are in thermodynamic equilibrium.</p>
Super-classes |[om:ThermodynamicTemperature](http://opendata.caceres.es/def/ontomunicipio#ThermodynamicTemperature) (c)<br />
### irradiance
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Irradiance`
Description | <p>Irradiance is the power of electromagnetic radiation at a surface per unit area.</p>
Super-classes |[om:PowerDensity](http://opendata.caceres.es/def/ontomunicipio#PowerDensity) (c)<br />
### Jeans mass
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#JeansMass`
Description | <p>The critical mass of a molecular cloud, above which it will be unstable to collapse.</p>
Super-classes |[om:Mass](http://opendata.caceres.es/def/ontomunicipio#Mass) (c)<br />
### Johnson magnitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#JohnsonMagnitude`
Description | <p>A magnitude measured in one of Johnson's standard passbands (using a standard filter, i.e. U, B, or V).</p>
Super-classes |[om:Magnitude](http://opendata.caceres.es/def/ontomunicipio#Magnitude) (c)<br />
Sub-classes |[om:BMagnitude](http://opendata.caceres.es/def/ontomunicipio#BMagnitude) (c)<br />[om:VMagnitude](http://opendata.caceres.es/def/ontomunicipio#VMagnitude) (c)<br />[om:UMagnitude](http://opendata.caceres.es/def/ontomunicipio#UMagnitude) (c)<br />
### kerma
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Kerma`
Super-classes |[om:AbsorbedDose](http://opendata.caceres.es/def/ontomunicipio#AbsorbedDose) (c)<br />
### kinematic viscosity
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#KinematicViscosity`
Description | <p>Kinematic viscosity is the ratio of viscosity to density.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:kinematicViscosityOrThermalDiffusivity-Dimension](http://opendata.caceres.es/def/ontomunicipio#kinematicViscosityOrThermalDiffusivity-Dimension) (c)<br />
### kinematic viscosity unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#KinematicViscosityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### kinetic energy
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#KineticEnergy`
Description | <p>Kinetic energy is energy due to motion.</p>
Super-classes |[om:Energy](http://opendata.caceres.es/def/ontomunicipio#Energy) (c)<br />
### Knudsen number
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#KnudsenNumber`
Description | <p>The Knudsen number is a dimensionless number defined as the ratio of the molecular mean free path length to a representative physical length scale.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
### Knudsen number unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#KnudsenNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### label mass
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#LabelMass`
Super-classes |[om:Mass](http://opendata.caceres.es/def/ontomunicipio#Mass) (c)<br />
Sub-classes |[om:BodyLabelMass](http://opendata.caceres.es/def/ontomunicipio#BodyLabelMass) (c)<br />
### lactose mass fraction
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#LactoseMassFraction`
Description | <p>The fraction of the mass of lactose in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### 长度
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Length`
Description | <p>Length is the amount of space between two geographical points along a curve. It is a base quantity in the International System of Units and other systems of units. Length is speed times time. The metre, a base unit of length in the International System of Units, is defined in terms of speed of light during a certain time interval.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:length-Dimension](http://opendata.caceres.es/def/ontomunicipio#length-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:Breadth](http://opendata.caceres.es/def/ontomunicipio#Breadth) (c)<br />[om:Diameter](http://opendata.caceres.es/def/ontomunicipio#Diameter) (c)<br />[om:Circumference](http://opendata.caceres.es/def/ontomunicipio#Circumference) (c)<br />[om:zRange](http://opendata.caceres.es/def/ontomunicipio#zRange) (c)<br />[om:Height](http://opendata.caceres.es/def/ontomunicipio#Height) (c)<br />[om:yRange](http://opendata.caceres.es/def/ontomunicipio#yRange) (c)<br />[om:Depth](http://opendata.caceres.es/def/ontomunicipio#Depth) (c)<br />[om:xRange](http://opendata.caceres.es/def/ontomunicipio#xRange) (c)<br />[om:Wavelength](http://opendata.caceres.es/def/ontomunicipio#Wavelength) (c)<br />[om:Displacement](http://opendata.caceres.es/def/ontomunicipio#Displacement) (c)<br />[om:Distance](http://opendata.caceres.es/def/ontomunicipio#Distance) (c)<br />[om:Width](http://opendata.caceres.es/def/ontomunicipio#Width) (c)<br />[om:Radius](http://opendata.caceres.es/def/ontomunicipio#Radius) (c)<br />[om:Thickness](http://opendata.caceres.es/def/ontomunicipio#Thickness) (c)<br />[om:ScaleLength](http://opendata.caceres.es/def/ontomunicipio#ScaleLength) (c)<br />[om:ScaleHeight](http://opendata.caceres.es/def/ontomunicipio#ScaleHeight) (c)<br />[om:FontSize](http://opendata.caceres.es/def/ontomunicipio#FontSize) (c)<br />
### length unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#LengthUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
Sub-classes |[om:FontSizeUnit](http://opendata.caceres.es/def/ontomunicipio#FontSizeUnit) (c)<br />
### getal van Lewis
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#LewisNumber`
Description | <p>The Lewis number is a dimensionless number defined as the ratio of thermal diffusivity to mass diffusivity.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
### Lewis number unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#LewisNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### light time
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#LightTime`
Description | <p>The time electromagnetic radiation takes to reach Earth from a distant source. Often the correction in light time is needed to accurately calculate the apparent position of solar system objects or to calculate the period of variable stars (different times are observed when the Earth is at a different position in its orbit).</p>
Super-classes |[om:Time](http://opendata.caceres.es/def/ontomunicipio#Time) (c)<br />
### limiting magnitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#LimitingMagnitude`
Description | <p>The magnitude of the faintest object (star) that can be detected by a telescope or other instrument. Depends not only on the telescope but also on the detector and on the observing method.</p>
Super-classes |[om:Magnitude](http://opendata.caceres.es/def/ontomunicipio#Magnitude) (c)<br />
### lineaire vervorming
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#LinearStrain`
Super-classes |[om:Strain](http://opendata.caceres.es/def/ontomunicipio#Strain) (c)<br />
### lipophilicity
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Lipophilicity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### locust bean gum mass fraction
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#LocustBeanGumMassFraction`
Description | <p>The fraction of the mass of locust bean gum in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### loss modulus
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#LossModulus`
Super-classes |[om:DynamicModulus](http://opendata.caceres.es/def/ontomunicipio#DynamicModulus) (c)<br />
### luminance
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Luminance`
Description | <p>Luminous flux is the total visible energy emitted by a source per unit time.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:luminance-Dimension](http://opendata.caceres.es/def/ontomunicipio#luminance-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### luminance unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#LuminanceUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### luminosity function
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#LuminosityFunction`
Description | <p>The number of stars of absolute magnitudes between Mv and Mv+ΔMv per cubic parsec.</p>
Super-classes |[om:NumberDensity](http://opendata.caceres.es/def/ontomunicipio#NumberDensity) (c)<br />
### luminous efficacy
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#LuminousEfficacy`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:luminousEfficacy-Dimension](http://opendata.caceres.es/def/ontomunicipio#luminousEfficacy-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### luminous efficacy unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#LuminousEfficacyUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### luminous energy
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#LuminousEnergy`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:luminousEnergy-Dimension](http://opendata.caceres.es/def/ontomunicipio#luminousEnergy-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### luminous energy unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#LuminousEnergyUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### luminous flux
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#LuminousFlux`
Description | <p>Luminous flux is the total visible energy emitted by a source per unit time.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:luminousFlux-Dimension](http://opendata.caceres.es/def/ontomunicipio#luminousFlux-Dimension) (c)<br />
### luminous flux unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#LuminousFluxUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### lichtsterkte
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#LuminousIntensity`
Description | <p>Luminous intensity is the wavelength-weighted power emitted by a light source in a particular direction per unit solid angle. It is a base quantity in the International System of Units. Luminous intensity is luminous flux divided by solid angle.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:luminousIntensity-Dimension](http://opendata.caceres.es/def/ontomunicipio#luminousIntensity-Dimension) (c)<br />
### luminous intensity unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#LuminousIntensityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### Mach number
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MachNumber`
Description | <p>The Mach number is the speed of an object that moves through air, or any fluid substance, divided by the speed of sound as it is in that substance.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
### Mach number unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MachNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### magnetic field
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MagneticField`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:MagneticField-Dimension](http://opendata.caceres.es/def/ontomunicipio#MagneticField-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### magnetic field unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MagneticFieldUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### magnetic flux
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MagneticFlux`
Description | <p>Magnetic flux through any area perpendicular to a magnetic field is the product of the area by the field strength.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:magneticFlux-Dimension](http://opendata.caceres.es/def/ontomunicipio#magneticFlux-Dimension) (c)<br />
### magnetic flux density
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MagneticFluxDensity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:magneticFluxDensity-Dimension](http://opendata.caceres.es/def/ontomunicipio#magneticFluxDensity-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### magnetic flux density unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MagneticFluxDensityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### magnetic flux unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MagneticFluxUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### magnetisch getal van Reynolds
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MagneticReynoldsNumber`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### magnetic Reynolds number unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MagneticReynoldsNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### magnetomotive force
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MagnetomotiveForce`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:electricCurrent-Dimension](http://opendata.caceres.es/def/ontomunicipio#electricCurrent-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### magnetomotive force unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MagnetomotiveForceUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### magnitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Magnitude`
Description | <p>Reverse logarithmic measure of the brightness of an object.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:TychoBroadbandMagnitude](http://opendata.caceres.es/def/ontomunicipio#TychoBroadbandMagnitude) (c)<br />[om:LimitingMagnitude](http://opendata.caceres.es/def/ontomunicipio#LimitingMagnitude) (c)<br />[om:ThuanAndGunnMagnitude](http://opendata.caceres.es/def/ontomunicipio#ThuanAndGunnMagnitude) (c)<br />[om:WhiteLightMagnitude](http://opendata.caceres.es/def/ontomunicipio#WhiteLightMagnitude) (c)<br />[om:JohnsonMagnitude](http://opendata.caceres.es/def/ontomunicipio#JohnsonMagnitude) (c)<br />[om:IntegratedMagnitude](http://opendata.caceres.es/def/ontomunicipio#IntegratedMagnitude) (c)<br />[om:_1040NanometreLockwoodMagnitude](http://opendata.caceres.es/def/ontomunicipio#_1040NanometreLockwoodMagnitude) (c)<br />[om:CousinsMagnitude](http://opendata.caceres.es/def/ontomunicipio#CousinsMagnitude) (c)<br />[om:PhotographicMagnitude](http://opendata.caceres.es/def/ontomunicipio#PhotographicMagnitude) (c)<br />[om:AbsoluteMagnitude](http://opendata.caceres.es/def/ontomunicipio#AbsoluteMagnitude) (c)<br />[om:ApparentMagnitude](http://opendata.caceres.es/def/ontomunicipio#ApparentMagnitude) (c)<br />[om:BolometricMagnitude](http://opendata.caceres.es/def/ontomunicipio#BolometricMagnitude) (c)<br />[om:MagnitudeAtMinimumBrightness](http://opendata.caceres.es/def/ontomunicipio#MagnitudeAtMinimumBrightness) (c)<br />[om:RedMagnitude](http://opendata.caceres.es/def/ontomunicipio#RedMagnitude) (c)<br />[om:StroemgrenMagnitude](http://opendata.caceres.es/def/ontomunicipio#StroemgrenMagnitude) (c)<br />[om:MagnitudeAtMaximumBrightness](http://opendata.caceres.es/def/ontomunicipio#MagnitudeAtMaximumBrightness) (c)<br />
### magnitude at maximum brightness
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MagnitudeAtMaximumBrightness`
Description | <p>The magnitude at maximum brightness of a variable star.</p>
Super-classes |[om:Magnitude](http://opendata.caceres.es/def/ontomunicipio#Magnitude) (c)<br />
Sub-classes |[om:PhotographicMagnitudeAtMaximumBrightness](http://opendata.caceres.es/def/ontomunicipio#PhotographicMagnitudeAtMaximumBrightness) (c)<br />[om:BMagnitudeAtMaximumBrightness](http://opendata.caceres.es/def/ontomunicipio#BMagnitudeAtMaximumBrightness) (c)<br />[om:VMagnitudeAtMaximumBrightness](http://opendata.caceres.es/def/ontomunicipio#VMagnitudeAtMaximumBrightness) (c)<br />[om:WhiteLightMagnitudeAtMaximumBrightness](http://opendata.caceres.es/def/ontomunicipio#WhiteLightMagnitudeAtMaximumBrightness) (c)<br />
### magnitude at minimum brightness
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MagnitudeAtMinimumBrightness`
Description | <p>The magnitude at minimum brightness of a variable star.</p>
Super-classes |[om:Magnitude](http://opendata.caceres.es/def/ontomunicipio#Magnitude) (c)<br />
Sub-classes |[om:BMagnitudeAtMinimumBrightness](http://opendata.caceres.es/def/ontomunicipio#BMagnitudeAtMinimumBrightness) (c)<br />[om:VMagnitudeAtMinimumBrightness](http://opendata.caceres.es/def/ontomunicipio#VMagnitudeAtMinimumBrightness) (c)<br />[om:PhotographicMagnitudeAtMinimumBrightness](http://opendata.caceres.es/def/ontomunicipio#PhotographicMagnitudeAtMinimumBrightness) (c)<br />[om:WhiteLightMagnitudeAtMinimumBrightness](http://opendata.caceres.es/def/ontomunicipio#WhiteLightMagnitudeAtMinimumBrightness) (c)<br />
### magnitude unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MagnitudeUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### manual firmness
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ManualFirmness`
Description | <p>Firmness manueel: code 0 - 5.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### massa
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Mass`
Description | <p>Mass is the amount of matter of a phenomenon. It is a base quantity in the International System of Units. Mass is force divided by acceleration.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:mass-Dimension](http://opendata.caceres.es/def/ontomunicipio#mass-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:DryMass](http://opendata.caceres.es/def/ontomunicipio#DryMass) (c)<br />[om:StrawMass](http://opendata.caceres.es/def/ontomunicipio#StrawMass) (c)<br />[om:VasePlusWaterMass](http://opendata.caceres.es/def/ontomunicipio#VasePlusWaterMass) (c)<br />[om:LabelMass](http://opendata.caceres.es/def/ontomunicipio#LabelMass) (c)<br />[om:CartonMass](http://opendata.caceres.es/def/ontomunicipio#CartonMass) (c)<br />[om:BodyMass](http://opendata.caceres.es/def/ontomunicipio#BodyMass) (c)<br />[om:FlowpackMass](http://opendata.caceres.es/def/ontomunicipio#FlowpackMass) (c)<br />[om:CapMass](http://opendata.caceres.es/def/ontomunicipio#CapMass) (c)<br />[om:JeansMass](http://opendata.caceres.es/def/ontomunicipio#JeansMass) (c)<br />[om:NeckRingMass](http://opendata.caceres.es/def/ontomunicipio#NeckRingMass) (c)<br />[om:TopMass](http://opendata.caceres.es/def/ontomunicipio#TopMass) (c)<br />[om:AtomicMass](http://opendata.caceres.es/def/ontomunicipio#AtomicMass) (c)<br />[om:VasePlusWaterPlusFlowerMass](http://opendata.caceres.es/def/ontomunicipio#VasePlusWaterPlusFlowerMass) (c)<br />
### mass flow
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MassFlow`
Description | <p>Mass flow is the movement of substances at equal rates or as a single body.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:massFlow-Dimension](http://opendata.caceres.es/def/ontomunicipio#massFlow-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### mass flow unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MassFlowUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### mass fraction
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MassFraction`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:LocustBeanGumMassFraction](http://opendata.caceres.es/def/ontomunicipio#LocustBeanGumMassFraction) (c)<br />[om:WaterMassFraction](http://opendata.caceres.es/def/ontomunicipio#WaterMassFraction) (c)<br />[om:XanthanMassFraction](http://opendata.caceres.es/def/ontomunicipio#XanthanMassFraction) (c)<br />[om:DryMatterMassFraction](http://opendata.caceres.es/def/ontomunicipio#DryMatterMassFraction) (c)<br />[om:GelatinMassFraction](http://opendata.caceres.es/def/ontomunicipio#GelatinMassFraction) (c)<br />[om:TweenMassFraction](http://opendata.caceres.es/def/ontomunicipio#TweenMassFraction) (c)<br />[om:SoyBeanMassFraction](http://opendata.caceres.es/def/ontomunicipio#SoyBeanMassFraction) (c)<br />[om:ColdGasMassFraction](http://opendata.caceres.es/def/ontomunicipio#ColdGasMassFraction) (c)<br />[om:ModeratedStarchMassFraction](http://opendata.caceres.es/def/ontomunicipio#ModeratedStarchMassFraction) (c)<br />[om:WheyProteinAggregateMassFraction](http://opendata.caceres.es/def/ontomunicipio#WheyProteinAggregateMassFraction) (c)<br />[om:PotassiumSorbateMassFraction](http://opendata.caceres.es/def/ontomunicipio#PotassiumSorbateMassFraction) (c)<br />[om:StarchVA85MassFraction](http://opendata.caceres.es/def/ontomunicipio#StarchVA85MassFraction) (c)<br />[om:EggMassFraction](http://opendata.caceres.es/def/ontomunicipio#EggMassFraction) (c)<br />[om:SugarMassFraction](http://opendata.caceres.es/def/ontomunicipio#SugarMassFraction) (c)<br />[om:GuarGumMassFraction](http://opendata.caceres.es/def/ontomunicipio#GuarGumMassFraction) (c)<br />[om:MustardPowderMassFraction](http://opendata.caceres.es/def/ontomunicipio#MustardPowderMassFraction) (c)<br />[om:ProteinMassFraction](http://opendata.caceres.es/def/ontomunicipio#ProteinMassFraction) (c)<br />[om:SaltMassFraction](http://opendata.caceres.es/def/ontomunicipio#SaltMassFraction) (c)<br />[om:StarchMassFraction](http://opendata.caceres.es/def/ontomunicipio#StarchMassFraction) (c)<br />[om:StarchVA40MassFraction](http://opendata.caceres.es/def/ontomunicipio#StarchVA40MassFraction) (c)<br />[om:WheyProteinBeadsMassFraction](http://opendata.caceres.es/def/ontomunicipio#WheyProteinBeadsMassFraction) (c)<br />[om:AceticAcidMassFraction](http://opendata.caceres.es/def/ontomunicipio#AceticAcidMassFraction) (c)<br />[om:LactoseMassFraction](http://opendata.caceres.es/def/ontomunicipio#LactoseMassFraction) (c)<br />[om:FatMassFraction](http://opendata.caceres.es/def/ontomunicipio#FatMassFraction) (c)<br />[om:WheyProteinMassFraction](http://opendata.caceres.es/def/ontomunicipio#WheyProteinMassFraction) (c)<br />[om:DisodiumEthyleneDiamineTetreAcetateMassFraction](http://opendata.caceres.es/def/ontomunicipio#DisodiumEthyleneDiamineTetreAcetateMassFraction) (c)<br />
### mass fraction unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MassFractionUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### mass unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MassUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### measure
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Measure`
Description | <p>A measure combines a number to a unit of measure. For example, "3 m" is a measure.</p>
### metallicity
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Metallicity`
Description | <p>The log of the ratio between the ratios of the observed Fe and H quantities in a star and the same ratio in the Sun. This is a very important quantity that is often used in astronomy as an indicator of the age of a star.</p>
Super-classes |[om:QuantityOfDimensionOne](http://opendata.caceres.es/def/ontomunicipio#QuantityOfDimensionOne) (c)<br />
### metre per prefixed second (time)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MetrePerPrefixedSecond-Time`
Super-classes |[om:UnitDivision](http://opendata.caceres.es/def/ontomunicipio#UnitDivision) (c)<br />
### metre per prefixed second (time) squared
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MetrePerPrefixedSecond-TimeSquared`
Super-classes |[om:UnitDivision](http://opendata.caceres.es/def/ontomunicipio#UnitDivision) (c)<br />
### moderated starch mass fraction
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ModeratedStarchMassFraction`
Description | <p>The fraction of the mass of moderated starch in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### elasticiteitsmodulus
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ModulusOfElasticity`
Super-classes |[om:DynamicModulus](http://opendata.caceres.es/def/ontomunicipio#DynamicModulus) (c)<br />
### molality
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Molality`
Description | <p>Molality is the number of moles of solute per kilogram of solvent.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### molality unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MolalityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### molaire energie
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MolarEnergy`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:molarEnergy-Dimension](http://opendata.caceres.es/def/ontomunicipio#molarEnergy-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:ResonanceEnergy](http://opendata.caceres.es/def/ontomunicipio#ResonanceEnergy) (c)<br />
### molar energy unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MolarEnergyUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### molar entropy
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MolarEntropy`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:molarEntropyOrMolarHeatCapacityOrGasConstant-Dimension](http://opendata.caceres.es/def/ontomunicipio#molarEntropyOrMolarHeatCapacityOrGasConstant-Dimension) (c)<br />
### molar entropy unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MolarEntropyUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### molaire warmtecapaciteit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MolarHeatCapacity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:molarEntropyOrMolarHeatCapacityOrGasConstant-Dimension](http://opendata.caceres.es/def/ontomunicipio#molarEntropyOrMolarHeatCapacityOrGasConstant-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### molar heat capacity unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MolarHeatCapacityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### molar mass
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MolarMass`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### molar mass unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MolarMassUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### molair volume
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MolarVolume`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### molar volume unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MolarVolumeUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### mole per prefixed litre
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MolePerPrefixedLitre`
Super-classes |[om:UnitDivision](http://opendata.caceres.es/def/ontomunicipio#UnitDivision) (c)<br />
### mole per prefixed metre
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MolePerPrefixedMetre`
Super-classes |[om:UnitDivision](http://opendata.caceres.es/def/ontomunicipio#UnitDivision) (c)<br />
### moment of force
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MomentOfForce`
Description | <p>Moment of force is the effectiveness of a force to produce rotation about an axis measured by the product of the force and the perpendicular distance from the line of action of the force to the axis.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:energy-Dimension](http://opendata.caceres.es/def/ontomunicipio#energy-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### moment of force unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MomentOfForceUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### traagheidsmoment
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MomentOfInertia`
Description | <p>Moment of inertia is a measure of the effectiveness of mass in rotation.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### moment of inertia unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MomentOfInertiaUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### momentum
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Momentum`
Description | <p>Momentum is the product of mass and velocity of an object.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### momentum unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MomentumUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### mustard powder mass fraction
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#MustardPowderMassFraction`
Description | <p>The fraction of the mass of mustard powder in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### neck ring mass
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NeckRingMass`
Super-classes |[om:Mass](http://opendata.caceres.es/def/ontomunicipio#Mass) (c)<br />
### noise equivalent power
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NoiseEquivalentPower`
Description | <p>Radiative flux on a detector needed for a signal/noise ratio of 1 (Kitchin, Astrophysical Techniques, IoP, Table 1.1.2).</p>
Super-classes |[om:Power](http://opendata.caceres.es/def/ontomunicipio#Power) (c)<br />
### normal albedo
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NormalAlbedo`
Description | <p>Ratio between radiation falling vertically onto an object and the radiation radiated back vertically.</p>
Super-classes |[om:Albedo](http://opendata.caceres.es/def/ontomunicipio#Albedo) (c)<br />
### normaalvervorming
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NormalStrain`
Super-classes |[om:Strain](http://opendata.caceres.es/def/ontomunicipio#Strain) (c)<br />
### normaalspanning
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NormalStress`
Super-classes |[om:Stress](http://opendata.caceres.es/def/ontomunicipio#Stress) (c)<br />
### normalised detectivity
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NormalisedDetectivity`
Description | <p>The detectivity normalised by multiplying by the square root of the detector area, and by the electrical bandwidth. The units cm Hz(1/2)/W are commonly used and it then represents the signal-to-noise ratio when 1 W of radiation is incident on a detector with an area of 1 cm2, and the electrical bandwidth is 1 Hz.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### number
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Number`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:NumberExternalBrowning](http://opendata.caceres.es/def/ontomunicipio#NumberExternalBrowning) (c)<br />[om:NumberBuds](http://opendata.caceres.es/def/ontomunicipio#NumberBuds) (c)<br />[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />[om:NumberBotrytis](http://opendata.caceres.es/def/ontomunicipio#NumberBotrytis) (c)<br />[om:NumberManualFirmness](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness) (c)<br />[om:NumberPulpBrowning](http://opendata.caceres.es/def/ontomunicipio#NumberPulpBrowning) (c)<br />[om:NumberVascularBrowning](http://opendata.caceres.es/def/ontomunicipio#NumberVascularBrowning) (c)<br />[om:NumberFlowers](http://opendata.caceres.es/def/ontomunicipio#NumberFlowers) (c)<br />[om:NumberLeaves](http://opendata.caceres.es/def/ontomunicipio#NumberLeaves) (c)<br />[om:NumberBudStadium](http://opendata.caceres.es/def/ontomunicipio#NumberBudStadium) (c)<br />
### number abscised buds
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberAbscisedBuds`
Description | <p>Aantal gevallen knoppen.</p>
Super-classes |[om:NumberBuds](http://opendata.caceres.es/def/ontomunicipio#NumberBuds) (c)<br />
### aantal gevallen bloemen
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberAbscisedFlowers`
Description | <p>Aantal gevallen bloemen.</p>
Super-classes |[om:NumberFlowers](http://opendata.caceres.es/def/ontomunicipio#NumberFlowers) (c)<br />
### number abscised leaves
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberAbscisedLeaves`
Description | <p>Aantal gevallen bladeren.</p>
Super-classes |[om:NumberLeaves](http://opendata.caceres.es/def/ontomunicipio#NumberLeaves) (c)<br />
### number blue-discolored flowers
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberBlue-DiscoloredFlowers`
Description | <p>Aantal blauwverkleurde bloemen.</p>
Super-classes |[om:NumberFlowers](http://opendata.caceres.es/def/ontomunicipio#NumberFlowers) (c)<br />
### number Botrytis
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberBotrytis`
Super-classes |[om:Number](http://opendata.caceres.es/def/ontomunicipio#Number) (c)<br />
Sub-classes |[om:NumberBotrytis0](http://opendata.caceres.es/def/ontomunicipio#NumberBotrytis0) (c)<br />[om:NumberBotrytis4](http://opendata.caceres.es/def/ontomunicipio#NumberBotrytis4) (c)<br />[om:NumberBotrytis3](http://opendata.caceres.es/def/ontomunicipio#NumberBotrytis3) (c)<br />[om:NumberBotrytis1](http://opendata.caceres.es/def/ontomunicipio#NumberBotrytis1) (c)<br />[om:NumberBotrytis2](http://opendata.caceres.es/def/ontomunicipio#NumberBotrytis2) (c)<br />
### aantal Botrytis 0
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberBotrytis0`
Description | <p>Aantal bloemen zonder Botrytis.</p>
Super-classes |[om:NumberBotrytis](http://opendata.caceres.es/def/ontomunicipio#NumberBotrytis) (c)<br />
### number Botrytis 1
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberBotrytis1`
Description | <p>Aantal bloemen met Botrytis 1: enkele laesies: max 3 op één petaal of max 5 op meerdere plekken.</p>
Super-classes |[om:NumberBotrytis](http://opendata.caceres.es/def/ontomunicipio#NumberBotrytis) (c)<br />
### aantal Botrytis 2
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberBotrytis2`
Description | <p>Aantal bloemen met Botrytis 2: grotere vlek(ken) op één petaal.</p>
Super-classes |[om:NumberBotrytis](http://opendata.caceres.es/def/ontomunicipio#NumberBotrytis) (c)<br />
### number Botrytis 3
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberBotrytis3`
Description | <p>Aantal bloemen met Botrytis 3: één bruin petaal of vlekken op meer petalen.</p>
Super-classes |[om:NumberBotrytis](http://opendata.caceres.es/def/ontomunicipio#NumberBotrytis) (c)<br />
### aantal Botrytis 4
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberBotrytis4`
Description | <p>Aantal bloemen met Botrytis 4: minimaal één bruin petaal en hart aangetast.</p>
Super-classes |[om:NumberBotrytis](http://opendata.caceres.es/def/ontomunicipio#NumberBotrytis) (c)<br />
### aantal knopstadium
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberBudStadium`
Super-classes |[om:Number](http://opendata.caceres.es/def/ontomunicipio#Number) (c)<br />
Sub-classes |[om:NumberBudStadium5](http://opendata.caceres.es/def/ontomunicipio#NumberBudStadium5) (c)<br />[om:NumberBudStadium2](http://opendata.caceres.es/def/ontomunicipio#NumberBudStadium2) (c)<br />[om:NumberBudStadium3](http://opendata.caceres.es/def/ontomunicipio#NumberBudStadium3) (c)<br />[om:NumberBudStadium1](http://opendata.caceres.es/def/ontomunicipio#NumberBudStadium1) (c)<br />[om:NumberBudStadium4](http://opendata.caceres.es/def/ontomunicipio#NumberBudStadium4) (c)<br />
### number bud stadium 1
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberBudStadium1`
Description | <p>Roos aantal in knopstadium 1: spitse knop.</p>
Super-classes |[om:NumberBudStadium](http://opendata.caceres.es/def/ontomunicipio#NumberBudStadium) (c)<br />
### aantal knopstadium 2
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberBudStadium2`
Description | <p>Roos aantal in knopstadium 2: spitse knop.</p>
Super-classes |[om:NumberBudStadium](http://opendata.caceres.es/def/ontomunicipio#NumberBudStadium) (c)<br />
### number bud stadium 3
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberBudStadium3`
Description | <p>Roos aantal in knopstadium 3: spitse knop.</p>
Super-classes |[om:NumberBudStadium](http://opendata.caceres.es/def/ontomunicipio#NumberBudStadium) (c)<br />
### aantal knopstadium 4
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberBudStadium4`
Description | <p>Roos aantal in knopstadium 4: spitse knop.</p>
Super-classes |[om:NumberBudStadium](http://opendata.caceres.es/def/ontomunicipio#NumberBudStadium) (c)<br />
### number bud stadium 5
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberBudStadium5`
Description | <p>Roos aantal in knopstadium 5: spitse knop.</p>
Super-classes |[om:NumberBudStadium](http://opendata.caceres.es/def/ontomunicipio#NumberBudStadium) (c)<br />
### number buds
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberBuds`
Super-classes |[om:Number](http://opendata.caceres.es/def/ontomunicipio#Number) (c)<br />
Sub-classes |[om:NumberDryBuds](http://opendata.caceres.es/def/ontomunicipio#NumberDryBuds) (c)<br />[om:NumberAbscisedBuds](http://opendata.caceres.es/def/ontomunicipio#NumberAbscisedBuds) (c)<br />[om:TotalNumberBuds](http://opendata.caceres.es/def/ontomunicipio#TotalNumberBuds) (c)<br />[om:NumberMalformedBuds](http://opendata.caceres.es/def/ontomunicipio#NumberMalformedBuds) (c)<br />
### number color
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberColor`
Super-classes |[om:Number](http://opendata.caceres.es/def/ontomunicipio#Number) (c)<br />
Sub-classes |[om:NumberPulpBrowning5](http://opendata.caceres.es/def/ontomunicipio#NumberPulpBrowning5) (c)<br />[om:NumberVascularBrowning4](http://opendata.caceres.es/def/ontomunicipio#NumberVascularBrowning4) (c)<br />[om:NumberColor4](http://opendata.caceres.es/def/ontomunicipio#NumberColor4) (c)<br />[om:NumberVascularBrowning2](http://opendata.caceres.es/def/ontomunicipio#NumberVascularBrowning2) (c)<br />[om:NumberVascularBrowning5](http://opendata.caceres.es/def/ontomunicipio#NumberVascularBrowning5) (c)<br />[om:NumberExternalBrowning5](http://opendata.caceres.es/def/ontomunicipio#NumberExternalBrowning5) (c)<br />[om:NumberPulpBrowning3](http://opendata.caceres.es/def/ontomunicipio#NumberPulpBrowning3) (c)<br />[om:NumberPulpBrowning1](http://opendata.caceres.es/def/ontomunicipio#NumberPulpBrowning1) (c)<br />[om:NumberColor3](http://opendata.caceres.es/def/ontomunicipio#NumberColor3) (c)<br />[om:NumberVascularBrowning1](http://opendata.caceres.es/def/ontomunicipio#NumberVascularBrowning1) (c)<br />[om:NumberColor1](http://opendata.caceres.es/def/ontomunicipio#NumberColor1) (c)<br />[om:NumberExternalBrowning4](http://opendata.caceres.es/def/ontomunicipio#NumberExternalBrowning4) (c)<br />[om:NumberColor5](http://opendata.caceres.es/def/ontomunicipio#NumberColor5) (c)<br />[om:NumberColor2](http://opendata.caceres.es/def/ontomunicipio#NumberColor2) (c)<br />[om:NumberVascularBrowning3](http://opendata.caceres.es/def/ontomunicipio#NumberVascularBrowning3) (c)<br />[om:NumberExternalBrowning3](http://opendata.caceres.es/def/ontomunicipio#NumberExternalBrowning3) (c)<br />[om:NumberPulpBrowning4](http://opendata.caceres.es/def/ontomunicipio#NumberPulpBrowning4) (c)<br />[om:NumberExternalBrowning1](http://opendata.caceres.es/def/ontomunicipio#NumberExternalBrowning1) (c)<br />[om:NumberPulpBrowning2](http://opendata.caceres.es/def/ontomunicipio#NumberPulpBrowning2) (c)<br />[om:NumberExternalBrowning2](http://opendata.caceres.es/def/ontomunicipio#NumberExternalBrowning2) (c)<br />
### aantal kleur 1
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberColor1`
Description | <p>Voorbeeld avocado Hass: code 1 poster (vrijwel) geheel groen.</p>
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### aantal kleur 2
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberColor2`
Description | <p>Voorbeeld avocado Hass: code 2 poster meer groen dan donker.</p>
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### aantal kleur 3
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberColor3`
Description | <p>Voorbeeld avocado Hass: code 3 poster 50% groen.</p>
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### number color 4
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberColor4`
Description | <p>Voorbeeld avocado Hass: code 4 poster meer donker dan groen.</p>
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### number color 5
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberColor5`
Description | <p>Voorbeeld avocado Hass: code 5 poster (vrijwel) geheel donker.</p>
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### number density
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberDensity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:numberDensity-Dimension](http://opendata.caceres.es/def/ontomunicipio#numberDensity-Dimension) (c)<br />
Sub-classes |[om:InitialMassFunction](http://opendata.caceres.es/def/ontomunicipio#InitialMassFunction) (c)<br />[om:LuminosityFunction](http://opendata.caceres.es/def/ontomunicipio#LuminosityFunction) (c)<br />
### number density unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberDensityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### number dry buds
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberDryBuds`
Description | <p>Aantal verdroogde knoppen.</p>
Super-classes |[om:NumberBuds](http://opendata.caceres.es/def/ontomunicipio#NumberBuds) (c)<br />
### number dry flowers
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberDryFlowers`
Description | <p>Aantal verdroogde bloemen.</p>
Super-classes |[om:NumberFlowers](http://opendata.caceres.es/def/ontomunicipio#NumberFlowers) (c)<br />
### number dry leaves
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberDryLeaves`
Description | <p>Aantal verdroogde bladeren.</p>
Super-classes |[om:NumberLeaves](http://opendata.caceres.es/def/ontomunicipio#NumberLeaves) (c)<br />
### number external browning
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberExternalBrowning`
Super-classes |[om:Number](http://opendata.caceres.es/def/ontomunicipio#Number) (c)<br />
### number external browning 1
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberExternalBrowning1`
Description | <p>Voorbeeld avocado Hass: code 1 poster.</p>
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### number external browning 2
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberExternalBrowning2`
Description | <p>Voorbeeld avocado Hass: code 2 poster.</p>
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### number external browning 3
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberExternalBrowning3`
Description | <p>Voorbeeld avocado Hass: code 3 poster.</p>
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### number external browning 4
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberExternalBrowning4`
Description | <p>Voorbeeld avocado Hass: code 4 poster.</p>
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### number external browning 5
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberExternalBrowning5`
Description | <p>Voorbeeld avocado Hass: code 5 poster.</p>
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### aantal bloemen
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberFlowers`
Super-classes |[om:Number](http://opendata.caceres.es/def/ontomunicipio#Number) (c)<br />
Sub-classes |[om:NumberDryFlowers](http://opendata.caceres.es/def/ontomunicipio#NumberDryFlowers) (c)<br />[om:NumberNonturgidFlowers](http://opendata.caceres.es/def/ontomunicipio#NumberNonturgidFlowers) (c)<br />[om:NumberAbscisedFlowers](http://opendata.caceres.es/def/ontomunicipio#NumberAbscisedFlowers) (c)<br />[om:NumberWiltedFlowers](http://opendata.caceres.es/def/ontomunicipio#NumberWiltedFlowers) (c)<br />[om:TotalNumberFlowers](http://opendata.caceres.es/def/ontomunicipio#TotalNumberFlowers) (c)<br />[om:NumberMalformedFlowers](http://opendata.caceres.es/def/ontomunicipio#NumberMalformedFlowers) (c)<br />[om:NumberBlue-DiscoloredFlowers](http://opendata.caceres.es/def/ontomunicipio#NumberBlue-DiscoloredFlowers) (c)<br />[om:NumberRottenFlowers](http://opendata.caceres.es/def/ontomunicipio#NumberRottenFlowers) (c)<br />
### aantal bladeren
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberLeaves`
Super-classes |[om:Number](http://opendata.caceres.es/def/ontomunicipio#Number) (c)<br />
Sub-classes |[om:NumberAbscisedLeaves](http://opendata.caceres.es/def/ontomunicipio#NumberAbscisedLeaves) (c)<br />[om:NumberRottenLeaves](http://opendata.caceres.es/def/ontomunicipio#NumberRottenLeaves) (c)<br />[om:NumberWiltedLeaves](http://opendata.caceres.es/def/ontomunicipio#NumberWiltedLeaves) (c)<br />[om:NumberDryLeaves](http://opendata.caceres.es/def/ontomunicipio#NumberDryLeaves) (c)<br />[om:NumberNonturgidLeaves](http://opendata.caceres.es/def/ontomunicipio#NumberNonturgidLeaves) (c)<br />[om:TotalNumberLeaves](http://opendata.caceres.es/def/ontomunicipio#TotalNumberLeaves) (c)<br />[om:NumberYellowLeaves](http://opendata.caceres.es/def/ontomunicipio#NumberYellowLeaves) (c)<br />
### aantal misvormde knoppen
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberMalformedBuds`
Description | <p>Aantal misvormde knoppen.</p>
Super-classes |[om:NumberBuds](http://opendata.caceres.es/def/ontomunicipio#NumberBuds) (c)<br />
### number malformed flowers
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberMalformedFlowers`
Description | <p>Aantal misvormde bloemen.</p>
Super-classes |[om:NumberFlowers](http://opendata.caceres.es/def/ontomunicipio#NumberFlowers) (c)<br />
### number manual firmness
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness`
Super-classes |[om:Number](http://opendata.caceres.es/def/ontomunicipio#Number) (c)<br />
Sub-classes |[om:NumberManualFirmness1.5](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness1.5) (c)<br />[om:NumberManualFirmness3.5](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness3.5) (c)<br />[om:NumberManualFirmness5](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness5) (c)<br />[om:NumberManualFirmness2](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness2) (c)<br />[om:NumberManualFirmness3](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness3) (c)<br />[om:NumberManualFirmness0](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness0) (c)<br />[om:NumberManualFirmness1](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness1) (c)<br />[om:NumberManualFirmness4](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness4) (c)<br />[om:NumberManualFirmness2.5](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness2.5) (c)<br />[om:NumberManualFirmness0.5](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness0.5) (c)<br />[om:NumberManualFirmness4.5](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness4.5) (c)<br />
### aantal manuele stevigheid 0
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness0`
Description | <p>Firmness manueel: 0 = steenhard.</p>
Super-classes |[om:NumberManualFirmness](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness) (c)<br />
### number manual firmness 0.5
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness0.5`
Description | <p>Firmness manueel: 0.5 = hard.</p>
Super-classes |[om:NumberManualFirmness](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness) (c)<br />
### aantal manuele stevigheid 1
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness1`
Description | <p>Firmness manueel: 1 = zeer stevig.</p>
Super-classes |[om:NumberManualFirmness](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness) (c)<br />
### aantal manuele stevigheid 1.5
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness1.5`
Description | <p>Firmness manueel: 1.5 = stevig.</p>
Super-classes |[om:NumberManualFirmness](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness) (c)<br />
### number manual firmness 2
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness2`
Description | <p>Firmness manueel: 2 = halfzacht.</p>
Super-classes |[om:NumberManualFirmness](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness) (c)<br />
### aantal manuele stevigheid 2.5
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness2.5`
Description | <p>Firmness manueel: 2.5 = eetrijp.</p>
Super-classes |[om:NumberManualFirmness](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness) (c)<br />
### number manual firmness 3
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness3`
Description | <p>Firmness manueel: 3 = zacht.</p>
Super-classes |[om:NumberManualFirmness](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness) (c)<br />
### aantal manuele stevigheid 3.5
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness3.5`
Description | <p>Firmness manueel: 3.5 = te zacht.</p>
Super-classes |[om:NumberManualFirmness](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness) (c)<br />
### aantal manuele stevigheid 4
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness4`
Description | <p>Firmness manueel: 4 = week.</p>
Super-classes |[om:NumberManualFirmness](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness) (c)<br />
### aantal manuele stevigheid 4.5
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness4.5`
Description | <p>Firmness manueel: 4.5 = vies.</p>
Super-classes |[om:NumberManualFirmness](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness) (c)<br />
### aantal manuele stevigheid 5
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness5`
Description | <p>Firmness manueel: 5 = zeer vies.</p>
Super-classes |[om:NumberManualFirmness](http://opendata.caceres.es/def/ontomunicipio#NumberManualFirmness) (c)<br />
### number nonturgid flowers
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberNonturgidFlowers`
Description | <p>Aantal slappe bloemen.</p>
Super-classes |[om:NumberFlowers](http://opendata.caceres.es/def/ontomunicipio#NumberFlowers) (c)<br />
### number nonturgid leaves
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberNonturgidLeaves`
Description | <p>Aantal slappe bladeren.</p>
Super-classes |[om:NumberLeaves](http://opendata.caceres.es/def/ontomunicipio#NumberLeaves) (c)<br />
### number pulp browning
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberPulpBrowning`
Super-classes |[om:Number](http://opendata.caceres.es/def/ontomunicipio#Number) (c)<br />
### number pulp browning 1
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberPulpBrowning1`
Description | <p>Voorbeeld avocado Hass: code 1 poster pulp browning.</p>
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### number pulp browning 2
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberPulpBrowning2`
Description | <p>Voorbeeld avocado Hass: code 2 poster pulp browning.</p>
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### number pulp browning 3
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberPulpBrowning3`
Description | <p>Voorbeeld avocado Hass: code 3 poster pulp browning.</p>
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### number pulp browning 4
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberPulpBrowning4`
Description | <p>Voorbeeld avocado Hass: code 4 poster pulp browning.</p>
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### number pulp browning 5
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberPulpBrowning5`
Description | <p>Voorbeeld avocado Hass: code 5 poster pulp browning.</p>
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### number rotten flowers
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberRottenFlowers`
Description | <p>Aantal rotte bloemen.</p>
Super-classes |[om:NumberFlowers](http://opendata.caceres.es/def/ontomunicipio#NumberFlowers) (c)<br />
### aantal rotte bladeren
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberRottenLeaves`
Description | <p>Aantal rotte bladeren.</p>
Super-classes |[om:NumberLeaves](http://opendata.caceres.es/def/ontomunicipio#NumberLeaves) (c)<br />
### number unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### number vascular browning
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberVascularBrowning`
Super-classes |[om:Number](http://opendata.caceres.es/def/ontomunicipio#Number) (c)<br />
### number vascular browning 1
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberVascularBrowning1`
Description | <p>Voorbeeld avocado Hass: code 1 poster vascular browning.</p>
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### number vascular browning 2
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberVascularBrowning2`
Description | <p>Voorbeeld avocado Hass: code 2 poster vascular browning.</p>
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### number vascular browning 3
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberVascularBrowning3`
Description | <p>Voorbeeld avocado Hass: code 3 poster vascular browning.</p>
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### number vascular browning 4
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberVascularBrowning4`
Description | <p>Voorbeeld avocado Hass: code 4 poster vascular browning.</p>
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### number vascular browning 5
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberVascularBrowning5`
Description | <p>Voorbeeld avocado Hass: code 5 poster vascular browning.</p>
Super-classes |[om:NumberColor](http://opendata.caceres.es/def/ontomunicipio#NumberColor) (c)<br />
### aantal verwelkte bloemen
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberWiltedFlowers`
Description | <p>Aantal verwelkte bloemen.</p>
Super-classes |[om:NumberFlowers](http://opendata.caceres.es/def/ontomunicipio#NumberFlowers) (c)<br />
### aantal verwelkte bladeren
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberWiltedLeaves`
Description | <p>Aantal verwelkte bladeren.</p>
Super-classes |[om:NumberLeaves](http://opendata.caceres.es/def/ontomunicipio#NumberLeaves) (c)<br />
### aantal vergeelde bladeren
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NumberYellowLeaves`
Description | <p>Aantal yellow bladeren.</p>
Super-classes |[om:NumberLeaves](http://opendata.caceres.es/def/ontomunicipio#NumberLeaves) (c)<br />
### Nusselt number
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NusseltNumber`
Description | <p>The Nusselt number is the ratio of convective to conductive heat transfer across (normal to) the boundary.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
### Nusselt number for mass transfer
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NusseltNumberForMassTransfer`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
### Nusselt number for mass transfer unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NusseltNumberForMassTransferUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### Nusselt number unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#NusseltNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### organ dose equivalent
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#OrganDoseEquivalent`
Super-classes |[om:DoseEquivalent](http://opendata.caceres.es/def/ontomunicipio#DoseEquivalent) (c)<br />
### overrun
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Overrun`
Super-classes |[om:VolumeFraction](http://opendata.caceres.es/def/ontomunicipio#VolumeFraction) (c)<br />
### peak wavelength
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PeakWavelength`
Description | <p>Wavelength for which the detectivity is at a maximum.</p>
Super-classes |[om:Wavelength](http://opendata.caceres.es/def/ontomunicipio#Wavelength) (c)<br />
### Péclet number
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PecletNumber`
Description | <p>The Péclet number is a dimensionless number that relates the rate of advection of a flow to its rate of diffusion, often thermal diffusion.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### Péclet number for mass transfer
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PecletNumberForMassTransfer`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### Péclet number for mass transfer unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PecletNumberForMassTransferUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### Péclet number unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PecletNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### percentage
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Percentage`
Super-classes |[om:Ratio](http://opendata.caceres.es/def/ontomunicipio#Ratio) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### percentage unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PercentageUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### period
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Period`
Super-classes |[om:Time](http://opendata.caceres.es/def/ontomunicipio#Time) (c)<br />
### period of variability
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PeriodOfVariability`
Description | <p>The duration of one cycle in a (semi) periodical star.</p>
Super-classes |[om:Time](http://opendata.caceres.es/def/ontomunicipio#Time) (c)<br />
### permeability (earth science)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Permeability-EarthScience`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:area-Dimension](http://opendata.caceres.es/def/ontomunicipio#area-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### permeability (earth science) unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Permeability-EarthScienceUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### permeability of free space
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PermeabilityOfFreeSpace`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:permeabilityOfFreeSpace-Dimension](http://opendata.caceres.es/def/ontomunicipio#permeabilityOfFreeSpace-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### permeability of free space unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PermeabilityOfFreeSpaceUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### permeance (electromagnetic)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Permeance-Electromagnetic`
Description | <p>Electromagnetic permeance is a measure of flux for a number of current-turns in magnetic circuit.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:inductanceOrPermeance-Electromagnetic-Dimension](http://opendata.caceres.es/def/ontomunicipio#inductanceOrPermeance-Electromagnetic-Dimension) (c)<br />
### permeance (electromagnetic) unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Permeance-ElectromagneticUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### permeance (materials science)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Permeance-MaterialsScience`
Description | <p>Permeance is the degree to which a material transmits another substance.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:permeance-MaterialsScience-Dimension](http://opendata.caceres.es/def/ontomunicipio#permeance-MaterialsScience-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### permeance (materials science) unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Permeance-MaterialsScienceUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### permittivity
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Permittivity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:permittivity-Dimension](http://opendata.caceres.es/def/ontomunicipio#permittivity-Dimension) (c)<br />
### permittivity unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PermittivityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### personal dose equivalent
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PersonalDoseEquivalent`
Super-classes |[om:DoseEquivalent](http://opendata.caceres.es/def/ontomunicipio#DoseEquivalent) (c)<br />
### photographic amplitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PhotographicAmplitude`
Description | <p>Amplitude of the light variation in photographic magnitude.</p>
Super-classes |[om:Amplitude](http://opendata.caceres.es/def/ontomunicipio#Amplitude) (c)<br />
### photographic magnitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PhotographicMagnitude`
Super-classes |[om:Magnitude](http://opendata.caceres.es/def/ontomunicipio#Magnitude) (c)<br />
Sub-classes |[om:PhotographicMagnitudeAtMaximumBrightness](http://opendata.caceres.es/def/ontomunicipio#PhotographicMagnitudeAtMaximumBrightness) (c)<br />[om:PhotographicMagnitudeAtMinimumBrightness](http://opendata.caceres.es/def/ontomunicipio#PhotographicMagnitudeAtMinimumBrightness) (c)<br />
### photographic magnitude at maximum brightness
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PhotographicMagnitudeAtMaximumBrightness`
Super-classes |[om:MagnitudeAtMaximumBrightness](http://opendata.caceres.es/def/ontomunicipio#MagnitudeAtMaximumBrightness) (c)<br />[om:PhotographicMagnitude](http://opendata.caceres.es/def/ontomunicipio#PhotographicMagnitude) (c)<br />
### photographic magnitude at minimum brightness
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PhotographicMagnitudeAtMinimumBrightness`
Super-classes |[om:MagnitudeAtMinimumBrightness](http://opendata.caceres.es/def/ontomunicipio#MagnitudeAtMinimumBrightness) (c)<br />[om:PhotographicMagnitude](http://opendata.caceres.es/def/ontomunicipio#PhotographicMagnitude) (c)<br />
### planetary aberration
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PlanetaryAberration`
Description | <p>The apparent angular displacement of the observed position of a celestial object produced by the motion of the observer and the actual motion of the observed object.</p>
Super-classes |[om:Aberration](http://opendata.caceres.es/def/ontomunicipio#Aberration) (c)<br />
### point
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Point`
Description | <p>A point is an element of an interval scale or a ratio scale, for example, 273.16 on the Kelvin scale indicates the triple point of water thermodynamic temperature.</p>
Sub-classes |[om:FixedPoint](http://opendata.caceres.es/def/ontomunicipio#FixedPoint) (c)<br />
In range of |[om:hasPoint](http://opendata.caceres.es/def/ontomunicipio#hasPoint) (op)<br />
### potassium sorbate mass fraction
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PotassiumSorbateMassFraction`
Description | <p>The fraction of the mass of potassium sorbate in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### potential difference
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PotentialDifference`
Super-classes |[om:ElectricPotential](http://opendata.caceres.es/def/ontomunicipio#ElectricPotential) (c)<br />
### potentiële energie
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PotentialEnergy`
Description | <p>Potential energy is energy due to position of one body with respect to another or to the relative parts of the same body.</p>
Super-classes |[om:Energy](http://opendata.caceres.es/def/ontomunicipio#Energy) (c)<br />
### 功率
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Power`
Description | <p>Power is the time rate at which work is done. It is a derived quantity in the International System of Units. Power is energy divided by time.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:power-Dimension](http://opendata.caceres.es/def/ontomunicipio#power-Dimension) (c)<br />
Sub-classes |[om:NoiseEquivalentPower](http://opendata.caceres.es/def/ontomunicipio#NoiseEquivalentPower) (c)<br />[om:HeatFlowRate](http://opendata.caceres.es/def/ontomunicipio#HeatFlowRate) (c)<br />[om:RadiantFlux](http://opendata.caceres.es/def/ontomunicipio#RadiantFlux) (c)<br />
### power density
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PowerDensity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:powerDensity-Dimension](http://opendata.caceres.es/def/ontomunicipio#powerDensity-Dimension) (c)<br />
Sub-classes |[om:HeatFluxDensity](http://opendata.caceres.es/def/ontomunicipio#HeatFluxDensity) (c)<br />[om:Irradiance](http://opendata.caceres.es/def/ontomunicipio#Irradiance) (c)<br />
### power density unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PowerDensityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### power unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PowerUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### getal van Prandtl
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrandtlNumber`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
### Prandtl number unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrandtlNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### prefix
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Prefix`
Description | <p>A prefix is a name that precedes a basic unit of measure to indicate a decimal or binary multiple or fraction of the unit. Each prefix has a unique symbol that is prepended to the unit symbol. For example, an electric current of 0.000 000 001 ampere is written by using the SI-prefix nano as 1 nanoampere or 1 nA.</p>
Sub-classes |[om:BinaryPrefix](http://opendata.caceres.es/def/ontomunicipio#BinaryPrefix) (c)<br />[om:SIPrefix](http://opendata.caceres.es/def/ontomunicipio#SIPrefix) (c)<br />
In range of |[om:hasPrefix](http://opendata.caceres.es/def/ontomunicipio#hasPrefix) (op)<br />
### prefixed ampere
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedAmpere`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed are
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedAre`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed becquerel
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedBecquerel`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed bit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedBit`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed byte
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedByte`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed calorie (mean)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedCalorie-Mean`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed candela
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedCandela`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed coulomb
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedCoulomb`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed degree Celsius
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedDegreeCelsius`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed electronvolt
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedElectronvolt`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed farad
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedFarad`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed gram
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedGram`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed gram per litre
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedGramPerLitre`
Super-classes |[om:UnitDivision](http://opendata.caceres.es/def/ontomunicipio#UnitDivision) (c)<br />
### prefixed gram per prefixed litre
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedGramPerPrefixedLitre`
Super-classes |[om:UnitDivision](http://opendata.caceres.es/def/ontomunicipio#UnitDivision) (c)<br />
### prefixed gray
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedGray`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed henry
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedHenry`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed hertz
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedHertz`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed joule
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedJoule`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed katal
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedKatal`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed kelvin
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedKelvin`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed litre
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedLitre`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed lumen
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedLumen`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed lux
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedLux`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed metre
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedMetre`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed metre per prefixed second (time)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedMetrePerPrefixedSecond-Time`
Super-classes |[om:UnitDivision](http://opendata.caceres.es/def/ontomunicipio#UnitDivision) (c)<br />
### prefixed metre per prefixed secon (time) squared
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedMetrePerPrefixedSecond-TimeSquared`
Super-classes |[om:UnitDivision](http://opendata.caceres.es/def/ontomunicipio#UnitDivision) (c)<br />
### prefixed metre per second (time)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedMetrePerSecond-Time`
Super-classes |[om:UnitDivision](http://opendata.caceres.es/def/ontomunicipio#UnitDivision) (c)<br />
### prefixed metre per second (time) squared
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedMetrePerSecond-TimeSquared`
Super-classes |[om:UnitDivision](http://opendata.caceres.es/def/ontomunicipio#UnitDivision) (c)<br />
### prefixed metre prefixed gram
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedMetrePrefixedGram`
Super-classes |[om:UnitMultiplication](http://opendata.caceres.es/def/ontomunicipio#UnitMultiplication) (c)<br />
### prefixed molair
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedMolair`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed mole
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedMole`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed mole per litre
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedMolePerLitre`
Super-classes |[om:UnitDivision](http://opendata.caceres.es/def/ontomunicipio#UnitDivision) (c)<br />
### prefixed mole per metre
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedMolePerMetre`
Super-classes |[om:UnitDivision](http://opendata.caceres.es/def/ontomunicipio#UnitDivision) (c)<br />
### prefixed mole per prefixed litre
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedMolePerPrefixedLitre`
Super-classes |[om:UnitDivision](http://opendata.caceres.es/def/ontomunicipio#UnitDivision) (c)<br />
### prefixed mole per prefixed metre
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedMolePerPrefixedMetre`
Super-classes |[om:UnitDivision](http://opendata.caceres.es/def/ontomunicipio#UnitDivision) (c)<br />
### prefixed newton
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedNewton`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed ohm
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedOhm`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed pascal
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedPascal`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed poise
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedPoise`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed radian
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedRadian`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed second (time)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedSecond-Time`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed second (time) squared
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedSecond-TimeSquared`
Super-classes |[om:UnitExponentiation](http://opendata.caceres.es/def/ontomunicipio#UnitExponentiation) (c)<br />
### prefixed siemens
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedSiemens`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed sievert
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedSievert`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed steradian
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedSteradian`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed stokes
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedStokes`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed tesla
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedTesla`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed tonne
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedTonne`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed unified atomic mass unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedUnifiedAtomicMassUnit`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
Restrictions |[om:hasUnit](http://opendata.caceres.es/def/ontomunicipio#hasUnit) (op) **only** [om:SingularUnit](http://opendata.caceres.es/def/ontomunicipio#SingularUnit) (c)<br />
Sub-classes |[om:PrefixedMolair](http://opendata.caceres.es/def/ontomunicipio#PrefixedMolair) (c)<br />[om:PrefixedCandela](http://opendata.caceres.es/def/ontomunicipio#PrefixedCandela) (c)<br />[om:PrefixedSiemens](http://opendata.caceres.es/def/ontomunicipio#PrefixedSiemens) (c)<br />[om:PrefixedUnifiedAtomicMassUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnifiedAtomicMassUnit) (c)<br />[om:PrefixedFarad](http://opendata.caceres.es/def/ontomunicipio#PrefixedFarad) (c)<br />[om:PrefixedCoulomb](http://opendata.caceres.es/def/ontomunicipio#PrefixedCoulomb) (c)<br />[om:PrefixedRadian](http://opendata.caceres.es/def/ontomunicipio#PrefixedRadian) (c)<br />[om:PrefixedMetre](http://opendata.caceres.es/def/ontomunicipio#PrefixedMetre) (c)<br />[om:PrefixedKatal](http://opendata.caceres.es/def/ontomunicipio#PrefixedKatal) (c)<br />[om:PrefixedElectronvolt](http://opendata.caceres.es/def/ontomunicipio#PrefixedElectronvolt) (c)<br />[om:PrefixedSecond-Time](http://opendata.caceres.es/def/ontomunicipio#PrefixedSecond-Time) (c)<br />[om:PrefixedWeber](http://opendata.caceres.es/def/ontomunicipio#PrefixedWeber) (c)<br />[om:PrefixedMole](http://opendata.caceres.es/def/ontomunicipio#PrefixedMole) (c)<br />[om:PrefixedSievert](http://opendata.caceres.es/def/ontomunicipio#PrefixedSievert) (c)<br />[om:PrefixedTesla](http://opendata.caceres.es/def/ontomunicipio#PrefixedTesla) (c)<br />[om:PrefixedHertz](http://opendata.caceres.es/def/ontomunicipio#PrefixedHertz) (c)<br />[om:PrefixedLitre](http://opendata.caceres.es/def/ontomunicipio#PrefixedLitre) (c)<br />[om:PrefixedGray](http://opendata.caceres.es/def/ontomunicipio#PrefixedGray) (c)<br />[om:PrefixedVolt](http://opendata.caceres.es/def/ontomunicipio#PrefixedVolt) (c)<br />[om:PrefixedAmpere](http://opendata.caceres.es/def/ontomunicipio#PrefixedAmpere) (c)<br />[om:PrefixedBecquerel](http://opendata.caceres.es/def/ontomunicipio#PrefixedBecquerel) (c)<br />[om:PrefixedPascal](http://opendata.caceres.es/def/ontomunicipio#PrefixedPascal) (c)<br />[om:PrefixedLumen](http://opendata.caceres.es/def/ontomunicipio#PrefixedLumen) (c)<br />[om:PrefixedJoule](http://opendata.caceres.es/def/ontomunicipio#PrefixedJoule) (c)<br />[om:PrefixedByte](http://opendata.caceres.es/def/ontomunicipio#PrefixedByte) (c)<br />[om:PrefixedStokes](http://opendata.caceres.es/def/ontomunicipio#PrefixedStokes) (c)<br />[om:PrefixedTonne](http://opendata.caceres.es/def/ontomunicipio#PrefixedTonne) (c)<br />[om:PrefixedCalorie-Mean](http://opendata.caceres.es/def/ontomunicipio#PrefixedCalorie-Mean) (c)<br />[om:PrefixedKelvin](http://opendata.caceres.es/def/ontomunicipio#PrefixedKelvin) (c)<br />[om:PrefixedDegreeCelsius](http://opendata.caceres.es/def/ontomunicipio#PrefixedDegreeCelsius) (c)<br />[om:PrefixedHenry](http://opendata.caceres.es/def/ontomunicipio#PrefixedHenry) (c)<br />[om:PrefixedNewton](http://opendata.caceres.es/def/ontomunicipio#PrefixedNewton) (c)<br />[om:PrefixedAre](http://opendata.caceres.es/def/ontomunicipio#PrefixedAre) (c)<br />[om:PrefixedWatt](http://opendata.caceres.es/def/ontomunicipio#PrefixedWatt) (c)<br />[om:PrefixedBit](http://opendata.caceres.es/def/ontomunicipio#PrefixedBit) (c)<br />[om:PrefixedLux](http://opendata.caceres.es/def/ontomunicipio#PrefixedLux) (c)<br />[om:PrefixedOhm](http://opendata.caceres.es/def/ontomunicipio#PrefixedOhm) (c)<br />[om:PrefixedGram](http://opendata.caceres.es/def/ontomunicipio#PrefixedGram) (c)<br />[om:PrefixedPoise](http://opendata.caceres.es/def/ontomunicipio#PrefixedPoise) (c)<br />[om:PrefixedSteradian](http://opendata.caceres.es/def/ontomunicipio#PrefixedSteradian) (c)<br />
In domain of |[om:hasPrefix](http://opendata.caceres.es/def/ontomunicipio#hasPrefix) (op)<br />
### prefixed volt
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedVolt`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed watt
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedWatt`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### prefixed weber
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PrefixedWeber`
Super-classes |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
### druk
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Pressure`
Description | <p>Pressure is the force applied to or distributed over a surface. It is a derived quantity in the International System of Units. Pressure is force divided by area.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:pressure-Dimension](http://opendata.caceres.es/def/ontomunicipio#pressure-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### pressure unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PressureUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### protein mass fraction
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ProteinMassFraction`
Description | <p>The fraction of the mass of protein in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### pulp browning
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#PulpBrowning`
Description | <p>Voorbeeld avocado Hass: poster (code).</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### quality mark
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#QualityMark`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Sub-classes |[om:QualityMarkLeaf](http://opendata.caceres.es/def/ontomunicipio#QualityMarkLeaf) (c)<br />[om:QualityMarkTotal](http://opendata.caceres.es/def/ontomunicipio#QualityMarkTotal) (c)<br />[om:QualityMarkFlower](http://opendata.caceres.es/def/ontomunicipio#QualityMarkFlower) (c)<br />
### kwaliteitscijfer bloem(en)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#QualityMarkFlower`
Super-classes |[om:QualityMark](http://opendata.caceres.es/def/ontomunicipio#QualityMark) (c)<br />
### quality mark leafs
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#QualityMarkLeaf`
Super-classes |[om:QualityMark](http://opendata.caceres.es/def/ontomunicipio#QualityMark) (c)<br />
### kwaliteitscijfer total
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#QualityMarkTotal`
Super-classes |[om:QualityMark](http://opendata.caceres.es/def/ontomunicipio#QualityMark) (c)<br />
### quantity
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Quantity`
Description | <p>A quantity is a representation of a quantifiable (standardised) aspect (such as length, mass, and time) of a phenomenon (e.g., a star, a molecule, or a food product). Quantities are classified according to similarity in their (implicit) metrological aspect, e.g. the length of my table and the length of my chair are both classified as length.</p>
Sub-classes |[om:ElectricalResistivity](http://opendata.caceres.es/def/ontomunicipio#ElectricalResistivity) (c)<br />[om:ElectricDipoleMoment](http://opendata.caceres.es/def/ontomunicipio#ElectricDipoleMoment) (c)<br />[om:Impulse](http://opendata.caceres.es/def/ontomunicipio#Impulse) (c)<br />[om:Momentum](http://opendata.caceres.es/def/ontomunicipio#Momentum) (c)<br />[om:Hydrophobicity](http://opendata.caceres.es/def/ontomunicipio#Hydrophobicity) (c)<br />[om:SchmidtNumber](http://opendata.caceres.es/def/ontomunicipio#SchmidtNumber) (c)<br />[om:Action](http://opendata.caceres.es/def/ontomunicipio#Action) (c)<br />[om:Area](http://opendata.caceres.es/def/ontomunicipio#Area) (c)<br />[om:Reddening](http://opendata.caceres.es/def/ontomunicipio#Reddening) (c)<br />[om:SymbolRate](http://opendata.caceres.es/def/ontomunicipio#SymbolRate) (c)<br />[om:Exposure](http://opendata.caceres.es/def/ontomunicipio#Exposure) (c)<br />[om:Number](http://opendata.caceres.es/def/ontomunicipio#Number) (c)<br />[om:CosmologicalConstant](http://opendata.caceres.es/def/ontomunicipio#CosmologicalConstant) (c)<br />[om:CauseEndOfVaseLifeAbscisedLeaves](http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeAbscisedLeaves) (c)<br />[om:ExternalBrowning](http://opendata.caceres.es/def/ontomunicipio#ExternalBrowning) (c)<br />[om:MagneticFluxDensity](http://opendata.caceres.es/def/ontomunicipio#MagneticFluxDensity) (c)<br />[om:PulpBrowning](http://opendata.caceres.es/def/ontomunicipio#PulpBrowning) (c)<br />[om:CauseEndOfVaseLifeNonturgidFlowers](http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeNonturgidFlowers) (c)<br />[om:AreaDensity](http://opendata.caceres.es/def/ontomunicipio#AreaDensity) (c)<br />[om:MagneticField](http://opendata.caceres.es/def/ontomunicipio#MagneticField) (c)<br />[om:Molality](http://opendata.caceres.es/def/ontomunicipio#Molality) (c)<br />[om:ElectricChargeDensity](http://opendata.caceres.es/def/ontomunicipio#ElectricChargeDensity) (c)<br />[om:MagneticReynoldsNumber](http://opendata.caceres.es/def/ontomunicipio#MagneticReynoldsNumber) (c)<br />[om:PrandtlNumber](http://opendata.caceres.es/def/ontomunicipio#PrandtlNumber) (c)<br />[om:CauseEndOfVaseLifeWiltedLeaves](http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeWiltedLeaves) (c)<br />[om:MolarEntropy](http://opendata.caceres.es/def/ontomunicipio#MolarEntropy) (c)<br />[om:Extinction](http://opendata.caceres.es/def/ontomunicipio#Extinction) (c)<br />[om:HartmannNumber](http://opendata.caceres.es/def/ontomunicipio#HartmannNumber) (c)<br />[om:SpectralResponse](http://opendata.caceres.es/def/ontomunicipio#SpectralResponse) (c)<br />[om:VolumetricViableCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCount) (c)<br />[om:SpecificViableCount](http://opendata.caceres.es/def/ontomunicipio#SpecificViableCount) (c)<br />[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />[om:CauseEndOfVaseLifeWiltedFlowers](http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeWiltedFlowers) (c)<br />[om:DarkNoise](http://opendata.caceres.es/def/ontomunicipio#DarkNoise) (c)<br />[om:PowerDensity](http://opendata.caceres.es/def/ontomunicipio#PowerDensity) (c)<br />[om:PecletNumber](http://opendata.caceres.es/def/ontomunicipio#PecletNumber) (c)<br />[om:SpecificHeatCapacity](http://opendata.caceres.es/def/ontomunicipio#SpecificHeatCapacity) (c)<br />[om:ElectricField](http://opendata.caceres.es/def/ontomunicipio#ElectricField) (c)<br />[om:LuminousEfficacy](http://opendata.caceres.es/def/ontomunicipio#LuminousEfficacy) (c)<br />[om:GasConstant](http://opendata.caceres.es/def/ontomunicipio#GasConstant) (c)<br />[om:GrashofNumberForMassTransfer](http://opendata.caceres.es/def/ontomunicipio#GrashofNumberForMassTransfer) (c)<br />[om:Activity](http://opendata.caceres.es/def/ontomunicipio#Activity) (c)<br />[om:ElectricCurrent](http://opendata.caceres.es/def/ontomunicipio#ElectricCurrent) (c)<br />[om:Radiance](http://opendata.caceres.es/def/ontomunicipio#Radiance) (c)<br />[om:Ratio](http://opendata.caceres.es/def/ontomunicipio#Ratio) (c)<br />[om:Permittivity](http://opendata.caceres.es/def/ontomunicipio#Permittivity) (c)<br />[om:AmountOfSubstanceFlow](http://opendata.caceres.es/def/ontomunicipio#AmountOfSubstanceFlow) (c)<br />[om:ColumnNumberDensity](http://opendata.caceres.es/def/ontomunicipio#ColumnNumberDensity) (c)<br />[om:ElectricFluxDensity](http://opendata.caceres.es/def/ontomunicipio#ElectricFluxDensity) (c)<br />[om:Admittance](http://opendata.caceres.es/def/ontomunicipio#Admittance) (c)<br />[om:DynamicViscosity](http://opendata.caceres.es/def/ontomunicipio#DynamicViscosity) (c)<br />[om:SolidAngle](http://opendata.caceres.es/def/ontomunicipio#SolidAngle) (c)<br />[om:StemEndRot](http://opendata.caceres.es/def/ontomunicipio#StemEndRot) (c)<br />[om:Reluctance](http://opendata.caceres.es/def/ontomunicipio#Reluctance) (c)<br />[om:MolarMass](http://opendata.caceres.es/def/ontomunicipio#MolarMass) (c)<br />[om:RadiantIntensity](http://opendata.caceres.es/def/ontomunicipio#RadiantIntensity) (c)<br />[om:HubbleConstant](http://opendata.caceres.es/def/ontomunicipio#HubbleConstant) (c)<br />[om:LuminousIntensity](http://opendata.caceres.es/def/ontomunicipio#LuminousIntensity) (c)<br />[om:GrashofNumber](http://opendata.caceres.es/def/ontomunicipio#GrashofNumber) (c)<br />[om:CauseEndOfVaseLifeMalformedBuds](http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeMalformedBuds) (c)<br />[om:Wavenumber](http://opendata.caceres.es/def/ontomunicipio#Wavenumber) (c)<br />[om:AmountOfSubstanceConcentration](http://opendata.caceres.es/def/ontomunicipio#AmountOfSubstanceConcentration) (c)<br />[om:BolometricCorrection](http://opendata.caceres.es/def/ontomunicipio#BolometricCorrection) (c)<br />[om:AngularAcceleration](http://opendata.caceres.es/def/ontomunicipio#AngularAcceleration) (c)<br />[om:ElectricPotential](http://opendata.caceres.es/def/ontomunicipio#ElectricPotential) (c)<br />[om:Energy](http://opendata.caceres.es/def/ontomunicipio#Energy) (c)<br />[om:Amplitude](http://opendata.caceres.es/def/ontomunicipio#Amplitude) (c)<br />[om:PermeabilityOfFreeSpace](http://opendata.caceres.es/def/ontomunicipio#PermeabilityOfFreeSpace) (c)<br />[om:EnergyDensity](http://opendata.caceres.es/def/ontomunicipio#EnergyDensity) (c)<br />[om:CauseEndOfVaseLifeMalformedFlowers](http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeMalformedFlowers) (c)<br />[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />[om:ThermalConductivity](http://opendata.caceres.es/def/ontomunicipio#ThermalConductivity) (c)<br />[om:NumberDensity](http://opendata.caceres.es/def/ontomunicipio#NumberDensity) (c)<br />[om:SpecificEnergy](http://opendata.caceres.es/def/ontomunicipio#SpecificEnergy) (c)<br />[om:CauseEndOfVaseLifeDryBuds](http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeDryBuds) (c)<br />[om:DensityParameter](http://opendata.caceres.es/def/ontomunicipio#DensityParameter) (c)<br />[om:Capacitance](http://opendata.caceres.es/def/ontomunicipio#Capacitance) (c)<br />[om:EulerNumber](http://opendata.caceres.es/def/ontomunicipio#EulerNumber) (c)<br />[om:Entropy](http://opendata.caceres.es/def/ontomunicipio#Entropy) (c)<br />[om:MagneticFlux](http://opendata.caceres.es/def/ontomunicipio#MagneticFlux) (c)<br />[om:VolumetricFlowRate](http://opendata.caceres.es/def/ontomunicipio#VolumetricFlowRate) (c)<br />[om:Mass](http://opendata.caceres.es/def/ontomunicipio#Mass) (c)<br />[om:RayleighNumber](http://opendata.caceres.es/def/ontomunicipio#RayleighNumber) (c)<br />[om:NormalisedDetectivity](http://opendata.caceres.es/def/ontomunicipio#NormalisedDetectivity) (c)<br />[om:ReynoldsNumber](http://opendata.caceres.es/def/ontomunicipio#ReynoldsNumber) (c)<br />[om:AcousticFirmness](http://opendata.caceres.es/def/ontomunicipio#AcousticFirmness) (c)<br />[om:NusseltNumberForMassTransfer](http://opendata.caceres.es/def/ontomunicipio#NusseltNumberForMassTransfer) (c)<br />[om:Torque](http://opendata.caceres.es/def/ontomunicipio#Torque) (c)<br />[om:ElectricCharge](http://opendata.caceres.es/def/ontomunicipio#ElectricCharge) (c)<br />[om:AlfvenNumber](http://opendata.caceres.es/def/ontomunicipio#AlfvenNumber) (c)<br />[om:VolumeFraction](http://opendata.caceres.es/def/ontomunicipio#VolumeFraction) (c)<br />[om:MachNumber](http://opendata.caceres.es/def/ontomunicipio#MachNumber) (c)<br />[om:HeatCapacity](http://opendata.caceres.es/def/ontomunicipio#HeatCapacity) (c)<br />[om:AmountOfSubstanceFractionFlow](http://opendata.caceres.es/def/ontomunicipio#AmountOfSubstanceFractionFlow) (c)<br />[om:FourierNumber](http://opendata.caceres.es/def/ontomunicipio#FourierNumber) (c)<br />[om:Acidity](http://opendata.caceres.es/def/ontomunicipio#Acidity) (c)<br />[om:BudStadium](http://opendata.caceres.es/def/ontomunicipio#BudStadium) (c)<br />[om:Detectivity](http://opendata.caceres.es/def/ontomunicipio#Detectivity) (c)<br />[om:AreaDensityRate](http://opendata.caceres.es/def/ontomunicipio#AreaDensityRate) (c)<br />[om:StantonNumberForMassTransfer](http://opendata.caceres.es/def/ontomunicipio#StantonNumberForMassTransfer) (c)<br />[om:StantonNumber](http://opendata.caceres.es/def/ontomunicipio#StantonNumber) (c)<br />[om:Force](http://opendata.caceres.es/def/ontomunicipio#Force) (c)<br />[om:Pressure](http://opendata.caceres.es/def/ontomunicipio#Pressure) (c)<br />[om:Speed](http://opendata.caceres.es/def/ontomunicipio#Speed) (c)<br />[om:Length](http://opendata.caceres.es/def/ontomunicipio#Length) (c)<br />[om:LewisNumber](http://opendata.caceres.es/def/ontomunicipio#LewisNumber) (c)<br />[om:FourierNumberForMassTransfer](http://opendata.caceres.es/def/ontomunicipio#FourierNumberForMassTransfer) (c)<br />[om:NusseltNumber](http://opendata.caceres.es/def/ontomunicipio#NusseltNumber) (c)<br />[om:QuantityOfDimensionOne](http://opendata.caceres.es/def/ontomunicipio#QuantityOfDimensionOne) (c)<br />[om:Firmness-Penetrometer-Method1](http://opendata.caceres.es/def/ontomunicipio#Firmness-Penetrometer-Method1) (c)<br />[om:Fluidity](http://opendata.caceres.es/def/ontomunicipio#Fluidity) (c)<br />[om:InformationCapacity](http://opendata.caceres.es/def/ontomunicipio#InformationCapacity) (c)<br />[om:MolarHeatCapacity](http://opendata.caceres.es/def/ontomunicipio#MolarHeatCapacity) (c)<br />[om:FirstCowlingNumber](http://opendata.caceres.es/def/ontomunicipio#FirstCowlingNumber) (c)<br />[om:Illuminance](http://opendata.caceres.es/def/ontomunicipio#Illuminance) (c)<br />[om:ThermalDiffusivity](http://opendata.caceres.es/def/ontomunicipio#ThermalDiffusivity) (c)<br />[om:Permeance-Electromagnetic](http://opendata.caceres.es/def/ontomunicipio#Permeance-Electromagnetic) (c)<br />[om:AbsorbedDoseRate](http://opendata.caceres.es/def/ontomunicipio#AbsorbedDoseRate) (c)<br />[om:Frequency](http://opendata.caceres.es/def/ontomunicipio#Frequency) (c)<br />[om:Acceleration](http://opendata.caceres.es/def/ontomunicipio#Acceleration) (c)<br />[om:CauseEndOfVaseLifeDryFlowers](http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeDryFlowers) (c)<br />[om:DynamicModulus](http://opendata.caceres.es/def/ontomunicipio#DynamicModulus) (c)<br />[om:ManualFirmness](http://opendata.caceres.es/def/ontomunicipio#ManualFirmness) (c)<br />[om:SurfaceTension](http://opendata.caceres.es/def/ontomunicipio#SurfaceTension) (c)<br />[om:PecletNumberForMassTransfer](http://opendata.caceres.es/def/ontomunicipio#PecletNumberForMassTransfer) (c)<br />[om:LuminousEnergy](http://opendata.caceres.es/def/ontomunicipio#LuminousEnergy) (c)<br />[om:QualityMark](http://opendata.caceres.es/def/ontomunicipio#QualityMark) (c)<br />[om:Temperature](http://opendata.caceres.es/def/ontomunicipio#Temperature) (c)<br />[om:Magnitude](http://opendata.caceres.es/def/ontomunicipio#Magnitude) (c)<br />[om:AmountOfSubstance](http://opendata.caceres.es/def/ontomunicipio#AmountOfSubstance) (c)<br />[om:Time](http://opendata.caceres.es/def/ontomunicipio#Time) (c)<br />[om:CauseEndOfVaseLifeYellowLeaves](http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeYellowLeaves) (c)<br />[om:CauseEndOfVaseLifeRottenFlowers](http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeRottenFlowers) (c)<br />[om:CauseEndOfVaseLifeNonturgidLeaves](http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeNonturgidLeaves) (c)<br />[om:MolarVolume](http://opendata.caceres.es/def/ontomunicipio#MolarVolume) (c)<br />[om:AreaFraction](http://opendata.caceres.es/def/ontomunicipio#AreaFraction) (c)<br />[om:CauseEndOfVaseLifeDryLeaves](http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeDryLeaves) (c)<br />[om:AngularMomentum](http://opendata.caceres.es/def/ontomunicipio#AngularMomentum) (c)<br />[om:MagnetomotiveForce](http://opendata.caceres.es/def/ontomunicipio#MagnetomotiveForce) (c)<br />[om:CauseEndOfVaseLifeBlueFlowers](http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeBlueFlowers) (c)<br />[om:VascularBrowning](http://opendata.caceres.es/def/ontomunicipio#VascularBrowning) (c)<br />[om:MassFlow](http://opendata.caceres.es/def/ontomunicipio#MassFlow) (c)<br />[om:FroudeNumber](http://opendata.caceres.es/def/ontomunicipio#FroudeNumber) (c)<br />[om:StrouhalNumber](http://opendata.caceres.es/def/ontomunicipio#StrouhalNumber) (c)<br />[om:Volume](http://opendata.caceres.es/def/ontomunicipio#Volume) (c)<br />[om:Strain](http://opendata.caceres.es/def/ontomunicipio#Strain) (c)<br />[om:HeatTransferCoefficient](http://opendata.caceres.es/def/ontomunicipio#HeatTransferCoefficient) (c)<br />[om:ShearRate](http://opendata.caceres.es/def/ontomunicipio#ShearRate) (c)<br />[om:Responsivity](http://opendata.caceres.es/def/ontomunicipio#Responsivity) (c)<br />[om:VolumetricHeatCapacity](http://opendata.caceres.es/def/ontomunicipio#VolumetricHeatCapacity) (c)<br />[om:CauseEndOfVaseLifeAbscisedBuds](http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeAbscisedBuds) (c)<br />[om:CatalyticActivityConcentration](http://opendata.caceres.es/def/ontomunicipio#CatalyticActivityConcentration) (c)<br />[om:CurrentDensity](http://opendata.caceres.es/def/ontomunicipio#CurrentDensity) (c)<br />[om:TemperatureRate](http://opendata.caceres.es/def/ontomunicipio#TemperatureRate) (c)<br />[om:LuminousFlux](http://opendata.caceres.es/def/ontomunicipio#LuminousFlux) (c)<br />[om:KinematicViscosity](http://opendata.caceres.es/def/ontomunicipio#KinematicViscosity) (c)<br />[om:RelativeHumidity](http://opendata.caceres.es/def/ontomunicipio#RelativeHumidity) (c)<br />[om:Firmness-Penetrometer-Method2](http://opendata.caceres.es/def/ontomunicipio#Firmness-Penetrometer-Method2) (c)<br />[om:Permeance-MaterialsScience](http://opendata.caceres.es/def/ontomunicipio#Permeance-MaterialsScience) (c)<br />[om:SpecificVolume](http://opendata.caceres.es/def/ontomunicipio#SpecificVolume) (c)<br />[om:SpecificEntropy](http://opendata.caceres.es/def/ontomunicipio#SpecificEntropy) (c)<br />[om:CauseEndOfVaseLifeBotrytis](http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeBotrytis) (c)<br />[om:ElectricalConductance](http://opendata.caceres.es/def/ontomunicipio#ElectricalConductance) (c)<br />[om:AmountOfMoney](http://opendata.caceres.es/def/ontomunicipio#AmountOfMoney) (c)<br />[om:MolarEnergy](http://opendata.caceres.es/def/ontomunicipio#MolarEnergy) (c)<br />[om:CauseEndOfVaseLifeAbscisedFlowers](http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeAbscisedFlowers) (c)<br />[om:ThermalInsulance](http://opendata.caceres.es/def/ontomunicipio#ThermalInsulance) (c)<br />[om:CurvatureConstant](http://opendata.caceres.es/def/ontomunicipio#CurvatureConstant) (c)<br />[om:ThermalResistance](http://opendata.caceres.es/def/ontomunicipio#ThermalResistance) (c)<br />[om:Amphiphilicity](http://opendata.caceres.es/def/ontomunicipio#Amphiphilicity) (c)<br />[om:AngularSpeed](http://opendata.caceres.es/def/ontomunicipio#AngularSpeed) (c)<br />[om:MomentOfForce](http://opendata.caceres.es/def/ontomunicipio#MomentOfForce) (c)<br />[om:Power](http://opendata.caceres.es/def/ontomunicipio#Power) (c)<br />[om:DoseEquivalent](http://opendata.caceres.es/def/ontomunicipio#DoseEquivalent) (c)<br />[om:SpecificCatalyticActivity](http://opendata.caceres.es/def/ontomunicipio#SpecificCatalyticActivity) (c)<br />[om:AmountOfSubstanceFraction](http://opendata.caceres.es/def/ontomunicipio#AmountOfSubstanceFraction) (c)<br />[om:DynamicRange](http://opendata.caceres.es/def/ontomunicipio#DynamicRange) (c)<br />[om:Permeability-EarthScience](http://opendata.caceres.es/def/ontomunicipio#Permeability-EarthScience) (c)<br />[om:ColourIndex](http://opendata.caceres.es/def/ontomunicipio#ColourIndex) (c)<br />[om:Lipophilicity](http://opendata.caceres.es/def/ontomunicipio#Lipophilicity) (c)<br />[om:WeberNumber](http://opendata.caceres.es/def/ontomunicipio#WeberNumber) (c)<br />[om:Density](http://opendata.caceres.es/def/ontomunicipio#Density) (c)<br />[om:QuantumEfficiency](http://opendata.caceres.es/def/ontomunicipio#QuantumEfficiency) (c)<br />[om:Stress](http://opendata.caceres.es/def/ontomunicipio#Stress) (c)<br />[om:ScaleFactor](http://opendata.caceres.es/def/ontomunicipio#ScaleFactor) (c)<br />[om:ElectricalResistance](http://opendata.caceres.es/def/ontomunicipio#ElectricalResistance) (c)<br />[om:Inductance](http://opendata.caceres.es/def/ontomunicipio#Inductance) (c)<br />[om:Hydrophilicity](http://opendata.caceres.es/def/ontomunicipio#Hydrophilicity) (c)<br />[om:CatalyticActivity](http://opendata.caceres.es/def/ontomunicipio#CatalyticActivity) (c)<br />[om:Luminance](http://opendata.caceres.es/def/ontomunicipio#Luminance) (c)<br />[om:StickStone](http://opendata.caceres.es/def/ontomunicipio#StickStone) (c)<br />[om:ElectricalConductivity](http://opendata.caceres.es/def/ontomunicipio#ElectricalConductivity) (c)<br />[om:DecelerationParameter](http://opendata.caceres.es/def/ontomunicipio#DecelerationParameter) (c)<br />[om:CauseEndOfVaseLifeRottenLeaves](http://opendata.caceres.es/def/ontomunicipio#CauseEndOfVaseLifeRottenLeaves) (c)<br />[om:ExposureToXAndGammaRays](http://opendata.caceres.es/def/ontomunicipio#ExposureToXAndGammaRays) (c)<br />[om:MomentOfInertia](http://opendata.caceres.es/def/ontomunicipio#MomentOfInertia) (c)<br />[om:SaltStrength](http://opendata.caceres.es/def/ontomunicipio#SaltStrength) (c)<br />[om:KnudsenNumber](http://opendata.caceres.es/def/ontomunicipio#KnudsenNumber) (c)<br />[om:CowlingNumber](http://opendata.caceres.es/def/ontomunicipio#CowlingNumber) (c)<br />[om:AbsorbedDose](http://opendata.caceres.es/def/ontomunicipio#AbsorbedDose) (c)<br />
In domain of |[om:hasContext](http://opendata.caceres.es/def/ontomunicipio#hasContext) (op)<br />[om:hasPhenomenon](http://opendata.caceres.es/def/ontomunicipio#hasPhenomenon) (op)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op)<br />[om:hasAggregateFunction](http://opendata.caceres.es/def/ontomunicipio#hasAggregateFunction) (op)<br />
In range of |[om:hasDerivedQuantity](http://opendata.caceres.es/def/ontomunicipio#hasDerivedQuantity) (op)<br />[om:hasQuantity](http://opendata.caceres.es/def/ontomunicipio#hasQuantity) (op)<br />[om:hasBaseQuantity](http://opendata.caceres.es/def/ontomunicipio#hasBaseQuantity) (op)<br />[om:usesQuantity](http://opendata.caceres.es/def/ontomunicipio#usesQuantity) (op)<br />
### quantity of dimension one
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#QuantityOfDimensionOne`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:Metallicity](http://opendata.caceres.es/def/ontomunicipio#Metallicity) (c)<br />[om:Ellipticity](http://opendata.caceres.es/def/ontomunicipio#Ellipticity) (c)<br />[om:Albedo](http://opendata.caceres.es/def/ontomunicipio#Albedo) (c)<br />[om:Eccentricity](http://opendata.caceres.es/def/ontomunicipio#Eccentricity) (c)<br />
### quantity of dimension one unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#QuantityOfDimensionOneUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### quantum efficiency
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#QuantumEfficiency`
Description | <p>Ratio (of a detector such as a CCD) of actual number of detected photons and the number of incident photons.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
Sub-classes |[om:DetectiveQuantumEfficiency](http://opendata.caceres.es/def/ontomunicipio#DetectiveQuantumEfficiency) (c)<br />
### quantum efficiency unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#QuantumEfficiencyUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### R magnitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#RMagnitude`
Description | <p>R magnitude in the Cousins photometric system.</p>
Super-classes |[om:CousinsMagnitude](http://opendata.caceres.es/def/ontomunicipio#CousinsMagnitude) (c)<br />
### radiance
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Radiance`
Description | <p>Radiance is a radiometric measure that describes the amount of light that passes through or is emitted from a particular area and falls within a given solid angle in a specified direction.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:radiance-Dimension](http://opendata.caceres.es/def/ontomunicipio#radiance-Dimension) (c)<br />
### radiance unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#RadianceUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### radiant energy
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#RadiantEnergy`
Super-classes |[om:Energy](http://opendata.caceres.es/def/ontomunicipio#Energy) (c)<br />
### radiant flux
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#RadiantFlux`
Description | <p>Radiant flux is the measure of the total power of electromagnetic radiation.</p>
Super-classes |[om:Power](http://opendata.caceres.es/def/ontomunicipio#Power) (c)<br />
### radiant intensity
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#RadiantIntensity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### radiant intensity unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#RadiantIntensityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### straal
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Radius`
Super-classes |[om:Length](http://opendata.caceres.es/def/ontomunicipio#Length) (c)<br />
Sub-classes |[om:Co-RotationRadius](http://opendata.caceres.es/def/ontomunicipio#Co-RotationRadius) (c)<br />
### radius (angle)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Radius-Angle`
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
### Rankinetemperatuur
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#RankineTemperature`
Super-classes |[om:Temperature](http://opendata.caceres.es/def/ontomunicipio#Temperature) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasScale](http://opendata.caceres.es/def/ontomunicipio#hasScale) (op) **value** [om:RankineScale](http://opendata.caceres.es/def/ontomunicipio#RankineScale) (c)<br />
### Rankine temperature scale
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#RankineTemperatureScale`
Super-classes |[om:Scale](http://opendata.caceres.es/def/ontomunicipio#Scale) (c)<br />
### Rankine temperature unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#RankineTemperatureUnit`
Super-classes |[om:TemperatureUnit](http://opendata.caceres.es/def/ontomunicipio#TemperatureUnit) (c)<br />
### ratio
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Ratio`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
Sub-classes |[om:Percentage](http://opendata.caceres.es/def/ontomunicipio#Percentage) (c)<br />
### ratio scale
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#RatioScale`
Super-classes |[om:Scale](http://opendata.caceres.es/def/ontomunicipio#Scale) (c)<br />
### ratio unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#RatioUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### Rayleigh number
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#RayleighNumber`
Description | <p>The Rayleigh number for a fluid is a dimensionless number associated with buoyancy driven flow.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
### Rayleigh number unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#RayleighNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### Réaumurtemperatuur
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ReaumurTemperature`
Super-classes |[om:Temperature](http://opendata.caceres.es/def/ontomunicipio#Temperature) (c)<br />
Restrictions |[om:hasScale](http://opendata.caceres.es/def/ontomunicipio#hasScale) (op) **value** [om:ReaumurScale](http://opendata.caceres.es/def/ontomunicipio#ReaumurScale) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### Réaumur temperature scale
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ReaumurTemperatureScale`
Super-classes |[om:Scale](http://opendata.caceres.es/def/ontomunicipio#Scale) (c)<br />
### Réaumur temperature unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ReaumurTemperatureUnit`
Super-classes |[om:TemperatureUnit](http://opendata.caceres.es/def/ontomunicipio#TemperatureUnit) (c)<br />
### red magnitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#RedMagnitude`
Description | <p>A red magnitude not specified for a specific photometric system.</p>
Super-classes |[om:Magnitude](http://opendata.caceres.es/def/ontomunicipio#Magnitude) (c)<br />
### reddening
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Reddening`
Description | <p>Reddening causes the star to appear redder if more dust or gas is between the star and the observer.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Sub-classes |[om:ReddeningB-V](http://opendata.caceres.es/def/ontomunicipio#ReddeningB-V) (c)<br />[om:ReddeningU-B](http://opendata.caceres.es/def/ontomunicipio#ReddeningU-B) (c)<br />
### reddening (B-V)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ReddeningB-V`
Description | <p>Reddening causes the star to appear redder if more dust or gas is between the star and the observer. The standard reddening is measured using the B and V passbands.</p>
Super-classes |[om:Reddening](http://opendata.caceres.es/def/ontomunicipio#Reddening) (c)<br />
### reddening (U-B)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ReddeningU-B`
Description | <p>Reddening measured with the U and B passbands.</p>
Super-classes |[om:Reddening](http://opendata.caceres.es/def/ontomunicipio#Reddening) (c)<br />
### relatieve luchtvochtigheid
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#RelativeHumidity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
### relative humidity unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#RelativeHumidityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### reluctance
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Reluctance`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:reluctance-Dimension](http://opendata.caceres.es/def/ontomunicipio#reluctance-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### reluctance unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ReluctanceUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### resonance energy
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ResonanceEnergy`
Super-classes |[om:MolarEnergy](http://opendata.caceres.es/def/ontomunicipio#MolarEnergy) (c)<br />
### responsivity
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Responsivity`
Description | <p>Detector output for unit intensity input. Units are usually volts per watt or amps per watt.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### responsivity unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ResponsivityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### getal van Reynolds
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ReynoldsNumber`
Description | <p>The Reynolds number is a dimensionless number that gives a measure of the ratio of inertial forces to viscous forces and, consequently, quantifies the relative importance of these two types of forces for given flow conditions.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
### Reynolds number unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ReynoldsNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### rechte klimming
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#RightAscension`
Description | <p>The angular distance on the celestial sphere measured eastward along the celestial equator from the equinox to the great circle passing through the celestial object and the celestial north pole.</p>
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
### SI prefix
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SIPrefix`
Super-classes |[om:Prefix](http://opendata.caceres.es/def/ontomunicipio#Prefix) (c)<br />
### salt mass fraction
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SaltMassFraction`
Description | <p>The fraction of the mass of salt in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### zoutsterkte
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SaltStrength`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### scale
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Scale`
Sub-classes |[om:IntervalScale](http://opendata.caceres.es/def/ontomunicipio#IntervalScale) (c)<br />[om:CelsiusTemperatureScale](http://opendata.caceres.es/def/ontomunicipio#CelsiusTemperatureScale) (c)<br />[om:ThermodynamicTemperatureScale](http://opendata.caceres.es/def/ontomunicipio#ThermodynamicTemperatureScale) (c)<br />[om:Temperature_scale](http://opendata.caceres.es/def/ontomunicipio#Temperature_scale) (c)<br />[om:RankineTemperatureScale](http://opendata.caceres.es/def/ontomunicipio#RankineTemperatureScale) (c)<br />[om:ReaumurTemperatureScale](http://opendata.caceres.es/def/ontomunicipio#ReaumurTemperatureScale) (c)<br />[om:RatioScale](http://opendata.caceres.es/def/ontomunicipio#RatioScale) (c)<br />[om:FahrenheitTemperatureScale](http://opendata.caceres.es/def/ontomunicipio#FahrenheitTemperatureScale) (c)<br />
In domain of |[om:hasOff-Set](http://opendata.caceres.es/def/ontomunicipio#hasOff-Set) (dp)<br />
In range of |[om:hasScale](http://opendata.caceres.es/def/ontomunicipio#hasScale) (op)<br />
### schaalfactor
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ScaleFactor`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### scale height
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ScaleHeight`
Description | <p>The scale height of a feature (such as the thin galactic disk) is the height (or position) at which the number density of the feature (for instance of the number of Population II stars) is equal to 1/e times the number density at the origin (for instance the Galactic Plane).</p>
Super-classes |[om:Length](http://opendata.caceres.es/def/ontomunicipio#Length) (c)<br />
### scale length
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ScaleLength`
Description | <p>The radial distance from a galaxy's core at which the average intensity has fallen to 1/e of the intensity at the centre of the galaxy.</p>
Super-classes |[om:Length](http://opendata.caceres.es/def/ontomunicipio#Length) (c)<br />
### Schmidt number
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SchmidtNumber`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
### Schmidt number unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SchmidtNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### secular aberration
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SecularAberration`
Description | <p>The component of the stellar abberation resulting from the motion of the solar system in space. This component is usually ignored. The abberation is the apparent angular displacement of the observed position of a celestial object from its geometric position, caused by the finite velocity of light in combination with the motions of the observer and of the observed object.</p>
Super-classes |[om:AngularDisplacement](http://opendata.caceres.es/def/ontomunicipio#AngularDisplacement) (c)<br />
### shear loss modulus
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ShearLossModulus`
Super-classes |[om:StorageModulus](http://opendata.caceres.es/def/ontomunicipio#StorageModulus) (c)<br />
### shear modulus
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ShearModulus`
Description | <p>Shear modulus is the ratio of shear stress to shear strain.</p>
Super-classes |[om:DynamicModulus](http://opendata.caceres.es/def/ontomunicipio#DynamicModulus) (c)<br />
### shear rate
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ShearRate`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### shear rate unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ShearRateUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### shear storage modulus
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ShearStorageModulus`
Super-classes |[om:StorageModulus](http://opendata.caceres.es/def/ontomunicipio#StorageModulus) (c)<br />
### shear strain
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ShearStrain`
Description | <p>Shear strain is a strain that acts parallel to the surface of a material that it acts on.</p>
Super-classes |[om:Strain](http://opendata.caceres.es/def/ontomunicipio#Strain) (c)<br />
### shear stress
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ShearStress`
Description | <p>Shear stress is a stress that is applied parallel or tangential to a face of a material.</p>
Super-classes |[om:Stress](http://opendata.caceres.es/def/ontomunicipio#Stress) (c)<br />
### singular unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SingularUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### 立体角
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SolidAngle`
Description | <p>Solid angle is the ratio of the surface of a portion of a sphere enclosed by the conical surface that forms an angle to the square of the radius of the sphere.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
Sub-classes |[om:AngularSize](http://opendata.caceres.es/def/ontomunicipio#AngularSize) (c)<br />
### solid angle unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SolidAngleUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### soy bean mass fraction
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SoyBeanMassFraction`
Description | <p>The fraction of the mass of soy bean oil in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### specific amylase activity
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SpecificAmylaseActivity`
Super-classes |[om:SpecificCatalyticActivity](http://opendata.caceres.es/def/ontomunicipio#SpecificCatalyticActivity) (c)<br />
### specific catalytic activity
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SpecificCatalyticActivity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:specificCatalyticActivity-Dimension](http://opendata.caceres.es/def/ontomunicipio#specificCatalyticActivity-Dimension) (c)<br />
Sub-classes |[om:SpecificAmylaseActivity](http://opendata.caceres.es/def/ontomunicipio#SpecificAmylaseActivity) (c)<br />[om:SpecificProteaseActivity](http://opendata.caceres.es/def/ontomunicipio#SpecificProteaseActivity) (c)<br />
### specific catalytic activity unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SpecificCatalyticActivityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### coliform bacteria count (specific)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SpecificColiformBacterieCount`
Super-classes |[om:SpecificViableCount](http://opendata.caceres.es/def/ontomunicipio#SpecificViableCount) (c)<br />
### Corynebacterium bovis count (specific)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SpecificCorynebacteriumBovisCount`
Super-classes |[om:SpecificViableCount](http://opendata.caceres.es/def/ontomunicipio#SpecificViableCount) (c)<br />
### Corynebacterium count (specific)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SpecificCorynebacteriumCount`
Super-classes |[om:SpecificViableCount](http://opendata.caceres.es/def/ontomunicipio#SpecificViableCount) (c)<br />
### specific energy
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SpecificEnergy`
Description | <p>Specific energy is energy per unit mass.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:specificEnergyOrAbsorbedDoseOrDoseEquivalent-Dimension](http://opendata.caceres.es/def/ontomunicipio#specificEnergyOrAbsorbedDoseOrDoseEquivalent-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### specific energy imparted
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SpecificEnergyImparted`
Super-classes |[om:AbsorbedDose](http://opendata.caceres.es/def/ontomunicipio#AbsorbedDose) (c)<br />
### specific energy unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SpecificEnergyUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### Enterobacteriaceae count (specific)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SpecificEnterobacteriaceaeCount`
Super-classes |[om:SpecificViableCount](http://opendata.caceres.es/def/ontomunicipio#SpecificViableCount) (c)<br />
### Enterococcus count (specific)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SpecificEnterococcusCount`
Super-classes |[om:SpecificViableCount](http://opendata.caceres.es/def/ontomunicipio#SpecificViableCount) (c)<br />
### specific entropy
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SpecificEntropy`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:specificEntropyOrSpecificHeatCapacity-Dimension](http://opendata.caceres.es/def/ontomunicipio#specificEntropyOrSpecificHeatCapacity-Dimension) (c)<br />
### specific entropy unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SpecificEntropyUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### Escherichia coli count (specific)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SpecificEscherichiaColiCount`
Super-classes |[om:SpecificViableCount](http://opendata.caceres.es/def/ontomunicipio#SpecificViableCount) (c)<br />
### soortelijke warmte
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SpecificHeatCapacity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:specificEntropyOrSpecificHeatCapacity-Dimension](http://opendata.caceres.es/def/ontomunicipio#specificEntropyOrSpecificHeatCapacity-Dimension) (c)<br />
### specific heat capacity unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SpecificHeatCapacityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### Klebsiella count (specific)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SpecificKlebsiellaCount`
Super-classes |[om:SpecificViableCount](http://opendata.caceres.es/def/ontomunicipio#SpecificViableCount) (c)<br />
### Listeria monocytogenes count (specific)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SpecificListeriaMonocytogenesCount`
Super-classes |[om:SpecificViableCount](http://opendata.caceres.es/def/ontomunicipio#SpecificViableCount) (c)<br />
### specific protease activity
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SpecificProteaseActivity`
Super-classes |[om:SpecificCatalyticActivity](http://opendata.caceres.es/def/ontomunicipio#SpecificCatalyticActivity) (c)<br />
### Salmonella count (specific)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SpecificSalmonellaCount`
Super-classes |[om:SpecificViableCount](http://opendata.caceres.es/def/ontomunicipio#SpecificViableCount) (c)<br />
### Serratia marcescens count (specific)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SpecificSerratiaMarcescensCount`
Super-classes |[om:SpecificViableCount](http://opendata.caceres.es/def/ontomunicipio#SpecificViableCount) (c)<br />
### Staphylococcus aureus count (specific)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SpecificStaphylococcusAureusCount`
Super-classes |[om:SpecificViableCount](http://opendata.caceres.es/def/ontomunicipio#SpecificViableCount) (c)<br />
### Streptococcus agalactiae count (specific)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SpecificStreptococcusAgalactiaeCount`
Super-classes |[om:SpecificViableCount](http://opendata.caceres.es/def/ontomunicipio#SpecificViableCount) (c)<br />
### Streptococcus dysgalactiae count (specific)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SpecificStreptococcusDysgalactiaeCount`
Super-classes |[om:SpecificViableCount](http://opendata.caceres.es/def/ontomunicipio#SpecificViableCount) (c)<br />
### Streptococcus uberis count (specific)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SpecificStreptococcusUberisCount`
Super-classes |[om:SpecificViableCount](http://opendata.caceres.es/def/ontomunicipio#SpecificViableCount) (c)<br />
### viable count (specific)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SpecificViableCount`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:SpecificStreptococcusAgalactiaeCount](http://opendata.caceres.es/def/ontomunicipio#SpecificStreptococcusAgalactiaeCount) (c)<br />[om:SpecificStreptococcusUberisCount](http://opendata.caceres.es/def/ontomunicipio#SpecificStreptococcusUberisCount) (c)<br />[om:SpecificStreptococcusDysgalactiaeCount](http://opendata.caceres.es/def/ontomunicipio#SpecificStreptococcusDysgalactiaeCount) (c)<br />[om:SpecificKlebsiellaCount](http://opendata.caceres.es/def/ontomunicipio#SpecificKlebsiellaCount) (c)<br />[om:SpecificEnterococcusCount](http://opendata.caceres.es/def/ontomunicipio#SpecificEnterococcusCount) (c)<br />[om:SpecificCorynebacteriumCount](http://opendata.caceres.es/def/ontomunicipio#SpecificCorynebacteriumCount) (c)<br />[om:SpecificStaphylococcusAureusCount](http://opendata.caceres.es/def/ontomunicipio#SpecificStaphylococcusAureusCount) (c)<br />[om:SpecificYeastAndFungiCount](http://opendata.caceres.es/def/ontomunicipio#SpecificYeastAndFungiCount) (c)<br />[om:SpecificEnterobacteriaceaeCount](http://opendata.caceres.es/def/ontomunicipio#SpecificEnterobacteriaceaeCount) (c)<br />[om:SpecificColiformBacterieCount](http://opendata.caceres.es/def/ontomunicipio#SpecificColiformBacterieCount) (c)<br />[om:SpecificEscherichiaColiCount](http://opendata.caceres.es/def/ontomunicipio#SpecificEscherichiaColiCount) (c)<br />[om:SpecificSalmonellaCount](http://opendata.caceres.es/def/ontomunicipio#SpecificSalmonellaCount) (c)<br />[om:SpecificSerratiaMarcescensCount](http://opendata.caceres.es/def/ontomunicipio#SpecificSerratiaMarcescensCount) (c)<br />[om:SpecificListeriaMonocytogenesCount](http://opendata.caceres.es/def/ontomunicipio#SpecificListeriaMonocytogenesCount) (c)<br />[om:SpecificCorynebacteriumBovisCount](http://opendata.caceres.es/def/ontomunicipio#SpecificCorynebacteriumBovisCount) (c)<br />
### specific viable count unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SpecificViableCountUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### specific volume
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SpecificVolume`
Description | <p>Specific volume is volume per unit mass.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:specificVolume-Dimension](http://opendata.caceres.es/def/ontomunicipio#specificVolume-Dimension) (c)<br />
### specific volume unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SpecificVolumeUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### yeast and fungi count (specific)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SpecificYeastAndFungiCount`
Super-classes |[om:SpecificViableCount](http://opendata.caceres.es/def/ontomunicipio#SpecificViableCount) (c)<br />
### spectral response
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SpectralResponse`
Description | <p>The change in output signal as a function of changes in the wavelength of the input signal.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### 速度
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Speed`
Description | <p>Speed is the time rate of motion measured by the distance moved over in unit time.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:speed-Dimension](http://opendata.caceres.es/def/ontomunicipio#speed-Dimension) (c)<br />
Sub-classes |[om:Velocity](http://opendata.caceres.es/def/ontomunicipio#Velocity) (c)<br />[om:DrainageSpeed](http://opendata.caceres.es/def/ontomunicipio#DrainageSpeed) (c)<br />
### speed unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SpeedUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### square prefixed metre
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SquarePrefixedMetre`
Super-classes |[om:UnitExponentiation](http://opendata.caceres.es/def/ontomunicipio#UnitExponentiation) (c)<br />
### Stanton number
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#StantonNumber`
Description | <p>The Stanton number is a dimensionless number that measures the ratio of heat transferred into a fluid to the thermal capacity of fluid.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### Stanton number for mass transfer
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#StantonNumberForMassTransfer`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### Stanton number for mass transfer unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#StantonNumberForMassTransferUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### Stanton number unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#StantonNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### starch mass fraction
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#StarchMassFraction`
Description | <p>The fraction of the mass of starch in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### starch VA40 mass fraction
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#StarchVA40MassFraction`
Description | <p>The fraction of the mass of starch VA40 in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### starch VA85 mass fraction
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#StarchVA85MassFraction`
Description | <p>The fraction of the mass of starch VA85 in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### stellar aberration
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#StellarAberration`
Description | <p>The apparent angular displacement of the observed position of a celestial object resulting from the motion of the observer. Stellar aberration is divided into diurnal, annual, and secular components.</p>
Super-classes |[om:Aberration](http://opendata.caceres.es/def/ontomunicipio#Aberration) (c)<br />
### stem end rot
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#StemEndRot`
Description | <p>Aanwezigheid stem end rot (1/0).</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### stem-end-rot-oppervlaktefractie
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#StemEndRotAreaFraction`
Description | <p>Percentage van het oppervlak stem end rot.</p>
Super-classes |[om:AreaFraction](http://opendata.caceres.es/def/ontomunicipio#AreaFraction) (c)<br />
### stick stone
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#StickStone`
Description | <p>Kleefpit of niet (1/0).</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### storage modulus
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#StorageModulus`
Super-classes |[om:DynamicModulus](http://opendata.caceres.es/def/ontomunicipio#DynamicModulus) (c)<br />
Sub-classes |[om:ShearStorageModulus](http://opendata.caceres.es/def/ontomunicipio#ShearStorageModulus) (c)<br />[om:ShearLossModulus](http://opendata.caceres.es/def/ontomunicipio#ShearLossModulus) (c)<br />
### strain
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Strain`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:NormalStrain](http://opendata.caceres.es/def/ontomunicipio#NormalStrain) (c)<br />[om:ShearStrain](http://opendata.caceres.es/def/ontomunicipio#ShearStrain) (c)<br />[om:LinearStrain](http://opendata.caceres.es/def/ontomunicipio#LinearStrain) (c)<br />[om:VolumeStrain](http://opendata.caceres.es/def/ontomunicipio#VolumeStrain) (c)<br />[om:StrainTensor](http://opendata.caceres.es/def/ontomunicipio#StrainTensor) (c)<br />
### strain tensor
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#StrainTensor`
Super-classes |[om:Strain](http://opendata.caceres.es/def/ontomunicipio#Strain) (c)<br />
### strain unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#StrainUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### straw mass
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#StrawMass`
Super-classes |[om:Mass](http://opendata.caceres.es/def/ontomunicipio#Mass) (c)<br />
### mechanische spanning
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Stress`
Description | <p>Stress is a force that produces or tends to produce deformation in a body measured by the force applied per unit area.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:pressure-Dimension](http://opendata.caceres.es/def/ontomunicipio#pressure-Dimension) (c)<br />
Sub-classes |[om:StressTensor](http://opendata.caceres.es/def/ontomunicipio#StressTensor) (c)<br />[om:ShearStress](http://opendata.caceres.es/def/ontomunicipio#ShearStress) (c)<br />[om:CompressiveStress](http://opendata.caceres.es/def/ontomunicipio#CompressiveStress) (c)<br />[om:NormalStress](http://opendata.caceres.es/def/ontomunicipio#NormalStress) (c)<br />
### stress tensor
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#StressTensor`
Super-classes |[om:Stress](http://opendata.caceres.es/def/ontomunicipio#Stress) (c)<br />
### stress unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#StressUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### Strömgren magnitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#StroemgrenMagnitude`
Description | <p>A magnitude measured in one of Strömgren's standard passbands (using a standard filter, u, b, v, or y) or in the passbands defined by Crawford (β_narrow or β_wide).</p>
Super-classes |[om:Magnitude](http://opendata.caceres.es/def/ontomunicipio#Magnitude) (c)<br />
Sub-classes |[om:BetaNarrowMagnitude](http://opendata.caceres.es/def/ontomunicipio#BetaNarrowMagnitude) (c)<br />[om:uMagnitude](http://opendata.caceres.es/def/ontomunicipio#uMagnitude) (c)<br />[om:BetaWideMagnitude](http://opendata.caceres.es/def/ontomunicipio#BetaWideMagnitude) (c)<br />[om:yMagnitude](http://opendata.caceres.es/def/ontomunicipio#yMagnitude) (c)<br />[om:bMagnitude](http://opendata.caceres.es/def/ontomunicipio#bMagnitude) (c)<br />[om:vMagnitude](http://opendata.caceres.es/def/ontomunicipio#vMagnitude) (c)<br />
### Strouhal number
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#StrouhalNumber`
Description | <p>The Strouhal number is a dimensionless number that describes oscillating flow mechanisms.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
### Strouhal number unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#StrouhalNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### sugar mass fraction
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SugarMassFraction`
Description | <p>The fraction of the mass of sugar in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### supergalactic latitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SupergalacticLatitude`
Description | <p>The angular distance on the celestial sphere north or south of the supergalactic equator. It is measured along the great circle passing through the object and the supergalactic poles and perpendicular to the supergalactic equator.</p>
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
### supergalactic longitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SupergalacticLongitude`
Description | <p>The angular distance on the celestial sphere measured clockwise from the supergalactic centre (as defined by the International Astronomical Union (IAU)) along the supergalactic equator to the intersection with the great circle drawn from the supergalactic north pole through the object.</p>
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
### oppervlaktespanning
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SurfaceTension`
Description | <p>Surface tension is an attractive property of the surface of a liquid.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:surfaceTension-Dimension](http://opendata.caceres.es/def/ontomunicipio#surfaceTension-Dimension) (c)<br />
### surface tension unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SurfaceTensionUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### symbol rate
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SymbolRate`
Description | <p>Symbol rate is the number of symbol changes (signalling events) made to the transmission medium per second using a digitally modulated signal or a line code.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### symbol rate unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SymbolRateUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### system of units
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#SystemOfUnits`
Description | <p>In order to achieve a coherent, interdependent set of units of measure in the wide variety of units that exist, units are organised in systems of units. A system of units is based on a set of units chosen by convention to be the system’s base units, units that are considered to be mutually independent (i.e., can’t be expressed in terms of each other).</p>
In domain of |[om:hasBaseQuantity](http://opendata.caceres.es/def/ontomunicipio#hasBaseQuantity) (op)<br />[om:hasBaseUnit](http://opendata.caceres.es/def/ontomunicipio#hasBaseUnit) (op)<br />[om:hasDerivedUnit](http://opendata.caceres.es/def/ontomunicipio#hasDerivedUnit) (op)<br />[om:hasDerivedQuantity](http://opendata.caceres.es/def/ontomunicipio#hasDerivedQuantity) (op)<br />
### temperatuur
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Temperature`
Description | <p>Temperature is the extent to which an object is hot.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:thermodynamicTemperature-Dimension](http://opendata.caceres.es/def/ontomunicipio#thermodynamicTemperature-Dimension) (c)<br />[om:hasScale](http://opendata.caceres.es/def/ontomunicipio#hasScale) (op) **only** ()<br />
Sub-classes |[om:RankineTemperature](http://opendata.caceres.es/def/ontomunicipio#RankineTemperature) (c)<br />[om:ThermodynamicTemperature](http://opendata.caceres.es/def/ontomunicipio#ThermodynamicTemperature) (c)<br />[om:FahrenheitTemperature](http://opendata.caceres.es/def/ontomunicipio#FahrenheitTemperature) (c)<br />[om:CelsiusTemperature](http://opendata.caceres.es/def/ontomunicipio#CelsiusTemperature) (c)<br />[om:ReaumurTemperature](http://opendata.caceres.es/def/ontomunicipio#ReaumurTemperature) (c)<br />
### temperatuur-rate
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#TemperatureRate`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### temperature rate unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#TemperatureRateUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### temperature unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#TemperatureUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
Sub-classes |[om:CelsiusTemperatureUnit](http://opendata.caceres.es/def/ontomunicipio#CelsiusTemperatureUnit) (c)<br />[om:FahrenheitTemperatureUnit](http://opendata.caceres.es/def/ontomunicipio#FahrenheitTemperatureUnit) (c)<br />[om:ReaumurTemperatureUnit](http://opendata.caceres.es/def/ontomunicipio#ReaumurTemperatureUnit) (c)<br />[om:RankineTemperatureUnit](http://opendata.caceres.es/def/ontomunicipio#RankineTemperatureUnit) (c)<br />[om:ThermodynamicTemperatureUnit](http://opendata.caceres.es/def/ontomunicipio#ThermodynamicTemperatureUnit) (c)<br />
### Temperature_scale
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Temperature_scale`
Super-classes |[om:Scale](http://opendata.caceres.es/def/ontomunicipio#Scale) (c)<br />
### thermische geleidbaarheid
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ThermalConductivity`
Description | <p>Termal conductivity indicates the ability of a material to conduct heat.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:thermalConductivity-Dimension](http://opendata.caceres.es/def/ontomunicipio#thermalConductivity-Dimension) (c)<br />
### thermal conductivity unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ThermalConductivityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### thermal diffusivity
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ThermalDiffusivity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### thermal diffusivity unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ThermalDiffusivityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### thermal insulance
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ThermalInsulance`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:thermalInsulance-Dimension](http://opendata.caceres.es/def/ontomunicipio#thermalInsulance-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### thermal insulance unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ThermalInsulanceUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### thermal resistance
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ThermalResistance`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:thermalResistance-Dimension](http://opendata.caceres.es/def/ontomunicipio#thermalResistance-Dimension) (c)<br />
### thermal resistance unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ThermalResistanceUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### thermodynamic temperature
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ThermodynamicTemperature`
Description | <p>Thermodynamic temperature is the absolute measure of temperature. Its zero point is the temperature at which the particle constituents of matter have minimal motion and can be no colder. Thermodynamic temperature is a base quantity in the International System of Units.</p>
Super-classes |[om:Temperature](http://opendata.caceres.es/def/ontomunicipio#Temperature) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasScale](http://opendata.caceres.es/def/ontomunicipio#hasScale) (op) **value** [om:KelvinScale](http://opendata.caceres.es/def/ontomunicipio#KelvinScale) (c)<br />
Sub-classes |[om:ElectronTemperature](http://opendata.caceres.es/def/ontomunicipio#ElectronTemperature) (c)<br />[om:BrightnessTemperature](http://opendata.caceres.es/def/ontomunicipio#BrightnessTemperature) (c)<br />[om:IonizationTemperature](http://opendata.caceres.es/def/ontomunicipio#IonizationTemperature) (c)<br />[om:ColourTemperature](http://opendata.caceres.es/def/ontomunicipio#ColourTemperature) (c)<br />
### thermodynamic temperature scale
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ThermodynamicTemperatureScale`
Super-classes |[om:Scale](http://opendata.caceres.es/def/ontomunicipio#Scale) (c)<br />
### thermodynamic temperature unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ThermodynamicTemperatureUnit`
Super-classes |[om:TemperatureUnit](http://opendata.caceres.es/def/ontomunicipio#TemperatureUnit) (c)<br />
### dikte
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Thickness`
Super-classes |[om:Length](http://opendata.caceres.es/def/ontomunicipio#Length) (c)<br />
### thrust
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Thrust`
Description | <p>Thrust is a reaction force that is caused by an accelerated mass expelled by a system in one direction.</p>
Super-classes |[om:Force](http://opendata.caceres.es/def/ontomunicipio#Force) (c)<br />
### Thuan and Gunn magnitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ThuanAndGunnMagnitude`
Description | <p>A magnitude measured in one of Thuan and Gunn's standard passbands (using a standard filter, i.e. g).</p>
Super-classes |[om:Magnitude](http://opendata.caceres.es/def/ontomunicipio#Magnitude) (c)<br />
Sub-classes |[om:gMagnitude](http://opendata.caceres.es/def/ontomunicipio#gMagnitude) (c)<br />
### time
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Time`
Description | <p>Time is a base quantity in the International System of Units and other systems of units. It is measured by numbers of repetitions of cyclical events.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:time-Dimension](http://opendata.caceres.es/def/ontomunicipio#time-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:VaseLife](http://opendata.caceres.es/def/ontomunicipio#VaseLife) (c)<br />[om:LightTime](http://opendata.caceres.es/def/ontomunicipio#LightTime) (c)<br />[om:TimeConstant](http://opendata.caceres.es/def/ontomunicipio#TimeConstant) (c)<br />[om:Date](http://opendata.caceres.es/def/ontomunicipio#Date) (c)<br />[om:PeriodOfVariability](http://opendata.caceres.es/def/ontomunicipio#PeriodOfVariability) (c)<br />[om:Half-Life](http://opendata.caceres.es/def/ontomunicipio#Half-Life) (c)<br />[om:Duration](http://opendata.caceres.es/def/ontomunicipio#Duration) (c)<br />[om:Period](http://opendata.caceres.es/def/ontomunicipio#Period) (c)<br />
### time constant
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#TimeConstant`
Description | <p>Time required to approach (1-1/e) of the final output value of a detector (about 63%) (Kitchin, Astrophysical Techniques, IoP, Table 1.1.2).</p>
Super-classes |[om:Time](http://opendata.caceres.es/def/ontomunicipio#Time) (c)<br />
### time unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#TimeUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### top mass
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#TopMass`
Super-classes |[om:Mass](http://opendata.caceres.es/def/ontomunicipio#Mass) (c)<br />
### 扭矩
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Torque`
Description | <p>Torque is the effectiveness of a force to produce rotation about an axis, measured by the product of the force and the perpendicular distance from the line of action of the force to the axis.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:energy-Dimension](http://opendata.caceres.es/def/ontomunicipio#energy-Dimension) (c)<br />
### torque unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#TorqueUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### total 3D start-end distance
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Total3DStartEndDistance`
Super-classes |[om:Distance](http://opendata.caceres.es/def/ontomunicipio#Distance) (c)<br />
### total density parameter
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#TotalDensityParameter`
Description | <p>The total density parameter.</p>
Super-classes |[om:DensityParameter](http://opendata.caceres.es/def/ontomunicipio#DensityParameter) (c)<br />
### total distance travelled
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#TotalDistanceTravelled`
Super-classes |[om:Distance](http://opendata.caceres.es/def/ontomunicipio#Distance) (c)<br />
### totaal aantal knoppen
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#TotalNumberBuds`
Description | <p>Totaal aantal knoppen.</p>
Super-classes |[om:NumberBuds](http://opendata.caceres.es/def/ontomunicipio#NumberBuds) (c)<br />
### total number flowers
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#TotalNumberFlowers`
Description | <p>Totaal aantal bloemen.</p>
Super-classes |[om:NumberFlowers](http://opendata.caceres.es/def/ontomunicipio#NumberFlowers) (c)<br />
### totaal aantal bladeren
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#TotalNumberLeaves`
Description | <p>Totaal aantal bladeren.</p>
Super-classes |[om:NumberLeaves](http://opendata.caceres.es/def/ontomunicipio#NumberLeaves) (c)<br />
### true distance modulus
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#TrueDistanceModulus`
Super-classes |[om:DistanceModulus](http://opendata.caceres.es/def/ontomunicipio#DistanceModulus) (c)<br />
### tween mass fraction
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#TweenMassFraction`
Description | <p>The fraction of the mass of tween in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### Tycho broadband magnitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#TychoBroadbandMagnitude`
Description | <p>Broadband Tycho magnitude (formed from B and V magintude measurements.</p>
Super-classes |[om:Magnitude](http://opendata.caceres.es/def/ontomunicipio#Magnitude) (c)<br />
### U magnitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#UMagnitude`
Description | <p>Johnson U magnitude. The Johnson U band is a standard passband in the ultraviolet area. The central wavelength is 365nm and the bandwidth is 70nm.  The filter to be used is the Corning 9863 filter.</p>
Super-classes |[om:JohnsonMagnitude](http://opendata.caceres.es/def/ontomunicipio#JohnsonMagnitude) (c)<br />
### unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Unit`
Description | <p>A unit of measure is a definite magnitude of a quantity, defined and adopted by convention or by law. It is used as a standard for measurement of the same quantity, where any other value of the quantity can be expressed as a simple multiple of the unit. For example, length is a quantity; the metre is a unit of length that represents a definite predetermined length. When we say 10 metre (or 10 m), we actually mean 10 times the definite predetermined length called "metre".</p>
Sub-classes |[om:MagnitudeUnit](http://opendata.caceres.es/def/ontomunicipio#MagnitudeUnit) (c)<br />[om:DoseEquivalentUnit](http://opendata.caceres.es/def/ontomunicipio#DoseEquivalentUnit) (c)<br />[om:ElectricDipoleMomentUnit](http://opendata.caceres.es/def/ontomunicipio#ElectricDipoleMomentUnit) (c)<br />[om:MolalityUnit](http://opendata.caceres.es/def/ontomunicipio#MolalityUnit) (c)<br />[om:SpecificEntropyUnit](http://opendata.caceres.es/def/ontomunicipio#SpecificEntropyUnit) (c)<br />[om:CompoundUnit](http://opendata.caceres.es/def/ontomunicipio#CompoundUnit) (c)<br />[om:SurfaceTensionUnit](http://opendata.caceres.es/def/ontomunicipio#SurfaceTensionUnit) (c)<br />[om:RatioUnit](http://opendata.caceres.es/def/ontomunicipio#RatioUnit) (c)<br />[om:DynamicRangeUnit](http://opendata.caceres.es/def/ontomunicipio#DynamicRangeUnit) (c)<br />[om:MolarVolumeUnit](http://opendata.caceres.es/def/ontomunicipio#MolarVolumeUnit) (c)<br />[om:FirstCowlingNumberUnit](http://opendata.caceres.es/def/ontomunicipio#FirstCowlingNumberUnit) (c)<br />[om:ExposureUnit](http://opendata.caceres.es/def/ontomunicipio#ExposureUnit) (c)<br />[om:EulerNumberUnit](http://opendata.caceres.es/def/ontomunicipio#EulerNumberUnit) (c)<br />[om:MassFlowUnit](http://opendata.caceres.es/def/ontomunicipio#MassFlowUnit) (c)<br />[om:AmountOfSubstanceUnit](http://opendata.caceres.es/def/ontomunicipio#AmountOfSubstanceUnit) (c)<br />[om:ExposureToXAndGammaRaysUnit](http://opendata.caceres.es/def/ontomunicipio#ExposureToXAndGammaRaysUnit) (c)<br />[om:ColumnNumberDensityUnit](http://opendata.caceres.es/def/ontomunicipio#ColumnNumberDensityUnit) (c)<br />[om:ElectricalResistivityUnit](http://opendata.caceres.es/def/ontomunicipio#ElectricalResistivityUnit) (c)<br />[om:PercentageUnit](http://opendata.caceres.es/def/ontomunicipio#PercentageUnit) (c)<br />[om:ActionUnit](http://opendata.caceres.es/def/ontomunicipio#ActionUnit) (c)<br />[om:SolidAngleUnit](http://opendata.caceres.es/def/ontomunicipio#SolidAngleUnit) (c)<br />[om:MassUnit](http://opendata.caceres.es/def/ontomunicipio#MassUnit) (c)<br />[om:UnitMultiple](http://opendata.caceres.es/def/ontomunicipio#UnitMultiple) (c)<br />[om:CatalyticActivityUnit](http://opendata.caceres.es/def/ontomunicipio#CatalyticActivityUnit) (c)<br />[om:AreaDensityRateUnit](http://opendata.caceres.es/def/ontomunicipio#AreaDensityRateUnit) (c)<br />[om:MagneticFieldUnit](http://opendata.caceres.es/def/ontomunicipio#MagneticFieldUnit) (c)<br />[om:MagneticFluxDensityUnit](http://opendata.caceres.es/def/ontomunicipio#MagneticFluxDensityUnit) (c)<br />[om:ElectricCurrentUnit](http://opendata.caceres.es/def/ontomunicipio#ElectricCurrentUnit) (c)<br />[om:GasConstantUnit](http://opendata.caceres.es/def/ontomunicipio#GasConstantUnit) (c)<br />[om:RadiantIntensityUnit](http://opendata.caceres.es/def/ontomunicipio#RadiantIntensityUnit) (c)<br />[om:FluidityUnit](http://opendata.caceres.es/def/ontomunicipio#FluidityUnit) (c)<br />[om:AngularMomentumUnit](http://opendata.caceres.es/def/ontomunicipio#AngularMomentumUnit) (c)<br />[om:EnergyUnit](http://opendata.caceres.es/def/ontomunicipio#EnergyUnit) (c)<br />[om:GrashofNumberUnit](http://opendata.caceres.es/def/ontomunicipio#GrashofNumberUnit) (c)<br />[om:StressUnit](http://opendata.caceres.es/def/ontomunicipio#StressUnit) (c)<br />[om:HubbleConstantUnit](http://opendata.caceres.es/def/ontomunicipio#HubbleConstantUnit) (c)<br />[om:EntropyUnit](http://opendata.caceres.es/def/ontomunicipio#EntropyUnit) (c)<br />[om:PecletNumberUnit](http://opendata.caceres.es/def/ontomunicipio#PecletNumberUnit) (c)<br />[om:AngularSpeedUnit](http://opendata.caceres.es/def/ontomunicipio#AngularSpeedUnit) (c)<br />[om:CurrentDensityUnit](http://opendata.caceres.es/def/ontomunicipio#CurrentDensityUnit) (c)<br />[om:ActivityUnit](http://opendata.caceres.es/def/ontomunicipio#ActivityUnit) (c)<br />[om:LuminousFluxUnit](http://opendata.caceres.es/def/ontomunicipio#LuminousFluxUnit) (c)<br />[om:RelativeHumidityUnit](http://opendata.caceres.es/def/ontomunicipio#RelativeHumidityUnit) (c)<br />[om:HeatTransferCoefficientUnit](http://opendata.caceres.es/def/ontomunicipio#HeatTransferCoefficientUnit) (c)<br />[om:LuminousIntensityUnit](http://opendata.caceres.es/def/ontomunicipio#LuminousIntensityUnit) (c)<br />[om:PowerDensityUnit](http://opendata.caceres.es/def/ontomunicipio#PowerDensityUnit) (c)<br />[om:CowlingNumberUnit](http://opendata.caceres.es/def/ontomunicipio#CowlingNumberUnit) (c)<br />[om:WeberNumberUnit](http://opendata.caceres.es/def/ontomunicipio#WeberNumberUnit) (c)<br />[om:HartmannNumberUnit](http://opendata.caceres.es/def/ontomunicipio#HartmannNumberUnit) (c)<br />[om:SymbolRateUnit](http://opendata.caceres.es/def/ontomunicipio#SymbolRateUnit) (c)<br />[om:AbsorbedDoseUnit](http://opendata.caceres.es/def/ontomunicipio#AbsorbedDoseUnit) (c)<br />[om:RadianceUnit](http://opendata.caceres.es/def/ontomunicipio#RadianceUnit) (c)<br />[om:SpeedUnit](http://opendata.caceres.es/def/ontomunicipio#SpeedUnit) (c)<br />[om:GrashofNumberForMassTransferUnit](http://opendata.caceres.es/def/ontomunicipio#GrashofNumberForMassTransferUnit) (c)<br />[om:ShearRateUnit](http://opendata.caceres.es/def/ontomunicipio#ShearRateUnit) (c)<br />[om:TemperatureUnit](http://opendata.caceres.es/def/ontomunicipio#TemperatureUnit) (c)<br />[om:MomentOfInertiaUnit](http://opendata.caceres.es/def/ontomunicipio#MomentOfInertiaUnit) (c)<br />[om:Permeance-MaterialsScienceUnit](http://opendata.caceres.es/def/ontomunicipio#Permeance-MaterialsScienceUnit) (c)<br />[om:AbsorbedDoseRateUnit](http://opendata.caceres.es/def/ontomunicipio#AbsorbedDoseRateUnit) (c)<br />[om:ThermalInsulanceUnit](http://opendata.caceres.es/def/ontomunicipio#ThermalInsulanceUnit) (c)<br />[om:DecelerationParameterUnit](http://opendata.caceres.es/def/ontomunicipio#DecelerationParameterUnit) (c)<br />[om:LewisNumberUnit](http://opendata.caceres.es/def/ontomunicipio#LewisNumberUnit) (c)<br />[om:FourierNumberUnit](http://opendata.caceres.es/def/ontomunicipio#FourierNumberUnit) (c)<br />[om:KinematicViscosityUnit](http://opendata.caceres.es/def/ontomunicipio#KinematicViscosityUnit) (c)<br />[om:SpecificCatalyticActivityUnit](http://opendata.caceres.es/def/ontomunicipio#SpecificCatalyticActivityUnit) (c)<br />[om:AccelerationUnit](http://opendata.caceres.es/def/ontomunicipio#AccelerationUnit) (c)<br />[om:LuminanceUnit](http://opendata.caceres.es/def/ontomunicipio#LuminanceUnit) (c)<br />[om:StantonNumberUnit](http://opendata.caceres.es/def/ontomunicipio#StantonNumberUnit) (c)<br />[om:Permeance-ElectromagneticUnit](http://opendata.caceres.es/def/ontomunicipio#Permeance-ElectromagneticUnit) (c)<br />[om:PecletNumberForMassTransferUnit](http://opendata.caceres.es/def/ontomunicipio#PecletNumberForMassTransferUnit) (c)<br />[om:LengthUnit](http://opendata.caceres.es/def/ontomunicipio#LengthUnit) (c)<br />[om:SpecificVolumeUnit](http://opendata.caceres.es/def/ontomunicipio#SpecificVolumeUnit) (c)<br />[om:StantonNumberForMassTransferUnit](http://opendata.caceres.es/def/ontomunicipio#StantonNumberForMassTransferUnit) (c)<br />[om:NumberDensityUnit](http://opendata.caceres.es/def/ontomunicipio#NumberDensityUnit) (c)<br />[om:ThermalDiffusivityUnit](http://opendata.caceres.es/def/ontomunicipio#ThermalDiffusivityUnit) (c)<br />[om:LuminousEfficacyUnit](http://opendata.caceres.es/def/ontomunicipio#LuminousEfficacyUnit) (c)<br />[om:DetectivityUnit](http://opendata.caceres.es/def/ontomunicipio#DetectivityUnit) (c)<br />[om:NusseltNumberUnit](http://opendata.caceres.es/def/ontomunicipio#NusseltNumberUnit) (c)<br />[om:AreaFractionUnit](http://opendata.caceres.es/def/ontomunicipio#AreaFractionUnit) (c)<br />[om:InductanceUnit](http://opendata.caceres.es/def/ontomunicipio#InductanceUnit) (c)<br />[om:DynamicViscosityUnit](http://opendata.caceres.es/def/ontomunicipio#DynamicViscosityUnit) (c)<br />[om:SingularUnit](http://opendata.caceres.es/def/ontomunicipio#SingularUnit) (c)<br />[om:ElectricPotentialUnit](http://opendata.caceres.es/def/ontomunicipio#ElectricPotentialUnit) (c)<br />[om:DensityUnit](http://opendata.caceres.es/def/ontomunicipio#DensityUnit) (c)<br />[om:MolarHeatCapacityUnit](http://opendata.caceres.es/def/ontomunicipio#MolarHeatCapacityUnit) (c)<br />[om:ReluctanceUnit](http://opendata.caceres.es/def/ontomunicipio#ReluctanceUnit) (c)<br />[om:LuminousEnergyUnit](http://opendata.caceres.es/def/ontomunicipio#LuminousEnergyUnit) (c)<br />[om:ElectricalConductivityUnit](http://opendata.caceres.es/def/ontomunicipio#ElectricalConductivityUnit) (c)<br />[om:MassFractionUnit](http://opendata.caceres.es/def/ontomunicipio#MassFractionUnit) (c)<br />[om:MachNumberUnit](http://opendata.caceres.es/def/ontomunicipio#MachNumberUnit) (c)<br />[om:ResponsivityUnit](http://opendata.caceres.es/def/ontomunicipio#ResponsivityUnit) (c)<br />[om:ElectricalConductanceUnit](http://opendata.caceres.es/def/ontomunicipio#ElectricalConductanceUnit) (c)<br />[om:RayleighNumberUnit](http://opendata.caceres.es/def/ontomunicipio#RayleighNumberUnit) (c)<br />[om:VolumeUnit](http://opendata.caceres.es/def/ontomunicipio#VolumeUnit) (c)<br />[om:MomentOfForceUnit](http://opendata.caceres.es/def/ontomunicipio#MomentOfForceUnit) (c)<br />[om:MolarEnergyUnit](http://opendata.caceres.es/def/ontomunicipio#MolarEnergyUnit) (c)<br />[om:TemperatureRateUnit](http://opendata.caceres.es/def/ontomunicipio#TemperatureRateUnit) (c)<br />[om:FrequencyUnit](http://opendata.caceres.es/def/ontomunicipio#FrequencyUnit) (c)<br />[om:PermittivityUnit](http://opendata.caceres.es/def/ontomunicipio#PermittivityUnit) (c)<br />[om:AmountOfSubstanceFractionUnit](http://opendata.caceres.es/def/ontomunicipio#AmountOfSubstanceFractionUnit) (c)<br />[om:AmountOfMoneyUnit](http://opendata.caceres.es/def/ontomunicipio#AmountOfMoneyUnit) (c)<br />[om:CapacitanceUnit](http://opendata.caceres.es/def/ontomunicipio#CapacitanceUnit) (c)<br />[om:ElectricChargeUnit](http://opendata.caceres.es/def/ontomunicipio#ElectricChargeUnit) (c)<br />[om:AngleUnit](http://opendata.caceres.es/def/ontomunicipio#AngleUnit) (c)<br />[om:FroudeNumberUnit](http://opendata.caceres.es/def/ontomunicipio#FroudeNumberUnit) (c)<br />[om:ElectricFieldUnit](http://opendata.caceres.es/def/ontomunicipio#ElectricFieldUnit) (c)<br />[om:AreaUnit](http://opendata.caceres.es/def/ontomunicipio#AreaUnit) (c)<br />[om:MolarMassUnit](http://opendata.caceres.es/def/ontomunicipio#MolarMassUnit) (c)<br />[om:AngularAccelerationUnit](http://opendata.caceres.es/def/ontomunicipio#AngularAccelerationUnit) (c)<br />[om:StrainUnit](http://opendata.caceres.es/def/ontomunicipio#StrainUnit) (c)<br />[om:ThermalConductivityUnit](http://opendata.caceres.es/def/ontomunicipio#ThermalConductivityUnit) (c)<br />[om:InformationCapacityUnit](http://opendata.caceres.es/def/ontomunicipio#InformationCapacityUnit) (c)<br />[om:QuantityOfDimensionOneUnit](http://opendata.caceres.es/def/ontomunicipio#QuantityOfDimensionOneUnit) (c)<br />[om:CatalyticActivityConcentrationUnit](http://opendata.caceres.es/def/ontomunicipio#CatalyticActivityConcentrationUnit) (c)<br />[om:EnergyDensityUnit](http://opendata.caceres.es/def/ontomunicipio#EnergyDensityUnit) (c)<br />[om:ForceUnit](http://opendata.caceres.es/def/ontomunicipio#ForceUnit) (c)<br />[om:NusseltNumberForMassTransferUnit](http://opendata.caceres.es/def/ontomunicipio#NusseltNumberForMassTransferUnit) (c)<br />[om:MomentumUnit](http://opendata.caceres.es/def/ontomunicipio#MomentumUnit) (c)<br />[om:CurvatureConstantUnit](http://opendata.caceres.es/def/ontomunicipio#CurvatureConstantUnit) (c)<br />[om:FourierNumberForMassTransferUnit](http://opendata.caceres.es/def/ontomunicipio#FourierNumberForMassTransferUnit) (c)<br />[om:StrouhalNumberUnit](http://opendata.caceres.es/def/ontomunicipio#StrouhalNumberUnit) (c)<br />[om:WavenumberUnit](http://opendata.caceres.es/def/ontomunicipio#WavenumberUnit) (c)<br />[om:ElectricFluxDensityUnit](http://opendata.caceres.es/def/ontomunicipio#ElectricFluxDensityUnit) (c)<br />[om:TorqueUnit](http://opendata.caceres.es/def/ontomunicipio#TorqueUnit) (c)<br />[om:ElectricChargeDensityUnit](http://opendata.caceres.es/def/ontomunicipio#ElectricChargeDensityUnit) (c)<br />[om:AlfvenNumberUnit](http://opendata.caceres.es/def/ontomunicipio#AlfvenNumberUnit) (c)<br />[om:ThermalResistanceUnit](http://opendata.caceres.es/def/ontomunicipio#ThermalResistanceUnit) (c)<br />[om:SpecificEnergyUnit](http://opendata.caceres.es/def/ontomunicipio#SpecificEnergyUnit) (c)<br />[om:AreaDensityUnit](http://opendata.caceres.es/def/ontomunicipio#AreaDensityUnit) (c)<br />[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />[om:ReynoldsNumberUnit](http://opendata.caceres.es/def/ontomunicipio#ReynoldsNumberUnit) (c)<br />[om:IlluminanceUnit](http://opendata.caceres.es/def/ontomunicipio#IlluminanceUnit) (c)<br />[om:PressureUnit](http://opendata.caceres.es/def/ontomunicipio#PressureUnit) (c)<br />[om:AmountOfSubstanceFlowUnit](http://opendata.caceres.es/def/ontomunicipio#AmountOfSubstanceFlowUnit) (c)<br />[om:AmountOfSubstanceConcentrationUnit](http://opendata.caceres.es/def/ontomunicipio#AmountOfSubstanceConcentrationUnit) (c)<br />[om:MolarEntropyUnit](http://opendata.caceres.es/def/ontomunicipio#MolarEntropyUnit) (c)<br />[om:QuantumEfficiencyUnit](http://opendata.caceres.es/def/ontomunicipio#QuantumEfficiencyUnit) (c)<br />[om:SchmidtNumberUnit](http://opendata.caceres.es/def/ontomunicipio#SchmidtNumberUnit) (c)<br />[om:MagneticReynoldsNumberUnit](http://opendata.caceres.es/def/ontomunicipio#MagneticReynoldsNumberUnit) (c)<br />[om:MagneticFluxUnit](http://opendata.caceres.es/def/ontomunicipio#MagneticFluxUnit) (c)<br />[om:Permeability-EarthScienceUnit](http://opendata.caceres.es/def/ontomunicipio#Permeability-EarthScienceUnit) (c)<br />[om:NumberUnit](http://opendata.caceres.es/def/ontomunicipio#NumberUnit) (c)<br />[om:VolumetricHeatCapacityUnit](http://opendata.caceres.es/def/ontomunicipio#VolumetricHeatCapacityUnit) (c)<br />[om:HeatCapacityUnit](http://opendata.caceres.es/def/ontomunicipio#HeatCapacityUnit) (c)<br />[om:MagnetomotiveForceUnit](http://opendata.caceres.es/def/ontomunicipio#MagnetomotiveForceUnit) (c)<br />[om:PermeabilityOfFreeSpaceUnit](http://opendata.caceres.es/def/ontomunicipio#PermeabilityOfFreeSpaceUnit) (c)<br />[om:SpecificHeatCapacityUnit](http://opendata.caceres.es/def/ontomunicipio#SpecificHeatCapacityUnit) (c)<br />[om:PowerUnit](http://opendata.caceres.es/def/ontomunicipio#PowerUnit) (c)<br />[om:SpecificViableCountUnit](http://opendata.caceres.es/def/ontomunicipio#SpecificViableCountUnit) (c)<br />[om:VolumeFractionUnit](http://opendata.caceres.es/def/ontomunicipio#VolumeFractionUnit) (c)<br />[om:TimeUnit](http://opendata.caceres.es/def/ontomunicipio#TimeUnit) (c)<br />[om:ElectricalResistanceUnit](http://opendata.caceres.es/def/ontomunicipio#ElectricalResistanceUnit) (c)<br />[om:VolumetricViableCountUnit](http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCountUnit) (c)<br />[om:PrandtlNumberUnit](http://opendata.caceres.es/def/ontomunicipio#PrandtlNumberUnit) (c)<br />[om:KnudsenNumberUnit](http://opendata.caceres.es/def/ontomunicipio#KnudsenNumberUnit) (c)<br />[om:VolumetricFlowRateUnit](http://opendata.caceres.es/def/ontomunicipio#VolumetricFlowRateUnit) (c)<br />[om:DensityParameterUnit](http://opendata.caceres.es/def/ontomunicipio#DensityParameterUnit) (c)<br />
In range of |[om:commonlyHasUnit](http://opendata.caceres.es/def/ontomunicipio#commonlyHasUnit) (op)<br />[om:hasDerivedUnit](http://opendata.caceres.es/def/ontomunicipio#hasDerivedUnit) (op)<br />[om:usesUnit](http://opendata.caceres.es/def/ontomunicipio#usesUnit) (op)<br />[om:hasBaseUnit](http://opendata.caceres.es/def/ontomunicipio#hasBaseUnit) (op)<br />[om:hasUnit](http://opendata.caceres.es/def/ontomunicipio#hasUnit) (op)<br />
### unit division
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#UnitDivision`
Super-classes |[om:CompoundUnit](http://opendata.caceres.es/def/ontomunicipio#CompoundUnit) (c)<br />
Sub-classes |[om:PrefixedMolePerPrefixedLitre](http://opendata.caceres.es/def/ontomunicipio#PrefixedMolePerPrefixedLitre) (c)<br />[om:PrefixedGramPerLitre](http://opendata.caceres.es/def/ontomunicipio#PrefixedGramPerLitre) (c)<br />[om:GramPerPrefixedLitre](http://opendata.caceres.es/def/ontomunicipio#GramPerPrefixedLitre) (c)<br />[om:PrefixedMetrePerPrefixedSecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#PrefixedMetrePerPrefixedSecond-TimeSquared) (c)<br />[om:PrefixedGramPerPrefixedLitre](http://opendata.caceres.es/def/ontomunicipio#PrefixedGramPerPrefixedLitre) (c)<br />[om:PrefixedMetrePerSecond-Time](http://opendata.caceres.es/def/ontomunicipio#PrefixedMetrePerSecond-Time) (c)<br />[om:PrefixedMolePerMetre](http://opendata.caceres.es/def/ontomunicipio#PrefixedMolePerMetre) (c)<br />[om:PrefixedMetrePerSecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#PrefixedMetrePerSecond-TimeSquared) (c)<br />[om:PrefixedMolePerPrefixedMetre](http://opendata.caceres.es/def/ontomunicipio#PrefixedMolePerPrefixedMetre) (c)<br />[om:PrefixedMolePerLitre](http://opendata.caceres.es/def/ontomunicipio#PrefixedMolePerLitre) (c)<br />[om:PrefixedMetrePerPrefixedSecond-Time](http://opendata.caceres.es/def/ontomunicipio#PrefixedMetrePerPrefixedSecond-Time) (c)<br />[om:MetrePerPrefixedSecond-Time](http://opendata.caceres.es/def/ontomunicipio#MetrePerPrefixedSecond-Time) (c)<br />[om:MolePerPrefixedMetre](http://opendata.caceres.es/def/ontomunicipio#MolePerPrefixedMetre) (c)<br />[om:MolePerPrefixedLitre](http://opendata.caceres.es/def/ontomunicipio#MolePerPrefixedLitre) (c)<br />[om:MetrePerPrefixedSecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#MetrePerPrefixedSecond-TimeSquared) (c)<br />
### unit exponentiation
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#UnitExponentiation`
Super-classes |[om:CompoundUnit](http://opendata.caceres.es/def/ontomunicipio#CompoundUnit) (c)<br />
Sub-classes |[om:CubicPrefixedMetre](http://opendata.caceres.es/def/ontomunicipio#CubicPrefixedMetre) (c)<br />[om:PrefixedSecond-TimeSquared](http://opendata.caceres.es/def/ontomunicipio#PrefixedSecond-TimeSquared) (c)<br />[om:SquarePrefixedMetre](http://opendata.caceres.es/def/ontomunicipio#SquarePrefixedMetre) (c)<br />
### unit multiple
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#UnitMultiple`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### unit multiplication
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#UnitMultiplication`
Super-classes |[om:CompoundUnit](http://opendata.caceres.es/def/ontomunicipio#CompoundUnit) (c)<br />
Sub-classes |[om:PrefixedMetrePrefixedGram](http://opendata.caceres.es/def/ontomunicipio#PrefixedMetrePrefixedGram) (c)<br />
### V amplitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#VAmplitude`
Description | <p>Amplitude of the light variation in Johnson V magnitude. The Johnson V band is a standard passband in the visual area, matching the response curve of the human eye. The central wavelength is 550nm and the bandwidth is 90nm.  The filter to be used is the Corning 3384 filter.</p>
Super-classes |[om:Amplitude](http://opendata.caceres.es/def/ontomunicipio#Amplitude) (c)<br />
### V magnitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#VMagnitude`
Description | <p>Johnson V magnitude. The Johnson V band is a standard passband in the visual area, matching the response curve of the human eye. The central wavelength is 550nm and the bandwidth is 90nm.  The filter to be used is the Corning 3384 filter.</p>
Super-classes |[om:JohnsonMagnitude](http://opendata.caceres.es/def/ontomunicipio#JohnsonMagnitude) (c)<br />
Sub-classes |[om:VMagnitudeAtMaximumBrightness](http://opendata.caceres.es/def/ontomunicipio#VMagnitudeAtMaximumBrightness) (c)<br />[om:VMagnitudeAtMinimumBrightness](http://opendata.caceres.es/def/ontomunicipio#VMagnitudeAtMinimumBrightness) (c)<br />
### V magnitude at maximum brightness
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#VMagnitudeAtMaximumBrightness`
Description | <p>Johnson V magnitude (apparent) at maximum brightness (i.e. for a variable star). The Johnson V band is a standard filter in the visual area, matching the response curve of the human eye. The central wavelength is 550nm and the bandwidth is 90nm.  The filter to be used is the Corning 3384 filter.</p>
Super-classes |[om:VMagnitude](http://opendata.caceres.es/def/ontomunicipio#VMagnitude) (c)<br />[om:MagnitudeAtMaximumBrightness](http://opendata.caceres.es/def/ontomunicipio#MagnitudeAtMaximumBrightness) (c)<br />
### V magnitude at minimum brightness
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#VMagnitudeAtMinimumBrightness`
Description | <p>Johnson V magnitude (apparent) at minimum brightness (i.e. for a variable star). The Johnson V band is a standard filter in the visual area, matching the response curve of the human eye. The central wavelength is 550nm and the bandwidth is 90nm.  The filter to be used is the Corning 3384 filter.</p>
Super-classes |[om:MagnitudeAtMinimumBrightness](http://opendata.caceres.es/def/ontomunicipio#MagnitudeAtMinimumBrightness) (c)<br />[om:VMagnitude](http://opendata.caceres.es/def/ontomunicipio#VMagnitude) (c)<br />
### vascular browning
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#VascularBrowning`
Description | <p>Voorbeeld avocado Hass: poster (code).</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
### vaasleven
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#VaseLife`
Description | <p>Aantal dagen op de vaas tot onvoldoende.</p>
Super-classes |[om:Time](http://opendata.caceres.es/def/ontomunicipio#Time) (c)<br />
### vaas- plus watermassa
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#VasePlusWaterMass`
Description | <p>Gewicht vaas plus water.</p>
Super-classes |[om:Mass](http://opendata.caceres.es/def/ontomunicipio#Mass) (c)<br />
### vaas- plus water- plus bloemmassa
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#VasePlusWaterPlusFlowerMass`
Description | <p>Gewicht vaas plus water plus bloem (= steel plus blad plus bloem).</p>
Super-classes |[om:Mass](http://opendata.caceres.es/def/ontomunicipio#Mass) (c)<br />
### snelheid (vector)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Velocity`
Description | <p>Velocity is the rate of change of position.</p>
Super-classes |[om:Speed](http://opendata.caceres.es/def/ontomunicipio#Speed) (c)<br />
### visual albedo
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#VisualAlbedo`
Description | <p>The albedo only for radiation in the visual part of the spectrum.</p>
Super-classes |[om:Albedo](http://opendata.caceres.es/def/ontomunicipio#Albedo) (c)<br />
### volume
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Volume`
Description | <p>Volume is a measure of how much three-dimensional space any phenomenon occupies. It is a derived quantity in the International System of Units. Volume is length to the power 3.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:volume-Dimension](http://opendata.caceres.es/def/ontomunicipio#volume-Dimension) (c)<br />
### volumefractie
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#VolumeFraction`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />
Sub-classes |[om:Overrun](http://opendata.caceres.es/def/ontomunicipio#Overrun) (c)<br />
### volume fraction unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#VolumeFractionUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### volume strain
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#VolumeStrain`
Super-classes |[om:Strain](http://opendata.caceres.es/def/ontomunicipio#Strain) (c)<br />
### volume unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#VolumeUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### coliform bacteria count (volumetric)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricColiformBacterieCount`
Super-classes |[om:VolumetricViableCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCount) (c)<br />
### Corynebacterium bovis count (volumetric)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricCorynebacteriumBovisCount`
Super-classes |[om:VolumetricViableCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCount) (c)<br />
### Corynebacterium count (volumetric)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricCorynebacteriumCount`
Super-classes |[om:VolumetricViableCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCount) (c)<br />
### Enterobacteriaceae count (volumetric)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricEnterobacteriaceaeCount`
Super-classes |[om:VolumetricViableCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCount) (c)<br />
### Enterococcus count (volumetric)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricEnterococcusCount`
Super-classes |[om:VolumetricViableCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCount) (c)<br />
### Escherichia coli count (volumetric)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricEscherichiaColiCount`
Super-classes |[om:VolumetricViableCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCount) (c)<br />
### volumetric flow rate
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricFlowRate`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:volumetricFlowRate-Dimension](http://opendata.caceres.es/def/ontomunicipio#volumetricFlowRate-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### volumetric flow rate unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricFlowRateUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### volumetric heat capacity
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricHeatCapacity`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:volumetricHeatCapacity-Dimension](http://opendata.caceres.es/def/ontomunicipio#volumetricHeatCapacity-Dimension) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### volumetric heat capacity unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricHeatCapacityUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### Klebsiella count (volumetric)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricKlebsiellaCount`
Super-classes |[om:VolumetricViableCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCount) (c)<br />
### Listeria monocytogenes count (volumetric)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricListeriaMonocytogenesCount`
Super-classes |[om:VolumetricViableCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCount) (c)<br />
### Salmonella count (volumetric)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricSalmonellaCount`
Super-classes |[om:VolumetricViableCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCount) (c)<br />
### Serratia marcescens count (volumetric)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricSerratiaMarcescensCount`
Super-classes |[om:VolumetricViableCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCount) (c)<br />
### Staphylococcus aureus count (volumetric)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricStaphylococcusAureusCount`
Super-classes |[om:VolumetricViableCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCount) (c)<br />
### Streptococcus agalactiae count (volumetric)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricStreptococcusAgalactiaeCount`
Super-classes |[om:VolumetricViableCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCount) (c)<br />
### Streptococcus dysgalactiae count (volumetric)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricStreptococcusDysgalactiaeCount`
Super-classes |[om:VolumetricViableCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCount) (c)<br />
### Streptococcus uberis count (volumetric)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricStreptococcusUberisCount`
Super-classes |[om:VolumetricViableCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCount) (c)<br />
### viable count (volumetric)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCount`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
Sub-classes |[om:VolumetricSerratiaMarcescensCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricSerratiaMarcescensCount) (c)<br />[om:VolumetricStreptococcusUberisCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricStreptococcusUberisCount) (c)<br />[om:VolumetricEscherichiaColiCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricEscherichiaColiCount) (c)<br />[om:VolumetricColiformBacterieCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricColiformBacterieCount) (c)<br />[om:VolumetricListeriaMonocytogenesCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricListeriaMonocytogenesCount) (c)<br />[om:VolumetricEnterobacteriaceaeCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricEnterobacteriaceaeCount) (c)<br />[om:VolumetricEnterococcusCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricEnterococcusCount) (c)<br />[om:VolumetricSalmonellaCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricSalmonellaCount) (c)<br />[om:VolumetricStreptococcusAgalactiaeCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricStreptococcusAgalactiaeCount) (c)<br />[om:VolumetricStreptococcusDysgalactiaeCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricStreptococcusDysgalactiaeCount) (c)<br />[om:VolumetricCorynebacteriumBovisCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricCorynebacteriumBovisCount) (c)<br />[om:VolumetricYeastAndFungiCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricYeastAndFungiCount) (c)<br />[om:VolumetricKlebsiellaCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricKlebsiellaCount) (c)<br />[om:VolumetricStaphylococcusAureusCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricStaphylococcusAureusCount) (c)<br />[om:VolumetricCorynebacteriumCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricCorynebacteriumCount) (c)<br />
### volumetric viable count unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCountUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### yeast and fungi count (volumetric)
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#VolumetricYeastAndFungiCount`
Super-classes |[om:VolumetricViableCount](http://opendata.caceres.es/def/ontomunicipio#VolumetricViableCount) (c)<br />
### water mass fraction
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#WaterMassFraction`
Description | <p>The fraction of the mass of water in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### golflengte
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Wavelength`
Super-classes |[om:Length](http://opendata.caceres.es/def/ontomunicipio#Length) (c)<br />
Sub-classes |[om:PeakWavelength](http://opendata.caceres.es/def/ontomunicipio#PeakWavelength) (c)<br />[om:Cut-OffWavelength](http://opendata.caceres.es/def/ontomunicipio#Cut-OffWavelength) (c)<br />
### wavenumber
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Wavenumber`
Description | <p>Wavenumber is the number of repeating units of a propagating wave (the number of times a wave has the same phase) per unit of space.</p>
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:wavenumber-Dimension](http://opendata.caceres.es/def/ontomunicipio#wavenumber-Dimension) (c)<br />
### wave number unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#WavenumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### Weber number
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#WeberNumber`
Super-classes |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Restrictions |[om:hasDimension](http://opendata.caceres.es/def/ontomunicipio#hasDimension) (op) **value** [om:dimensionOne](http://opendata.caceres.es/def/ontomunicipio#dimensionOne) (c)<br />[om:hasValue](http://opendata.caceres.es/def/ontomunicipio#hasValue) (op) **only** ()<br />
### Weber number unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#WeberNumberUnit`
Super-classes |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
### weight
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Weight`
Description | <p>Weight is a force that attracts a body towards another (reference) body.</p>
Super-classes |[om:Force](http://opendata.caceres.es/def/ontomunicipio#Force) (c)<br />
### wetting angle
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#WettingAngle`
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
### whey protein aggregate mass fraction
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#WheyProteinAggregateMassFraction`
Description | <p>The fraction of the mass of whey protein aggregate in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### whey protein beads mass fraction
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#WheyProteinBeadsMassFraction`
Description | <p>The fraction of the mass of whey protein beads in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### whey protein mass fraction
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#WheyProteinMassFraction`
Description | <p>The fraction of the mass of whey protein in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### white light magnitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#WhiteLightMagnitude`
Super-classes |[om:Magnitude](http://opendata.caceres.es/def/ontomunicipio#Magnitude) (c)<br />
Sub-classes |[om:WhiteLightMagnitudeAtMinimumBrightness](http://opendata.caceres.es/def/ontomunicipio#WhiteLightMagnitudeAtMinimumBrightness) (c)<br />[om:WhiteLightMagnitudeAtMaximumBrightness](http://opendata.caceres.es/def/ontomunicipio#WhiteLightMagnitudeAtMaximumBrightness) (c)<br />
### white light magnitude at maximum brightness
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#WhiteLightMagnitudeAtMaximumBrightness`
Super-classes |[om:WhiteLightMagnitude](http://opendata.caceres.es/def/ontomunicipio#WhiteLightMagnitude) (c)<br />[om:MagnitudeAtMaximumBrightness](http://opendata.caceres.es/def/ontomunicipio#MagnitudeAtMaximumBrightness) (c)<br />
### white light magnitude at minimum brightness
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#WhiteLightMagnitudeAtMinimumBrightness`
Super-classes |[om:WhiteLightMagnitude](http://opendata.caceres.es/def/ontomunicipio#WhiteLightMagnitude) (c)<br />[om:MagnitudeAtMinimumBrightness](http://opendata.caceres.es/def/ontomunicipio#MagnitudeAtMinimumBrightness) (c)<br />
### breedte
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Width`
Super-classes |[om:Length](http://opendata.caceres.es/def/ontomunicipio#Length) (c)<br />
### work
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#Work`
Description | <p>Work is the energy when a force acts against resistance to produce motion in a body.</p>
Super-classes |[om:Energy](http://opendata.caceres.es/def/ontomunicipio#Energy) (c)<br />
### xanthan mass fraction
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#XanthanMassFraction`
Description | <p>The fraction of the mass of xanthan in a phenomenon</p>
Super-classes |[om:MassFraction](http://opendata.caceres.es/def/ontomunicipio#MassFraction) (c)<br />
### zenitafstand
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#ZenithDistance`
Description | <p>The angular distance on the celestial sphere measured along the great circle from the zenith to the celestial object. z = 90° - h.</p>
Super-classes |[om:Angle](http://opendata.caceres.es/def/ontomunicipio#Angle) (c)<br />
### 1040 nm Lockwood magnitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#_1040NanometreLockwoodMagnitude`
Description | <p>A magnitude in the 1.04 micrometre band of the photometric system introduced by G.W. Lockwood.</p>
Super-classes |[om:Magnitude](http://opendata.caceres.es/def/ontomunicipio#Magnitude) (c)<br />
### b magnitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#bMagnitude`
Description | <p>b Magnitude in the Strömgren photometric system with a peak wavelength at 467 nm and a peak-half-width of 18 nm.</p>
Super-classes |[om:StroemgrenMagnitude](http://opendata.caceres.es/def/ontomunicipio#StroemgrenMagnitude) (c)<br />
### g magnitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#gMagnitude`
Description | <p>g Magnitude in the Thuan and Gunn photometric system.</p>
Super-classes |[om:ThuanAndGunnMagnitude](http://opendata.caceres.es/def/ontomunicipio#ThuanAndGunnMagnitude) (c)<br />
### u magnitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#uMagnitude`
Description | <p>u Magnitude in the Strömgren photometric system with a peak wavelength at 350 nm and a peak-half-width of 30 nm.</p>
Super-classes |[om:StroemgrenMagnitude](http://opendata.caceres.es/def/ontomunicipio#StroemgrenMagnitude) (c)<br />
### v magnitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#vMagnitude`
Description | <p>v Magnitude in the Strömgren photometric system with a peak wavelength at 411 nm and a peak-half-width of 19 nm.</p>
Super-classes |[om:StroemgrenMagnitude](http://opendata.caceres.es/def/ontomunicipio#StroemgrenMagnitude) (c)<br />
### x range
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#xRange`
Super-classes |[om:Length](http://opendata.caceres.es/def/ontomunicipio#Length) (c)<br />
### xy 2D start-end distance
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#xy2DStartEndDistance`
Super-classes |[om:Distance](http://opendata.caceres.es/def/ontomunicipio#Distance) (c)<br />
### xy distance travelled
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#xyDistanceTravelled`
Super-classes |[om:Distance](http://opendata.caceres.es/def/ontomunicipio#Distance) (c)<br />
### y magnitude
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#yMagnitude`
Description | <p>y Magnitude in the Strömgren photometric system with a peak wavelength at 547 nm and a peak-half-width of 23 nm.</p>
Super-classes |[om:StroemgrenMagnitude](http://opendata.caceres.es/def/ontomunicipio#StroemgrenMagnitude) (c)<br />
### y range
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#yRange`
Super-classes |[om:Length](http://opendata.caceres.es/def/ontomunicipio#Length) (c)<br />
### z range
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#zRange`
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
IRI | `http://opendata.caceres.es/def/ontomunicipio#commonlyHasUnit`
Description | This property indicates a commonly-used unit.
Domain(s) |([om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c))<br />
Range(s) |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
[](hasaggregatefunction)
### has aggregate function
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#hasAggregateFunction`
Domain(s) |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Range(s) |[om:Function](http://opendata.caceres.es/def/ontomunicipio#Function) (c)<br />
[](hasbase)
### has base
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#hasBase`
Domain(s) |([om:UnitExponentiation](http://opendata.caceres.es/def/ontomunicipio#UnitExponentiation) (c))<br />
Range(s) |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
[](hasbasequantity)
### has base quantity
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#hasBaseQuantity`
Domain(s) |[om:SystemOfUnits](http://opendata.caceres.es/def/ontomunicipio#SystemOfUnits) (c)<br />
Range(s) |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
[](hasbaseunit)
### has base unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#hasBaseUnit`
Domain(s) |[om:SystemOfUnits](http://opendata.caceres.es/def/ontomunicipio#SystemOfUnits) (c)<br />
Range(s) |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
[](hascontext)
### has context
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#hasContext`
Domain(s) |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
[](hasdenominator)
### has denominator
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#hasDenominator`
Domain(s) |([om:UnitDivision](http://opendata.caceres.es/def/ontomunicipio#UnitDivision) (c))<br />
Range(s) |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
[](hasderivedquantity)
### has derived quantity
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#hasDerivedQuantity`
Domain(s) |[om:SystemOfUnits](http://opendata.caceres.es/def/ontomunicipio#SystemOfUnits) (c)<br />
Range(s) |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
[](hasderivedunit)
### has derived unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#hasDerivedUnit`
Domain(s) |[om:SystemOfUnits](http://opendata.caceres.es/def/ontomunicipio#SystemOfUnits) (c)<br />
Range(s) |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
[](hasdimension)
### has dimension
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#hasDimension`
Domain(s) |([om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c) or [om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c) or [om:Scale](http://opendata.caceres.es/def/ontomunicipio#Scale) (c))<br />
Range(s) |[om:Dimension](http://opendata.caceres.es/def/ontomunicipio#Dimension) (c)<br />
[](hasnumerator)
### has numerator
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#hasNumerator`
Domain(s) |([om:UnitDivision](http://opendata.caceres.es/def/ontomunicipio#UnitDivision) (c))<br />
Range(s) |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
[](hasphenomenon)
### has phenomenon
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#hasPhenomenon`
Domain(s) |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
[](haspoint)
### has point
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#hasPoint`
Domain(s) |([om:IntervalScale](http://opendata.caceres.es/def/ontomunicipio#IntervalScale) (c) or [om:RatioScale](http://opendata.caceres.es/def/ontomunicipio#RatioScale) (c) or [om:FixedPoint](http://opendata.caceres.es/def/ontomunicipio#FixedPoint) (c))<br />
Range(s) |[om:Point](http://opendata.caceres.es/def/ontomunicipio#Point) (c)<br />
[](hasprefix)
### has prefix
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#hasPrefix`
Domain(s) |[om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c)<br />
Range(s) |[om:Prefix](http://opendata.caceres.es/def/ontomunicipio#Prefix) (c)<br />
[](hasquantity)
### has quantity
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#hasQuantity`
Domain(s) |([om:SingularUnit](http://opendata.caceres.es/def/ontomunicipio#SingularUnit) (c) or [om:FixedPoint](http://opendata.caceres.es/def/ontomunicipio#FixedPoint) (c))<br />
Range(s) |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
[](hasscale)
### has scale
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#hasScale`
Domain(s) |([om:Scale](http://opendata.caceres.es/def/ontomunicipio#Scale) (c) or [om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c) or [om:ApplicationArea](http://opendata.caceres.es/def/ontomunicipio#ApplicationArea) (c))<br />
Range(s) |[om:Scale](http://opendata.caceres.es/def/ontomunicipio#Scale) (c)<br />
[](hasterm1)
### has term 1
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#hasTerm1`
Domain(s) |([om:UnitMultiplication](http://opendata.caceres.es/def/ontomunicipio#UnitMultiplication) (c))<br />
Range(s) |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
[](hasterm2)
### has term 2
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#hasTerm2`
Domain(s) |([om:UnitMultiplication](http://opendata.caceres.es/def/ontomunicipio#UnitMultiplication) (c))<br />
Range(s) |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
[](hasunit)
### has unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#hasUnit`
Domain(s) |([om:PrefixedUnit](http://opendata.caceres.es/def/ontomunicipio#PrefixedUnit) (c) or [om:UnitMultiple](http://opendata.caceres.es/def/ontomunicipio#UnitMultiple) (c) or [om:SingularUnit](http://opendata.caceres.es/def/ontomunicipio#SingularUnit) (c) or [om:IntervalScale](http://opendata.caceres.es/def/ontomunicipio#IntervalScale) (c) or [om:RatioScale](http://opendata.caceres.es/def/ontomunicipio#RatioScale) (c) or [om:Measure](http://opendata.caceres.es/def/ontomunicipio#Measure) (c))<br />
Range(s) |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
[](hasvalue)
### has value
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#hasValue`
Domain(s) |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
Range(s) |[om:Measure](http://opendata.caceres.es/def/ontomunicipio#Measure) (c)<br />[om:Point](http://opendata.caceres.es/def/ontomunicipio#Point) (c)<br />
[](usesquantity)
### uses quantity
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#usesQuantity`
Domain(s) |[om:ApplicationArea](http://opendata.caceres.es/def/ontomunicipio#ApplicationArea) (c)<br />
Range(s) |[om:Quantity](http://opendata.caceres.es/def/ontomunicipio#Quantity) (c)<br />
[](usesunit)
### uses unit
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#usesUnit`
Domain(s) |[om:ApplicationArea](http://opendata.caceres.es/def/ontomunicipio#ApplicationArea) (c)<br />
Range(s) |[om:Unit](http://opendata.caceres.es/def/ontomunicipio#Unit) (c)<br />
[](reference)
### reference
Property | Value
--- | ---
IRI | `http://www.wurvoc.org/bibliography/om-2/reference`
Domain(s) |[bibo:Document](http://purl.org/ontology/bibo/Document) (c)<br />

## Functional Properties
[has factor](#hasfactor),
[](hasfactor)
### has factor
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#hasFactor`
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
IRI | `http://opendata.caceres.es/def/ontomunicipio#hasExponent`
Domain(s) |([om:UnitExponentiation](http://opendata.caceres.es/def/ontomunicipio#UnitExponentiation) (c))<br />
Range(s) |[xsd:integer](http://www.w3.org/2001/XMLSchema#integer) (c)<br />
[](hasnumericalvalue)
### has numerical value
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#hasNumericalValue`
Domain(s) |([om:Measure](http://opendata.caceres.es/def/ontomunicipio#Measure) (c) or [om:Point](http://opendata.caceres.es/def/ontomunicipio#Point) (c))<br />
[](hasoff-set)
### has off-set
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#hasOff-Set`
Domain(s) |[om:Scale](http://opendata.caceres.es/def/ontomunicipio#Scale) (c)<br />
Range(s) |[xsd:float](http://www.w3.org/2001/XMLSchema#float) (c)<br />
[](hasSIamountofsubstancedimensionexponent)
### has SI amount of substance dimension exponent
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#hasSIAmountOfSubstanceDimensionExponent`
Domain(s) |[om:Dimension](http://opendata.caceres.es/def/ontomunicipio#Dimension) (c)<br />
Range(s) |[xsd:integer](http://www.w3.org/2001/XMLSchema#integer) (c)<br />
[](hasSIelectriccurrentdimensionexponent)
### has SI electric current dimension exponent
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#hasSIElectricCurrentDimensionExponent`
Domain(s) |[om:Dimension](http://opendata.caceres.es/def/ontomunicipio#Dimension) (c)<br />
Range(s) |[xsd:integer](http://www.w3.org/2001/XMLSchema#integer) (c)<br />
[](hasSIlengthdimensionexponent)
### has SI length dimension exponent
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#hasSILengthDimensionExponent`
Domain(s) |[om:Dimension](http://opendata.caceres.es/def/ontomunicipio#Dimension) (c)<br />
Range(s) |[xsd:integer](http://www.w3.org/2001/XMLSchema#integer) (c)<br />
[](hasSIluminousintensitydimensionexponent)
### has SI luminous intensity dimension exponent
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#hasSILuminousIntensityDimensionExponent`
Domain(s) |[om:Dimension](http://opendata.caceres.es/def/ontomunicipio#Dimension) (c)<br />
Range(s) |[xsd:integer](http://www.w3.org/2001/XMLSchema#integer) (c)<br />
[](hasSImassdimensionexponent)
### has SI mass dimension exponent
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#hasSIMassDimensionExponent`
Domain(s) |[om:Dimension](http://opendata.caceres.es/def/ontomunicipio#Dimension) (c)<br />
Range(s) |[xsd:integer](http://www.w3.org/2001/XMLSchema#integer) (c)<br />
[](hasSIthermodynamictemperaturedimensionexponent)
### has SI thermodynamic temperature dimension exponent
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#hasSIThermodynamicTemperatureDimensionExponent`
Domain(s) |[om:Dimension](http://opendata.caceres.es/def/ontomunicipio#Dimension) (c)<br />
Range(s) |[xsd:integer](http://www.w3.org/2001/XMLSchema#integer) (c)<br />
[](hasSItimedimensionexponent)
### has SI time dimension exponent
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#hasSITimeDimensionExponent`
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
IRI | `http://opendata.caceres.es/def/ontomunicipio#LaTeXCommand`
Description | OMLaTeX command that can be used to render this quantity or unit.
[](LaTeXsymbol)
### LaTeX symbol
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#LaTeXSymbol`
Description | OMLaTeX formatted symbol may include commands such as \unit and \E as defined in OMLaTeX.
[](abbreviation)
### abbreviation
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#abbreviation`
[](alternativeLaTeXsymbol)
### alternative LaTeX symbol
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#alternativeLaTeXSymbol`
Description | An alternative OMLaTeX formatted symbol, which may include commands such as \unit and \E as defined in OMLaTeX.
[](alternativelabel)
### alternative label
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#alternativeLabel`
[](alternativesymbol)
### alternative symbol
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#alternativeSymbol`
[](longcomment)
### longcomment
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#longcomment`
[](symbol)
### symbol
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#symbol`
[](unofficialabbreviation)
### unofficial abbreviation
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#unofficialAbbreviation`
Description | Used to specify abbreviations that are used in e.g. every day speech but are not defined in any standard.
Super-properties |[skos:hiddenLabel](http://www.w3.org/2004/02/skos/core#hiddenLabel) (ap)<br />
[](unofficiallabel)
### unofficial label
Property | Value
--- | ---
IRI | `http://opendata.caceres.es/def/ontomunicipio#unofficialLabel`
Description | Used to specify labels that are used in e.g. every day speech but are not defined in any standard.
Super-properties |[skos:hiddenLabel](http://www.w3.org/2004/02/skos/core#hiddenLabel) (ap)<br />
[](creator)
### creator
Property | Value
--- | ---
IRI | `http://purl.org/dc/elements/1.1/creator`
[](date)
### date
Property | Value
--- | ---
IRI | `http://purl.org/dc/elements/1.1/date`
[](identifier)
### identifier
Property | Value
--- | ---
IRI | `http://purl.org/dc/elements/1.1/identifier`
[](hiddenLabel)
### hiddenLabel
Property | Value
--- | ---
IRI | `http://www.w3.org/2004/02/skos/core#hiddenLabel`
[](illustration)
### illustration
Property | Value
--- | ---
IRI | `http://www.wurvoc.org/vocabularies/WV/illustration`
[](logo)
### logo
Property | Value
--- | ---
IRI | `http://www.wurvoc.org/vocabularies/WV/logo`

## Named Individuals
## Namespaces
* **bib**
  * `http://www.wurvoc.org/bibliography/om-2/`
* **bibo**
  * `http://purl.org/ontology/bibo/`
* **dc**
  * `http://purl.org/dc/elements/1.1/`
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
* **vw**
  * `http://www.wurvoc.org/vocabularies/WV/`
* **xml**
  * `http://www.w3.org/XML/1998/namespace`
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