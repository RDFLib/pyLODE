# Brick
Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE)


## Metadata
* **IRI**
  * `https://brickschema.org/schema/1.0.3/Brick`
* **Creators(s)**
  * None
* **Modified**
  * 2019-06-23
* **License**
  * [https://github.com/BrickSchema/brick-owl-dl/blob/master/LICENSE](https://github.com/BrickSchema/brick-owl-dl/blob/master/LICENSE)
* **Ontology RDF**
  * RDF ([brick.ttl](turtle))
### Description
<p>Brick is an open-source, BSD-licensed development effort to create a uniform schema for representing metadata in buildings.</p>

## Table of Contents
1. [Classes](#classes)
1. [Object Properties](#objectproperties)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Classes
[AHU](#AHU),
[Absorption_Chiller](#Absorption_Chiller),
[Active_Power](#Active_Power),
[Air](#Air),
[Air_Enthalpy_Sensor](#Air_Enthalpy_Sensor),
[Air_Flow_Dead_Band_Setpoint](#Air_Flow_Dead_Band_Setpoint),
[Air_Flow_Demand_Setpoint](#Air_Flow_Demand_Setpoint),
[Air_Flow_Sensor](#Air_Flow_Sensor),
[Air_Flow_Setpoint](#Air_Flow_Setpoint),
[Air_Flow_Setpoint_Limit](#Air_Flow_Setpoint_Limit),
[Air_Grains_Sensor](#Air_Grains_Sensor),
[Air_Handler_Unit](#Air_Handler_Unit),
[Air_Humidity_Sensor](#Air_Humidity_Sensor),
[Air_Quality](#Air_Quality),
[Air_Static_Pressure_Increase_Decrease_Step_Setpoint](#Air_Static_Pressure_Increase_Decrease_Step_Setpoint),
[Air_Temperature_Increase_Decrease_Step_Setpoint](#Air_Temperature_Increase_Decrease_Step_Setpoint),
[Air_Temperature_Sensor](#Air_Temperature_Sensor),
[Air_Temperature_Setpoint](#Air_Temperature_Setpoint),
[Alternating_Current_Frequency](#Alternating_Current_Frequency),
[Angle_Sensor](#Angle_Sensor),
[Apparent_Power](#Apparent_Power),
[Atmospheric_Pressure](#Atmospheric_Pressure),
[Average_Discharge_Air_Flow_Sensor](#Average_Discharge_Air_Flow_Sensor),
[Average_Exhaust_Air_Static_Pressure_Sensor:](#Average_Exhaust_Air_Static_Pressure_Sensor:),
[Average_Supply_Air_Flow_Sensor](#Average_Supply_Air_Flow_Sensor),
[Average_Zone_Temperature_Sensor](#Average_Zone_Temperature_Sensor),
[Basement](#Basement),
[Battery_Voltage_Sensor](#Battery_Voltage_Sensor),
[Blowdown_Water](#Blowdown_Water),
[Boiler](#Boiler),
[Booster_Fan](#Booster_Fan),
[Booster_Fan_Air_Flow_Sensor](#Booster_Fan_Air_Flow_Sensor),
[Building](#Building),
[Building_Static_Pressure_Sensor:](#Building_Static_Pressure_Sensor:),
[Building_Static_Pressure_Setpoint](#Building_Static_Pressure_Setpoint),
[Bypass_Air_Flow_Sensor](#Bypass_Air_Flow_Sensor),
[CO2](#CO2),
[CO2_Differential_Sensor](#CO2_Differential_Sensor),
[CO2_Level_Sensor](#CO2_Level_Sensor),
[CO2_Sensor](#CO2_Sensor),
[CO2_Setpoint](#CO2_Setpoint),
[CRAC](#CRAC),
[Capacity](#Capacity),
[Capacity_Sensor](#Capacity_Sensor),
[Centrifugal_Chiller](#Centrifugal_Chiller),
[Chilled_Water](#Chilled_Water),
[Chilled_Water_Differential_Pressure_Dead_Band_Setpoint](#Chilled_Water_Differential_Pressure_Dead_Band_Setpoint),
[Chilled_Water_Differential_Pressure_Increase_Decrease_Step_Setpoint](#Chilled_Water_Differential_Pressure_Increase_Decrease_Step_Setpoint),
[Chilled_Water_Differential_Pressure_Integral_Time_Setpoint](#Chilled_Water_Differential_Pressure_Integral_Time_Setpoint),
[Chilled_Water_Differential_Pressure_Load_Shed_Reset_Status](#Chilled_Water_Differential_Pressure_Load_Shed_Reset_Status),
[Chilled_Water_Differential_Pressure_Load_Shed_Setpoint](#Chilled_Water_Differential_Pressure_Load_Shed_Setpoint),
[Chilled_Water_Differential_Pressure_Load_Shed_Status](#Chilled_Water_Differential_Pressure_Load_Shed_Status),
[Chilled_Water_Differential_Pressure_Proportional_Band_Setpoint](#Chilled_Water_Differential_Pressure_Proportional_Band_Setpoint),
[Chilled_Water_Differential_Pressure_Sensor](#Chilled_Water_Differential_Pressure_Sensor),
[Chilled_Water_Differential_Pressure_Setpoint](#Chilled_Water_Differential_Pressure_Setpoint),
[Chilled_Water_Differential_Temperature_Sensor](#Chilled_Water_Differential_Temperature_Sensor),
[Chilled_Water_Discharge_Flow_Sensor](#Chilled_Water_Discharge_Flow_Sensor),
[Chilled_Water_Pump](#Chilled_Water_Pump),
[Chilled_Water_Pump_Differential_Pressure_Dead_Band_Setpoint](#Chilled_Water_Pump_Differential_Pressure_Dead_Band_Setpoint),
[Chilled_Water_Pump_Differential_Pressure_Integration_Time_Setpoint](#Chilled_Water_Pump_Differential_Pressure_Integration_Time_Setpoint),
[Chilled_Water_Return_Temperature_Sensor](#Chilled_Water_Return_Temperature_Sensor),
[Chilled_Water_Static_Pressure_Setpoint](#Chilled_Water_Static_Pressure_Setpoint),
[Chilled_Water_Supply_Flow_Sensor](#Chilled_Water_Supply_Flow_Sensor),
[Chilled_Water_Supply_Temperature_Sensor](#Chilled_Water_Supply_Temperature_Sensor),
[Chilled_Water_System](#Chilled_Water_System),
[Chilled_Water_Temperature_Sensor](#Chilled_Water_Temperature_Sensor),
[Chilled_Water_Valve](#Chilled_Water_Valve),
[Chiller](#Chiller),
[City](#City),
[Cloudage](#Cloudage),
[Coil](#Coil),
[Cold_Box](#Cold_Box),
[Complex_Power](#Complex_Power),
[Compressor](#Compressor),
[Computer_Room_Air_Conditioning](#Computer_Room_Air_Conditioning),
[Condenser](#Condenser),
[Condenser_Heat_Exchanger](#Condenser_Heat_Exchanger),
[Condenser_Water](#Condenser_Water),
[Condenser_Water_Pump](#Condenser_Water_Pump),
[Conductivity](#Conductivity),
[Conductivity_Sensor](#Conductivity_Sensor),
[Cooling_Coil](#Cooling_Coil),
[Cooling_Coil_Discharge_Air_Temperature_Sensor](#Cooling_Coil_Discharge_Air_Temperature_Sensor),
[Cooling_Demand_Setpoint](#Cooling_Demand_Setpoint),
[Cooling_Discharge_Air_Flow_Setpoint](#Cooling_Discharge_Air_Flow_Setpoint),
[Cooling_Discharge_Air_Temperature_Dead_Band_Setpoint](#Cooling_Discharge_Air_Temperature_Dead_Band_Setpoint),
[Cooling_Discharge_Air_Temperature_Integral_Time_Setpoint](#Cooling_Discharge_Air_Temperature_Integral_Time_Setpoint),
[Cooling_Discharge_Air_Temperature_Proportional_Band_Setpoint](#Cooling_Discharge_Air_Temperature_Proportional_Band_Setpoint),
[Cooling_On_Off_Status](#Cooling_On_Off_Status),
[Cooling_Request_Percent_Setpoint](#Cooling_Request_Percent_Setpoint),
[Cooling_Request_Setpoint](#Cooling_Request_Setpoint),
[Cooling_Supply_Air_Flow_Setpoint](#Cooling_Supply_Air_Flow_Setpoint),
[Cooling_Supply_Air_Temperature_Dead_Band_Setpoint](#Cooling_Supply_Air_Temperature_Dead_Band_Setpoint),
[Cooling_Supply_Air_Temperature_Integral_Time_Setpoint](#Cooling_Supply_Air_Temperature_Integral_Time_Setpoint),
[Cooling_Supply_Air_Temperature_Proportional_Band_Setpoint](#Cooling_Supply_Air_Temperature_Proportional_Band_Setpoint),
[Cooling_Tower_Fan](#Cooling_Tower_Fan),
[Current](#Current),
[Current_Angle](#Current_Angle),
[Current_Imbalance](#Current_Imbalance),
[Current_Magnitude](#Current_Magnitude),
[Current_Sensor](#Current_Sensor),
[Current_Total_Harmonic_Distortion](#Current_Total_Harmonic_Distortion),
[DC_Bus_Voltage_Sensor](#DC_Bus_Voltage_Sensor),
[Damper](#Damper),
[Damper_Position_Limit](#Damper_Position_Limit),
[Damper_Position_Sensor](#Damper_Position_Sensor),
[Damper_Position_Setpoint](#Damper_Position_Setpoint),
[Daytime](#Daytime),
[Dead_Band_Setpoint](#Dead_Band_Setpoint),
[Dehumidification_On_Off_Status](#Dehumidification_On_Off_Status),
[Deionised_Water_Conductivity_Sensor](#Deionised_Water_Conductivity_Sensor),
[Deionised_Water_Level_Sensor](#Deionised_Water_Level_Sensor),
[Demand_Sensor](#Demand_Sensor),
[Demand_Setpoint](#Demand_Setpoint),
[Dew_Point_Setpoint](#Dew_Point_Setpoint),
[Dewpoint](#Dewpoint),
[Dewpoint_Sensor](#Dewpoint_Sensor),
[Differential_Pressure_Dead_Band_Setpoint](#Differential_Pressure_Dead_Band_Setpoint),
[Differential_Pressure_Increase_Decrease_Step_Setpoint](#Differential_Pressure_Increase_Decrease_Step_Setpoint),
[Differential_Pressure_Integral_Time](#Differential_Pressure_Integral_Time),
[Differential_Pressure_Integral_Time_Setpoint](#Differential_Pressure_Integral_Time_Setpoint),
[Differential_Pressure_Load_Shed_Status](#Differential_Pressure_Load_Shed_Status),
[Differential_Pressure_Proportional_Band](#Differential_Pressure_Proportional_Band),
[Differential_Pressure_Sensor](#Differential_Pressure_Sensor),
[Differential_Pressure_Setpoint](#Differential_Pressure_Setpoint),
[Differential_Pressure_Setpoint_Limit](#Differential_Pressure_Setpoint_Limit),
[Differential_Speed_Sensor](#Differential_Speed_Sensor),
[Differential_Speed_Setpoint](#Differential_Speed_Setpoint),
[Dimmer](#Dimmer),
[Direction](#Direction),
[Direction_Sensor](#Direction_Sensor),
[Direction_Status](#Direction_Status),
[Disable_Status](#Disable_Status),
[Discharge_Air_Duct_Pressure_Status](#Discharge_Air_Duct_Pressure_Status),
[Discharge_Air_Flow_Demand_Setpoint](#Discharge_Air_Flow_Demand_Setpoint),
[Discharge_Air_Flow_Sensor](#Discharge_Air_Flow_Sensor),
[Discharge_Air_Flow_Setpoint](#Discharge_Air_Flow_Setpoint),
[Discharge_Air_Humidity_Sensor:](#Discharge_Air_Humidity_Sensor:),
[Discharge_Air_Static_Pressure_Integral_Time_Setpoint](#Discharge_Air_Static_Pressure_Integral_Time_Setpoint),
[Discharge_Air_Static_Pressure_Proportional_Band_Setpoint](#Discharge_Air_Static_Pressure_Proportional_Band_Setpoint),
[Discharge_Air_Static_Pressure_Sensor:](#Discharge_Air_Static_Pressure_Sensor:),
[Discharge_Air_Static_Pressure_Setpoint](#Discharge_Air_Static_Pressure_Setpoint),
[Discharge_Air_Temperature_Cooling_Setpoint](#Discharge_Air_Temperature_Cooling_Setpoint),
[Discharge_Air_Temperature_Dead_Band_Setpoint](#Discharge_Air_Temperature_Dead_Band_Setpoint),
[Discharge_Air_Temperature_Heating_Setpoint](#Discharge_Air_Temperature_Heating_Setpoint),
[Discharge_Air_Temperature_Proportional_Band_Setpoint](#Discharge_Air_Temperature_Proportional_Band_Setpoint),
[Discharge_Air_Temperature_Sensor](#Discharge_Air_Temperature_Sensor),
[Discharge_Air_Temperature_Setpoint](#Discharge_Air_Temperature_Setpoint),
[Discharge_Air_Velocity_Pressure_Sensor:](#Discharge_Air_Velocity_Pressure_Sensor:),
[Discharge_Fan_Air_Flow_Sensor](#Discharge_Fan_Air_Flow_Sensor),
[Domestic_Hot_Water_Supply_Temperature_Sensor](#Domestic_Hot_Water_Supply_Temperature_Sensor),
[Domestic_Hot_Water_Valve](#Domestic_Hot_Water_Valve),
[Domestic_Water](#Domestic_Water),
[Drive_Ready_Status](#Drive_Ready_Status),
[Dual_Band_Mode_Setpoint](#Dual_Band_Mode_Setpoint),
[Duration_Sensor](#Duration_Sensor),
[EconCycle_On_Off_Status](#EconCycle_On_Off_Status),
[Economizer](#Economizer),
[Economizer_Damper](#Economizer_Damper),
[Electric_Current](#Electric_Current),
[Electric_Energy](#Electric_Energy),
[Electric_Power](#Electric_Power),
[Electric_Voltage](#Electric_Voltage),
[Elevator](#Elevator),
[Emergency_Air_Flow_Status](#Emergency_Air_Flow_Status),
[Emergency_Generator_Status](#Emergency_Generator_Status),
[Emergency_Power_Off_Activated_By_High_Temperature_Status](#Emergency_Power_Off_Activated_By_High_Temperature_Status),
[Emergency_Power_Off_Activated_By_Leak_Detection_System_Status](#Emergency_Power_Off_Activated_By_Leak_Detection_System_Status),
[Emergency_Power_Off_Enable_Status](#Emergency_Power_Off_Enable_Status),
[Emergency_Power_Off_Status](#Emergency_Power_Off_Status),
[Emergency_Power_Off_System_Enable_Status](#Emergency_Power_Off_System_Enable_Status),
[Emergency_Push_Button_Status](#Emergency_Push_Button_Status),
[Enable_Status](#Enable_Status),
[Energy](#Energy),
[Energy_Sensor](#Energy_Sensor),
[Energy_Storage](#Energy_Storage),
[Entering_Water_Temperature_Sensor](#Entering_Water_Temperature_Sensor),
[Entering_Water_Temperature_Setpoint](#Entering_Water_Temperature_Setpoint),
[Enthalpy](#Enthalpy),
[Enthalpy_Sensor](#Enthalpy_Sensor),
[Enthalpy_Setpoint](#Enthalpy_Setpoint),
[Environment_Box](#Environment_Box),
[Equipment](#Equipment),
[Evaporative_Heat_Exchanger](#Evaporative_Heat_Exchanger),
[Even_Month_Status](#Even_Month_Status),
[Exhaust_Air](#Exhaust_Air),
[Exhaust_Air_Flow_Integral_Time_Setpoint](#Exhaust_Air_Flow_Integral_Time_Setpoint),
[Exhaust_Air_Flow_Proportional_Band_Setpoint](#Exhaust_Air_Flow_Proportional_Band_Setpoint),
[Exhaust_Air_Flow_Sensor](#Exhaust_Air_Flow_Sensor),
[Exhaust_Air_Flow_Setpoint](#Exhaust_Air_Flow_Setpoint),
[Exhaust_Air_Humidity_Sensor:](#Exhaust_Air_Humidity_Sensor:),
[Exhaust_Air_Stack_Flow_Dead_Band_Setpoint](#Exhaust_Air_Stack_Flow_Dead_Band_Setpoint),
[Exhaust_Air_Stack_Flow_Integral_Time_Setpoint](#Exhaust_Air_Stack_Flow_Integral_Time_Setpoint),
[Exhaust_Air_Stack_Flow_Sensor](#Exhaust_Air_Stack_Flow_Sensor),
[Exhaust_Air_Stack_Flow_Setpoint](#Exhaust_Air_Stack_Flow_Setpoint),
[Exhaust_Air_Static_Pressure_Proportional_Band_Setpoint](#Exhaust_Air_Static_Pressure_Proportional_Band_Setpoint),
[Exhaust_Air_Static_Pressure_Sensor:](#Exhaust_Air_Static_Pressure_Sensor:),
[Exhaust_Air_Static_Pressure_Setpoint](#Exhaust_Air_Static_Pressure_Setpoint),
[Exhaust_Air_Temperature_Sensor](#Exhaust_Air_Temperature_Sensor),
[Exhaust_Air_Velocity_Pressure_Sensor:](#Exhaust_Air_Velocity_Pressure_Sensor:),
[Exhaust_Damper](#Exhaust_Damper),
[Exhaust_Fan](#Exhaust_Fan),
[Fan](#Fan),
[Fan_Air_Flow_Sensor](#Fan_Air_Flow_Sensor),
[Fan_Air_Flow_Setpoint](#Fan_Air_Flow_Setpoint),
[Fan_Coil_Unit](#Fan_Coil_Unit),
[Fan_Start_Stop_Status](#Fan_Start_Stop_Status),
[Fan_Status](#Fan_Status),
[Fault_Indicator_Status](#Fault_Indicator_Status),
[Fault_Status](#Fault_Status),
[Filter](#Filter),
[Filter_Differential_Pressure_Sensor](#Filter_Differential_Pressure_Sensor),
[Filter_Status](#Filter_Status),
[Fire_Safety_System](#Fire_Safety_System),
[Fire_Zone](#Fire_Zone),
[Floor](#Floor),
[Flow](#Flow),
[Flow_Sensor](#Flow_Sensor),
[Flow_Setpoint](#Flow_Setpoint),
[Fluid](#Fluid),
[Freeze_Status](#Freeze_Status),
[Freezer](#Freezer),
[Frequency](#Frequency),
[Frequency_Sensor](#Frequency_Sensor),
[Frost](#Frost),
[Frost_Sensor](#Frost_Sensor),
[Fuel_Oil](#Fuel_Oil),
[Fume_Hood](#Fume_Hood),
[Fume_Hood_Air_Flow_Sensor](#Fume_Hood_Air_Flow_Sensor),
[Furniture](#Furniture),
[Gas](#Gas),
[Gasoline](#Gasoline),
[Grains](#Grains),
[HVAC](#HVAC),
[HVAC_Zone](#HVAC_Zone),
[Hail](#Hail),
[Hail_Sensor](#Hail_Sensor),
[Hand_Auto_Status](#Hand_Auto_Status),
[Heat_Exchanger](#Heat_Exchanger),
[Heat_Exchanger_Discharge_Water_Temperature_Proportional_Band_Setpoint](#Heat_Exchanger_Discharge_Water_Temperature_Proportional_Band_Setpoint),
[Heat_Exchanger_Supply_Water_Temperature_Dead_Band_Setpoint](#Heat_Exchanger_Supply_Water_Temperature_Dead_Band_Setpoint),
[Heat_Exchanger_Supply_Water_Temperature_Proportional_Band_Setpoint](#Heat_Exchanger_Supply_Water_Temperature_Proportional_Band_Setpoint),
[Heat_Exchanger_Supply_Water_Temperature_Sensor](#Heat_Exchanger_Supply_Water_Temperature_Sensor),
[Heat_Exchanger_System_Enable_Status](#Heat_Exchanger_System_Enable_Status),
[Heat_Wheel_Differential_Pressure_Sensor](#Heat_Wheel_Differential_Pressure_Sensor),
[Heat_Wheel_Discharge_Air_Temperature_Sensor](#Heat_Wheel_Discharge_Air_Temperature_Sensor),
[Heat_Wheel_Speed_Sensor](#Heat_Wheel_Speed_Sensor),
[Heat_Wheel_VFD](#Heat_Wheel_VFD),
[Heat_Wheel_Voltage_Sensor](#Heat_Wheel_Voltage_Sensor),
[Heating_Coil](#Heating_Coil),
[Heating_Demand_Setpoint](#Heating_Demand_Setpoint),
[Heating_Discharge_Air_Flow_Setpoint](#Heating_Discharge_Air_Flow_Setpoint),
[Heating_Discharge_Air_Temperature_Dead_Band_Setpoint](#Heating_Discharge_Air_Temperature_Dead_Band_Setpoint),
[Heating_Discharge_Air_Temperature_Integral_Time_Setpoint](#Heating_Discharge_Air_Temperature_Integral_Time_Setpoint),
[Heating_Discharge_Air_Temperature_Proportional_Band_Setpoint](#Heating_Discharge_Air_Temperature_Proportional_Band_Setpoint),
[Heating_On_Off_Status](#Heating_On_Off_Status),
[Heating_Request_Percent_Setpoint](#Heating_Request_Percent_Setpoint),
[Heating_Request_Setpoint](#Heating_Request_Setpoint),
[Heating_Supply_Air_Flow_Setpoint](#Heating_Supply_Air_Flow_Setpoint),
[Heating_Supply_Air_Temperature_Dead_Band_Setpoint](#Heating_Supply_Air_Temperature_Dead_Band_Setpoint),
[Heating_Supply_Air_Temperature_Integral_Time_Setpoint](#Heating_Supply_Air_Temperature_Integral_Time_Setpoint),
[Heating_Supply_Air_Temperature_Proportional_Band_Setpoint](#Heating_Supply_Air_Temperature_Proportional_Band_Setpoint),
[Heating_Valve](#Heating_Valve),
[Heating_Ventilation_Air_Conditioning_System](#Heating_Ventilation_Air_Conditioning_System),
[High_Humidity_Alarm_Setpoint](#High_Humidity_Alarm_Setpoint),
[High_Outside_Air_Lockout_Temperature_Differential_Sensor](#High_Outside_Air_Lockout_Temperature_Differential_Sensor),
[High_Static_Pressure_Cutout_Limit_Setpoint](#High_Static_Pressure_Cutout_Limit_Setpoint),
[High_Temperature_Hot_Water_Supply_Temperature_Sensor](#High_Temperature_Hot_Water_Supply_Temperature_Sensor),
[Highest_Zone_Temperature_Sensor](#Highest_Zone_Temperature_Sensor),
[Hold_Status](#Hold_Status),
[Hot_Box](#Hot_Box),
[Hot_Water](#Hot_Water),
[Hot_Water_Coil_Entering_Temperature_Sensor](#Hot_Water_Coil_Entering_Temperature_Sensor),
[Hot_Water_Differential_Pressure_Dead_Band_Setpoint](#Hot_Water_Differential_Pressure_Dead_Band_Setpoint),
[Hot_Water_Differential_Pressure_Integral_Time_Setpoint](#Hot_Water_Differential_Pressure_Integral_Time_Setpoint),
[Hot_Water_Differential_Pressure_Load_Shed_Reset_Status](#Hot_Water_Differential_Pressure_Load_Shed_Reset_Status),
[Hot_Water_Differential_Pressure_Load_Shed_Status](#Hot_Water_Differential_Pressure_Load_Shed_Status),
[Hot_Water_Differential_Pressure_Proportional_Band_Setpoint](#Hot_Water_Differential_Pressure_Proportional_Band_Setpoint),
[Hot_Water_Differential_Pressure_Sensor](#Hot_Water_Differential_Pressure_Sensor),
[Hot_Water_Differential_Pressure_Setpoint](#Hot_Water_Differential_Pressure_Setpoint),
[Hot_Water_Discharge_Temperature_Load_Shed_Status](#Hot_Water_Discharge_Temperature_Load_Shed_Status),
[Hot_Water_Pump](#Hot_Water_Pump),
[Hot_Water_Return_Temperature_Sensor](#Hot_Water_Return_Temperature_Sensor),
[Hot_Water_Static_Pressure_Setpoint](#Hot_Water_Static_Pressure_Setpoint),
[Hot_Water_Supply_Temperature_Load_Shed_Status](#Hot_Water_Supply_Temperature_Load_Shed_Status),
[Hot_Water_Supply_Temperature_Sensor](#Hot_Water_Supply_Temperature_Sensor),
[Hot_Water_System](#Hot_Water_System),
[Humidification_On_Off_Status](#Humidification_On_Off_Status),
[Humidifier_Fault_Status](#Humidifier_Fault_Status),
[Humidity](#Humidity),
[Humidity_Sensor](#Humidity_Sensor),
[Humidity_Setpoint](#Humidity_Setpoint),
[Ice](#Ice),
[Ice_Tank_Entering_Water_Temperature_Sensor](#Ice_Tank_Entering_Water_Temperature_Sensor),
[Ice_Tank_Leaving_Water_Temperature_Sensor](#Ice_Tank_Leaving_Water_Temperature_Sensor),
[Illuminance](#Illuminance),
[Increase_Decrease_Step_Setpoint](#Increase_Decrease_Step_Setpoint),
[Integral_Gain_Setpoint](#Integral_Gain_Setpoint),
[Integral_Time_Setpoint](#Integral_Time_Setpoint),
[Interface](#Interface),
[Irradiance](#Irradiance),
[Isolation_Valve](#Isolation_Valve),
[Laboratory](#Laboratory),
[Last_Fault_Code_Status](#Last_Fault_Code_Status),
[Lead_Lag_Status](#Lead_Lag_Status),
[Leaving_Water_Temperature_Sensor](#Leaving_Water_Temperature_Sensor),
[Leaving_Water_Temperature_Setpoint](#Leaving_Water_Temperature_Setpoint),
[Level](#Level),
[Lighting](#Lighting),
[Lighting_System](#Lighting_System),
[Lighting_Zone](#Lighting_Zone),
[Limit](#Limit),
[Liquid](#Liquid),
[Load_Current_Sensor](#Load_Current_Sensor),
[Load_Setpoint](#Load_Setpoint),
[Load_Shed_Differential_Pressure_Setpoint](#Load_Shed_Differential_Pressure_Setpoint),
[Load_Shed_Status](#Load_Shed_Status),
[Locally_On_Off_Status](#Locally_On_Off_Status),
[Location](#Location),
[Low_Humidity_Alarm_Setpoint](#Low_Humidity_Alarm_Setpoint),
[Low_Outside_Air_Lockout_Temperature_Differential_Sensor](#Low_Outside_Air_Lockout_Temperature_Differential_Sensor),
[Low_Outside_Air_Temperature_Enable_Setpoint](#Low_Outside_Air_Temperature_Enable_Setpoint),
[Lowest_Exhaust_Air_Static_Pressure_Sensor:](#Lowest_Exhaust_Air_Static_Pressure_Sensor:),
[Lowest_Zone_Temperature_Sensor](#Lowest_Zone_Temperature_Sensor),
[Luminaire](#Luminaire),
[Luminaire_Driver](#Luminaire_Driver),
[Luminance](#Luminance),
[Luminance_Sensor](#Luminance_Sensor),
[Luminance_Setpoint](#Luminance_Setpoint),
[Luminous_Flux](#Luminous_Flux),
[Luminous_Intensity](#Luminous_Intensity),
[Makeup_Water](#Makeup_Water),
[Manual_Auto_Status](#Manual_Auto_Status),
[Max_Air_Flow_Setpoint_Limit](#Max_Air_Flow_Setpoint_Limit),
[Max_Chilled_Water_Differential_Pressure_Setpoint_Limit](#Max_Chilled_Water_Differential_Pressure_Setpoint_Limit),
[Max_Cooling_Discharge_Air_Flow_Setpoint_Limit](#Max_Cooling_Discharge_Air_Flow_Setpoint_Limit),
[Max_Cooling_Supply_Air_Flow_Setpoint_Limit](#Max_Cooling_Supply_Air_Flow_Setpoint_Limit),
[Max_Damper_Position_Setpoint_Limit](#Max_Damper_Position_Setpoint_Limit),
[Max_Discharge_Air_Static_Pressure_Setpoint_Limit](#Max_Discharge_Air_Static_Pressure_Setpoint_Limit),
[Max_Heating_Discharge_Air_Flow_Setpoint_Limit](#Max_Heating_Discharge_Air_Flow_Setpoint_Limit),
[Max_Heating_Supply_Air_Flow_Setpoint_Limit](#Max_Heating_Supply_Air_Flow_Setpoint_Limit),
[Max_Hot_Water_Differential_Pressure_Setpoint_Limit](#Max_Hot_Water_Differential_Pressure_Setpoint_Limit),
[Max_Limit](#Max_Limit),
[Max_Load_Setpoint](#Max_Load_Setpoint),
[Max_Occupied_Cooling_Discharge_Air_Flow_Setpoint_Limit](#Max_Occupied_Cooling_Discharge_Air_Flow_Setpoint_Limit),
[Max_Occupied_Cooling_Supply_Air_Flow_Setpoint_Limit](#Max_Occupied_Cooling_Supply_Air_Flow_Setpoint_Limit),
[Max_Occupied_Heating_Discharge_Air_Flow_Setpoint_Limit](#Max_Occupied_Heating_Discharge_Air_Flow_Setpoint_Limit),
[Max_Occupied_Heating_Supply_Air_Flow_Setpoint_Limit](#Max_Occupied_Heating_Supply_Air_Flow_Setpoint_Limit),
[Max_Return_Air_CO2_Setpoint](#Max_Return_Air_CO2_Setpoint),
[Max_Speed_Setpoint_Limit](#Max_Speed_Setpoint_Limit),
[Max_Static_Pressure_Setpoint_Limit](#Max_Static_Pressure_Setpoint_Limit),
[Max_Supply_Air_Static_Pressure_Setpoint_Limit](#Max_Supply_Air_Static_Pressure_Setpoint_Limit),
[Max_Unoccupied_Cooling_Discharge_Air_Flow_Setpoint_Limit](#Max_Unoccupied_Cooling_Discharge_Air_Flow_Setpoint_Limit),
[Max_Unoccupied_Cooling_Supply_Air_Flow_Setpoint_Limit](#Max_Unoccupied_Cooling_Supply_Air_Flow_Setpoint_Limit),
[Max_Unoccupied_Heating_Discharge_Air_Flow_Setpoint_Limit](#Max_Unoccupied_Heating_Discharge_Air_Flow_Setpoint_Limit),
[Max_Unoccupied_Heating_Supply_Air_Flow_Setpoint_Limit](#Max_Unoccupied_Heating_Supply_Air_Flow_Setpoint_Limit),
[Medium_Temperature_Hot_Water_Differential_Pressure_Load_Shed_Setpoint](#Medium_Temperature_Hot_Water_Differential_Pressure_Load_Shed_Setpoint),
[Medium_Temperature_Hot_Water_Differential_Pressure_Sensor](#Medium_Temperature_Hot_Water_Differential_Pressure_Sensor),
[Medium_Temperature_Hot_Water_Supply_Temperature_Sensor](#Medium_Temperature_Hot_Water_Supply_Temperature_Sensor),
[Meter](#Meter),
[Min_Air_Flow_Setpoint_Limit](#Min_Air_Flow_Setpoint_Limit),
[Min_Chilled_Water_Differential_Pressure_Setpoint_Limit](#Min_Chilled_Water_Differential_Pressure_Setpoint_Limit),
[Min_Cooling_Discharge_Air_Flow_Setpoint_Limit](#Min_Cooling_Discharge_Air_Flow_Setpoint_Limit),
[Min_Cooling_Supply_Air_Flow_Setpoint_Limit](#Min_Cooling_Supply_Air_Flow_Setpoint_Limit),
[Min_Damper_Position_Setpoint_Limit](#Min_Damper_Position_Setpoint_Limit),
[Min_Discharge_Air_Static_Pressure_Setpoint_Limit](#Min_Discharge_Air_Static_Pressure_Setpoint_Limit),
[Min_Heating_Discharge_Air_Flow_Setpoint_Limit](#Min_Heating_Discharge_Air_Flow_Setpoint_Limit),
[Min_Heating_Supply_Air_Flow_Setpoint_Limit](#Min_Heating_Supply_Air_Flow_Setpoint_Limit),
[Min_Hot_Water_Differential_Pressure_Setpoint_Limit](#Min_Hot_Water_Differential_Pressure_Setpoint_Limit),
[Min_Limit](#Min_Limit),
[Min_Occupied_Cooling_Discharge_Air_Flow_Setpoint_Limit](#Min_Occupied_Cooling_Discharge_Air_Flow_Setpoint_Limit),
[Min_Occupied_Cooling_Supply_Air_Flow_Setpoint_Limit](#Min_Occupied_Cooling_Supply_Air_Flow_Setpoint_Limit),
[Min_Occupied_Heating_Discharge_Air_Flow_Setpoint_Limit](#Min_Occupied_Heating_Discharge_Air_Flow_Setpoint_Limit),
[Min_Occupied_Heating_Supply_Air_Flow_Setpoint_Limit](#Min_Occupied_Heating_Supply_Air_Flow_Setpoint_Limit),
[Min_Outside_Air_Flow_Setpoint_Limit](#Min_Outside_Air_Flow_Setpoint_Limit),
[Min_Speed_Setpoint_Limit](#Min_Speed_Setpoint_Limit),
[Min_Static_Pressure_Setpoint_Limit](#Min_Static_Pressure_Setpoint_Limit),
[Min_Supply_Air_Static_Pressure_Setpoint_Limit](#Min_Supply_Air_Static_Pressure_Setpoint_Limit),
[Min_Unoccupied_Cooling_Discharge_Air_Flow_Setpoint_Limit](#Min_Unoccupied_Cooling_Discharge_Air_Flow_Setpoint_Limit),
[Min_Unoccupied_Cooling_Supply_Air_Flow_Setpoint_Limit](#Min_Unoccupied_Cooling_Supply_Air_Flow_Setpoint_Limit),
[Min_Unoccupied_Heating_Discharge_Air_Flow_Setpoint_Limit](#Min_Unoccupied_Heating_Discharge_Air_Flow_Setpoint_Limit),
[Min_Unoccupied_Heating_Supply_Air_Flow_Setpoint_Limit](#Min_Unoccupied_Heating_Supply_Air_Flow_Setpoint_Limit),
[Mixed_Air](#Mixed_Air),
[Mixed_Air_Filter](#Mixed_Air_Filter),
[Mixed_Air_Temperature_Sensor](#Mixed_Air_Temperature_Sensor),
[Mixed_Air_Temperature_Setpoint](#Mixed_Air_Temperature_Setpoint),
[Mode_Setpoint](#Mode_Setpoint),
[Mode_Status](#Mode_Status),
[Motion_Sensor](#Motion_Sensor),
[Motor_Current_Sensor](#Motor_Current_Sensor),
[Motor_Direction_Status](#Motor_Direction_Status),
[Motor_Speed_Sensor](#Motor_Speed_Sensor),
[Motor_Start_Stop_Status](#Motor_Start_Stop_Status),
[Motor_Torque_Sensor](#Motor_Torque_Sensor),
[Natural_Gas](#Natural_Gas),
[Occupancy_Sensor](#Occupancy_Sensor),
[Occupancy_Status](#Occupancy_Status),
[Occupied_Cooling_Supply_Air_Flow_Setpoint](#Occupied_Cooling_Supply_Air_Flow_Setpoint),
[Occupied_Cooling_Temperature_Dead_Band_Setpoint](#Occupied_Cooling_Temperature_Dead_Band_Setpoint),
[Occupied_Heating_Supply_Air_Flow_Setpoint](#Occupied_Heating_Supply_Air_Flow_Setpoint),
[Occupied_Heating_Temperature_Dead_Band_Setpoint](#Occupied_Heating_Temperature_Dead_Band_Setpoint),
[Occupied_Mode_Setpoint](#Occupied_Mode_Setpoint),
[Occupied_Mode_Status](#Occupied_Mode_Status),
[Occupied_Supply_Air_Flow_Setpoint](#Occupied_Supply_Air_Flow_Setpoint),
[Off_Status](#Off_Status),
[Oil](#Oil),
[On_Off_Status](#On_Off_Status),
[On_Status](#On_Status),
[On_Timer_Sensor](#On_Timer_Sensor),
[Open_Heating_Valve_Outside_Air_Temperature_Setpoint](#Open_Heating_Valve_Outside_Air_Temperature_Setpoint),
[Operating_Mode_Status](#Operating_Mode_Status),
[Operative_Temperature](#Operative_Temperature),
[Output_Frequency_Sensor](#Output_Frequency_Sensor),
[Output_Voltage_Sensor](#Output_Voltage_Sensor),
[Outside](#Outside),
[Outside_Air](#Outside_Air),
[Outside_Air_CO2_Sensor](#Outside_Air_CO2_Sensor),
[Outside_Air_Dewpoint_Sensor](#Outside_Air_Dewpoint_Sensor),
[Outside_Air_Enthalpy_Sensor](#Outside_Air_Enthalpy_Sensor),
[Outside_Air_Flow_Sensor](#Outside_Air_Flow_Sensor),
[Outside_Air_Flow_Setpoint](#Outside_Air_Flow_Setpoint),
[Outside_Air_Grains_Sensor](#Outside_Air_Grains_Sensor),
[Outside_Air_Humidity_Sensor:](#Outside_Air_Humidity_Sensor:),
[Outside_Air_Lockout_Temperature_Differential_Sensor](#Outside_Air_Lockout_Temperature_Differential_Sensor),
[Outside_Air_Lockout_Temperature_Setpoint](#Outside_Air_Lockout_Temperature_Setpoint),
[Outside_Air_Temperature_Sensor](#Outside_Air_Temperature_Sensor),
[Outside_Air_Temperature_Setpoint](#Outside_Air_Temperature_Setpoint),
[Outside_Damper](#Outside_Damper),
[Outside_Luminance_Sensor](#Outside_Luminance_Sensor),
[Overridden_Off_Status](#Overridden_Off_Status),
[Overridden_On_Status](#Overridden_On_Status),
[Overridden_Status](#Overridden_Status),
[PIR_Sensor](#PIR_Sensor),
[PM10](#PM10),
[PM25](#PM25),
[Peak_Power_Demand_Sensor](#Peak_Power_Demand_Sensor),
[Photovoltaic_Current_Output_Sensor](#Photovoltaic_Current_Output_Sensor),
[Piezoelectric_Sensor](#Piezoelectric_Sensor),
[PlugStrip](#PlugStrip),
[Point](#Point),
[Power](#Power),
[Power_Factor](#Power_Factor),
[Power_System](#Power_System),
[PreHeat_Coil_Entering_Air_Temperature_Sensor](#PreHeat_Coil_Entering_Air_Temperature_Sensor),
[PreHeat_Coil_Leaving_Air_Temperature_Sensor](#PreHeat_Coil_Leaving_Air_Temperature_Sensor),
[Pre_Filter_Status](#Pre_Filter_Status),
[Precipitation](#Precipitation),
[Preheat_Demand_Setpoint](#Preheat_Demand_Setpoint),
[Preheat_Discharge_Air_Temperature_Sensor](#Preheat_Discharge_Air_Temperature_Sensor),
[Preheat_Hot_Water_Valve](#Preheat_Hot_Water_Valve),
[Preheat_Valve_VFD](#Preheat_Valve_VFD),
[Pressure](#Pressure),
[Pressure_Sensor](#Pressure_Sensor),
[Pressure_Setpoint](#Pressure_Setpoint),
[Pressure_Status](#Pressure_Status),
[Proportional_Band_Setpoint](#Proportional_Band_Setpoint),
[Pump](#Pump),
[Pump_Start_Stop_Status](#Pump_Start_Stop_Status),
[Quantity](#Quantity),
[Radiant_Temperature](#Radiant_Temperature),
[Rain_Duration_Sensor](#Rain_Duration_Sensor),
[Rain_Sensor](#Rain_Sensor),
[Reactive_Power](#Reactive_Power),
[Reheat_Valve](#Reheat_Valve),
[Relative_Humidity_Sensor:](#Relative_Humidity_Sensor:),
[Remotely_On_Off_Status](#Remotely_On_Off_Status),
[Reset_Setpoint](#Reset_Setpoint),
[Return_Air](#Return_Air),
[Return_Air_CO2_Sensor](#Return_Air_CO2_Sensor),
[Return_Air_CO2_Setpoint](#Return_Air_CO2_Setpoint),
[Return_Air_Dewpoint_Sensor](#Return_Air_Dewpoint_Sensor),
[Return_Air_Enthalpy_Sensor](#Return_Air_Enthalpy_Sensor),
[Return_Air_Flow_Sensor](#Return_Air_Flow_Sensor),
[Return_Air_Grains_Sensor](#Return_Air_Grains_Sensor),
[Return_Air_Humidity_Sensor:](#Return_Air_Humidity_Sensor:),
[Return_Air_Temperature_Sensor](#Return_Air_Temperature_Sensor),
[Return_Damper](#Return_Damper),
[Return_Discharge_Fan_Differential_Speed_Setpoint](#Return_Discharge_Fan_Differential_Speed_Setpoint),
[Return_Fan](#Return_Fan),
[Return_Fan_Air_Flow_Sensor](#Return_Fan_Air_Flow_Sensor),
[Return_Fan_Differential_Speed_Sensor](#Return_Fan_Differential_Speed_Sensor),
[Return_Fan_Differential_Speed_Setpoint](#Return_Fan_Differential_Speed_Setpoint),
[Return_Supply_Fan_Differential_Speed_Setpoint](#Return_Supply_Fan_Differential_Speed_Setpoint),
[Return_Water_Temperature_Sensor](#Return_Water_Temperature_Sensor),
[Roof](#Roof),
[Rooftop_Unit](#Rooftop_Unit),
[Room](#Room),
[Room_Air_Temperature_Setpoint](#Room_Air_Temperature_Setpoint),
[Run_Direction_Status](#Run_Direction_Status),
[Run_Enable_Status](#Run_Enable_Status),
[Run_Status](#Run_Status),
[Run_Time_Sensor](#Run_Time_Sensor),
[Sensor](#Sensor),
[Server_Room](#Server_Room),
[Setpoint](#Setpoint),
[Shading_System](#Shading_System),
[Solar_Azimuth_Angle_Sensor](#Solar_Azimuth_Angle_Sensor),
[Solar_Irradiance](#Solar_Irradiance),
[Solar_Panel](#Solar_Panel),
[Solar_Radiance_Sensor](#Solar_Radiance_Sensor),
[Solar_Zenith_Angle_Sensor](#Solar_Zenith_Angle_Sensor),
[Solid](#Solid),
[Space](#Space),
[Space_Heater](#Space_Heater),
[Speed](#Speed),
[Speed_Sensor](#Speed_Sensor),
[Speed_Setpoint](#Speed_Setpoint),
[Speed_Setpoint_Limit](#Speed_Setpoint_Limit),
[Speed_Status](#Speed_Status),
[Stages_Status](#Stages_Status),
[Standby_Fan](#Standby_Fan),
[Standby_Glycool_Unit_On_Off_Status](#Standby_Glycool_Unit_On_Off_Status),
[Standby_Unit_On_Off_Status](#Standby_Unit_On_Off_Status),
[Start_Stop_Status](#Start_Stop_Status),
[Static_Pressure](#Static_Pressure),
[Static_Pressure_Dead_Band_Setpoint](#Static_Pressure_Dead_Band_Setpoint),
[Static_Pressure_Increase_Decrease_Step_Setpoint](#Static_Pressure_Increase_Decrease_Step_Setpoint),
[Static_Pressure_Integral_Time_Setpoint](#Static_Pressure_Integral_Time_Setpoint),
[Static_Pressure_Proportional_Band_Setpoint](#Static_Pressure_Proportional_Band_Setpoint),
[Static_Pressure_Sensor](#Static_Pressure_Sensor),
[Static_Pressure_Setpoint](#Static_Pressure_Setpoint),
[Static_Pressure_Setpoint_Limit](#Static_Pressure_Setpoint_Limit),
[Status](#Status),
[Steam](#Steam),
[Steam_System](#Steam_System),
[Substance](#Substance),
[Supply_Air](#Supply_Air),
[Supply_Air_Duct_Pressure_Status](#Supply_Air_Duct_Pressure_Status),
[Supply_Air_Flow_Demand_Setpoint](#Supply_Air_Flow_Demand_Setpoint),
[Supply_Air_Flow_Sensor](#Supply_Air_Flow_Sensor),
[Supply_Air_Flow_Setpoint](#Supply_Air_Flow_Setpoint),
[Supply_Air_Humidity_Sensor:](#Supply_Air_Humidity_Sensor:),
[Supply_Air_Static_Pressure_Integral_Time_Setpoint](#Supply_Air_Static_Pressure_Integral_Time_Setpoint),
[Supply_Air_Static_Pressure_Proportional_Band_Setpoint](#Supply_Air_Static_Pressure_Proportional_Band_Setpoint),
[Supply_Air_Static_Pressure_Sensor:](#Supply_Air_Static_Pressure_Sensor:),
[Supply_Air_Static_Pressure_Setpoint](#Supply_Air_Static_Pressure_Setpoint),
[Supply_Air_Temperature_Dead_Band_Setpoint](#Supply_Air_Temperature_Dead_Band_Setpoint),
[Supply_Air_Temperature_Proportional_Band_Setpoint](#Supply_Air_Temperature_Proportional_Band_Setpoint),
[Supply_Air_Velocity_Pressure_Sensor:](#Supply_Air_Velocity_Pressure_Sensor:),
[Supply_Fan](#Supply_Fan),
[Supply_Fan_Air_Flow_Sensor](#Supply_Fan_Air_Flow_Sensor),
[Supply_Water_Differential_Pressure_Dead_Band_Setpoint](#Supply_Water_Differential_Pressure_Dead_Band_Setpoint),
[Supply_Water_Differential_Pressure_Integral_Time_Setpoint](#Supply_Water_Differential_Pressure_Integral_Time_Setpoint),
[Supply_Water_Differential_Pressure_Proportional_Band_Setpoint](#Supply_Water_Differential_Pressure_Proportional_Band_Setpoint),
[Supply_Water_Flow_Sensor](#Supply_Water_Flow_Sensor),
[Supply_Water_Temperature_Dead_Band_Setpoint](#Supply_Water_Temperature_Dead_Band_Setpoint),
[Supply_Water_Temperature_Integral_Time_Setpoint](#Supply_Water_Temperature_Integral_Time_Setpoint),
[Supply_Water_Temperature_Proportional_Band_Setpoint](#Supply_Water_Temperature_Proportional_Band_Setpoint),
[Switch](#Switch),
[System_Mode_Status](#System_Mode_Status),
[System_Shutdown_Status](#System_Shutdown_Status),
[System_Status](#System_Status),
[TVOC](#TVOC),
[Tag](#Tag),
[Temperature](#Temperature),
[Temperature_Dead_Band_Setpoint](#Temperature_Dead_Band_Setpoint),
[Temperature_Increase_Decrease_Step_Setpoint](#Temperature_Increase_Decrease_Step_Setpoint),
[Temperature_Sensor](#Temperature_Sensor),
[Temperature_Setpoint](#Temperature_Setpoint),
[Temporary_Occupancy_Status](#Temporary_Occupancy_Status),
[Terminal_Unit](#Terminal_Unit),
[Thermal_Energy](#Thermal_Energy),
[Thermal_Energy_Storage_Discharge_Water_Differential_Pressure_ProportionalBandSetpoint](#Thermal_Energy_Storage_Discharge_Water_Differential_Pressure_ProportionalBandSetpoint),
[Thermal_Energy_Storage_Supply_Water_Differential_Pressure_Dead_Band_Setpoint](#Thermal_Energy_Storage_Supply_Water_Differential_Pressure_Dead_Band_Setpoint),
[Thermal_Energy_Storage_Supply_Water_Differential_Pressure_Proportional_BandSetpoint](#Thermal_Energy_Storage_Supply_Water_Differential_Pressure_Proportional_BandSetpoint),
[Thermal_Power](#Thermal_Power),
[Thermostat](#Thermostat),
[Torque_Sensor](#Torque_Sensor),
[Touchpanel](#Touchpanel),
[Trace_Heat_Sensor](#Trace_Heat_Sensor),
[Turn_Off_Status](#Turn_Off_Status),
[Unoccupied_Mode_Setpoint](#Unoccupied_Mode_Setpoint),
[VFD](#VFD),
[Valve](#Valve),
[Variable_Air_Volume_Box](#Variable_Air_Volume_Box),
[Variable_Air_Volume_Box_With_Reheat](#Variable_Air_Volume_Box_With_Reheat),
[Variable_Frequency_Drive](#Variable_Frequency_Drive),
[Velocity_Pressure_Sensor:](#Velocity_Pressure_Sensor:),
[Velocity_Pressure_Setpoint](#Velocity_Pressure_Setpoint),
[Vent_Operating_Mode_Status](#Vent_Operating_Mode_Status),
[Voltage](#Voltage),
[Voltage_Angle](#Voltage_Angle),
[Voltage_Imbalance](#Voltage_Imbalance),
[Voltage_Magnitude](#Voltage_Magnitude),
[Voltage_Sensor](#Voltage_Sensor),
[Water](#Water),
[Water_Flow_Sensor](#Water_Flow_Sensor),
[Water_Level_Sensor](#Water_Level_Sensor),
[Water_Pump](#Water_Pump),
[Water_System](#Water_System),
[Water_Temperature_Sensor](#Water_Temperature_Sensor),
[Water_Temperature_Setpoint](#Water_Temperature_Setpoint),
[Water_Valve](#Water_Valve),
[Weather](#Weather),
[Weather_Condition](#Weather_Condition),
[Wet_Bulb_Temperature](#Wet_Bulb_Temperature),
[Wind_Direction](#Wind_Direction),
[Wind_Direction_Sensor](#Wind_Direction_Sensor),
[Wind_Speed](#Wind_Speed),
[Wind_Speed_Sensor](#Wind_Speed_Sensor),
[Wing](#Wing),
[Zone](#Zone),
[Zone_Air_Temperature_Sensor](#Zone_Air_Temperature_Sensor),
[Zone_Humidity_Sensor:](#Zone_Humidity_Sensor:),
[Zone_Temperature_Sensor](#Zone_Temperature_Sensor),
### AHU
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#AHU`
Super-classes |[brick:HVAC](HVAC) (c)<br />
Sub-classes |[brick:Rooftop_Unit](Rooftop_Unit) (c)<br />
In range of |[brick:ahuRef](ahuRef) (op)<br />
### Absorption_Chiller
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Absorption_Chiller`
Super-classes |[brick:Chiller](Chiller) (c)<br />
### Active_Power
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Active_Power`
Super-classes |[brick:Electric_Power](Electric_Power) (c)<br />
### Air
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Air`
Super-classes |[brick:Gas](Gas) (c)<br />
Sub-classes |[brick:Mixed_Air](Mixed_Air) (c)<br />[brick:Return_Air](Return_Air) (c)<br />[brick:Exhaust_Air](Exhaust_Air) (c)<br />[brick:Supply_Air](Supply_Air) (c)<br />[brick:Outside_Air](Outside_Air) (c)<br />
### Air_Enthalpy_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Air_Enthalpy_Sensor`
Super-classes |[brick:Enthalpy_Sensor](Enthalpy_Sensor) (c)<br />
Sub-classes |[brick:Outside_Air_Enthalpy_Sensor](Outside_Air_Enthalpy_Sensor) (c)<br />[brick:Return_Air_Enthalpy_Sensor](Return_Air_Enthalpy_Sensor) (c)<br />
### Air_Flow_Dead_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Dead_Band_Setpoint`
Super-classes |[brick:Dead_Band_Setpoint](Dead_Band_Setpoint) (c)<br />
Sub-classes |[brick:Exhaust_Air_Stack_Flow_Dead_Band_Setpoint](Exhaust_Air_Stack_Flow_Dead_Band_Setpoint) (c)<br />
### Air_Flow_Demand_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Demand_Setpoint`
Super-classes |[brick:Air_Flow_Setpoint](Air_Flow_Setpoint) (c)<br />[brick:Demand_Setpoint](Demand_Setpoint) (c)<br />
Sub-classes |[brick:Discharge_Air_Flow_Demand_Setpoint](Discharge_Air_Flow_Demand_Setpoint) (c)<br />[brick:Supply_Air_Flow_Demand_Setpoint](Supply_Air_Flow_Demand_Setpoint) (c)<br />
### Air_Flow_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Sensor`
Super-classes |[brick:Flow_Sensor](Flow_Sensor) (c)<br />
Sub-classes |[brick:Fan_Air_Flow_Sensor](Fan_Air_Flow_Sensor) (c)<br />[brick:Supply_Air_Flow_Sensor](Supply_Air_Flow_Sensor) (c)<br />[brick:Fume_Hood_Air_Flow_Sensor](Fume_Hood_Air_Flow_Sensor) (c)<br />[brick:Return_Air_Flow_Sensor](Return_Air_Flow_Sensor) (c)<br />[brick:Bypass_Air_Flow_Sensor](Bypass_Air_Flow_Sensor) (c)<br />[brick:Discharge_Air_Flow_Sensor](Discharge_Air_Flow_Sensor) (c)<br />[brick:Exhaust_Air_Flow_Sensor](Exhaust_Air_Flow_Sensor) (c)<br />[brick:Outside_Air_Flow_Sensor](Outside_Air_Flow_Sensor) (c)<br />
### Air_Flow_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Setpoint`
Super-classes |[brick:Flow_Setpoint](Flow_Setpoint) (c)<br />
Sub-classes |[brick:Fan_Air_Flow_Setpoint](Fan_Air_Flow_Setpoint) (c)<br />[brick:Supply_Air_Flow_Setpoint](Supply_Air_Flow_Setpoint) (c)<br />[brick:Outside_Air_Flow_Setpoint](Outside_Air_Flow_Setpoint) (c)<br />[brick:Air_Flow_Demand_Setpoint](Air_Flow_Demand_Setpoint) (c)<br />[brick:Exhaust_Air_Flow_Setpoint](Exhaust_Air_Flow_Setpoint) (c)<br />[brick:Discharge_Air_Flow_Setpoint](Discharge_Air_Flow_Setpoint) (c)<br />
### Air_Flow_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Setpoint_Limit`
Super-classes |[brick:Limit](Limit) (c)<br />
Sub-classes |[brick:Max_Air_Flow_Setpoint_Limit](Max_Air_Flow_Setpoint_Limit) (c)<br />[brick:Min_Air_Flow_Setpoint_Limit](Min_Air_Flow_Setpoint_Limit) (c)<br />
### Air_Grains_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Air_Grains_Sensor`
Super-classes |[brick:Sensor](Sensor) (c)<br />
Sub-classes |[brick:Outside_Air_Grains_Sensor](Outside_Air_Grains_Sensor) (c)<br />[brick:Return_Air_Grains_Sensor](Return_Air_Grains_Sensor) (c)<br />
### Air_Handler_Unit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Air_Handler_Unit`
Description | <p>Assembly consisting of sections containing a fan or fans and other necessary equipment to perform one or more of the following functions: circulating, filtration, heating, cooling, heat recovery, humidifying, dehumidifying, and mixing of air. Is usually connected to an air-distribution system.</p>
Super-classes |[brick:HVAC](HVAC) (c)<br />
### Air_Humidity_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Air_Humidity_Sensor`
Super-classes |[brick:Humidity_Sensor](Humidity_Sensor) (c)<br />
Sub-classes |[brick:Relative_Humidity_Sensor:](Relative_Humidity_Sensor:) (c)<br />[brick:Outside_Air_Humidity_Sensor:](Outside_Air_Humidity_Sensor:) (c)<br />[brick:Zone_Humidity_Sensor:](Zone_Humidity_Sensor:) (c)<br />[brick:Supply_Air_Humidity_Sensor:](Supply_Air_Humidity_Sensor:) (c)<br />[brick:Return_Air_Humidity_Sensor:](Return_Air_Humidity_Sensor:) (c)<br />[brick:Discharge_Air_Humidity_Sensor:](Discharge_Air_Humidity_Sensor:) (c)<br />[brick:Exhaust_Air_Humidity_Sensor:](Exhaust_Air_Humidity_Sensor:) (c)<br />
### Air_Quality
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Air_Quality`
Super-classes |[brick:Quantity](Quantity) (c)<br />
Sub-classes |[brick:PM25](PM25) (c)<br />[brick:TVOC](TVOC) (c)<br />[brick:PM10](PM10) (c)<br />[brick:CO2](CO2) (c)<br />
### Air_Static_Pressure_Increase_Decrease_Step_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Air_Static_Pressure_Increase_Decrease_Step_Setpoint`
Super-classes |[brick:Static_Pressure_Increase_Decrease_Step_Setpoint](Static_Pressure_Increase_Decrease_Step_Setpoint) (c)<br />
### Air_Temperature_Increase_Decrease_Step_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Air_Temperature_Increase_Decrease_Step_Setpoint`
Super-classes |[brick:Temperature_Increase_Decrease_Step_Setpoint](Temperature_Increase_Decrease_Step_Setpoint) (c)<br />
### Air_Temperature_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Air_Temperature_Sensor`
Super-classes |[brick:Temperature_Sensor](Temperature_Sensor) (c)<br />
Sub-classes |[brick:Return_Air_Temperature_Sensor](Return_Air_Temperature_Sensor) (c)<br />[brick:Outside_Air_Temperature_Sensor](Outside_Air_Temperature_Sensor) (c)<br />[brick:Zone_Air_Temperature_Sensor](Zone_Air_Temperature_Sensor) (c)<br />[brick:Discharge_Air_Temperature_Sensor](Discharge_Air_Temperature_Sensor) (c)<br />[brick:Mixed_Air_Temperature_Sensor](Mixed_Air_Temperature_Sensor) (c)<br />[brick:Exhaust_Air_Temperature_Sensor](Exhaust_Air_Temperature_Sensor) (c)<br />
### Air_Temperature_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Air_Temperature_Setpoint`
Super-classes |[brick:Temperature_Setpoint](Temperature_Setpoint) (c)<br />
Sub-classes |[brick:Room_Air_Temperature_Setpoint](Room_Air_Temperature_Setpoint) (c)<br />[brick:Discharge_Air_Temperature_Setpoint](Discharge_Air_Temperature_Setpoint) (c)<br />[brick:Outside_Air_Temperature_Setpoint](Outside_Air_Temperature_Setpoint) (c)<br />[brick:Mixed_Air_Temperature_Setpoint](Mixed_Air_Temperature_Setpoint) (c)<br />
### Alternating_Current_Frequency
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Alternating_Current_Frequency`
Super-classes |[brick:Electric_Current](Electric_Current) (c)<br />[brick:Frequency](Frequency) (c)<br />
### Angle_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Angle_Sensor`
Super-classes |[brick:Sensor](Sensor) (c)<br />
Sub-classes |[brick:Solar_Zenith_Angle_Sensor](Solar_Zenith_Angle_Sensor) (c)<br />[brick:Solar_Azimuth_Angle_Sensor](Solar_Azimuth_Angle_Sensor) (c)<br />
### Apparent_Power
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Apparent_Power`
Super-classes |[brick:Electric_Power](Electric_Power) (c)<br />
### Atmospheric_Pressure
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Atmospheric_Pressure`
Super-classes |[brick:Pressure](Pressure) (c)<br />
### Average_Discharge_Air_Flow_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Average_Discharge_Air_Flow_Sensor`
Super-classes |[brick:Discharge_Air_Flow_Sensor](Discharge_Air_Flow_Sensor) (c)<br />
### Average_Exhaust_Air_Static_Pressure_Sensor:
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Average_Exhaust_Air_Static_Pressure_Sensor:`
Super-classes |[brick:Exhaust_Air_Static_Pressure_Sensor:](Exhaust_Air_Static_Pressure_Sensor:) (c)<br />
### Average_Supply_Air_Flow_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Average_Supply_Air_Flow_Sensor`
Super-classes |[brick:Discharge_Air_Flow_Sensor](Discharge_Air_Flow_Sensor) (c)<br />
### Average_Zone_Temperature_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Average_Zone_Temperature_Sensor`
Super-classes |[brick:Zone_Temperature_Sensor](Zone_Temperature_Sensor) (c)<br />
### Basement
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Basement`
Super-classes |[brick:Location](Location) (c)<br />
### Battery_Voltage_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Battery_Voltage_Sensor`
Super-classes |[brick:Voltage_Sensor](Voltage_Sensor) (c)<br />
### Blowdown_Water
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Blowdown_Water`
Description | <p>Water expelled from a system to remove mineral build up</p>
Super-classes |[brick:Water](Water) (c)<br />
### Boiler
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Boiler`
Description | <p>A closed, pressure vessel that uses fuel or electricity for heating water or other fluids to supply steam or hot water for heating, humidification, or other applications.</p>
Super-classes |[brick:HVAC](HVAC) (c)<br />
### Booster_Fan
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Booster_Fan`
Super-classes |[brick:Supply_Fan](Supply_Fan) (c)<br />
### Booster_Fan_Air_Flow_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Booster_Fan_Air_Flow_Sensor`
Super-classes |[brick:Fan_Air_Flow_Sensor](Fan_Air_Flow_Sensor) (c)<br />
### Building
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Building`
Super-classes |[brick:Location](Location) (c)<br />
### Building_Static_Pressure_Sensor:
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Building_Static_Pressure_Sensor:`
Super-classes |[brick:Static_Pressure_Sensor](Static_Pressure_Sensor) (c)<br />
### Building_Static_Pressure_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Building_Static_Pressure_Setpoint`
Super-classes |[brick:Static_Pressure_Setpoint](Static_Pressure_Setpoint) (c)<br />
### Bypass_Air_Flow_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Bypass_Air_Flow_Sensor`
Super-classes |[brick:Air_Flow_Sensor](Air_Flow_Sensor) (c)<br />
### CO2
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#CO2`
Super-classes |[brick:Air_Quality](Air_Quality) (c)<br />
### CO2_Differential_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#CO2_Differential_Sensor`
Super-classes |[brick:CO2_Sensor](CO2_Sensor) (c)<br />
### CO2_Level_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#CO2_Level_Sensor`
Super-classes |[brick:CO2_Sensor](CO2_Sensor) (c)<br />
### CO2_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#CO2_Sensor`
Super-classes |[brick:Sensor](Sensor) (c)<br />
Sub-classes |[brick:Return_Air_CO2_Sensor](Return_Air_CO2_Sensor) (c)<br />[brick:CO2_Differential_Sensor](CO2_Differential_Sensor) (c)<br />[brick:CO2_Level_Sensor](CO2_Level_Sensor) (c)<br />[brick:Outside_Air_CO2_Sensor](Outside_Air_CO2_Sensor) (c)<br />
### CO2_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#CO2_Setpoint`
Super-classes |[brick:Setpoint](Setpoint) (c)<br />
Sub-classes |[brick:Return_Air_CO2_Setpoint](Return_Air_CO2_Setpoint) (c)<br />
### CRAC
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#CRAC`
Super-classes |[brick:HVAC](HVAC) (c)<br />
### Capacity
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Capacity`
Super-classes |[brick:Quantity](Quantity) (c)<br />
### Capacity_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Capacity_Sensor`
Super-classes |[brick:Sensor](Sensor) (c)<br />
### Centrifugal_Chiller
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Centrifugal_Chiller`
Super-classes |[brick:Chiller](Chiller) (c)<br />
### Chilled_Water
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water`
Description | <p>water used as a cooling medium (particularly in air-conditioning systems or in processes) at below ambient temperature.</p>
Super-classes |[brick:Water](Water) (c)<br />
### Chilled_Water_Differential_Pressure_Dead_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Pressure_Dead_Band_Setpoint`
Super-classes |[brick:Dead_Band_Setpoint](Dead_Band_Setpoint) (c)<br />
### Chilled_Water_Differential_Pressure_Increase_Decrease_Step_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Pressure_Increase_Decrease_Step_Setpoint`
Super-classes |[brick:Differential_Pressure_Increase_Decrease_Step_Setpoint](Differential_Pressure_Increase_Decrease_Step_Setpoint) (c)<br />
### Chilled_Water_Differential_Pressure_Integral_Time_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Pressure_Integral_Time_Setpoint`
Super-classes |[brick:Integral_Time_Setpoint](Integral_Time_Setpoint) (c)<br />
### Chilled_Water_Differential_Pressure_Load_Shed_Reset_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Pressure_Load_Shed_Reset_Status`
Super-classes |[brick:Differential_Pressure_Load_Shed_Status](Differential_Pressure_Load_Shed_Status) (c)<br />
### Chilled_Water_Differential_Pressure_Load_Shed_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Pressure_Load_Shed_Setpoint`
Super-classes |[brick:Load_Shed_Differential_Pressure_Setpoint](Load_Shed_Differential_Pressure_Setpoint) (c)<br />
### Chilled_Water_Differential_Pressure_Load_Shed_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Pressure_Load_Shed_Status`
Super-classes |[brick:Differential_Pressure_Load_Shed_Status](Differential_Pressure_Load_Shed_Status) (c)<br />
### Chilled_Water_Differential_Pressure_Proportional_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Pressure_Proportional_Band_Setpoint`
Super-classes |[brick:Proportional_Band_Setpoint](Proportional_Band_Setpoint) (c)<br />
### Chilled_Water_Differential_Pressure_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Pressure_Sensor`
Super-classes |[brick:Differential_Pressure_Sensor](Differential_Pressure_Sensor) (c)<br />
### Chilled_Water_Differential_Pressure_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Pressure_Setpoint`
Super-classes |[brick:Differential_Pressure_Setpoint](Differential_Pressure_Setpoint) (c)<br />
### Chilled_Water_Differential_Temperature_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Temperature_Sensor`
Super-classes |[brick:Chilled_Water_Temperature_Sensor](Chilled_Water_Temperature_Sensor) (c)<br />
### Chilled_Water_Discharge_Flow_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Discharge_Flow_Sensor`
Super-classes |[brick:Supply_Water_Flow_Sensor](Supply_Water_Flow_Sensor) (c)<br />
### Chilled_Water_Pump
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Pump`
Super-classes |[brick:Water_Pump](Water_Pump) (c)<br />
### Chilled_Water_Pump_Differential_Pressure_Dead_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Pump_Differential_Pressure_Dead_Band_Setpoint`
Super-classes |[brick:Differential_Pressure_Dead_Band_Setpoint](Differential_Pressure_Dead_Band_Setpoint) (c)<br />
### Chilled_Water_Pump_Differential_Pressure_Integration_Time_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Pump_Differential_Pressure_Integration_Time_Setpoint`
Super-classes |[brick:Differential_Pressure_Integral_Time](Differential_Pressure_Integral_Time) (c)<br />
### Chilled_Water_Return_Temperature_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Return_Temperature_Sensor`
Super-classes |[brick:Return_Water_Temperature_Sensor](Return_Water_Temperature_Sensor) (c)<br />
### Chilled_Water_Static_Pressure_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Static_Pressure_Setpoint`
Super-classes |[brick:Static_Pressure_Setpoint](Static_Pressure_Setpoint) (c)<br />
### Chilled_Water_Supply_Flow_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Supply_Flow_Sensor`
Super-classes |[brick:Supply_Water_Flow_Sensor](Supply_Water_Flow_Sensor) (c)<br />
### Chilled_Water_Supply_Temperature_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Supply_Temperature_Sensor`
Super-classes |[brick:Chilled_Water_Temperature_Sensor](Chilled_Water_Temperature_Sensor) (c)<br />
### Chilled_Water_System
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_System`
Super-classes |[brick:Water_System](Water_System) (c)<br />
### Chilled_Water_Temperature_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Temperature_Sensor`
Super-classes |[brick:Water_Temperature_Sensor](Water_Temperature_Sensor) (c)<br />
Sub-classes |[brick:Chilled_Water_Differential_Temperature_Sensor](Chilled_Water_Differential_Temperature_Sensor) (c)<br />[brick:Chilled_Water_Supply_Temperature_Sensor](Chilled_Water_Supply_Temperature_Sensor) (c)<br />
### Chilled_Water_Valve
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Valve`
Super-classes |[brick:Water_Valve](Water_Valve) (c)<br />
### Chiller
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Chiller`
Super-classes |[brick:HVAC](HVAC) (c)<br />
Sub-classes |[brick:Centrifugal_Chiller](Centrifugal_Chiller) (c)<br />[brick:Absorption_Chiller](Absorption_Chiller) (c)<br />
### City
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#City`
Super-classes |[brick:Location](Location) (c)<br />
### Cloudage
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Cloudage`
Super-classes |[brick:Quantity](Quantity) (c)<br />
### Coil
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Coil`
Description | <p>Exchanger that transfers heat from an exhaust airstream to a separated supply airstream.</p>
Super-classes |[brick:HVAC](HVAC) (c)<br />
Sub-classes |[brick:Heating_Coil](Heating_Coil) (c)<br />[brick:Cooling_Coil](Cooling_Coil) (c)<br />
### Cold_Box
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Cold_Box`
Super-classes |[brick:Laboratory](Laboratory) (c)<br />
### Complex_Power
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Complex_Power`
Super-classes |[brick:Electric_Power](Electric_Power) (c)<br />
### Compressor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Compressor`
Description | <p>(1) device for mechanically increasing the pressure of a gas. (2) often described as being either open, hermetic, or semihermetic to describe how the compressor and motor drive is situated in relation to the gas or vapor being compressed. Types include centrifugal, axial flow, reciprocating, rotary screw, rotary vane, scroll, or diaphragm. 1. device for mechanically increasing the pressure of a gas. 2. specific machine, with or without accessories, for compressing refrigerant vapor.</p>
Super-classes |[brick:HVAC](HVAC) (c)<br />
### Computer_Room_Air_Conditioning
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Computer_Room_Air_Conditioning`
Description | <p>A device that monitors and maintains the temperature, air distribution and humidity in a network room or data center. </p>
Super-classes |[brick:HVAC](HVAC) (c)<br />
### Condenser
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Condenser`
Description | <p>A heat exchanger in which the primary heat transfer vapor changes its state to a liquid phase.</p>
Super-classes |[brick:HVAC](HVAC) (c)<br />
### Condenser_Heat_Exchanger
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Condenser_Heat_Exchanger`
Super-classes |[brick:Heat_Exchanger](Heat_Exchanger) (c)<br />
### Condenser_Water
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Condenser_Water`
Description | <p>Water used used to remove heat through condensation</p>
Super-classes |[brick:Water](Water) (c)<br />
### Condenser_Water_Pump
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Condenser_Water_Pump`
Super-classes |[brick:Water_Pump](Water_Pump) (c)<br />
### Conductivity
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Conductivity`
Super-classes |[brick:Quantity](Quantity) (c)<br />
### Conductivity_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Conductivity_Sensor`
Super-classes |[brick:Sensor](Sensor) (c)<br />
Sub-classes |[brick:Deionised_Water_Conductivity_Sensor](Deionised_Water_Conductivity_Sensor) (c)<br />
### Cooling_Coil
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Cooling_Coil`
Super-classes |[brick:Coil](Coil) (c)<br />
### Cooling_Coil_Discharge_Air_Temperature_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Cooling_Coil_Discharge_Air_Temperature_Sensor`
Super-classes |[brick:Discharge_Air_Temperature_Sensor](Discharge_Air_Temperature_Sensor) (c)<br />
### Cooling_Demand_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Cooling_Demand_Setpoint`
Super-classes |[brick:Demand_Setpoint](Demand_Setpoint) (c)<br />
### Cooling_Discharge_Air_Flow_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Cooling_Discharge_Air_Flow_Setpoint`
Super-classes |[brick:Discharge_Air_Flow_Setpoint](Discharge_Air_Flow_Setpoint) (c)<br />
### Cooling_Discharge_Air_Temperature_Dead_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Cooling_Discharge_Air_Temperature_Dead_Band_Setpoint`
Super-classes |[brick:Discharge_Air_Temperature_Dead_Band_Setpoint](Discharge_Air_Temperature_Dead_Band_Setpoint) (c)<br />[brick:Dead_Band_Setpoint](Dead_Band_Setpoint) (c)<br />
### Cooling_Discharge_Air_Temperature_Integral_Time_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Cooling_Discharge_Air_Temperature_Integral_Time_Setpoint`
Super-classes |[brick:Integral_Time_Setpoint](Integral_Time_Setpoint) (c)<br />
### Cooling_Discharge_Air_Temperature_Proportional_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Cooling_Discharge_Air_Temperature_Proportional_Band_Setpoint`
Super-classes |[brick:Proportional_Band_Setpoint](Proportional_Band_Setpoint) (c)<br />
### Cooling_On_Off_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Cooling_On_Off_Status`
Super-classes |[brick:On_Off_Status](On_Off_Status) (c)<br />
### Cooling_Request_Percent_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Cooling_Request_Percent_Setpoint`
Super-classes |[brick:Demand_Setpoint](Demand_Setpoint) (c)<br />
### Cooling_Request_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Cooling_Request_Setpoint`
Super-classes |[brick:Demand_Setpoint](Demand_Setpoint) (c)<br />
### Cooling_Supply_Air_Flow_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Cooling_Supply_Air_Flow_Setpoint`
Super-classes |[brick:Supply_Air_Flow_Setpoint](Supply_Air_Flow_Setpoint) (c)<br />
### Cooling_Supply_Air_Temperature_Dead_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Cooling_Supply_Air_Temperature_Dead_Band_Setpoint`
Super-classes |[brick:Supply_Air_Temperature_Dead_Band_Setpoint](Supply_Air_Temperature_Dead_Band_Setpoint) (c)<br />[brick:Dead_Band_Setpoint](Dead_Band_Setpoint) (c)<br />
### Cooling_Supply_Air_Temperature_Integral_Time_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Cooling_Supply_Air_Temperature_Integral_Time_Setpoint`
Super-classes |[brick:Integral_Time_Setpoint](Integral_Time_Setpoint) (c)<br />
### Cooling_Supply_Air_Temperature_Proportional_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Cooling_Supply_Air_Temperature_Proportional_Band_Setpoint`
Super-classes |[brick:Proportional_Band_Setpoint](Proportional_Band_Setpoint) (c)<br />
### Cooling_Tower_Fan
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Cooling_Tower_Fan`
Super-classes |[brick:Fan](Fan) (c)<br />
### Current
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Current`
Super-classes |[brick:Quantity](Quantity) (c)<br />
Sub-classes |[brick:Electric_Current](Electric_Current) (c)<br />
### Current_Angle
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Current_Angle`
Super-classes |[brick:Electric_Current](Electric_Current) (c)<br />
### Current_Imbalance
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Current_Imbalance`
Super-classes |[brick:Electric_Current](Electric_Current) (c)<br />
### Current_Magnitude
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Current_Magnitude`
Super-classes |[brick:Electric_Current](Electric_Current) (c)<br />
### Current_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Current_Sensor`
Super-classes |[brick:Sensor](Sensor) (c)<br />
Sub-classes |[brick:Motor_Current_Sensor](Motor_Current_Sensor) (c)<br />[brick:Load_Current_Sensor](Load_Current_Sensor) (c)<br />[brick:Photovoltaic_Current_Output_Sensor](Photovoltaic_Current_Output_Sensor) (c)<br />
### Current_Total_Harmonic_Distortion
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Current_Total_Harmonic_Distortion`
Super-classes |[brick:Electric_Current](Electric_Current) (c)<br />
### DC_Bus_Voltage_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#DC_Bus_Voltage_Sensor`
Super-classes |[brick:Voltage_Sensor](Voltage_Sensor) (c)<br />
### Damper
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Damper`
Description | <p>Element inserted into an air-distribution system or element of an air-distribution system permitting modification of the air resistance of the system and consequently changing the airflow rate or shutting off the airflow.</p>
Super-classes |[brick:HVAC](HVAC) (c)<br />
Sub-classes |[brick:Return_Damper](Return_Damper) (c)<br />[brick:Outside_Damper](Outside_Damper) (c)<br />[brick:Economizer_Damper](Economizer_Damper) (c)<br />[brick:Exhaust_Damper](Exhaust_Damper) (c)<br />
### Damper_Position_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Damper_Position_Limit`
Super-classes |[brick:Limit](Limit) (c)<br />
Sub-classes |[brick:Max_Damper_Position_Setpoint_Limit](Max_Damper_Position_Setpoint_Limit) (c)<br />[brick:Min_Damper_Position_Setpoint_Limit](Min_Damper_Position_Setpoint_Limit) (c)<br />
### Damper_Position_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Damper_Position_Sensor`
Super-classes |[brick:Sensor](Sensor) (c)<br />
### Damper_Position_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Damper_Position_Setpoint`
Super-classes |[brick:Setpoint](Setpoint) (c)<br />
### Daytime
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Daytime`
Super-classes |[brick:Quantity](Quantity) (c)<br />
### Dead_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Dead_Band_Setpoint`
Super-classes |[brick:Setpoint](Setpoint) (c)<br />
Sub-classes |[brick:Supply_Air_Temperature_Dead_Band_Setpoint](Supply_Air_Temperature_Dead_Band_Setpoint) (c)<br />[brick:Air_Flow_Dead_Band_Setpoint](Air_Flow_Dead_Band_Setpoint) (c)<br />[brick:Chilled_Water_Differential_Pressure_Dead_Band_Setpoint](Chilled_Water_Differential_Pressure_Dead_Band_Setpoint) (c)<br />[brick:Cooling_Supply_Air_Temperature_Dead_Band_Setpoint](Cooling_Supply_Air_Temperature_Dead_Band_Setpoint) (c)<br />[brick:Supply_Water_Differential_Pressure_Dead_Band_Setpoint](Supply_Water_Differential_Pressure_Dead_Band_Setpoint) (c)<br />[brick:Supply_Water_Temperature_Dead_Band_Setpoint](Supply_Water_Temperature_Dead_Band_Setpoint) (c)<br />[brick:Differential_Pressure_Dead_Band_Setpoint](Differential_Pressure_Dead_Band_Setpoint) (c)<br />[brick:Discharge_Air_Temperature_Dead_Band_Setpoint](Discharge_Air_Temperature_Dead_Band_Setpoint) (c)<br />[brick:Cooling_Discharge_Air_Temperature_Dead_Band_Setpoint](Cooling_Discharge_Air_Temperature_Dead_Band_Setpoint) (c)<br />[brick:Temperature_Dead_Band_Setpoint](Temperature_Dead_Band_Setpoint) (c)<br />[brick:Static_Pressure_Dead_Band_Setpoint](Static_Pressure_Dead_Band_Setpoint) (c)<br />
### Dehumidification_On_Off_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Dehumidification_On_Off_Status`
Super-classes |[brick:On_Off_Status](On_Off_Status) (c)<br />
### Deionised_Water_Conductivity_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Deionised_Water_Conductivity_Sensor`
Super-classes |[brick:Conductivity_Sensor](Conductivity_Sensor) (c)<br />
### Deionised_Water_Level_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Deionised_Water_Level_Sensor`
Super-classes |[brick:Water_Level_Sensor](Water_Level_Sensor) (c)<br />
### Demand_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Demand_Sensor`
Super-classes |[brick:Sensor](Sensor) (c)<br />
Sub-classes |[brick:Peak_Power_Demand_Sensor](Peak_Power_Demand_Sensor) (c)<br />
### Demand_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Demand_Setpoint`
Super-classes |[brick:Setpoint](Setpoint) (c)<br />
Sub-classes |[brick:Air_Flow_Demand_Setpoint](Air_Flow_Demand_Setpoint) (c)<br />[brick:Cooling_Request_Percent_Setpoint](Cooling_Request_Percent_Setpoint) (c)<br />[brick:Cooling_Demand_Setpoint](Cooling_Demand_Setpoint) (c)<br />[brick:Cooling_Request_Setpoint](Cooling_Request_Setpoint) (c)<br />[brick:Heating_Request_Setpoint](Heating_Request_Setpoint) (c)<br />[brick:Heating_Request_Percent_Setpoint](Heating_Request_Percent_Setpoint) (c)<br />[brick:Preheat_Demand_Setpoint](Preheat_Demand_Setpoint) (c)<br />[brick:Heating_Demand_Setpoint](Heating_Demand_Setpoint) (c)<br />
### Dew_Point_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Dew_Point_Setpoint`
Super-classes |[brick:Setpoint](Setpoint) (c)<br />
### Dewpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Dewpoint`
Super-classes |[brick:Quantity](Quantity) (c)<br />
### Dewpoint_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Dewpoint_Sensor`
Super-classes |[brick:Sensor](Sensor) (c)<br />
Sub-classes |[brick:Return_Air_Dewpoint_Sensor](Return_Air_Dewpoint_Sensor) (c)<br />[brick:Outside_Air_Dewpoint_Sensor](Outside_Air_Dewpoint_Sensor) (c)<br />
### Differential_Pressure_Dead_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Dead_Band_Setpoint`
Super-classes |[brick:Dead_Band_Setpoint](Dead_Band_Setpoint) (c)<br />
Sub-classes |[brick:Hot_Water_Differential_Pressure_Dead_Band_Setpoint](Hot_Water_Differential_Pressure_Dead_Band_Setpoint) (c)<br />[brick:Chilled_Water_Pump_Differential_Pressure_Dead_Band_Setpoint](Chilled_Water_Pump_Differential_Pressure_Dead_Band_Setpoint) (c)<br />
### Differential_Pressure_Increase_Decrease_Step_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Increase_Decrease_Step_Setpoint`
Super-classes |[brick:Increase_Decrease_Step_Setpoint](Increase_Decrease_Step_Setpoint) (c)<br />
Sub-classes |[brick:Chilled_Water_Differential_Pressure_Increase_Decrease_Step_Setpoint](Chilled_Water_Differential_Pressure_Increase_Decrease_Step_Setpoint) (c)<br />
### Differential_Pressure_Integral_Time
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Integral_Time`
Super-classes |[brick:Integral_Time_Setpoint](Integral_Time_Setpoint) (c)<br />
Sub-classes |[brick:Chilled_Water_Pump_Differential_Pressure_Integration_Time_Setpoint](Chilled_Water_Pump_Differential_Pressure_Integration_Time_Setpoint) (c)<br />
### Differential_Pressure_Integral_Time_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Integral_Time_Setpoint`
Super-classes |[brick:Integral_Time_Setpoint](Integral_Time_Setpoint) (c)<br />
Sub-classes |[brick:Hot_Water_Differential_Pressure_Integral_Time_Setpoint](Hot_Water_Differential_Pressure_Integral_Time_Setpoint) (c)<br />
### Differential_Pressure_Load_Shed_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Load_Shed_Status`
Super-classes |[brick:Load_Shed_Status](Load_Shed_Status) (c)<br />
Sub-classes |[brick:Hot_Water_Differential_Pressure_Load_Shed_Reset_Status](Hot_Water_Differential_Pressure_Load_Shed_Reset_Status) (c)<br />[brick:Chilled_Water_Differential_Pressure_Load_Shed_Reset_Status](Chilled_Water_Differential_Pressure_Load_Shed_Reset_Status) (c)<br />[brick:Hot_Water_Discharge_Temperature_Load_Shed_Status](Hot_Water_Discharge_Temperature_Load_Shed_Status) (c)<br />[brick:Chilled_Water_Differential_Pressure_Load_Shed_Status](Chilled_Water_Differential_Pressure_Load_Shed_Status) (c)<br />[brick:Hot_Water_Supply_Temperature_Load_Shed_Status](Hot_Water_Supply_Temperature_Load_Shed_Status) (c)<br />[brick:Hot_Water_Differential_Pressure_Load_Shed_Status](Hot_Water_Differential_Pressure_Load_Shed_Status) (c)<br />
### Differential_Pressure_Proportional_Band
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Proportional_Band`
Super-classes |[brick:Proportional_Band_Setpoint](Proportional_Band_Setpoint) (c)<br />
### Differential_Pressure_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Sensor`
Super-classes |[brick:Pressure_Sensor](Pressure_Sensor) (c)<br />
Sub-classes |[brick:Hot_Water_Differential_Pressure_Sensor](Hot_Water_Differential_Pressure_Sensor) (c)<br />[brick:Heat_Wheel_Differential_Pressure_Sensor](Heat_Wheel_Differential_Pressure_Sensor) (c)<br />[brick:Chilled_Water_Differential_Pressure_Sensor](Chilled_Water_Differential_Pressure_Sensor) (c)<br />[brick:Filter_Differential_Pressure_Sensor](Filter_Differential_Pressure_Sensor) (c)<br />
### Differential_Pressure_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Setpoint`
Super-classes |[brick:Pressure_Setpoint](Pressure_Setpoint) (c)<br />
Sub-classes |[brick:Chilled_Water_Differential_Pressure_Setpoint](Chilled_Water_Differential_Pressure_Setpoint) (c)<br />[brick:Hot_Water_Differential_Pressure_Setpoint](Hot_Water_Differential_Pressure_Setpoint) (c)<br />[brick:Load_Shed_Differential_Pressure_Setpoint](Load_Shed_Differential_Pressure_Setpoint) (c)<br />
### Differential_Pressure_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Setpoint_Limit`
Super-classes |[brick:Limit](Limit) (c)<br />
Sub-classes |[brick:Min_Hot_Water_Differential_Pressure_Setpoint_Limit](Min_Hot_Water_Differential_Pressure_Setpoint_Limit) (c)<br />[brick:Max_Hot_Water_Differential_Pressure_Setpoint_Limit](Max_Hot_Water_Differential_Pressure_Setpoint_Limit) (c)<br />[brick:Max_Chilled_Water_Differential_Pressure_Setpoint_Limit](Max_Chilled_Water_Differential_Pressure_Setpoint_Limit) (c)<br />[brick:Min_Chilled_Water_Differential_Pressure_Setpoint_Limit](Min_Chilled_Water_Differential_Pressure_Setpoint_Limit) (c)<br />
### Differential_Speed_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Differential_Speed_Sensor`
Super-classes |[brick:Speed_Sensor](Speed_Sensor) (c)<br />
Sub-classes |[brick:Return_Fan_Differential_Speed_Sensor](Return_Fan_Differential_Speed_Sensor) (c)<br />[brick:Heat_Wheel_Speed_Sensor](Heat_Wheel_Speed_Sensor) (c)<br />
### Differential_Speed_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Differential_Speed_Setpoint`
Super-classes |[brick:Speed_Setpoint](Speed_Setpoint) (c)<br />
Sub-classes |[brick:Return_Discharge_Fan_Differential_Speed_Setpoint](Return_Discharge_Fan_Differential_Speed_Setpoint) (c)<br />[brick:Return_Fan_Differential_Speed_Setpoint](Return_Fan_Differential_Speed_Setpoint) (c)<br />[brick:Return_Supply_Fan_Differential_Speed_Setpoint](Return_Supply_Fan_Differential_Speed_Setpoint) (c)<br />
### Dimmer
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Dimmer`
Super-classes |[brick:Switch](Switch) (c)<br />
### Direction
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Direction`
Super-classes |[brick:Quantity](Quantity) (c)<br />
Sub-classes |[brick:Wind_Direction](Wind_Direction) (c)<br />
### Direction_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Direction_Sensor`
Super-classes |[brick:Sensor](Sensor) (c)<br />
Sub-classes |[brick:Wind_Direction_Sensor](Wind_Direction_Sensor) (c)<br />
### Direction_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Direction_Status`
Super-classes |[brick:Status](Status) (c)<br />
Sub-classes |[brick:Motor_Direction_Status](Motor_Direction_Status) (c)<br />[brick:Run_Direction_Status](Run_Direction_Status) (c)<br />
### Disable_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Disable_Status`
Super-classes |[brick:Status](Status) (c)<br />
### Discharge_Air_Duct_Pressure_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Duct_Pressure_Status`
Super-classes |[brick:Pressure_Status](Pressure_Status) (c)<br />
### Discharge_Air_Flow_Demand_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Flow_Demand_Setpoint`
Super-classes |[brick:Discharge_Air_Flow_Setpoint](Discharge_Air_Flow_Setpoint) (c)<br />[brick:Air_Flow_Demand_Setpoint](Air_Flow_Demand_Setpoint) (c)<br />
### Discharge_Air_Flow_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Flow_Sensor`
Super-classes |[brick:Air_Flow_Sensor](Air_Flow_Sensor) (c)<br />
Sub-classes |[brick:Average_Discharge_Air_Flow_Sensor](Average_Discharge_Air_Flow_Sensor) (c)<br />[brick:Average_Supply_Air_Flow_Sensor](Average_Supply_Air_Flow_Sensor) (c)<br />
### Discharge_Air_Flow_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Flow_Setpoint`
Super-classes |[brick:Air_Flow_Setpoint](Air_Flow_Setpoint) (c)<br />
Sub-classes |[brick:Cooling_Discharge_Air_Flow_Setpoint](Cooling_Discharge_Air_Flow_Setpoint) (c)<br />[brick:Discharge_Air_Flow_Demand_Setpoint](Discharge_Air_Flow_Demand_Setpoint) (c)<br />[brick:Heating_Discharge_Air_Flow_Setpoint](Heating_Discharge_Air_Flow_Setpoint) (c)<br />
### Discharge_Air_Humidity_Sensor:
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Humidity_Sensor:`
Super-classes |[brick:Air_Humidity_Sensor](Air_Humidity_Sensor) (c)<br />
### Discharge_Air_Static_Pressure_Integral_Time_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Static_Pressure_Integral_Time_Setpoint`
Super-classes |[brick:Integral_Time_Setpoint](Integral_Time_Setpoint) (c)<br />
### Discharge_Air_Static_Pressure_Proportional_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Static_Pressure_Proportional_Band_Setpoint`
Super-classes |[brick:Proportional_Band_Setpoint](Proportional_Band_Setpoint) (c)<br />
### Discharge_Air_Static_Pressure_Sensor:
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Static_Pressure_Sensor:`
Super-classes |[brick:Static_Pressure_Sensor](Static_Pressure_Sensor) (c)<br />
### Discharge_Air_Static_Pressure_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Static_Pressure_Setpoint`
Super-classes |[brick:Static_Pressure_Setpoint](Static_Pressure_Setpoint) (c)<br />
### Discharge_Air_Temperature_Cooling_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Cooling_Setpoint`
Super-classes |[brick:Discharge_Air_Temperature_Setpoint](Discharge_Air_Temperature_Setpoint) (c)<br />
### Discharge_Air_Temperature_Dead_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Dead_Band_Setpoint`
Super-classes |[brick:Dead_Band_Setpoint](Dead_Band_Setpoint) (c)<br />
Sub-classes |[brick:Heating_Discharge_Air_Temperature_Dead_Band_Setpoint](Heating_Discharge_Air_Temperature_Dead_Band_Setpoint) (c)<br />[brick:Cooling_Discharge_Air_Temperature_Dead_Band_Setpoint](Cooling_Discharge_Air_Temperature_Dead_Band_Setpoint) (c)<br />
### Discharge_Air_Temperature_Heating_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Heating_Setpoint`
Super-classes |[brick:Discharge_Air_Temperature_Setpoint](Discharge_Air_Temperature_Setpoint) (c)<br />
### Discharge_Air_Temperature_Proportional_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Proportional_Band_Setpoint`
Super-classes |[brick:Proportional_Band_Setpoint](Proportional_Band_Setpoint) (c)<br />
### Discharge_Air_Temperature_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Sensor`
Super-classes |[brick:Air_Temperature_Sensor](Air_Temperature_Sensor) (c)<br />
Sub-classes |[brick:Heat_Wheel_Discharge_Air_Temperature_Sensor](Heat_Wheel_Discharge_Air_Temperature_Sensor) (c)<br />[brick:Preheat_Discharge_Air_Temperature_Sensor](Preheat_Discharge_Air_Temperature_Sensor) (c)<br />[brick:Cooling_Coil_Discharge_Air_Temperature_Sensor](Cooling_Coil_Discharge_Air_Temperature_Sensor) (c)<br />
### Discharge_Air_Temperature_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Setpoint`
Super-classes |[brick:Air_Temperature_Setpoint](Air_Temperature_Setpoint) (c)<br />
Sub-classes |[brick:Discharge_Air_Temperature_Heating_Setpoint](Discharge_Air_Temperature_Heating_Setpoint) (c)<br />[brick:Discharge_Air_Temperature_Cooling_Setpoint](Discharge_Air_Temperature_Cooling_Setpoint) (c)<br />
### Discharge_Air_Velocity_Pressure_Sensor:
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Velocity_Pressure_Sensor:`
Super-classes |[brick:Velocity_Pressure_Sensor:](Velocity_Pressure_Sensor:) (c)<br />
### Discharge_Fan_Air_Flow_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Discharge_Fan_Air_Flow_Sensor`
Super-classes |[brick:Fan_Air_Flow_Sensor](Fan_Air_Flow_Sensor) (c)<br />
### Domestic_Hot_Water_Supply_Temperature_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Domestic_Hot_Water_Supply_Temperature_Sensor`
Super-classes |[brick:Hot_Water_Supply_Temperature_Sensor](Hot_Water_Supply_Temperature_Sensor) (c)<br />
### Domestic_Hot_Water_Valve
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Domestic_Hot_Water_Valve`
Super-classes |[brick:Heating_Valve](Heating_Valve) (c)<br />
### Domestic_Water
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Domestic_Water`
Description | <p>Tap water for drinking, washing, cooking, and flushing of toliets</p>
Super-classes |[brick:Water](Water) (c)<br />
### Drive_Ready_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Drive_Ready_Status`
Super-classes |[brick:Status](Status) (c)<br />
### Dual_Band_Mode_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Dual_Band_Mode_Setpoint`
Super-classes |[brick:Mode_Setpoint](Mode_Setpoint) (c)<br />
### Duration_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Duration_Sensor`
Super-classes |[brick:Sensor](Sensor) (c)<br />
Sub-classes |[brick:On_Timer_Sensor](On_Timer_Sensor) (c)<br />[brick:Rain_Duration_Sensor](Rain_Duration_Sensor) (c)<br />[brick:Run_Time_Sensor](Run_Time_Sensor) (c)<br />
### EconCycle_On_Off_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#EconCycle_On_Off_Status`
Super-classes |[brick:On_Off_Status](On_Off_Status) (c)<br />
### Economizer
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Economizer`
Description | <p>Device that, on proper variable sensing, initiates control signals or actions to conserve energy. A control system that reduces the mechanical heating and cooling requirement.</p>
Super-classes |[brick:HVAC](HVAC) (c)<br />
### Economizer_Damper
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Economizer_Damper`
Super-classes |[brick:Damper](Damper) (c)<br />
### Electric_Current
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Electric_Current`
Super-classes |[brick:Current](Current) (c)<br />
Sub-classes |[brick:Alternating_Current_Frequency](Alternating_Current_Frequency) (c)<br />[brick:Current_Angle](Current_Angle) (c)<br />[brick:Current_Magnitude](Current_Magnitude) (c)<br />[brick:Current_Imbalance](Current_Imbalance) (c)<br />[brick:Current_Total_Harmonic_Distortion](Current_Total_Harmonic_Distortion) (c)<br />
### Electric_Energy
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Electric_Energy`
Super-classes |[brick:Energy](Energy) (c)<br />
### Electric_Power
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Electric_Power`
Super-classes |[brick:Power](Power) (c)<br />
Sub-classes |[brick:Reactive_Power](Reactive_Power) (c)<br />[brick:Apparent_Power](Apparent_Power) (c)<br />[brick:Complex_Power](Complex_Power) (c)<br />[brick:Active_Power](Active_Power) (c)<br />
### Electric_Voltage
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Electric_Voltage`
Super-classes |[brick:Voltage](Voltage) (c)<br />
Sub-classes |[brick:Voltage_Magnitude](Voltage_Magnitude) (c)<br />[brick:Voltage_Angle](Voltage_Angle) (c)<br />[brick:Voltage_Imbalance](Voltage_Imbalance) (c)<br />
### Elevator
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Elevator`
Super-classes |[brick:Equipment](Equipment) (c)<br />
### Emergency_Air_Flow_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Emergency_Air_Flow_Status`
Super-classes |[brick:Status](Status) (c)<br />
### Emergency_Generator_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Emergency_Generator_Status`
Super-classes |[brick:Status](Status) (c)<br />
### Emergency_Power_Off_Activated_By_High_Temperature_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Emergency_Power_Off_Activated_By_High_Temperature_Status`
Super-classes |[brick:Emergency_Power_Off_Status](Emergency_Power_Off_Status) (c)<br />
### Emergency_Power_Off_Activated_By_Leak_Detection_System_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Emergency_Power_Off_Activated_By_Leak_Detection_System_Status`
Super-classes |[brick:Emergency_Power_Off_Status](Emergency_Power_Off_Status) (c)<br />
### Emergency_Power_Off_Enable_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Emergency_Power_Off_Enable_Status`
Super-classes |[brick:Emergency_Power_Off_Status](Emergency_Power_Off_Status) (c)<br />
### Emergency_Power_Off_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Emergency_Power_Off_Status`
Super-classes |[brick:Status](Status) (c)<br />
Sub-classes |[brick:Emergency_Power_Off_System_Enable_Status](Emergency_Power_Off_System_Enable_Status) (c)<br />[brick:Emergency_Power_Off_Enable_Status](Emergency_Power_Off_Enable_Status) (c)<br />[brick:Emergency_Power_Off_Activated_By_High_Temperature_Status](Emergency_Power_Off_Activated_By_High_Temperature_Status) (c)<br />[brick:Emergency_Power_Off_Activated_By_Leak_Detection_System_Status](Emergency_Power_Off_Activated_By_Leak_Detection_System_Status) (c)<br />
### Emergency_Power_Off_System_Enable_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Emergency_Power_Off_System_Enable_Status`
Super-classes |[brick:Emergency_Power_Off_Status](Emergency_Power_Off_Status) (c)<br />
### Emergency_Push_Button_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Emergency_Push_Button_Status`
Super-classes |[brick:Status](Status) (c)<br />
### Enable_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Enable_Status`
Super-classes |[brick:Status](Status) (c)<br />
Sub-classes |[brick:Heat_Exchanger_System_Enable_Status](Heat_Exchanger_System_Enable_Status) (c)<br />[brick:Run_Enable_Status](Run_Enable_Status) (c)<br />
### Energy
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Energy`
Super-classes |[brick:Quantity](Quantity) (c)<br />
Sub-classes |[brick:Electric_Energy](Electric_Energy) (c)<br />[brick:Thermal_Energy](Thermal_Energy) (c)<br />
### Energy_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Energy_Sensor`
Super-classes |[brick:Sensor](Sensor) (c)<br />
### Energy_Storage
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Energy_Storage`
Super-classes |[brick:Equipment](Equipment) (c)<br />
### Entering_Water_Temperature_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Entering_Water_Temperature_Sensor`
Super-classes |[brick:Water_Temperature_Sensor](Water_Temperature_Sensor) (c)<br />
Sub-classes |[brick:Hot_Water_Coil_Entering_Temperature_Sensor](Hot_Water_Coil_Entering_Temperature_Sensor) (c)<br />[brick:PreHeat_Coil_Entering_Air_Temperature_Sensor](PreHeat_Coil_Entering_Air_Temperature_Sensor) (c)<br />[brick:Ice_Tank_Entering_Water_Temperature_Sensor](Ice_Tank_Entering_Water_Temperature_Sensor) (c)<br />
### Entering_Water_Temperature_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Entering_Water_Temperature_Setpoint`
Super-classes |[brick:Water_Temperature_Setpoint](Water_Temperature_Setpoint) (c)<br />
### Enthalpy
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Enthalpy`
Description | <p>(also known as heat content), thermodynamic quantity equal to the sum of the internal energy of a system plus the product of the pressure volume work done on the system. H = E + pv, where H = enthalpy or total heat content, E = internal energy of the system, p = pressure, and v = volume. (Compare to [[specific enthalpy]].)</p>
Super-classes |[brick:Quantity](Quantity) (c)<br />[brick:Substance](Substance) (c)<br />
### Enthalpy_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Enthalpy_Sensor`
Super-classes |[brick:Sensor](Sensor) (c)<br />
Sub-classes |[brick:Air_Enthalpy_Sensor](Air_Enthalpy_Sensor) (c)<br />
### Enthalpy_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Enthalpy_Setpoint`
Super-classes |[brick:Setpoint](Setpoint) (c)<br />
### Environment_Box
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Environment_Box`
Super-classes |[brick:Laboratory](Laboratory) (c)<br />
### Equipment
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Equipment`
Sub-classes |[brick:Shading_System](Shading_System) (c)<br />[brick:Furniture](Furniture) (c)<br />[brick:Weather](Weather) (c)<br />[brick:Energy_Storage](Energy_Storage) (c)<br />[brick:Fire_Safety_System](Fire_Safety_System) (c)<br />[brick:Meter](Meter) (c)<br />[brick:Solar_Panel](Solar_Panel) (c)<br />[brick:Water_System](Water_System) (c)<br />[brick:PlugStrip](PlugStrip) (c)<br />[brick:Power_System](Power_System) (c)<br />[brick:Heating_Ventilation_Air_Conditioning_System](Heating_Ventilation_Air_Conditioning_System) (c)<br />[brick:Lighting_System](Lighting_System) (c)<br />[brick:Steam_System](Steam_System) (c)<br />[brick:Elevator](Elevator) (c)<br />[brick:HVAC](HVAC) (c)<br />
### Evaporative_Heat_Exchanger
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Evaporative_Heat_Exchanger`
Super-classes |[brick:Heat_Exchanger](Heat_Exchanger) (c)<br />
### Even_Month_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Even_Month_Status`
Super-classes |[brick:Status](Status) (c)<br />
### Exhaust_Air
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air`
Description | <p>air that must be removed from a space due to contaminants, regardless of pressurization</p>
Super-classes |[brick:Air](Air) (c)<br />
### Exhaust_Air_Flow_Integral_Time_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Flow_Integral_Time_Setpoint`
Super-classes |[brick:Integral_Time_Setpoint](Integral_Time_Setpoint) (c)<br />
Sub-classes |[brick:Exhaust_Air_Stack_Flow_Integral_Time_Setpoint](Exhaust_Air_Stack_Flow_Integral_Time_Setpoint) (c)<br />
### Exhaust_Air_Flow_Proportional_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Flow_Proportional_Band_Setpoint`
Super-classes |[brick:Proportional_Band_Setpoint](Proportional_Band_Setpoint) (c)<br />
### Exhaust_Air_Flow_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Flow_Sensor`
Super-classes |[brick:Air_Flow_Sensor](Air_Flow_Sensor) (c)<br />
Sub-classes |[brick:Exhaust_Air_Stack_Flow_Sensor](Exhaust_Air_Stack_Flow_Sensor) (c)<br />
### Exhaust_Air_Flow_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Flow_Setpoint`
Super-classes |[brick:Air_Flow_Setpoint](Air_Flow_Setpoint) (c)<br />
Sub-classes |[brick:Exhaust_Air_Stack_Flow_Setpoint](Exhaust_Air_Stack_Flow_Setpoint) (c)<br />
### Exhaust_Air_Humidity_Sensor:
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Humidity_Sensor:`
Super-classes |[brick:Air_Humidity_Sensor](Air_Humidity_Sensor) (c)<br />
### Exhaust_Air_Stack_Flow_Dead_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Stack_Flow_Dead_Band_Setpoint`
Super-classes |[brick:Air_Flow_Dead_Band_Setpoint](Air_Flow_Dead_Band_Setpoint) (c)<br />
### Exhaust_Air_Stack_Flow_Integral_Time_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Stack_Flow_Integral_Time_Setpoint`
Super-classes |[brick:Exhaust_Air_Flow_Integral_Time_Setpoint](Exhaust_Air_Flow_Integral_Time_Setpoint) (c)<br />
### Exhaust_Air_Stack_Flow_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Stack_Flow_Sensor`
Super-classes |[brick:Exhaust_Air_Flow_Sensor](Exhaust_Air_Flow_Sensor) (c)<br />
### Exhaust_Air_Stack_Flow_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Stack_Flow_Setpoint`
Super-classes |[brick:Exhaust_Air_Flow_Setpoint](Exhaust_Air_Flow_Setpoint) (c)<br />
### Exhaust_Air_Static_Pressure_Proportional_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Static_Pressure_Proportional_Band_Setpoint`
Super-classes |[brick:Static_Pressure_Proportional_Band_Setpoint](Static_Pressure_Proportional_Band_Setpoint) (c)<br />
### Exhaust_Air_Static_Pressure_Sensor:
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Static_Pressure_Sensor:`
Super-classes |[brick:Static_Pressure_Sensor](Static_Pressure_Sensor) (c)<br />
Sub-classes |[brick:Average_Exhaust_Air_Static_Pressure_Sensor:](Average_Exhaust_Air_Static_Pressure_Sensor:) (c)<br />[brick:Lowest_Exhaust_Air_Static_Pressure_Sensor:](Lowest_Exhaust_Air_Static_Pressure_Sensor:) (c)<br />
### Exhaust_Air_Static_Pressure_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Static_Pressure_Setpoint`
Super-classes |[brick:Static_Pressure_Setpoint](Static_Pressure_Setpoint) (c)<br />
### Exhaust_Air_Temperature_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Temperature_Sensor`
Super-classes |[brick:Air_Temperature_Sensor](Air_Temperature_Sensor) (c)<br />
### Exhaust_Air_Velocity_Pressure_Sensor:
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Velocity_Pressure_Sensor:`
Super-classes |[brick:Velocity_Pressure_Sensor:](Velocity_Pressure_Sensor:) (c)<br />
### Exhaust_Damper
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Exhaust_Damper`
Super-classes |[brick:Damper](Damper) (c)<br />
### Exhaust_Fan
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Exhaust_Fan`
Super-classes |[brick:Fan](Fan) (c)<br />
### Fan
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Fan`
Description | <p>Any device with two or more blades or vanes attached to a rotating shaft used to produce an airflow for the purpose of comfort, ventilation, exhaust, heating, cooling, or any other gaseous transport.</p>
Super-classes |[brick:HVAC](HVAC) (c)<br />
Sub-classes |[brick:Standby_Fan](Standby_Fan) (c)<br />[brick:Supply_Fan](Supply_Fan) (c)<br />[brick:Return_Fan](Return_Fan) (c)<br />[brick:Exhaust_Fan](Exhaust_Fan) (c)<br />[brick:Cooling_Tower_Fan](Cooling_Tower_Fan) (c)<br />
### Fan_Air_Flow_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Fan_Air_Flow_Sensor`
Super-classes |[brick:Air_Flow_Sensor](Air_Flow_Sensor) (c)<br />
Sub-classes |[brick:Return_Fan_Air_Flow_Sensor](Return_Fan_Air_Flow_Sensor) (c)<br />[brick:Discharge_Fan_Air_Flow_Sensor](Discharge_Fan_Air_Flow_Sensor) (c)<br />[brick:Booster_Fan_Air_Flow_Sensor](Booster_Fan_Air_Flow_Sensor) (c)<br />[brick:Supply_Fan_Air_Flow_Sensor](Supply_Fan_Air_Flow_Sensor) (c)<br />
### Fan_Air_Flow_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Fan_Air_Flow_Setpoint`
Super-classes |[brick:Air_Flow_Setpoint](Air_Flow_Setpoint) (c)<br />
### Fan_Coil_Unit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Fan_Coil_Unit`
Super-classes |[brick:Terminal_Unit](Terminal_Unit) (c)<br />
### Fan_Start_Stop_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Fan_Start_Stop_Status`
Super-classes |[brick:Start_Stop_Status](Start_Stop_Status) (c)<br />
### Fan_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Fan_Status`
Super-classes |[brick:Status](Status) (c)<br />
### Fault_Indicator_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Fault_Indicator_Status`
Super-classes |[brick:Status](Status) (c)<br />
### Fault_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Fault_Status`
Super-classes |[brick:Status](Status) (c)<br />
Sub-classes |[brick:Humidifier_Fault_Status](Humidifier_Fault_Status) (c)<br />
### Filter
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Filter`
Description | <p>Device to remove gases from a mixture of gases</p>
Super-classes |[brick:HVAC](HVAC) (c)<br />
Sub-classes |[brick:Mixed_Air_Filter](Mixed_Air_Filter) (c)<br />
### Filter_Differential_Pressure_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Filter_Differential_Pressure_Sensor`
Super-classes |[brick:Differential_Pressure_Sensor](Differential_Pressure_Sensor) (c)<br />
### Filter_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Filter_Status`
Super-classes |[brick:Status](Status) (c)<br />
Sub-classes |[brick:Pre_Filter_Status](Pre_Filter_Status) (c)<br />
### Fire_Safety_System
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Fire_Safety_System`
Super-classes |[brick:Equipment](Equipment) (c)<br />
### Fire_Zone
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Fire_Zone`
Super-classes |[brick:Zone](Zone) (c)<br />
### Floor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Floor`
Super-classes |[brick:Location](Location) (c)<br />
### Flow
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Flow`
Super-classes |[brick:Quantity](Quantity) (c)<br />
### Flow_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Flow_Sensor`
Super-classes |[brick:Sensor](Sensor) (c)<br />
Sub-classes |[brick:Water_Flow_Sensor](Water_Flow_Sensor) (c)<br />[brick:Air_Flow_Sensor](Air_Flow_Sensor) (c)<br />
### Flow_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Flow_Setpoint`
Super-classes |[brick:Setpoint](Setpoint) (c)<br />
Sub-classes |[brick:Air_Flow_Setpoint](Air_Flow_Setpoint) (c)<br />
### Fluid
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Fluid`
Super-classes |[brick:Substance](Substance) (c)<br />
Sub-classes |[brick:Gas](Gas) (c)<br />[brick:Liquid](Liquid) (c)<br />
### Freeze_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Freeze_Status`
Super-classes |[brick:Status](Status) (c)<br />
### Freezer
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Freezer`
Super-classes |[brick:Laboratory](Laboratory) (c)<br />
### Frequency
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Frequency`
Super-classes |[brick:Quantity](Quantity) (c)<br />
Sub-classes |[brick:Alternating_Current_Frequency](Alternating_Current_Frequency) (c)<br />
### Frequency_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Frequency_Sensor`
Super-classes |[brick:Sensor](Sensor) (c)<br />
Sub-classes |[brick:Output_Frequency_Sensor](Output_Frequency_Sensor) (c)<br />
### Frost
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Frost`
Super-classes |[brick:Solid](Solid) (c)<br />
### Frost_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Frost_Sensor`
Super-classes |[brick:Sensor](Sensor) (c)<br />
### Fuel_Oil
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Fuel_Oil`
Description | <p>Petroleum based oil burned for energy</p>
Super-classes |[brick:Oil](Oil) (c)<br />
### Fume_Hood
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Fume_Hood`
Description | <p>A fume-collection device mounted over a work space, table, or shelf and serving to conduct unwanted gases away from the area enclosed.</p>
Super-classes |[brick:HVAC](HVAC) (c)<br />
### Fume_Hood_Air_Flow_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Fume_Hood_Air_Flow_Sensor`
Super-classes |[brick:Air_Flow_Sensor](Air_Flow_Sensor) (c)<br />
### Furniture
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Furniture`
Super-classes |[brick:Equipment](Equipment) (c)<br />
### Gas
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Gas`
Super-classes |[brick:Fluid](Fluid) (c)<br />
Sub-classes |[brick:Natural_Gas](Natural_Gas) (c)<br />[brick:Steam](Steam) (c)<br />[brick:Air](Air) (c)<br />
### Gasoline
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Gasoline`
Description | <p>Petroleum derived liquid used as a fuel source</p>
Super-classes |[brick:Liquid](Liquid) (c)<br />
### Grains
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Grains`
Super-classes |[brick:Quantity](Quantity) (c)<br />
### HVAC
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#HVAC`
Super-classes |[brick:Equipment](Equipment) (c)<br />
Sub-classes |[brick:Fan](Fan) (c)<br />[brick:Condenser](Condenser) (c)<br />[brick:CRAC](CRAC) (c)<br />[brick:Computer_Room_Air_Conditioning](Computer_Room_Air_Conditioning) (c)<br />[brick:Valve](Valve) (c)<br />[brick:Damper](Damper) (c)<br />[brick:VFD](VFD) (c)<br />[brick:Heat_Exchanger](Heat_Exchanger) (c)<br />[brick:Terminal_Unit](Terminal_Unit) (c)<br />[brick:Chiller](Chiller) (c)<br />[brick:Pump](Pump) (c)<br />[brick:Coil](Coil) (c)<br />[brick:Fume_Hood](Fume_Hood) (c)<br />[brick:Air_Handler_Unit](Air_Handler_Unit) (c)<br />[brick:AHU](AHU) (c)<br />[brick:Boiler](Boiler) (c)<br />[brick:Economizer](Economizer) (c)<br />[brick:Space_Heater](Space_Heater) (c)<br />[brick:Thermostat](Thermostat) (c)<br />[brick:Variable_Frequency_Drive](Variable_Frequency_Drive) (c)<br />[brick:Compressor](Compressor) (c)<br />[brick:Filter](Filter) (c)<br />
### HVAC_Zone
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#HVAC_Zone`
Super-classes |[brick:Zone](Zone) (c)<br />
### Hail
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Hail`
Super-classes |[brick:Solid](Solid) (c)<br />
### Hail_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Hail_Sensor`
Super-classes |[brick:Sensor](Sensor) (c)<br />
### Hand_Auto_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Hand_Auto_Status`
Super-classes |[brick:Status](Status) (c)<br />
### Heat_Exchanger
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Heat_Exchanger`
Super-classes |[brick:HVAC](HVAC) (c)<br />
Sub-classes |[brick:Evaporative_Heat_Exchanger](Evaporative_Heat_Exchanger) (c)<br />[brick:Condenser_Heat_Exchanger](Condenser_Heat_Exchanger) (c)<br />
### Heat_Exchanger_Discharge_Water_Temperature_Proportional_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Heat_Exchanger_Discharge_Water_Temperature_Proportional_Band_Setpoint`
Super-classes |[brick:Supply_Water_Temperature_Proportional_Band_Setpoint](Supply_Water_Temperature_Proportional_Band_Setpoint) (c)<br />
### Heat_Exchanger_Supply_Water_Temperature_Dead_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Heat_Exchanger_Supply_Water_Temperature_Dead_Band_Setpoint`
Super-classes |[brick:Supply_Water_Temperature_Dead_Band_Setpoint](Supply_Water_Temperature_Dead_Band_Setpoint) (c)<br />
### Heat_Exchanger_Supply_Water_Temperature_Proportional_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Heat_Exchanger_Supply_Water_Temperature_Proportional_Band_Setpoint`
Super-classes |[brick:Supply_Water_Temperature_Proportional_Band_Setpoint](Supply_Water_Temperature_Proportional_Band_Setpoint) (c)<br />
### Heat_Exchanger_Supply_Water_Temperature_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Heat_Exchanger_Supply_Water_Temperature_Sensor`
Super-classes |[brick:Water_Temperature_Sensor](Water_Temperature_Sensor) (c)<br />
### Heat_Exchanger_System_Enable_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Heat_Exchanger_System_Enable_Status`
Super-classes |[brick:Enable_Status](Enable_Status) (c)<br />
### Heat_Wheel_Differential_Pressure_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Heat_Wheel_Differential_Pressure_Sensor`
Super-classes |[brick:Differential_Pressure_Sensor](Differential_Pressure_Sensor) (c)<br />
### Heat_Wheel_Discharge_Air_Temperature_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Heat_Wheel_Discharge_Air_Temperature_Sensor`
Super-classes |[brick:Discharge_Air_Temperature_Sensor](Discharge_Air_Temperature_Sensor) (c)<br />
### Heat_Wheel_Speed_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Heat_Wheel_Speed_Sensor`
Super-classes |[brick:Differential_Speed_Sensor](Differential_Speed_Sensor) (c)<br />
### Heat_Wheel_VFD
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Heat_Wheel_VFD`
Super-classes |[brick:VFD](VFD) (c)<br />
### Heat_Wheel_Voltage_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Heat_Wheel_Voltage_Sensor`
Super-classes |[brick:Voltage_Sensor](Voltage_Sensor) (c)<br />
### Heating_Coil
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Heating_Coil`
Super-classes |[brick:Coil](Coil) (c)<br />
### Heating_Demand_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Heating_Demand_Setpoint`
Super-classes |[brick:Demand_Setpoint](Demand_Setpoint) (c)<br />
### Heating_Discharge_Air_Flow_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Heating_Discharge_Air_Flow_Setpoint`
Super-classes |[brick:Discharge_Air_Flow_Setpoint](Discharge_Air_Flow_Setpoint) (c)<br />
### Heating_Discharge_Air_Temperature_Dead_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Heating_Discharge_Air_Temperature_Dead_Band_Setpoint`
Super-classes |[brick:Discharge_Air_Temperature_Dead_Band_Setpoint](Discharge_Air_Temperature_Dead_Band_Setpoint) (c)<br />
### Heating_Discharge_Air_Temperature_Integral_Time_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Heating_Discharge_Air_Temperature_Integral_Time_Setpoint`
Super-classes |[brick:Integral_Time_Setpoint](Integral_Time_Setpoint) (c)<br />
### Heating_Discharge_Air_Temperature_Proportional_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Heating_Discharge_Air_Temperature_Proportional_Band_Setpoint`
Super-classes |[brick:Proportional_Band_Setpoint](Proportional_Band_Setpoint) (c)<br />
### Heating_On_Off_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Heating_On_Off_Status`
Super-classes |[brick:On_Off_Status](On_Off_Status) (c)<br />
### Heating_Request_Percent_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Heating_Request_Percent_Setpoint`
Super-classes |[brick:Demand_Setpoint](Demand_Setpoint) (c)<br />
### Heating_Request_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Heating_Request_Setpoint`
Super-classes |[brick:Demand_Setpoint](Demand_Setpoint) (c)<br />
### Heating_Supply_Air_Flow_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Heating_Supply_Air_Flow_Setpoint`
Super-classes |[brick:Supply_Air_Flow_Setpoint](Supply_Air_Flow_Setpoint) (c)<br />
### Heating_Supply_Air_Temperature_Dead_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Heating_Supply_Air_Temperature_Dead_Band_Setpoint`
Super-classes |[brick:Supply_Air_Temperature_Dead_Band_Setpoint](Supply_Air_Temperature_Dead_Band_Setpoint) (c)<br />
### Heating_Supply_Air_Temperature_Integral_Time_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Heating_Supply_Air_Temperature_Integral_Time_Setpoint`
Super-classes |[brick:Integral_Time_Setpoint](Integral_Time_Setpoint) (c)<br />
### Heating_Supply_Air_Temperature_Proportional_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Heating_Supply_Air_Temperature_Proportional_Band_Setpoint`
Super-classes |[brick:Proportional_Band_Setpoint](Proportional_Band_Setpoint) (c)<br />
### Heating_Valve
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Heating_Valve`
Super-classes |[brick:Valve](Valve) (c)<br />
Sub-classes |[brick:Preheat_Hot_Water_Valve](Preheat_Hot_Water_Valve) (c)<br />[brick:Reheat_Valve](Reheat_Valve) (c)<br />[brick:Domestic_Hot_Water_Valve](Domestic_Hot_Water_Valve) (c)<br />
### Heating_Ventilation_Air_Conditioning_System
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Heating_Ventilation_Air_Conditioning_System`
Super-classes |[brick:Equipment](Equipment) (c)<br />
### High_Humidity_Alarm_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#High_Humidity_Alarm_Setpoint`
Super-classes |[brick:Humidity_Setpoint](Humidity_Setpoint) (c)<br />
### High_Outside_Air_Lockout_Temperature_Differential_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#High_Outside_Air_Lockout_Temperature_Differential_Sensor`
Super-classes |[brick:Outside_Air_Lockout_Temperature_Differential_Sensor](Outside_Air_Lockout_Temperature_Differential_Sensor) (c)<br />
### High_Static_Pressure_Cutout_Limit_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#High_Static_Pressure_Cutout_Limit_Setpoint`
Super-classes |[brick:Static_Pressure_Setpoint](Static_Pressure_Setpoint) (c)<br />
### High_Temperature_Hot_Water_Supply_Temperature_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#High_Temperature_Hot_Water_Supply_Temperature_Sensor`
Super-classes |[brick:Hot_Water_Supply_Temperature_Sensor](Hot_Water_Supply_Temperature_Sensor) (c)<br />
### Highest_Zone_Temperature_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Highest_Zone_Temperature_Sensor`
Super-classes |[brick:Zone_Temperature_Sensor](Zone_Temperature_Sensor) (c)<br />
### Hold_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Hold_Status`
Super-classes |[brick:Status](Status) (c)<br />
### Hot_Box
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Hot_Box`
Super-classes |[brick:Laboratory](Laboratory) (c)<br />
### Hot_Water
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Hot_Water`
Description | <p>Hot water used for HVAC heating or supply to hot taps</p>
Super-classes |[brick:Water](Water) (c)<br />
### Hot_Water_Coil_Entering_Temperature_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Coil_Entering_Temperature_Sensor`
Super-classes |[brick:Entering_Water_Temperature_Sensor](Entering_Water_Temperature_Sensor) (c)<br />
### Hot_Water_Differential_Pressure_Dead_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Differential_Pressure_Dead_Band_Setpoint`
Super-classes |[brick:Differential_Pressure_Dead_Band_Setpoint](Differential_Pressure_Dead_Band_Setpoint) (c)<br />
### Hot_Water_Differential_Pressure_Integral_Time_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Differential_Pressure_Integral_Time_Setpoint`
Super-classes |[brick:Differential_Pressure_Integral_Time_Setpoint](Differential_Pressure_Integral_Time_Setpoint) (c)<br />
### Hot_Water_Differential_Pressure_Load_Shed_Reset_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Differential_Pressure_Load_Shed_Reset_Status`
Super-classes |[brick:Differential_Pressure_Load_Shed_Status](Differential_Pressure_Load_Shed_Status) (c)<br />
### Hot_Water_Differential_Pressure_Load_Shed_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Differential_Pressure_Load_Shed_Status`
Super-classes |[brick:Differential_Pressure_Load_Shed_Status](Differential_Pressure_Load_Shed_Status) (c)<br />
### Hot_Water_Differential_Pressure_Proportional_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Differential_Pressure_Proportional_Band_Setpoint`
Super-classes |[brick:Proportional_Band_Setpoint](Proportional_Band_Setpoint) (c)<br />
### Hot_Water_Differential_Pressure_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Differential_Pressure_Sensor`
Super-classes |[brick:Differential_Pressure_Sensor](Differential_Pressure_Sensor) (c)<br />
Sub-classes |[brick:Medium_Temperature_Hot_Water_Differential_Pressure_Sensor](Medium_Temperature_Hot_Water_Differential_Pressure_Sensor) (c)<br />
### Hot_Water_Differential_Pressure_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Differential_Pressure_Setpoint`
Super-classes |[brick:Differential_Pressure_Setpoint](Differential_Pressure_Setpoint) (c)<br />
### Hot_Water_Discharge_Temperature_Load_Shed_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Discharge_Temperature_Load_Shed_Status`
Super-classes |[brick:Differential_Pressure_Load_Shed_Status](Differential_Pressure_Load_Shed_Status) (c)<br />
### Hot_Water_Pump
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Pump`
Super-classes |[brick:Water_Pump](Water_Pump) (c)<br />
### Hot_Water_Return_Temperature_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Return_Temperature_Sensor`
Super-classes |[brick:Return_Water_Temperature_Sensor](Return_Water_Temperature_Sensor) (c)<br />
### Hot_Water_Static_Pressure_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Static_Pressure_Setpoint`
Super-classes |[brick:Static_Pressure_Setpoint](Static_Pressure_Setpoint) (c)<br />
### Hot_Water_Supply_Temperature_Load_Shed_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Supply_Temperature_Load_Shed_Status`
Super-classes |[brick:Differential_Pressure_Load_Shed_Status](Differential_Pressure_Load_Shed_Status) (c)<br />
### Hot_Water_Supply_Temperature_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Supply_Temperature_Sensor`
Super-classes |[brick:Water_Temperature_Sensor](Water_Temperature_Sensor) (c)<br />
Sub-classes |[brick:Medium_Temperature_Hot_Water_Supply_Temperature_Sensor](Medium_Temperature_Hot_Water_Supply_Temperature_Sensor) (c)<br />[brick:Domestic_Hot_Water_Supply_Temperature_Sensor](Domestic_Hot_Water_Supply_Temperature_Sensor) (c)<br />[brick:High_Temperature_Hot_Water_Supply_Temperature_Sensor](High_Temperature_Hot_Water_Supply_Temperature_Sensor) (c)<br />
### Hot_Water_System
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Hot_Water_System`
Super-classes |[brick:Water_System](Water_System) (c)<br />
### Humidification_On_Off_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Humidification_On_Off_Status`
Super-classes |[brick:On_Off_Status](On_Off_Status) (c)<br />
### Humidifier_Fault_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Humidifier_Fault_Status`
Super-classes |[brick:Fault_Status](Fault_Status) (c)<br />
### Humidity
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Humidity`
Super-classes |[brick:Quantity](Quantity) (c)<br />
### Humidity_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Humidity_Sensor`
Super-classes |[brick:Sensor](Sensor) (c)<br />
Sub-classes |[brick:Air_Humidity_Sensor](Air_Humidity_Sensor) (c)<br />
### Humidity_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Humidity_Setpoint`
Super-classes |[brick:Setpoint](Setpoint) (c)<br />
Sub-classes |[brick:High_Humidity_Alarm_Setpoint](High_Humidity_Alarm_Setpoint) (c)<br />[brick:Low_Humidity_Alarm_Setpoint](Low_Humidity_Alarm_Setpoint) (c)<br />
### Ice
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Ice`
Description | <p>Water in its solid form</p>
Super-classes |[brick:Solid](Solid) (c)<br />
### Ice_Tank_Entering_Water_Temperature_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Ice_Tank_Entering_Water_Temperature_Sensor`
Super-classes |[brick:Entering_Water_Temperature_Sensor](Entering_Water_Temperature_Sensor) (c)<br />
### Ice_Tank_Leaving_Water_Temperature_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Ice_Tank_Leaving_Water_Temperature_Sensor`
Super-classes |[brick:Leaving_Water_Temperature_Sensor](Leaving_Water_Temperature_Sensor) (c)<br />
### Illuminance
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Illuminance`
Super-classes |[brick:Quantity](Quantity) (c)<br />
### Increase_Decrease_Step_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Increase_Decrease_Step_Setpoint`
Super-classes |[brick:Setpoint](Setpoint) (c)<br />
Sub-classes |[brick:Temperature_Increase_Decrease_Step_Setpoint](Temperature_Increase_Decrease_Step_Setpoint) (c)<br />[brick:Static_Pressure_Increase_Decrease_Step_Setpoint](Static_Pressure_Increase_Decrease_Step_Setpoint) (c)<br />[brick:Differential_Pressure_Increase_Decrease_Step_Setpoint](Differential_Pressure_Increase_Decrease_Step_Setpoint) (c)<br />
### Integral_Gain_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Integral_Gain_Setpoint`
Super-classes |[brick:Setpoint](Setpoint) (c)<br />
### Integral_Time_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Integral_Time_Setpoint`
Super-classes |[brick:Setpoint](Setpoint) (c)<br />
Sub-classes |[brick:Cooling_Discharge_Air_Temperature_Integral_Time_Setpoint](Cooling_Discharge_Air_Temperature_Integral_Time_Setpoint) (c)<br />[brick:Cooling_Supply_Air_Temperature_Integral_Time_Setpoint](Cooling_Supply_Air_Temperature_Integral_Time_Setpoint) (c)<br />[brick:Supply_Air_Static_Pressure_Integral_Time_Setpoint](Supply_Air_Static_Pressure_Integral_Time_Setpoint) (c)<br />[brick:Heating_Discharge_Air_Temperature_Integral_Time_Setpoint](Heating_Discharge_Air_Temperature_Integral_Time_Setpoint) (c)<br />[brick:Chilled_Water_Differential_Pressure_Integral_Time_Setpoint](Chilled_Water_Differential_Pressure_Integral_Time_Setpoint) (c)<br />[brick:Exhaust_Air_Flow_Integral_Time_Setpoint](Exhaust_Air_Flow_Integral_Time_Setpoint) (c)<br />[brick:Heating_Supply_Air_Temperature_Integral_Time_Setpoint](Heating_Supply_Air_Temperature_Integral_Time_Setpoint) (c)<br />[brick:Supply_Water_Temperature_Integral_Time_Setpoint](Supply_Water_Temperature_Integral_Time_Setpoint) (c)<br />[brick:Differential_Pressure_Integral_Time](Differential_Pressure_Integral_Time) (c)<br />[brick:Discharge_Air_Static_Pressure_Integral_Time_Setpoint](Discharge_Air_Static_Pressure_Integral_Time_Setpoint) (c)<br />[brick:Differential_Pressure_Integral_Time_Setpoint](Differential_Pressure_Integral_Time_Setpoint) (c)<br />[brick:Static_Pressure_Integral_Time_Setpoint](Static_Pressure_Integral_Time_Setpoint) (c)<br />[brick:Supply_Water_Differential_Pressure_Integral_Time_Setpoint](Supply_Water_Differential_Pressure_Integral_Time_Setpoint) (c)<br />
### Interface
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Interface`
Super-classes |[brick:Lighting_System](Lighting_System) (c)<br />
Sub-classes |[brick:Touchpanel](Touchpanel) (c)<br />[brick:Switch](Switch) (c)<br />
### Irradiance
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Irradiance`
Super-classes |[brick:Quantity](Quantity) (c)<br />
Sub-classes |[brick:Solar_Irradiance](Solar_Irradiance) (c)<br />
### Isolation_Valve
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Isolation_Valve`
Super-classes |[brick:Valve](Valve) (c)<br />
### Laboratory
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Laboratory`
Super-classes |[brick:Room](Room) (c)<br />
Sub-classes |[brick:Environment_Box](Environment_Box) (c)<br />[brick:Freezer](Freezer) (c)<br />[brick:Cold_Box](Cold_Box) (c)<br />[brick:Hot_Box](Hot_Box) (c)<br />
### Last_Fault_Code_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Last_Fault_Code_Status`
Super-classes |[brick:Status](Status) (c)<br />
### Lead_Lag_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Lead_Lag_Status`
Super-classes |[brick:Status](Status) (c)<br />
### Leaving_Water_Temperature_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Leaving_Water_Temperature_Sensor`
Super-classes |[brick:Water_Temperature_Sensor](Water_Temperature_Sensor) (c)<br />
Sub-classes |[brick:PreHeat_Coil_Leaving_Air_Temperature_Sensor](PreHeat_Coil_Leaving_Air_Temperature_Sensor) (c)<br />[brick:Ice_Tank_Leaving_Water_Temperature_Sensor](Ice_Tank_Leaving_Water_Temperature_Sensor) (c)<br />
### Leaving_Water_Temperature_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Leaving_Water_Temperature_Setpoint`
Super-classes |[brick:Water_Temperature_Setpoint](Water_Temperature_Setpoint) (c)<br />
### Level
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Level`
Super-classes |[brick:Quantity](Quantity) (c)<br />
### Lighting
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Lighting`
Super-classes |[brick:Lighting_System](Lighting_System) (c)<br />
Sub-classes |[brick:Luminaire](Luminaire) (c)<br />[brick:Luminaire_Driver](Luminaire_Driver) (c)<br />
### Lighting_System
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Lighting_System`
Super-classes |[brick:Equipment](Equipment) (c)<br />
Sub-classes |[brick:Interface](Interface) (c)<br />[brick:Lighting](Lighting) (c)<br />
### Lighting_Zone
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Lighting_Zone`
Super-classes |[brick:Zone](Zone) (c)<br />
### Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Limit`
Super-classes |[brick:Point](Point) (c)<br />
Sub-classes |[brick:Static_Pressure_Setpoint_Limit](Static_Pressure_Setpoint_Limit) (c)<br />[brick:Damper_Position_Limit](Damper_Position_Limit) (c)<br />[brick:Max_Limit](Max_Limit) (c)<br />[brick:Speed_Setpoint_Limit](Speed_Setpoint_Limit) (c)<br />[brick:Air_Flow_Setpoint_Limit](Air_Flow_Setpoint_Limit) (c)<br />[brick:Differential_Pressure_Setpoint_Limit](Differential_Pressure_Setpoint_Limit) (c)<br />[brick:Min_Limit](Min_Limit) (c)<br />
### Liquid
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Liquid`
Super-classes |[brick:Fluid](Fluid) (c)<br />
Sub-classes |[brick:Water](Water) (c)<br />[brick:Oil](Oil) (c)<br />[brick:Gasoline](Gasoline) (c)<br />
### Load_Current_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Load_Current_Sensor`
Super-classes |[brick:Current_Sensor](Current_Sensor) (c)<br />
### Load_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Load_Setpoint`
Super-classes |[brick:Setpoint](Setpoint) (c)<br />
Sub-classes |[brick:Max_Load_Setpoint](Max_Load_Setpoint) (c)<br />
### Load_Shed_Differential_Pressure_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Load_Shed_Differential_Pressure_Setpoint`
Super-classes |[brick:Differential_Pressure_Setpoint](Differential_Pressure_Setpoint) (c)<br />
Sub-classes |[brick:Medium_Temperature_Hot_Water_Differential_Pressure_Load_Shed_Setpoint](Medium_Temperature_Hot_Water_Differential_Pressure_Load_Shed_Setpoint) (c)<br />[brick:Chilled_Water_Differential_Pressure_Load_Shed_Setpoint](Chilled_Water_Differential_Pressure_Load_Shed_Setpoint) (c)<br />
### Load_Shed_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Load_Shed_Status`
Super-classes |[brick:Status](Status) (c)<br />
Sub-classes |[brick:Differential_Pressure_Load_Shed_Status](Differential_Pressure_Load_Shed_Status) (c)<br />
### Locally_On_Off_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Locally_On_Off_Status`
Super-classes |[brick:On_Off_Status](On_Off_Status) (c)<br />
### Location
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Location`
Sub-classes |[brick:Space](Space) (c)<br />[brick:Floor](Floor) (c)<br />[brick:City](City) (c)<br />[brick:Room](Room) (c)<br />[brick:Basement](Basement) (c)<br />[brick:Roof](Roof) (c)<br />[brick:Wing](Wing) (c)<br />[brick:Building](Building) (c)<br />[brick:Zone](Zone) (c)<br />[brick:Outside](Outside) (c)<br />
In domain of |[brick:isLocationOf](isLocationOf) (op)<br />
In range of |[brick:hasLocation](hasLocation) (op)<br />
### Low_Humidity_Alarm_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Low_Humidity_Alarm_Setpoint`
Super-classes |[brick:Humidity_Setpoint](Humidity_Setpoint) (c)<br />
### Low_Outside_Air_Lockout_Temperature_Differential_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Low_Outside_Air_Lockout_Temperature_Differential_Sensor`
Super-classes |[brick:Outside_Air_Lockout_Temperature_Differential_Sensor](Outside_Air_Lockout_Temperature_Differential_Sensor) (c)<br />
### Low_Outside_Air_Temperature_Enable_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Low_Outside_Air_Temperature_Enable_Setpoint`
Super-classes |[brick:Outside_Air_Temperature_Setpoint](Outside_Air_Temperature_Setpoint) (c)<br />
### Lowest_Exhaust_Air_Static_Pressure_Sensor:
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Lowest_Exhaust_Air_Static_Pressure_Sensor:`
Super-classes |[brick:Exhaust_Air_Static_Pressure_Sensor:](Exhaust_Air_Static_Pressure_Sensor:) (c)<br />
### Lowest_Zone_Temperature_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Lowest_Zone_Temperature_Sensor`
Super-classes |[brick:Zone_Temperature_Sensor](Zone_Temperature_Sensor) (c)<br />
### Luminaire
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Luminaire`
Super-classes |[brick:Lighting](Lighting) (c)<br />
### Luminaire_Driver
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Luminaire_Driver`
Super-classes |[brick:Lighting](Lighting) (c)<br />
### Luminance
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Luminance`
Super-classes |[brick:Substance](Substance) (c)<br />[brick:Quantity](Quantity) (c)<br />
Sub-classes |[brick:Luminous_Flux](Luminous_Flux) (c)<br />[brick:Luminous_Intensity](Luminous_Intensity) (c)<br />
### Luminance_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Luminance_Sensor`
Super-classes |[brick:Sensor](Sensor) (c)<br />
Sub-classes |[brick:Outside_Luminance_Sensor](Outside_Luminance_Sensor) (c)<br />
### Luminance_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Luminance_Setpoint`
Super-classes |[brick:Setpoint](Setpoint) (c)<br />
### Luminous_Flux
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Luminous_Flux`
Super-classes |[brick:Luminance](Luminance) (c)<br />
### Luminous_Intensity
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Luminous_Intensity`
Super-classes |[brick:Luminance](Luminance) (c)<br />
### Makeup_Water
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Makeup_Water`
Description | <p>Water used used to makeup water loss through leaks, evaporation, or blowdown</p>
Super-classes |[brick:Water](Water) (c)<br />
### Manual_Auto_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Manual_Auto_Status`
Super-classes |[brick:Status](Status) (c)<br />
### Max_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Max_Air_Flow_Setpoint_Limit`
Super-classes |[brick:Max_Limit](Max_Limit) (c)<br />[brick:Air_Flow_Setpoint_Limit](Air_Flow_Setpoint_Limit) (c)<br />
Sub-classes |[brick:Max_Cooling_Discharge_Air_Flow_Setpoint_Limit](Max_Cooling_Discharge_Air_Flow_Setpoint_Limit) (c)<br />[brick:Max_Heating_Supply_Air_Flow_Setpoint_Limit](Max_Heating_Supply_Air_Flow_Setpoint_Limit) (c)<br />[brick:Max_Cooling_Supply_Air_Flow_Setpoint_Limit](Max_Cooling_Supply_Air_Flow_Setpoint_Limit) (c)<br />[brick:Max_Heating_Discharge_Air_Flow_Setpoint_Limit](Max_Heating_Discharge_Air_Flow_Setpoint_Limit) (c)<br />
### Max_Chilled_Water_Differential_Pressure_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Max_Chilled_Water_Differential_Pressure_Setpoint_Limit`
Super-classes |[brick:Max_Limit](Max_Limit) (c)<br />[brick:Differential_Pressure_Setpoint_Limit](Differential_Pressure_Setpoint_Limit) (c)<br />
### Max_Cooling_Discharge_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Max_Cooling_Discharge_Air_Flow_Setpoint_Limit`
Super-classes |[brick:Max_Air_Flow_Setpoint_Limit](Max_Air_Flow_Setpoint_Limit) (c)<br />
Sub-classes |[brick:Max_Unoccupied_Cooling_Discharge_Air_Flow_Setpoint_Limit](Max_Unoccupied_Cooling_Discharge_Air_Flow_Setpoint_Limit) (c)<br />[brick:Max_Occupied_Cooling_Discharge_Air_Flow_Setpoint_Limit](Max_Occupied_Cooling_Discharge_Air_Flow_Setpoint_Limit) (c)<br />
### Max_Cooling_Supply_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Max_Cooling_Supply_Air_Flow_Setpoint_Limit`
Super-classes |[brick:Max_Air_Flow_Setpoint_Limit](Max_Air_Flow_Setpoint_Limit) (c)<br />
Sub-classes |[brick:Max_Unoccupied_Cooling_Supply_Air_Flow_Setpoint_Limit](Max_Unoccupied_Cooling_Supply_Air_Flow_Setpoint_Limit) (c)<br />[brick:Max_Occupied_Cooling_Supply_Air_Flow_Setpoint_Limit](Max_Occupied_Cooling_Supply_Air_Flow_Setpoint_Limit) (c)<br />
### Max_Damper_Position_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Max_Damper_Position_Setpoint_Limit`
Super-classes |[brick:Damper_Position_Limit](Damper_Position_Limit) (c)<br />[brick:Max_Limit](Max_Limit) (c)<br />
### Max_Discharge_Air_Static_Pressure_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Max_Discharge_Air_Static_Pressure_Setpoint_Limit`
Super-classes |[brick:Max_Static_Pressure_Setpoint_Limit](Max_Static_Pressure_Setpoint_Limit) (c)<br />[brick:Max_Limit](Max_Limit) (c)<br />
### Max_Heating_Discharge_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Max_Heating_Discharge_Air_Flow_Setpoint_Limit`
Super-classes |[brick:Max_Air_Flow_Setpoint_Limit](Max_Air_Flow_Setpoint_Limit) (c)<br />
Sub-classes |[brick:Max_Occupied_Heating_Discharge_Air_Flow_Setpoint_Limit](Max_Occupied_Heating_Discharge_Air_Flow_Setpoint_Limit) (c)<br />[brick:Max_Unoccupied_Heating_Discharge_Air_Flow_Setpoint_Limit](Max_Unoccupied_Heating_Discharge_Air_Flow_Setpoint_Limit) (c)<br />
### Max_Heating_Supply_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Max_Heating_Supply_Air_Flow_Setpoint_Limit`
Super-classes |[brick:Max_Air_Flow_Setpoint_Limit](Max_Air_Flow_Setpoint_Limit) (c)<br />
Sub-classes |[brick:Max_Unoccupied_Heating_Supply_Air_Flow_Setpoint_Limit](Max_Unoccupied_Heating_Supply_Air_Flow_Setpoint_Limit) (c)<br />[brick:Max_Occupied_Heating_Supply_Air_Flow_Setpoint_Limit](Max_Occupied_Heating_Supply_Air_Flow_Setpoint_Limit) (c)<br />
### Max_Hot_Water_Differential_Pressure_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Max_Hot_Water_Differential_Pressure_Setpoint_Limit`
Super-classes |[brick:Differential_Pressure_Setpoint_Limit](Differential_Pressure_Setpoint_Limit) (c)<br />[brick:Max_Limit](Max_Limit) (c)<br />
### Max_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Max_Limit`
Super-classes |[brick:Limit](Limit) (c)<br />
Sub-classes |[brick:Max_Damper_Position_Setpoint_Limit](Max_Damper_Position_Setpoint_Limit) (c)<br />[brick:Max_Air_Flow_Setpoint_Limit](Max_Air_Flow_Setpoint_Limit) (c)<br />[brick:Max_Supply_Air_Static_Pressure_Setpoint_Limit](Max_Supply_Air_Static_Pressure_Setpoint_Limit) (c)<br />[brick:Max_Discharge_Air_Static_Pressure_Setpoint_Limit](Max_Discharge_Air_Static_Pressure_Setpoint_Limit) (c)<br />[brick:Max_Speed_Setpoint_Limit](Max_Speed_Setpoint_Limit) (c)<br />[brick:Max_Hot_Water_Differential_Pressure_Setpoint_Limit](Max_Hot_Water_Differential_Pressure_Setpoint_Limit) (c)<br />[brick:Max_Static_Pressure_Setpoint_Limit](Max_Static_Pressure_Setpoint_Limit) (c)<br />[brick:Max_Chilled_Water_Differential_Pressure_Setpoint_Limit](Max_Chilled_Water_Differential_Pressure_Setpoint_Limit) (c)<br />
### Max_Load_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Max_Load_Setpoint`
Super-classes |[brick:Load_Setpoint](Load_Setpoint) (c)<br />
### Max_Occupied_Cooling_Discharge_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Max_Occupied_Cooling_Discharge_Air_Flow_Setpoint_Limit`
Super-classes |[brick:Max_Cooling_Discharge_Air_Flow_Setpoint_Limit](Max_Cooling_Discharge_Air_Flow_Setpoint_Limit) (c)<br />
### Max_Occupied_Cooling_Supply_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Max_Occupied_Cooling_Supply_Air_Flow_Setpoint_Limit`
Super-classes |[brick:Max_Cooling_Supply_Air_Flow_Setpoint_Limit](Max_Cooling_Supply_Air_Flow_Setpoint_Limit) (c)<br />
### Max_Occupied_Heating_Discharge_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Max_Occupied_Heating_Discharge_Air_Flow_Setpoint_Limit`
Super-classes |[brick:Max_Heating_Discharge_Air_Flow_Setpoint_Limit](Max_Heating_Discharge_Air_Flow_Setpoint_Limit) (c)<br />
### Max_Occupied_Heating_Supply_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Max_Occupied_Heating_Supply_Air_Flow_Setpoint_Limit`
Super-classes |[brick:Max_Heating_Supply_Air_Flow_Setpoint_Limit](Max_Heating_Supply_Air_Flow_Setpoint_Limit) (c)<br />
### Max_Return_Air_CO2_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Max_Return_Air_CO2_Setpoint`
Super-classes |[brick:Return_Air_CO2_Setpoint](Return_Air_CO2_Setpoint) (c)<br />
### Max_Speed_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Max_Speed_Setpoint_Limit`
Super-classes |[brick:Speed_Setpoint_Limit](Speed_Setpoint_Limit) (c)<br />[brick:Max_Limit](Max_Limit) (c)<br />
### Max_Static_Pressure_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Max_Static_Pressure_Setpoint_Limit`
Super-classes |[brick:Static_Pressure_Setpoint_Limit](Static_Pressure_Setpoint_Limit) (c)<br />[brick:Max_Limit](Max_Limit) (c)<br />
Sub-classes |[brick:Max_Discharge_Air_Static_Pressure_Setpoint_Limit](Max_Discharge_Air_Static_Pressure_Setpoint_Limit) (c)<br />[brick:Max_Supply_Air_Static_Pressure_Setpoint_Limit](Max_Supply_Air_Static_Pressure_Setpoint_Limit) (c)<br />
### Max_Supply_Air_Static_Pressure_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Max_Supply_Air_Static_Pressure_Setpoint_Limit`
Super-classes |[brick:Max_Limit](Max_Limit) (c)<br />[brick:Max_Static_Pressure_Setpoint_Limit](Max_Static_Pressure_Setpoint_Limit) (c)<br />
### Max_Unoccupied_Cooling_Discharge_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Max_Unoccupied_Cooling_Discharge_Air_Flow_Setpoint_Limit`
Super-classes |[brick:Max_Cooling_Discharge_Air_Flow_Setpoint_Limit](Max_Cooling_Discharge_Air_Flow_Setpoint_Limit) (c)<br />
### Max_Unoccupied_Cooling_Supply_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Max_Unoccupied_Cooling_Supply_Air_Flow_Setpoint_Limit`
Super-classes |[brick:Max_Cooling_Supply_Air_Flow_Setpoint_Limit](Max_Cooling_Supply_Air_Flow_Setpoint_Limit) (c)<br />
### Max_Unoccupied_Heating_Discharge_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Max_Unoccupied_Heating_Discharge_Air_Flow_Setpoint_Limit`
Super-classes |[brick:Max_Heating_Discharge_Air_Flow_Setpoint_Limit](Max_Heating_Discharge_Air_Flow_Setpoint_Limit) (c)<br />
### Max_Unoccupied_Heating_Supply_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Max_Unoccupied_Heating_Supply_Air_Flow_Setpoint_Limit`
Super-classes |[brick:Max_Heating_Supply_Air_Flow_Setpoint_Limit](Max_Heating_Supply_Air_Flow_Setpoint_Limit) (c)<br />
### Medium_Temperature_Hot_Water_Differential_Pressure_Load_Shed_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Medium_Temperature_Hot_Water_Differential_Pressure_Load_Shed_Setpoint`
Super-classes |[brick:Load_Shed_Differential_Pressure_Setpoint](Load_Shed_Differential_Pressure_Setpoint) (c)<br />
### Medium_Temperature_Hot_Water_Differential_Pressure_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Medium_Temperature_Hot_Water_Differential_Pressure_Sensor`
Super-classes |[brick:Hot_Water_Differential_Pressure_Sensor](Hot_Water_Differential_Pressure_Sensor) (c)<br />
### Medium_Temperature_Hot_Water_Supply_Temperature_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Medium_Temperature_Hot_Water_Supply_Temperature_Sensor`
Super-classes |[brick:Hot_Water_Supply_Temperature_Sensor](Hot_Water_Supply_Temperature_Sensor) (c)<br />
### Meter
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Meter`
Super-classes |[brick:Equipment](Equipment) (c)<br />
### Min_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Min_Air_Flow_Setpoint_Limit`
Super-classes |[brick:Min_Limit](Min_Limit) (c)<br />[brick:Air_Flow_Setpoint_Limit](Air_Flow_Setpoint_Limit) (c)<br />
Sub-classes |[brick:Min_Cooling_Discharge_Air_Flow_Setpoint_Limit](Min_Cooling_Discharge_Air_Flow_Setpoint_Limit) (c)<br />[brick:Min_Heating_Discharge_Air_Flow_Setpoint_Limit](Min_Heating_Discharge_Air_Flow_Setpoint_Limit) (c)<br />[brick:Min_Cooling_Supply_Air_Flow_Setpoint_Limit](Min_Cooling_Supply_Air_Flow_Setpoint_Limit) (c)<br />[brick:Min_Heating_Supply_Air_Flow_Setpoint_Limit](Min_Heating_Supply_Air_Flow_Setpoint_Limit) (c)<br />[brick:Min_Outside_Air_Flow_Setpoint_Limit](Min_Outside_Air_Flow_Setpoint_Limit) (c)<br />
### Min_Chilled_Water_Differential_Pressure_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Min_Chilled_Water_Differential_Pressure_Setpoint_Limit`
Super-classes |[brick:Min_Limit](Min_Limit) (c)<br />[brick:Differential_Pressure_Setpoint_Limit](Differential_Pressure_Setpoint_Limit) (c)<br />
### Min_Cooling_Discharge_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Min_Cooling_Discharge_Air_Flow_Setpoint_Limit`
Super-classes |[brick:Min_Air_Flow_Setpoint_Limit](Min_Air_Flow_Setpoint_Limit) (c)<br />
Sub-classes |[brick:Min_Occupied_Cooling_Discharge_Air_Flow_Setpoint_Limit](Min_Occupied_Cooling_Discharge_Air_Flow_Setpoint_Limit) (c)<br />[brick:Min_Unoccupied_Cooling_Discharge_Air_Flow_Setpoint_Limit](Min_Unoccupied_Cooling_Discharge_Air_Flow_Setpoint_Limit) (c)<br />
### Min_Cooling_Supply_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Min_Cooling_Supply_Air_Flow_Setpoint_Limit`
Super-classes |[brick:Min_Air_Flow_Setpoint_Limit](Min_Air_Flow_Setpoint_Limit) (c)<br />
Sub-classes |[brick:Min_Occupied_Cooling_Supply_Air_Flow_Setpoint_Limit](Min_Occupied_Cooling_Supply_Air_Flow_Setpoint_Limit) (c)<br />[brick:Min_Unoccupied_Cooling_Supply_Air_Flow_Setpoint_Limit](Min_Unoccupied_Cooling_Supply_Air_Flow_Setpoint_Limit) (c)<br />
### Min_Damper_Position_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Min_Damper_Position_Setpoint_Limit`
Super-classes |[brick:Damper_Position_Limit](Damper_Position_Limit) (c)<br />[brick:Min_Limit](Min_Limit) (c)<br />
### Min_Discharge_Air_Static_Pressure_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Min_Discharge_Air_Static_Pressure_Setpoint_Limit`
Super-classes |[brick:Min_Limit](Min_Limit) (c)<br />[brick:Min_Static_Pressure_Setpoint_Limit](Min_Static_Pressure_Setpoint_Limit) (c)<br />
### Min_Heating_Discharge_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Min_Heating_Discharge_Air_Flow_Setpoint_Limit`
Super-classes |[brick:Min_Air_Flow_Setpoint_Limit](Min_Air_Flow_Setpoint_Limit) (c)<br />
Sub-classes |[brick:Min_Occupied_Heating_Discharge_Air_Flow_Setpoint_Limit](Min_Occupied_Heating_Discharge_Air_Flow_Setpoint_Limit) (c)<br />[brick:Min_Unoccupied_Heating_Discharge_Air_Flow_Setpoint_Limit](Min_Unoccupied_Heating_Discharge_Air_Flow_Setpoint_Limit) (c)<br />
### Min_Heating_Supply_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Min_Heating_Supply_Air_Flow_Setpoint_Limit`
Super-classes |[brick:Min_Air_Flow_Setpoint_Limit](Min_Air_Flow_Setpoint_Limit) (c)<br />
Sub-classes |[brick:Min_Occupied_Heating_Supply_Air_Flow_Setpoint_Limit](Min_Occupied_Heating_Supply_Air_Flow_Setpoint_Limit) (c)<br />[brick:Min_Unoccupied_Heating_Supply_Air_Flow_Setpoint_Limit](Min_Unoccupied_Heating_Supply_Air_Flow_Setpoint_Limit) (c)<br />
### Min_Hot_Water_Differential_Pressure_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Min_Hot_Water_Differential_Pressure_Setpoint_Limit`
Super-classes |[brick:Differential_Pressure_Setpoint_Limit](Differential_Pressure_Setpoint_Limit) (c)<br />[brick:Min_Limit](Min_Limit) (c)<br />
### Min_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Min_Limit`
Super-classes |[brick:Limit](Limit) (c)<br />
Sub-classes |[brick:Min_Speed_Setpoint_Limit](Min_Speed_Setpoint_Limit) (c)<br />[brick:Min_Hot_Water_Differential_Pressure_Setpoint_Limit](Min_Hot_Water_Differential_Pressure_Setpoint_Limit) (c)<br />[brick:Min_Discharge_Air_Static_Pressure_Setpoint_Limit](Min_Discharge_Air_Static_Pressure_Setpoint_Limit) (c)<br />[brick:Min_Chilled_Water_Differential_Pressure_Setpoint_Limit](Min_Chilled_Water_Differential_Pressure_Setpoint_Limit) (c)<br />[brick:Min_Air_Flow_Setpoint_Limit](Min_Air_Flow_Setpoint_Limit) (c)<br />[brick:Min_Damper_Position_Setpoint_Limit](Min_Damper_Position_Setpoint_Limit) (c)<br />[brick:Min_Supply_Air_Static_Pressure_Setpoint_Limit](Min_Supply_Air_Static_Pressure_Setpoint_Limit) (c)<br />[brick:Min_Static_Pressure_Setpoint_Limit](Min_Static_Pressure_Setpoint_Limit) (c)<br />
### Min_Occupied_Cooling_Discharge_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Min_Occupied_Cooling_Discharge_Air_Flow_Setpoint_Limit`
Super-classes |[brick:Min_Cooling_Discharge_Air_Flow_Setpoint_Limit](Min_Cooling_Discharge_Air_Flow_Setpoint_Limit) (c)<br />
### Min_Occupied_Cooling_Supply_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Min_Occupied_Cooling_Supply_Air_Flow_Setpoint_Limit`
Super-classes |[brick:Min_Cooling_Supply_Air_Flow_Setpoint_Limit](Min_Cooling_Supply_Air_Flow_Setpoint_Limit) (c)<br />
### Min_Occupied_Heating_Discharge_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Min_Occupied_Heating_Discharge_Air_Flow_Setpoint_Limit`
Super-classes |[brick:Min_Heating_Discharge_Air_Flow_Setpoint_Limit](Min_Heating_Discharge_Air_Flow_Setpoint_Limit) (c)<br />
### Min_Occupied_Heating_Supply_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Min_Occupied_Heating_Supply_Air_Flow_Setpoint_Limit`
Super-classes |[brick:Min_Heating_Supply_Air_Flow_Setpoint_Limit](Min_Heating_Supply_Air_Flow_Setpoint_Limit) (c)<br />
### Min_Outside_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Min_Outside_Air_Flow_Setpoint_Limit`
Super-classes |[brick:Min_Air_Flow_Setpoint_Limit](Min_Air_Flow_Setpoint_Limit) (c)<br />
### Min_Speed_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Min_Speed_Setpoint_Limit`
Super-classes |[brick:Min_Limit](Min_Limit) (c)<br />[brick:Speed_Setpoint_Limit](Speed_Setpoint_Limit) (c)<br />
### Min_Static_Pressure_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Min_Static_Pressure_Setpoint_Limit`
Super-classes |[brick:Static_Pressure_Setpoint_Limit](Static_Pressure_Setpoint_Limit) (c)<br />[brick:Min_Limit](Min_Limit) (c)<br />
Sub-classes |[brick:Min_Supply_Air_Static_Pressure_Setpoint_Limit](Min_Supply_Air_Static_Pressure_Setpoint_Limit) (c)<br />[brick:Min_Discharge_Air_Static_Pressure_Setpoint_Limit](Min_Discharge_Air_Static_Pressure_Setpoint_Limit) (c)<br />
### Min_Supply_Air_Static_Pressure_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Min_Supply_Air_Static_Pressure_Setpoint_Limit`
Super-classes |[brick:Min_Static_Pressure_Setpoint_Limit](Min_Static_Pressure_Setpoint_Limit) (c)<br />[brick:Min_Limit](Min_Limit) (c)<br />
### Min_Unoccupied_Cooling_Discharge_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Min_Unoccupied_Cooling_Discharge_Air_Flow_Setpoint_Limit`
Super-classes |[brick:Min_Cooling_Discharge_Air_Flow_Setpoint_Limit](Min_Cooling_Discharge_Air_Flow_Setpoint_Limit) (c)<br />
### Min_Unoccupied_Cooling_Supply_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Min_Unoccupied_Cooling_Supply_Air_Flow_Setpoint_Limit`
Super-classes |[brick:Min_Cooling_Supply_Air_Flow_Setpoint_Limit](Min_Cooling_Supply_Air_Flow_Setpoint_Limit) (c)<br />
### Min_Unoccupied_Heating_Discharge_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Min_Unoccupied_Heating_Discharge_Air_Flow_Setpoint_Limit`
Super-classes |[brick:Min_Heating_Discharge_Air_Flow_Setpoint_Limit](Min_Heating_Discharge_Air_Flow_Setpoint_Limit) (c)<br />
### Min_Unoccupied_Heating_Supply_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Min_Unoccupied_Heating_Supply_Air_Flow_Setpoint_Limit`
Super-classes |[brick:Min_Heating_Supply_Air_Flow_Setpoint_Limit](Min_Heating_Supply_Air_Flow_Setpoint_Limit) (c)<br />
### Mixed_Air
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Mixed_Air`
Description | <p>(1) air that contains two or more streams of air. (2) combined outdoor air and recirculated air.</p>
Super-classes |[brick:Air](Air) (c)<br />
### Mixed_Air_Filter
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Mixed_Air_Filter`
Super-classes |[brick:Filter](Filter) (c)<br />
### Mixed_Air_Temperature_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Mixed_Air_Temperature_Sensor`
Super-classes |[brick:Air_Temperature_Sensor](Air_Temperature_Sensor) (c)<br />
### Mixed_Air_Temperature_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Mixed_Air_Temperature_Setpoint`
Super-classes |[brick:Air_Temperature_Setpoint](Air_Temperature_Setpoint) (c)<br />
### Mode_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Mode_Setpoint`
Super-classes |[brick:Setpoint](Setpoint) (c)<br />
Sub-classes |[brick:Dual_Band_Mode_Setpoint](Dual_Band_Mode_Setpoint) (c)<br />[brick:Occupied_Mode_Setpoint](Occupied_Mode_Setpoint) (c)<br />[brick:Unoccupied_Mode_Setpoint](Unoccupied_Mode_Setpoint) (c)<br />
### Mode_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Mode_Status`
Super-classes |[brick:Status](Status) (c)<br />
Sub-classes |[brick:Operating_Mode_Status](Operating_Mode_Status) (c)<br />[brick:System_Mode_Status](System_Mode_Status) (c)<br />[brick:Occupied_Mode_Status](Occupied_Mode_Status) (c)<br />
### Motion_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Motion_Sensor`
Super-classes |[brick:Sensor](Sensor) (c)<br />
Sub-classes |[brick:PIR_Sensor](PIR_Sensor) (c)<br />
### Motor_Current_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Motor_Current_Sensor`
Super-classes |[brick:Current_Sensor](Current_Sensor) (c)<br />
### Motor_Direction_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Motor_Direction_Status`
Super-classes |[brick:Direction_Status](Direction_Status) (c)<br />
### Motor_Speed_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Motor_Speed_Sensor`
Super-classes |[brick:Speed_Sensor](Speed_Sensor) (c)<br />
### Motor_Start_Stop_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Motor_Start_Stop_Status`
Super-classes |[brick:Start_Stop_Status](Start_Stop_Status) (c)<br />
### Motor_Torque_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Motor_Torque_Sensor`
Super-classes |[brick:Torque_Sensor](Torque_Sensor) (c)<br />
### Natural_Gas
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Natural_Gas`
Description | <p>Fossil fuel energy source consisting largely of methane and other hydrocarbons</p>
Super-classes |[brick:Gas](Gas) (c)<br />
### Occupancy_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Occupancy_Sensor`
Super-classes |[brick:Sensor](Sensor) (c)<br />
Sub-classes |[brick:PIR_Sensor](PIR_Sensor) (c)<br />
### Occupancy_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Occupancy_Status`
Super-classes |[brick:Status](Status) (c)<br />
Sub-classes |[brick:Temporary_Occupancy_Status](Temporary_Occupancy_Status) (c)<br />
### Occupied_Cooling_Supply_Air_Flow_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Occupied_Cooling_Supply_Air_Flow_Setpoint`
Super-classes |[brick:Occupied_Supply_Air_Flow_Setpoint](Occupied_Supply_Air_Flow_Setpoint) (c)<br />
### Occupied_Cooling_Temperature_Dead_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Occupied_Cooling_Temperature_Dead_Band_Setpoint`
Super-classes |[brick:Temperature_Dead_Band_Setpoint](Temperature_Dead_Band_Setpoint) (c)<br />
### Occupied_Heating_Supply_Air_Flow_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Occupied_Heating_Supply_Air_Flow_Setpoint`
Super-classes |[brick:Occupied_Supply_Air_Flow_Setpoint](Occupied_Supply_Air_Flow_Setpoint) (c)<br />
### Occupied_Heating_Temperature_Dead_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Occupied_Heating_Temperature_Dead_Band_Setpoint`
Super-classes |[brick:Temperature_Dead_Band_Setpoint](Temperature_Dead_Band_Setpoint) (c)<br />
### Occupied_Mode_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Occupied_Mode_Setpoint`
Super-classes |[brick:Mode_Setpoint](Mode_Setpoint) (c)<br />
### Occupied_Mode_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Occupied_Mode_Status`
Super-classes |[brick:Mode_Status](Mode_Status) (c)<br />
### Occupied_Supply_Air_Flow_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Occupied_Supply_Air_Flow_Setpoint`
Super-classes |[brick:Supply_Air_Flow_Setpoint](Supply_Air_Flow_Setpoint) (c)<br />
Sub-classes |[brick:Occupied_Heating_Supply_Air_Flow_Setpoint](Occupied_Heating_Supply_Air_Flow_Setpoint) (c)<br />[brick:Occupied_Cooling_Supply_Air_Flow_Setpoint](Occupied_Cooling_Supply_Air_Flow_Setpoint) (c)<br />
### Off_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Off_Status`
Super-classes |[brick:Status](Status) (c)<br />
### Oil
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Oil`
Super-classes |[brick:Liquid](Liquid) (c)<br />
Sub-classes |[brick:Fuel_Oil](Fuel_Oil) (c)<br />
### On_Off_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#On_Off_Status`
Super-classes |[brick:Status](Status) (c)<br />
Sub-classes |[brick:Standby_Glycool_Unit_On_Off_Status](Standby_Glycool_Unit_On_Off_Status) (c)<br />[brick:Cooling_On_Off_Status](Cooling_On_Off_Status) (c)<br />[brick:Remotely_On_Off_Status](Remotely_On_Off_Status) (c)<br />[brick:Heating_On_Off_Status](Heating_On_Off_Status) (c)<br />[brick:EconCycle_On_Off_Status](EconCycle_On_Off_Status) (c)<br />[brick:Standby_Unit_On_Off_Status](Standby_Unit_On_Off_Status) (c)<br />[brick:Humidification_On_Off_Status](Humidification_On_Off_Status) (c)<br />[brick:Locally_On_Off_Status](Locally_On_Off_Status) (c)<br />[brick:Dehumidification_On_Off_Status](Dehumidification_On_Off_Status) (c)<br />
### On_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#On_Status`
Super-classes |[brick:Status](Status) (c)<br />
### On_Timer_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#On_Timer_Sensor`
Super-classes |[brick:Duration_Sensor](Duration_Sensor) (c)<br />
### Open_Heating_Valve_Outside_Air_Temperature_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Open_Heating_Valve_Outside_Air_Temperature_Setpoint`
Super-classes |[brick:Outside_Air_Temperature_Setpoint](Outside_Air_Temperature_Setpoint) (c)<br />
### Operating_Mode_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Operating_Mode_Status`
Super-classes |[brick:Mode_Status](Mode_Status) (c)<br />
Sub-classes |[brick:Vent_Operating_Mode_Status](Vent_Operating_Mode_Status) (c)<br />
### Operative_Temperature
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Operative_Temperature`
Super-classes |[brick:Temperature](Temperature) (c)<br />
### Output_Frequency_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Output_Frequency_Sensor`
Super-classes |[brick:Frequency_Sensor](Frequency_Sensor) (c)<br />
### Output_Voltage_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Output_Voltage_Sensor`
Super-classes |[brick:Voltage_Sensor](Voltage_Sensor) (c)<br />
### Outside
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Outside`
Super-classes |[brick:Location](Location) (c)<br />
### Outside_Air
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Outside_Air`
Description | <p>air external to a defined zone (e.g., corridors).</p>
Super-classes |[brick:Air](Air) (c)<br />
### Outside_Air_CO2_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Outside_Air_CO2_Sensor`
Super-classes |[brick:CO2_Sensor](CO2_Sensor) (c)<br />
### Outside_Air_Dewpoint_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Dewpoint_Sensor`
Super-classes |[brick:Dewpoint_Sensor](Dewpoint_Sensor) (c)<br />
### Outside_Air_Enthalpy_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Enthalpy_Sensor`
Super-classes |[brick:Air_Enthalpy_Sensor](Air_Enthalpy_Sensor) (c)<br />
### Outside_Air_Flow_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Flow_Sensor`
Super-classes |[brick:Air_Flow_Sensor](Air_Flow_Sensor) (c)<br />
### Outside_Air_Flow_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Flow_Setpoint`
Super-classes |[brick:Air_Flow_Setpoint](Air_Flow_Setpoint) (c)<br />
### Outside_Air_Grains_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Grains_Sensor`
Super-classes |[brick:Air_Grains_Sensor](Air_Grains_Sensor) (c)<br />
### Outside_Air_Humidity_Sensor:
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Humidity_Sensor:`
Super-classes |[brick:Air_Humidity_Sensor](Air_Humidity_Sensor) (c)<br />
### Outside_Air_Lockout_Temperature_Differential_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Lockout_Temperature_Differential_Sensor`
Super-classes |[brick:Outside_Air_Temperature_Sensor](Outside_Air_Temperature_Sensor) (c)<br />
Sub-classes |[brick:Low_Outside_Air_Lockout_Temperature_Differential_Sensor](Low_Outside_Air_Lockout_Temperature_Differential_Sensor) (c)<br />[brick:High_Outside_Air_Lockout_Temperature_Differential_Sensor](High_Outside_Air_Lockout_Temperature_Differential_Sensor) (c)<br />
### Outside_Air_Lockout_Temperature_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Lockout_Temperature_Setpoint`
Super-classes |[brick:Outside_Air_Temperature_Setpoint](Outside_Air_Temperature_Setpoint) (c)<br />
### Outside_Air_Temperature_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Temperature_Sensor`
Super-classes |[brick:Air_Temperature_Sensor](Air_Temperature_Sensor) (c)<br />
Sub-classes |[brick:Outside_Air_Lockout_Temperature_Differential_Sensor](Outside_Air_Lockout_Temperature_Differential_Sensor) (c)<br />
### Outside_Air_Temperature_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Temperature_Setpoint`
Super-classes |[brick:Air_Temperature_Setpoint](Air_Temperature_Setpoint) (c)<br />
Sub-classes |[brick:Outside_Air_Lockout_Temperature_Setpoint](Outside_Air_Lockout_Temperature_Setpoint) (c)<br />[brick:Low_Outside_Air_Temperature_Enable_Setpoint](Low_Outside_Air_Temperature_Enable_Setpoint) (c)<br />[brick:Open_Heating_Valve_Outside_Air_Temperature_Setpoint](Open_Heating_Valve_Outside_Air_Temperature_Setpoint) (c)<br />
### Outside_Damper
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Outside_Damper`
Super-classes |[brick:Damper](Damper) (c)<br />
### Outside_Luminance_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Outside_Luminance_Sensor`
Super-classes |[brick:Luminance_Sensor](Luminance_Sensor) (c)<br />
### Overridden_Off_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Overridden_Off_Status`
Super-classes |[brick:Overridden_Status](Overridden_Status) (c)<br />
### Overridden_On_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Overridden_On_Status`
Super-classes |[brick:Overridden_Status](Overridden_Status) (c)<br />
### Overridden_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Overridden_Status`
Super-classes |[brick:Status](Status) (c)<br />
Sub-classes |[brick:Overridden_On_Status](Overridden_On_Status) (c)<br />[brick:Overridden_Off_Status](Overridden_Off_Status) (c)<br />
### PIR_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#PIR_Sensor`
Super-classes |[brick:Motion_Sensor](Motion_Sensor) (c)<br />[brick:Occupancy_Sensor](Occupancy_Sensor) (c)<br />
### PM10
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#PM10`
Super-classes |[brick:Air_Quality](Air_Quality) (c)<br />
### PM25
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#PM25`
Super-classes |[brick:Air_Quality](Air_Quality) (c)<br />
### Peak_Power_Demand_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Peak_Power_Demand_Sensor`
Super-classes |[brick:Demand_Sensor](Demand_Sensor) (c)<br />
### Photovoltaic_Current_Output_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Photovoltaic_Current_Output_Sensor`
Super-classes |[brick:Current_Sensor](Current_Sensor) (c)<br />
### Piezoelectric_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Piezoelectric_Sensor`
Super-classes |[brick:Sensor](Sensor) (c)<br />
### PlugStrip
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#PlugStrip`
Super-classes |[brick:Equipment](Equipment) (c)<br />
### Point
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Point`
Sub-classes |[brick:Sensor](Sensor) (c)<br />[brick:Status](Status) (c)<br />[brick:Setpoint](Setpoint) (c)<br />[brick:Limit](Limit) (c)<br />
In domain of |[brick:measures](measures) (op)<br />[brick:isPointOf](isPointOf) (op)<br />
In range of |[brick:isMeasuredBy](isMeasuredBy) (op)<br />[brick:hasPoint](hasPoint) (op)<br />
### Power
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Power`
Super-classes |[brick:Quantity](Quantity) (c)<br />
Sub-classes |[brick:Thermal_Power](Thermal_Power) (c)<br />[brick:Electric_Power](Electric_Power) (c)<br />
### Power_Factor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Power_Factor`
Super-classes |[brick:Quantity](Quantity) (c)<br />
### Power_System
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Power_System`
Super-classes |[brick:Equipment](Equipment) (c)<br />
### PreHeat_Coil_Entering_Air_Temperature_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#PreHeat_Coil_Entering_Air_Temperature_Sensor`
Super-classes |[brick:Entering_Water_Temperature_Sensor](Entering_Water_Temperature_Sensor) (c)<br />
### PreHeat_Coil_Leaving_Air_Temperature_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#PreHeat_Coil_Leaving_Air_Temperature_Sensor`
Super-classes |[brick:Leaving_Water_Temperature_Sensor](Leaving_Water_Temperature_Sensor) (c)<br />
### Pre_Filter_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Pre_Filter_Status`
Super-classes |[brick:Filter_Status](Filter_Status) (c)<br />
### Precipitation
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Precipitation`
Super-classes |[brick:Quantity](Quantity) (c)<br />
### Preheat_Demand_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Preheat_Demand_Setpoint`
Super-classes |[brick:Demand_Setpoint](Demand_Setpoint) (c)<br />
### Preheat_Discharge_Air_Temperature_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Preheat_Discharge_Air_Temperature_Sensor`
Super-classes |[brick:Discharge_Air_Temperature_Sensor](Discharge_Air_Temperature_Sensor) (c)<br />
### Preheat_Hot_Water_Valve
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Preheat_Hot_Water_Valve`
Super-classes |[brick:Heating_Valve](Heating_Valve) (c)<br />
### Preheat_Valve_VFD
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Preheat_Valve_VFD`
Super-classes |[brick:VFD](VFD) (c)<br />
### Pressure
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Pressure`
Super-classes |[brick:Quantity](Quantity) (c)<br />
Sub-classes |[brick:Static_Pressure](Static_Pressure) (c)<br />[brick:Atmospheric_Pressure](Atmospheric_Pressure) (c)<br />
### Pressure_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Pressure_Sensor`
Super-classes |[brick:Sensor](Sensor) (c)<br />
Sub-classes |[brick:Static_Pressure_Sensor](Static_Pressure_Sensor) (c)<br />[brick:Velocity_Pressure_Sensor:](Velocity_Pressure_Sensor:) (c)<br />[brick:Differential_Pressure_Sensor](Differential_Pressure_Sensor) (c)<br />
### Pressure_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Pressure_Setpoint`
Super-classes |[brick:Setpoint](Setpoint) (c)<br />
Sub-classes |[brick:Differential_Pressure_Setpoint](Differential_Pressure_Setpoint) (c)<br />[brick:Velocity_Pressure_Setpoint](Velocity_Pressure_Setpoint) (c)<br />[brick:Static_Pressure_Setpoint](Static_Pressure_Setpoint) (c)<br />
### Pressure_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Pressure_Status`
Super-classes |[brick:Status](Status) (c)<br />
Sub-classes |[brick:Supply_Air_Duct_Pressure_Status](Supply_Air_Duct_Pressure_Status) (c)<br />[brick:Discharge_Air_Duct_Pressure_Status](Discharge_Air_Duct_Pressure_Status) (c)<br />
### Proportional_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Proportional_Band_Setpoint`
Super-classes |[brick:Setpoint](Setpoint) (c)<br />
Sub-classes |[brick:Heating_Discharge_Air_Temperature_Proportional_Band_Setpoint](Heating_Discharge_Air_Temperature_Proportional_Band_Setpoint) (c)<br />[brick:Discharge_Air_Temperature_Proportional_Band_Setpoint](Discharge_Air_Temperature_Proportional_Band_Setpoint) (c)<br />[brick:Exhaust_Air_Flow_Proportional_Band_Setpoint](Exhaust_Air_Flow_Proportional_Band_Setpoint) (c)<br />[brick:Supply_Water_Differential_Pressure_Proportional_Band_Setpoint](Supply_Water_Differential_Pressure_Proportional_Band_Setpoint) (c)<br />[brick:Heating_Supply_Air_Temperature_Proportional_Band_Setpoint](Heating_Supply_Air_Temperature_Proportional_Band_Setpoint) (c)<br />[brick:Discharge_Air_Static_Pressure_Proportional_Band_Setpoint](Discharge_Air_Static_Pressure_Proportional_Band_Setpoint) (c)<br />[brick:Hot_Water_Differential_Pressure_Proportional_Band_Setpoint](Hot_Water_Differential_Pressure_Proportional_Band_Setpoint) (c)<br />[brick:Cooling_Supply_Air_Temperature_Proportional_Band_Setpoint](Cooling_Supply_Air_Temperature_Proportional_Band_Setpoint) (c)<br />[brick:Static_Pressure_Proportional_Band_Setpoint](Static_Pressure_Proportional_Band_Setpoint) (c)<br />[brick:Supply_Air_Static_Pressure_Proportional_Band_Setpoint](Supply_Air_Static_Pressure_Proportional_Band_Setpoint) (c)<br />[brick:Differential_Pressure_Proportional_Band](Differential_Pressure_Proportional_Band) (c)<br />[brick:Cooling_Discharge_Air_Temperature_Proportional_Band_Setpoint](Cooling_Discharge_Air_Temperature_Proportional_Band_Setpoint) (c)<br />[brick:Supply_Air_Temperature_Proportional_Band_Setpoint](Supply_Air_Temperature_Proportional_Band_Setpoint) (c)<br />[brick:Chilled_Water_Differential_Pressure_Proportional_Band_Setpoint](Chilled_Water_Differential_Pressure_Proportional_Band_Setpoint) (c)<br />[brick:Supply_Water_Temperature_Proportional_Band_Setpoint](Supply_Water_Temperature_Proportional_Band_Setpoint) (c)<br />
### Pump
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Pump`
Description | <p>Machine for imparting energy to a fluid, causing it to do work, drawing a fluid into itself through an entrance port, and forcing the fluid out through an exhaust port.</p>
Super-classes |[brick:HVAC](HVAC) (c)<br />
Sub-classes |[brick:Water_Pump](Water_Pump) (c)<br />
### Pump_Start_Stop_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Pump_Start_Stop_Status`
Super-classes |[brick:Start_Stop_Status](Start_Stop_Status) (c)<br />
### Quantity
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Quantity`
Super-classes |[brick:Quantity](Quantity) (c)<br />
Sub-classes |[brick:Power](Power) (c)<br />[brick:Pressure](Pressure) (c)<br />[brick:Luminance](Luminance) (c)<br />[brick:Energy](Energy) (c)<br />[brick:Humidity](Humidity) (c)<br />[brick:Cloudage](Cloudage) (c)<br />[brick:Weather_Condition](Weather_Condition) (c)<br />[brick:Conductivity](Conductivity) (c)<br />[brick:Temperature](Temperature) (c)<br />[brick:Illuminance](Illuminance) (c)<br />[brick:Speed](Speed) (c)<br />[brick:Quantity](Quantity) (c)<br />[brick:Enthalpy](Enthalpy) (c)<br />[brick:Grains](Grains) (c)<br />[brick:Power_Factor](Power_Factor) (c)<br />[brick:Dewpoint](Dewpoint) (c)<br />[brick:Voltage](Voltage) (c)<br />[brick:Level](Level) (c)<br />[brick:Flow](Flow) (c)<br />[brick:Frequency](Frequency) (c)<br />[brick:Capacity](Capacity) (c)<br />[brick:Direction](Direction) (c)<br />[brick:Precipitation](Precipitation) (c)<br />[brick:Daytime](Daytime) (c)<br />[brick:Air_Quality](Air_Quality) (c)<br />[brick:Irradiance](Irradiance) (c)<br />[brick:Current](Current) (c)<br />
### Radiant_Temperature
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Radiant_Temperature`
Super-classes |[brick:Temperature](Temperature) (c)<br />
### Rain_Duration_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Rain_Duration_Sensor`
Super-classes |[brick:Rain_Sensor](Rain_Sensor) (c)<br />[brick:Duration_Sensor](Duration_Sensor) (c)<br />
### Rain_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Rain_Sensor`
Super-classes |[brick:Sensor](Sensor) (c)<br />
Sub-classes |[brick:Rain_Duration_Sensor](Rain_Duration_Sensor) (c)<br />
### Reactive_Power
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Reactive_Power`
Super-classes |[brick:Electric_Power](Electric_Power) (c)<br />
### Reheat_Valve
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Reheat_Valve`
Super-classes |[brick:Heating_Valve](Heating_Valve) (c)<br />
### Relative_Humidity_Sensor:
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Relative_Humidity_Sensor:`
Super-classes |[brick:Air_Humidity_Sensor](Air_Humidity_Sensor) (c)<br />
### Remotely_On_Off_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Remotely_On_Off_Status`
Super-classes |[brick:On_Off_Status](On_Off_Status) (c)<br />
### Reset_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Reset_Setpoint`
Super-classes |[brick:Setpoint](Setpoint) (c)<br />
### Return_Air
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Return_Air`
Description | <p>air removed from a space to be recirculated or exhausted. Air extracted from a space and totally or partially returned to an air conditioner, furnace, or other heating, cooling, or ventilating system.</p>
Super-classes |[brick:Air](Air) (c)<br />
### Return_Air_CO2_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Return_Air_CO2_Sensor`
Super-classes |[brick:CO2_Sensor](CO2_Sensor) (c)<br />
### Return_Air_CO2_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Return_Air_CO2_Setpoint`
Super-classes |[brick:CO2_Setpoint](CO2_Setpoint) (c)<br />
Sub-classes |[brick:Max_Return_Air_CO2_Setpoint](Max_Return_Air_CO2_Setpoint) (c)<br />
### Return_Air_Dewpoint_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Return_Air_Dewpoint_Sensor`
Super-classes |[brick:Dewpoint_Sensor](Dewpoint_Sensor) (c)<br />
### Return_Air_Enthalpy_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Return_Air_Enthalpy_Sensor`
Super-classes |[brick:Air_Enthalpy_Sensor](Air_Enthalpy_Sensor) (c)<br />
### Return_Air_Flow_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Return_Air_Flow_Sensor`
Super-classes |[brick:Air_Flow_Sensor](Air_Flow_Sensor) (c)<br />
### Return_Air_Grains_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Return_Air_Grains_Sensor`
Super-classes |[brick:Air_Grains_Sensor](Air_Grains_Sensor) (c)<br />
### Return_Air_Humidity_Sensor:
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Return_Air_Humidity_Sensor:`
Super-classes |[brick:Air_Humidity_Sensor](Air_Humidity_Sensor) (c)<br />
### Return_Air_Temperature_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Return_Air_Temperature_Sensor`
Super-classes |[brick:Air_Temperature_Sensor](Air_Temperature_Sensor) (c)<br />
### Return_Damper
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Return_Damper`
Super-classes |[brick:Damper](Damper) (c)<br />
### Return_Discharge_Fan_Differential_Speed_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Return_Discharge_Fan_Differential_Speed_Setpoint`
Super-classes |[brick:Differential_Speed_Setpoint](Differential_Speed_Setpoint) (c)<br />
### Return_Fan
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Return_Fan`
Super-classes |[brick:Fan](Fan) (c)<br />
### Return_Fan_Air_Flow_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Return_Fan_Air_Flow_Sensor`
Super-classes |[brick:Fan_Air_Flow_Sensor](Fan_Air_Flow_Sensor) (c)<br />
### Return_Fan_Differential_Speed_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Return_Fan_Differential_Speed_Sensor`
Super-classes |[brick:Differential_Speed_Sensor](Differential_Speed_Sensor) (c)<br />
### Return_Fan_Differential_Speed_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Return_Fan_Differential_Speed_Setpoint`
Super-classes |[brick:Differential_Speed_Setpoint](Differential_Speed_Setpoint) (c)<br />
### Return_Supply_Fan_Differential_Speed_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Return_Supply_Fan_Differential_Speed_Setpoint`
Super-classes |[brick:Differential_Speed_Setpoint](Differential_Speed_Setpoint) (c)<br />
### Return_Water_Temperature_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Return_Water_Temperature_Sensor`
Super-classes |[brick:Water_Temperature_Sensor](Water_Temperature_Sensor) (c)<br />
Sub-classes |[brick:Hot_Water_Return_Temperature_Sensor](Hot_Water_Return_Temperature_Sensor) (c)<br />[brick:Chilled_Water_Return_Temperature_Sensor](Chilled_Water_Return_Temperature_Sensor) (c)<br />
### Roof
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Roof`
Super-classes |[brick:Location](Location) (c)<br />
### Rooftop_Unit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Rooftop_Unit`
Super-classes |[brick:AHU](AHU) (c)<br />
### Room
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Room`
Super-classes |[brick:Location](Location) (c)<br />
Sub-classes |[brick:Server_Room](Server_Room) (c)<br />[brick:Laboratory](Laboratory) (c)<br />
### Room_Air_Temperature_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Room_Air_Temperature_Setpoint`
Super-classes |[brick:Air_Temperature_Setpoint](Air_Temperature_Setpoint) (c)<br />
### Run_Direction_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Run_Direction_Status`
Super-classes |[brick:Direction_Status](Direction_Status) (c)<br />
### Run_Enable_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Run_Enable_Status`
Super-classes |[brick:Enable_Status](Enable_Status) (c)<br />
### Run_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Run_Status`
Super-classes |[brick:Start_Stop_Status](Start_Stop_Status) (c)<br />
### Run_Time_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Run_Time_Sensor`
Super-classes |[brick:Duration_Sensor](Duration_Sensor) (c)<br />
### Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Sensor`
Super-classes |[brick:Point](Point) (c)<br />
Sub-classes |[brick:Water_Level_Sensor](Water_Level_Sensor) (c)<br />[brick:Frequency_Sensor](Frequency_Sensor) (c)<br />[brick:CO2_Sensor](CO2_Sensor) (c)<br />[brick:Energy_Sensor](Energy_Sensor) (c)<br />[brick:Capacity_Sensor](Capacity_Sensor) (c)<br />[brick:Enthalpy_Sensor](Enthalpy_Sensor) (c)<br />[brick:Temperature_Sensor](Temperature_Sensor) (c)<br />[brick:Direction_Sensor](Direction_Sensor) (c)<br />[brick:Dewpoint_Sensor](Dewpoint_Sensor) (c)<br />[brick:Piezoelectric_Sensor](Piezoelectric_Sensor) (c)<br />[brick:Current_Sensor](Current_Sensor) (c)<br />[brick:Duration_Sensor](Duration_Sensor) (c)<br />[brick:Voltage_Sensor](Voltage_Sensor) (c)<br />[brick:Speed_Sensor](Speed_Sensor) (c)<br />[brick:Frost_Sensor](Frost_Sensor) (c)<br />[brick:Rain_Sensor](Rain_Sensor) (c)<br />[brick:Luminance_Sensor](Luminance_Sensor) (c)<br />[brick:Air_Grains_Sensor](Air_Grains_Sensor) (c)<br />[brick:Trace_Heat_Sensor](Trace_Heat_Sensor) (c)<br />[brick:Demand_Sensor](Demand_Sensor) (c)<br />[brick:Angle_Sensor](Angle_Sensor) (c)<br />[brick:Motion_Sensor](Motion_Sensor) (c)<br />[brick:Solar_Radiance_Sensor](Solar_Radiance_Sensor) (c)<br />[brick:Hail_Sensor](Hail_Sensor) (c)<br />[brick:Pressure_Sensor](Pressure_Sensor) (c)<br />[brick:Occupancy_Sensor](Occupancy_Sensor) (c)<br />[brick:Torque_Sensor](Torque_Sensor) (c)<br />[brick:Conductivity_Sensor](Conductivity_Sensor) (c)<br />[brick:Flow_Sensor](Flow_Sensor) (c)<br />[brick:Humidity_Sensor](Humidity_Sensor) (c)<br />[brick:Damper_Position_Sensor](Damper_Position_Sensor) (c)<br />
### Server_Room
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Server_Room`
Super-classes |[brick:Room](Room) (c)<br />
### Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Setpoint`
Super-classes |[brick:Point](Point) (c)<br />
Sub-classes |[brick:CO2_Setpoint](CO2_Setpoint) (c)<br />[brick:Humidity_Setpoint](Humidity_Setpoint) (c)<br />[brick:Enthalpy_Setpoint](Enthalpy_Setpoint) (c)<br />[brick:Mode_Setpoint](Mode_Setpoint) (c)<br />[brick:Flow_Setpoint](Flow_Setpoint) (c)<br />[brick:Speed_Setpoint](Speed_Setpoint) (c)<br />[brick:Demand_Setpoint](Demand_Setpoint) (c)<br />[brick:Proportional_Band_Setpoint](Proportional_Band_Setpoint) (c)<br />[brick:Temperature_Setpoint](Temperature_Setpoint) (c)<br />[brick:Dead_Band_Setpoint](Dead_Band_Setpoint) (c)<br />[brick:Luminance_Setpoint](Luminance_Setpoint) (c)<br />[brick:Damper_Position_Setpoint](Damper_Position_Setpoint) (c)<br />[brick:Integral_Gain_Setpoint](Integral_Gain_Setpoint) (c)<br />[brick:Reset_Setpoint](Reset_Setpoint) (c)<br />[brick:Load_Setpoint](Load_Setpoint) (c)<br />[brick:Dew_Point_Setpoint](Dew_Point_Setpoint) (c)<br />[brick:Integral_Time_Setpoint](Integral_Time_Setpoint) (c)<br />[brick:Pressure_Setpoint](Pressure_Setpoint) (c)<br />[brick:Increase_Decrease_Step_Setpoint](Increase_Decrease_Step_Setpoint) (c)<br />
### Shading_System
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Shading_System`
Super-classes |[brick:Equipment](Equipment) (c)<br />
### Solar_Azimuth_Angle_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Solar_Azimuth_Angle_Sensor`
Super-classes |[brick:Angle_Sensor](Angle_Sensor) (c)<br />
### Solar_Irradiance
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Solar_Irradiance`
Super-classes |[brick:Irradiance](Irradiance) (c)<br />
### Solar_Panel
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Solar_Panel`
Super-classes |[brick:Equipment](Equipment) (c)<br />
### Solar_Radiance_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Solar_Radiance_Sensor`
Super-classes |[brick:Sensor](Sensor) (c)<br />
### Solar_Zenith_Angle_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Solar_Zenith_Angle_Sensor`
Super-classes |[brick:Angle_Sensor](Angle_Sensor) (c)<br />
### Solid
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Solid`
Super-classes |[brick:Substance](Substance) (c)<br />
Sub-classes |[brick:Frost](Frost) (c)<br />[brick:Hail](Hail) (c)<br />[brick:Ice](Ice) (c)<br />
### Space
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Space`
Super-classes |[brick:Location](Location) (c)<br />
### Space_Heater
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Space_Heater`
Description | <p>A heater used to warm the air in an enclosed area, such as a room or office</p>
Super-classes |[brick:HVAC](HVAC) (c)<br />
### Speed
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Speed`
Super-classes |[brick:Quantity](Quantity) (c)<br />
Sub-classes |[brick:Wind_Speed](Wind_Speed) (c)<br />
### Speed_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Speed_Sensor`
Super-classes |[brick:Sensor](Sensor) (c)<br />
Sub-classes |[brick:Differential_Speed_Sensor](Differential_Speed_Sensor) (c)<br />[brick:Wind_Speed_Sensor](Wind_Speed_Sensor) (c)<br />[brick:Motor_Speed_Sensor](Motor_Speed_Sensor) (c)<br />
### Speed_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Speed_Setpoint`
Super-classes |[brick:Setpoint](Setpoint) (c)<br />
Sub-classes |[brick:Differential_Speed_Setpoint](Differential_Speed_Setpoint) (c)<br />
### Speed_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Speed_Setpoint_Limit`
Super-classes |[brick:Limit](Limit) (c)<br />
Sub-classes |[brick:Max_Speed_Setpoint_Limit](Max_Speed_Setpoint_Limit) (c)<br />[brick:Min_Speed_Setpoint_Limit](Min_Speed_Setpoint_Limit) (c)<br />
### Speed_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Speed_Status`
Super-classes |[brick:Status](Status) (c)<br />
### Stages_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Stages_Status`
Super-classes |[brick:Status](Status) (c)<br />
### Standby_Fan
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Standby_Fan`
Super-classes |[brick:Fan](Fan) (c)<br />
### Standby_Glycool_Unit_On_Off_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Standby_Glycool_Unit_On_Off_Status`
Super-classes |[brick:On_Off_Status](On_Off_Status) (c)<br />
### Standby_Unit_On_Off_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Standby_Unit_On_Off_Status`
Super-classes |[brick:On_Off_Status](On_Off_Status) (c)<br />
### Start_Stop_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Start_Stop_Status`
Super-classes |[brick:Status](Status) (c)<br />
Sub-classes |[brick:Pump_Start_Stop_Status](Pump_Start_Stop_Status) (c)<br />[brick:Run_Status](Run_Status) (c)<br />[brick:Fan_Start_Stop_Status](Fan_Start_Stop_Status) (c)<br />[brick:Motor_Start_Stop_Status](Motor_Start_Stop_Status) (c)<br />
### Static_Pressure
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Static_Pressure`
Super-classes |[brick:Pressure](Pressure) (c)<br />
### Static_Pressure_Dead_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Dead_Band_Setpoint`
Super-classes |[brick:Dead_Band_Setpoint](Dead_Band_Setpoint) (c)<br />
### Static_Pressure_Increase_Decrease_Step_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Increase_Decrease_Step_Setpoint`
Super-classes |[brick:Increase_Decrease_Step_Setpoint](Increase_Decrease_Step_Setpoint) (c)<br />
Sub-classes |[brick:Air_Static_Pressure_Increase_Decrease_Step_Setpoint](Air_Static_Pressure_Increase_Decrease_Step_Setpoint) (c)<br />
### Static_Pressure_Integral_Time_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Integral_Time_Setpoint`
Super-classes |[brick:Integral_Time_Setpoint](Integral_Time_Setpoint) (c)<br />
### Static_Pressure_Proportional_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Proportional_Band_Setpoint`
Super-classes |[brick:Proportional_Band_Setpoint](Proportional_Band_Setpoint) (c)<br />
Sub-classes |[brick:Exhaust_Air_Static_Pressure_Proportional_Band_Setpoint](Exhaust_Air_Static_Pressure_Proportional_Band_Setpoint) (c)<br />
### Static_Pressure_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Sensor`
Super-classes |[brick:Pressure_Sensor](Pressure_Sensor) (c)<br />
Sub-classes |[brick:Exhaust_Air_Static_Pressure_Sensor:](Exhaust_Air_Static_Pressure_Sensor:) (c)<br />[brick:Discharge_Air_Static_Pressure_Sensor:](Discharge_Air_Static_Pressure_Sensor:) (c)<br />[brick:Building_Static_Pressure_Sensor:](Building_Static_Pressure_Sensor:) (c)<br />[brick:Supply_Air_Static_Pressure_Sensor:](Supply_Air_Static_Pressure_Sensor:) (c)<br />
### Static_Pressure_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Setpoint`
Super-classes |[brick:Pressure_Setpoint](Pressure_Setpoint) (c)<br />
Sub-classes |[brick:High_Static_Pressure_Cutout_Limit_Setpoint](High_Static_Pressure_Cutout_Limit_Setpoint) (c)<br />[brick:Hot_Water_Static_Pressure_Setpoint](Hot_Water_Static_Pressure_Setpoint) (c)<br />[brick:Building_Static_Pressure_Setpoint](Building_Static_Pressure_Setpoint) (c)<br />[brick:Chilled_Water_Static_Pressure_Setpoint](Chilled_Water_Static_Pressure_Setpoint) (c)<br />[brick:Exhaust_Air_Static_Pressure_Setpoint](Exhaust_Air_Static_Pressure_Setpoint) (c)<br />[brick:Supply_Air_Static_Pressure_Setpoint](Supply_Air_Static_Pressure_Setpoint) (c)<br />[brick:Discharge_Air_Static_Pressure_Setpoint](Discharge_Air_Static_Pressure_Setpoint) (c)<br />
### Static_Pressure_Setpoint_Limit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Setpoint_Limit`
Super-classes |[brick:Limit](Limit) (c)<br />
Sub-classes |[brick:Min_Static_Pressure_Setpoint_Limit](Min_Static_Pressure_Setpoint_Limit) (c)<br />[brick:Max_Static_Pressure_Setpoint_Limit](Max_Static_Pressure_Setpoint_Limit) (c)<br />
### Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Status`
Super-classes |[brick:Point](Point) (c)<br />
Sub-classes |[brick:Off_Status](Off_Status) (c)<br />[brick:Occupancy_Status](Occupancy_Status) (c)<br />[brick:On_Off_Status](On_Off_Status) (c)<br />[brick:Fault_Indicator_Status](Fault_Indicator_Status) (c)<br />[brick:Pressure_Status](Pressure_Status) (c)<br />[brick:Load_Shed_Status](Load_Shed_Status) (c)<br />[brick:Overridden_Status](Overridden_Status) (c)<br />[brick:Emergency_Generator_Status](Emergency_Generator_Status) (c)<br />[brick:Emergency_Air_Flow_Status](Emergency_Air_Flow_Status) (c)<br />[brick:Enable_Status](Enable_Status) (c)<br />[brick:Last_Fault_Code_Status](Last_Fault_Code_Status) (c)<br />[brick:Drive_Ready_Status](Drive_Ready_Status) (c)<br />[brick:Emergency_Push_Button_Status](Emergency_Push_Button_Status) (c)<br />[brick:Manual_Auto_Status](Manual_Auto_Status) (c)<br />[brick:Fan_Status](Fan_Status) (c)<br />[brick:Emergency_Power_Off_Status](Emergency_Power_Off_Status) (c)<br />[brick:Hold_Status](Hold_Status) (c)<br />[brick:Disable_Status](Disable_Status) (c)<br />[brick:Start_Stop_Status](Start_Stop_Status) (c)<br />[brick:System_Shutdown_Status](System_Shutdown_Status) (c)<br />[brick:Stages_Status](Stages_Status) (c)<br />[brick:Direction_Status](Direction_Status) (c)<br />[brick:Hand_Auto_Status](Hand_Auto_Status) (c)<br />[brick:Even_Month_Status](Even_Month_Status) (c)<br />[brick:On_Status](On_Status) (c)<br />[brick:Freeze_Status](Freeze_Status) (c)<br />[brick:Lead_Lag_Status](Lead_Lag_Status) (c)<br />[brick:System_Status](System_Status) (c)<br />[brick:Filter_Status](Filter_Status) (c)<br />[brick:Mode_Status](Mode_Status) (c)<br />[brick:Turn_Off_Status](Turn_Off_Status) (c)<br />[brick:Fault_Status](Fault_Status) (c)<br />[brick:Speed_Status](Speed_Status) (c)<br />
### Steam
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Steam`
Description | <p>water in the vapor phase.</p>
Super-classes |[brick:Gas](Gas) (c)<br />
### Steam_System
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Steam_System`
Super-classes |[brick:Equipment](Equipment) (c)<br />
### Substance
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Substance`
Sub-classes |[brick:Solid](Solid) (c)<br />[brick:Luminance](Luminance) (c)<br />[brick:Enthalpy](Enthalpy) (c)<br />[brick:Fluid](Fluid) (c)<br />
In domain of |[brick:isMeasuredBy](isMeasuredBy) (op)<br />
In range of |[brick:measures](measures) (op)<br />[brick:hasOutputSubstance](hasOutputSubstance) (op)<br />[brick:hasInputSubstance](hasInputSubstance) (op)<br />
### Supply_Air
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Air`
Description | <p>(1) air delivered by mechanical or natural ventilation to a space, composed of any combination of outdoor air, recirculated air, or transfer air. (2) air entering a space from an air-conditioning, heating, or ventilating apparatus for the purpose of comfort conditioning. Supply air is generally filtered, fan forced, and either heated, cooled, humidified, or dehumidified as necessary to maintain specified conditions. Only the quantity of outdoor air within the supply airflow may be used as replacement air.</p>
Super-classes |[brick:Air](Air) (c)<br />
### Supply_Air_Duct_Pressure_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Duct_Pressure_Status`
Super-classes |[brick:Pressure_Status](Pressure_Status) (c)<br />
### Supply_Air_Flow_Demand_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Flow_Demand_Setpoint`
Super-classes |[brick:Air_Flow_Demand_Setpoint](Air_Flow_Demand_Setpoint) (c)<br />[brick:Supply_Air_Flow_Setpoint](Supply_Air_Flow_Setpoint) (c)<br />
### Supply_Air_Flow_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Flow_Sensor`
Super-classes |[brick:Air_Flow_Sensor](Air_Flow_Sensor) (c)<br />
### Supply_Air_Flow_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Flow_Setpoint`
Super-classes |[brick:Air_Flow_Setpoint](Air_Flow_Setpoint) (c)<br />
Sub-classes |[brick:Occupied_Supply_Air_Flow_Setpoint](Occupied_Supply_Air_Flow_Setpoint) (c)<br />[brick:Heating_Supply_Air_Flow_Setpoint](Heating_Supply_Air_Flow_Setpoint) (c)<br />[brick:Cooling_Supply_Air_Flow_Setpoint](Cooling_Supply_Air_Flow_Setpoint) (c)<br />[brick:Supply_Air_Flow_Demand_Setpoint](Supply_Air_Flow_Demand_Setpoint) (c)<br />
### Supply_Air_Humidity_Sensor:
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Humidity_Sensor:`
Super-classes |[brick:Air_Humidity_Sensor](Air_Humidity_Sensor) (c)<br />
### Supply_Air_Static_Pressure_Integral_Time_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Static_Pressure_Integral_Time_Setpoint`
Super-classes |[brick:Integral_Time_Setpoint](Integral_Time_Setpoint) (c)<br />
### Supply_Air_Static_Pressure_Proportional_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Static_Pressure_Proportional_Band_Setpoint`
Super-classes |[brick:Proportional_Band_Setpoint](Proportional_Band_Setpoint) (c)<br />
### Supply_Air_Static_Pressure_Sensor:
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Static_Pressure_Sensor:`
Super-classes |[brick:Static_Pressure_Sensor](Static_Pressure_Sensor) (c)<br />
### Supply_Air_Static_Pressure_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Static_Pressure_Setpoint`
Super-classes |[brick:Static_Pressure_Setpoint](Static_Pressure_Setpoint) (c)<br />
### Supply_Air_Temperature_Dead_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Temperature_Dead_Band_Setpoint`
Super-classes |[brick:Dead_Band_Setpoint](Dead_Band_Setpoint) (c)<br />
Sub-classes |[brick:Cooling_Supply_Air_Temperature_Dead_Band_Setpoint](Cooling_Supply_Air_Temperature_Dead_Band_Setpoint) (c)<br />[brick:Heating_Supply_Air_Temperature_Dead_Band_Setpoint](Heating_Supply_Air_Temperature_Dead_Band_Setpoint) (c)<br />
### Supply_Air_Temperature_Proportional_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Temperature_Proportional_Band_Setpoint`
Super-classes |[brick:Proportional_Band_Setpoint](Proportional_Band_Setpoint) (c)<br />
### Supply_Air_Velocity_Pressure_Sensor:
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Velocity_Pressure_Sensor:`
Super-classes |[brick:Velocity_Pressure_Sensor:](Velocity_Pressure_Sensor:) (c)<br />
### Supply_Fan
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Fan`
Super-classes |[brick:Fan](Fan) (c)<br />
Sub-classes |[brick:Booster_Fan](Booster_Fan) (c)<br />
### Supply_Fan_Air_Flow_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Fan_Air_Flow_Sensor`
Super-classes |[brick:Fan_Air_Flow_Sensor](Fan_Air_Flow_Sensor) (c)<br />
### Supply_Water_Differential_Pressure_Dead_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Differential_Pressure_Dead_Band_Setpoint`
Super-classes |[brick:Dead_Band_Setpoint](Dead_Band_Setpoint) (c)<br />
Sub-classes |[brick:Thermal_Energy_Storage_Supply_Water_Differential_Pressure_Dead_Band_Setpoint](Thermal_Energy_Storage_Supply_Water_Differential_Pressure_Dead_Band_Setpoint) (c)<br />
### Supply_Water_Differential_Pressure_Integral_Time_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Differential_Pressure_Integral_Time_Setpoint`
Super-classes |[brick:Integral_Time_Setpoint](Integral_Time_Setpoint) (c)<br />
### Supply_Water_Differential_Pressure_Proportional_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Differential_Pressure_Proportional_Band_Setpoint`
Super-classes |[brick:Proportional_Band_Setpoint](Proportional_Band_Setpoint) (c)<br />
Sub-classes |[brick:Thermal_Energy_Storage_Discharge_Water_Differential_Pressure_ProportionalBandSetpoint](Thermal_Energy_Storage_Discharge_Water_Differential_Pressure_ProportionalBandSetpoint) (c)<br />[brick:Thermal_Energy_Storage_Supply_Water_Differential_Pressure_Proportional_BandSetpoint](Thermal_Energy_Storage_Supply_Water_Differential_Pressure_Proportional_BandSetpoint) (c)<br />
### Supply_Water_Flow_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Flow_Sensor`
Super-classes |[brick:Water_Flow_Sensor](Water_Flow_Sensor) (c)<br />
Sub-classes |[brick:Chilled_Water_Discharge_Flow_Sensor](Chilled_Water_Discharge_Flow_Sensor) (c)<br />[brick:Chilled_Water_Supply_Flow_Sensor](Chilled_Water_Supply_Flow_Sensor) (c)<br />
### Supply_Water_Temperature_Dead_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Temperature_Dead_Band_Setpoint`
Super-classes |[brick:Dead_Band_Setpoint](Dead_Band_Setpoint) (c)<br />
Sub-classes |[brick:Heat_Exchanger_Supply_Water_Temperature_Dead_Band_Setpoint](Heat_Exchanger_Supply_Water_Temperature_Dead_Band_Setpoint) (c)<br />
### Supply_Water_Temperature_Integral_Time_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Temperature_Integral_Time_Setpoint`
Super-classes |[brick:Integral_Time_Setpoint](Integral_Time_Setpoint) (c)<br />
### Supply_Water_Temperature_Proportional_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Temperature_Proportional_Band_Setpoint`
Super-classes |[brick:Proportional_Band_Setpoint](Proportional_Band_Setpoint) (c)<br />
Sub-classes |[brick:Heat_Exchanger_Discharge_Water_Temperature_Proportional_Band_Setpoint](Heat_Exchanger_Discharge_Water_Temperature_Proportional_Band_Setpoint) (c)<br />[brick:Heat_Exchanger_Supply_Water_Temperature_Proportional_Band_Setpoint](Heat_Exchanger_Supply_Water_Temperature_Proportional_Band_Setpoint) (c)<br />
### Switch
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Switch`
Super-classes |[brick:Interface](Interface) (c)<br />
Sub-classes |[brick:Dimmer](Dimmer) (c)<br />
### System_Mode_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#System_Mode_Status`
Super-classes |[brick:Mode_Status](Mode_Status) (c)<br />
### System_Shutdown_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#System_Shutdown_Status`
Super-classes |[brick:Status](Status) (c)<br />
### System_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#System_Status`
Super-classes |[brick:Status](Status) (c)<br />
### TVOC
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#TVOC`
Super-classes |[brick:Air_Quality](Air_Quality) (c)<br />
### Tag
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Tag`
In range of |[brick:hasTag](hasTag) (op)<br />
### Temperature
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Temperature`
Super-classes |[brick:Quantity](Quantity) (c)<br />
Sub-classes |[brick:Wet_Bulb_Temperature](Wet_Bulb_Temperature) (c)<br />[brick:Operative_Temperature](Operative_Temperature) (c)<br />[brick:Radiant_Temperature](Radiant_Temperature) (c)<br />
### Temperature_Dead_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Temperature_Dead_Band_Setpoint`
Super-classes |[brick:Dead_Band_Setpoint](Dead_Band_Setpoint) (c)<br />
Sub-classes |[brick:Occupied_Cooling_Temperature_Dead_Band_Setpoint](Occupied_Cooling_Temperature_Dead_Band_Setpoint) (c)<br />[brick:Occupied_Heating_Temperature_Dead_Band_Setpoint](Occupied_Heating_Temperature_Dead_Band_Setpoint) (c)<br />
### Temperature_Increase_Decrease_Step_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Temperature_Increase_Decrease_Step_Setpoint`
Super-classes |[brick:Increase_Decrease_Step_Setpoint](Increase_Decrease_Step_Setpoint) (c)<br />
Sub-classes |[brick:Air_Temperature_Increase_Decrease_Step_Setpoint](Air_Temperature_Increase_Decrease_Step_Setpoint) (c)<br />
### Temperature_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Temperature_Sensor`
Super-classes |[brick:Sensor](Sensor) (c)<br />
Sub-classes |[brick:Water_Temperature_Sensor](Water_Temperature_Sensor) (c)<br />[brick:Air_Temperature_Sensor](Air_Temperature_Sensor) (c)<br />[brick:Zone_Temperature_Sensor](Zone_Temperature_Sensor) (c)<br />
### Temperature_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Temperature_Setpoint`
Super-classes |[brick:Setpoint](Setpoint) (c)<br />
Sub-classes |[brick:Air_Temperature_Setpoint](Air_Temperature_Setpoint) (c)<br />[brick:Water_Temperature_Setpoint](Water_Temperature_Setpoint) (c)<br />
### Temporary_Occupancy_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Temporary_Occupancy_Status`
Super-classes |[brick:Occupancy_Status](Occupancy_Status) (c)<br />
### Terminal_Unit
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Terminal_Unit`
Description | <p>A device that regulates the volumetric flow rate and/or the temperature of the controlled medium.</p>
Super-classes |[brick:HVAC](HVAC) (c)<br />
Sub-classes |[brick:Fan_Coil_Unit](Fan_Coil_Unit) (c)<br />[brick:Variable_Air_Volume_Box](Variable_Air_Volume_Box) (c)<br />
### Thermal_Energy
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Thermal_Energy`
Super-classes |[brick:Energy](Energy) (c)<br />
### Thermal_Energy_Storage_Discharge_Water_Differential_Pressure_ProportionalBandSetpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Thermal_Energy_Storage_Discharge_Water_Differential_Pressure_ProportionalBandSetpoint`
Super-classes |[brick:Supply_Water_Differential_Pressure_Proportional_Band_Setpoint](Supply_Water_Differential_Pressure_Proportional_Band_Setpoint) (c)<br />
### Thermal_Energy_Storage_Supply_Water_Differential_Pressure_Dead_Band_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Thermal_Energy_Storage_Supply_Water_Differential_Pressure_Dead_Band_Setpoint`
Super-classes |[brick:Supply_Water_Differential_Pressure_Dead_Band_Setpoint](Supply_Water_Differential_Pressure_Dead_Band_Setpoint) (c)<br />
### Thermal_Energy_Storage_Supply_Water_Differential_Pressure_Proportional_BandSetpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Thermal_Energy_Storage_Supply_Water_Differential_Pressure_Proportional_BandSetpoint`
Super-classes |[brick:Supply_Water_Differential_Pressure_Proportional_Band_Setpoint](Supply_Water_Differential_Pressure_Proportional_Band_Setpoint) (c)<br />
### Thermal_Power
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Thermal_Power`
Super-classes |[brick:Power](Power) (c)<br />
### Thermostat
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Thermostat`
Description | <p>An automatic control device used to maintain temperature at a fixed or adjustable setpoint.</p>
Super-classes |[brick:HVAC](HVAC) (c)<br />
### Torque_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Torque_Sensor`
Super-classes |[brick:Sensor](Sensor) (c)<br />
Sub-classes |[brick:Motor_Torque_Sensor](Motor_Torque_Sensor) (c)<br />
### Touchpanel
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Touchpanel`
Super-classes |[brick:Interface](Interface) (c)<br />
### Trace_Heat_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Trace_Heat_Sensor`
Super-classes |[brick:Sensor](Sensor) (c)<br />
### Turn_Off_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Turn_Off_Status`
Super-classes |[brick:Status](Status) (c)<br />
### Unoccupied_Mode_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Unoccupied_Mode_Setpoint`
Super-classes |[brick:Mode_Setpoint](Mode_Setpoint) (c)<br />
### VFD
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#VFD`
Super-classes |[brick:HVAC](HVAC) (c)<br />
Sub-classes |[brick:Heat_Wheel_VFD](Heat_Wheel_VFD) (c)<br />[brick:Preheat_Valve_VFD](Preheat_Valve_VFD) (c)<br />
### Valve
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Valve`
Super-classes |[brick:HVAC](HVAC) (c)<br />
Sub-classes |[brick:Water_Valve](Water_Valve) (c)<br />[brick:Isolation_Valve](Isolation_Valve) (c)<br />[brick:Heating_Valve](Heating_Valve) (c)<br />
### Variable_Air_Volume_Box
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Variable_Air_Volume_Box`
Super-classes |[brick:Terminal_Unit](Terminal_Unit) (c)<br />
Sub-classes |[brick:Variable_Air_Volume_Box_With_Reheat](Variable_Air_Volume_Box_With_Reheat) (c)<br />
### Variable_Air_Volume_Box_With_Reheat
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Variable_Air_Volume_Box_With_Reheat`
Super-classes |[brick:Variable_Air_Volume_Box](Variable_Air_Volume_Box) (c)<br />
### Variable_Frequency_Drive
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Variable_Frequency_Drive`
Description | <p>Electronic device that varies its output frequency to vary the rotating speed of a motor, given a fixed input frequency. Used with fans or pumps to vary the flow in the system as a function of a maintained pressure.</p>
Super-classes |[brick:HVAC](HVAC) (c)<br />
### Velocity_Pressure_Sensor:
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Velocity_Pressure_Sensor:`
Super-classes |[brick:Pressure_Sensor](Pressure_Sensor) (c)<br />
Sub-classes |[brick:Exhaust_Air_Velocity_Pressure_Sensor:](Exhaust_Air_Velocity_Pressure_Sensor:) (c)<br />[brick:Supply_Air_Velocity_Pressure_Sensor:](Supply_Air_Velocity_Pressure_Sensor:) (c)<br />[brick:Discharge_Air_Velocity_Pressure_Sensor:](Discharge_Air_Velocity_Pressure_Sensor:) (c)<br />
### Velocity_Pressure_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Velocity_Pressure_Setpoint`
Super-classes |[brick:Pressure_Setpoint](Pressure_Setpoint) (c)<br />
### Vent_Operating_Mode_Status
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Vent_Operating_Mode_Status`
Super-classes |[brick:Operating_Mode_Status](Operating_Mode_Status) (c)<br />
### Voltage
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Voltage`
Super-classes |[brick:Quantity](Quantity) (c)<br />
Sub-classes |[brick:Electric_Voltage](Electric_Voltage) (c)<br />
### Voltage_Angle
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Voltage_Angle`
Super-classes |[brick:Electric_Voltage](Electric_Voltage) (c)<br />
### Voltage_Imbalance
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Voltage_Imbalance`
Super-classes |[brick:Electric_Voltage](Electric_Voltage) (c)<br />
### Voltage_Magnitude
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Voltage_Magnitude`
Super-classes |[brick:Electric_Voltage](Electric_Voltage) (c)<br />
### Voltage_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Voltage_Sensor`
Super-classes |[brick:Sensor](Sensor) (c)<br />
Sub-classes |[brick:Heat_Wheel_Voltage_Sensor](Heat_Wheel_Voltage_Sensor) (c)<br />[brick:Output_Voltage_Sensor](Output_Voltage_Sensor) (c)<br />[brick:DC_Bus_Voltage_Sensor](DC_Bus_Voltage_Sensor) (c)<br />[brick:Battery_Voltage_Sensor](Battery_Voltage_Sensor) (c)<br />
### Water
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Water`
Description | <p>transparent, odorless, tasteless liquid; a compound of hydrogen and oxygen (H2O), containing 11.188% hydrogen and 88.812% oxygen by mass; freezing at 32°F (0°C); boiling near 212°F (100°C).</p>
Super-classes |[brick:Liquid](Liquid) (c)<br />
Sub-classes |[brick:Domestic_Water](Domestic_Water) (c)<br />[brick:Hot_Water](Hot_Water) (c)<br />[brick:Chilled_Water](Chilled_Water) (c)<br />[brick:Blowdown_Water](Blowdown_Water) (c)<br />[brick:Makeup_Water](Makeup_Water) (c)<br />[brick:Condenser_Water](Condenser_Water) (c)<br />
### Water_Flow_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Water_Flow_Sensor`
Super-classes |[brick:Flow_Sensor](Flow_Sensor) (c)<br />
Sub-classes |[brick:Supply_Water_Flow_Sensor](Supply_Water_Flow_Sensor) (c)<br />
### Water_Level_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Water_Level_Sensor`
Super-classes |[brick:Sensor](Sensor) (c)<br />
Sub-classes |[brick:Deionised_Water_Level_Sensor](Deionised_Water_Level_Sensor) (c)<br />
### Water_Pump
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Water_Pump`
Super-classes |[brick:Pump](Pump) (c)<br />
Sub-classes |[brick:Chilled_Water_Pump](Chilled_Water_Pump) (c)<br />[brick:Hot_Water_Pump](Hot_Water_Pump) (c)<br />[brick:Condenser_Water_Pump](Condenser_Water_Pump) (c)<br />
### Water_System
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Water_System`
Super-classes |[brick:Equipment](Equipment) (c)<br />
Sub-classes |[brick:Hot_Water_System](Hot_Water_System) (c)<br />[brick:Chilled_Water_System](Chilled_Water_System) (c)<br />
### Water_Temperature_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Water_Temperature_Sensor`
Super-classes |[brick:Temperature_Sensor](Temperature_Sensor) (c)<br />
Sub-classes |[brick:Leaving_Water_Temperature_Sensor](Leaving_Water_Temperature_Sensor) (c)<br />[brick:Return_Water_Temperature_Sensor](Return_Water_Temperature_Sensor) (c)<br />[brick:Entering_Water_Temperature_Sensor](Entering_Water_Temperature_Sensor) (c)<br />[brick:Heat_Exchanger_Supply_Water_Temperature_Sensor](Heat_Exchanger_Supply_Water_Temperature_Sensor) (c)<br />[brick:Hot_Water_Supply_Temperature_Sensor](Hot_Water_Supply_Temperature_Sensor) (c)<br />[brick:Chilled_Water_Temperature_Sensor](Chilled_Water_Temperature_Sensor) (c)<br />
### Water_Temperature_Setpoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Water_Temperature_Setpoint`
Super-classes |[brick:Temperature_Setpoint](Temperature_Setpoint) (c)<br />
Sub-classes |[brick:Entering_Water_Temperature_Setpoint](Entering_Water_Temperature_Setpoint) (c)<br />[brick:Leaving_Water_Temperature_Setpoint](Leaving_Water_Temperature_Setpoint) (c)<br />
### Water_Valve
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Water_Valve`
Super-classes |[brick:Valve](Valve) (c)<br />
Sub-classes |[brick:Chilled_Water_Valve](Chilled_Water_Valve) (c)<br />
### Weather
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Weather`
Super-classes |[brick:Equipment](Equipment) (c)<br />
### Weather_Condition
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Weather_Condition`
Super-classes |[brick:Quantity](Quantity) (c)<br />
### Wet_Bulb_Temperature
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Wet_Bulb_Temperature`
Super-classes |[brick:Temperature](Temperature) (c)<br />
### Wind_Direction
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Wind_Direction`
Super-classes |[brick:Direction](Direction) (c)<br />
### Wind_Direction_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Wind_Direction_Sensor`
Super-classes |[brick:Direction_Sensor](Direction_Sensor) (c)<br />
### Wind_Speed
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Wind_Speed`
Super-classes |[brick:Speed](Speed) (c)<br />
### Wind_Speed_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Wind_Speed_Sensor`
Super-classes |[brick:Speed_Sensor](Speed_Sensor) (c)<br />
### Wing
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Wing`
Super-classes |[brick:Location](Location) (c)<br />
### Zone
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Zone`
Super-classes |[brick:Location](Location) (c)<br />
Sub-classes |[brick:Fire_Zone](Fire_Zone) (c)<br />[brick:Lighting_Zone](Lighting_Zone) (c)<br />[brick:HVAC_Zone](HVAC_Zone) (c)<br />
### Zone_Air_Temperature_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Zone_Air_Temperature_Sensor`
Super-classes |[brick:Air_Temperature_Sensor](Air_Temperature_Sensor) (c)<br />
### Zone_Humidity_Sensor:
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Zone_Humidity_Sensor:`
Super-classes |[brick:Air_Humidity_Sensor](Air_Humidity_Sensor) (c)<br />
### Zone_Temperature_Sensor
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#Zone_Temperature_Sensor`
Super-classes |[brick:Temperature_Sensor](Temperature_Sensor) (c)<br />
Sub-classes |[brick:Highest_Zone_Temperature_Sensor](Highest_Zone_Temperature_Sensor) (c)<br />[brick:Average_Zone_Temperature_Sensor](Average_Zone_Temperature_Sensor) (c)<br />[brick:Lowest_Zone_Temperature_Sensor](Lowest_Zone_Temperature_Sensor) (c)<br />

## Object Properties
[ahuRef](#ahuRef),
[controls](#controls),
[feeds](#feeds),
[feedsAir](#feedsAir),
[hasInputSubstance](#hasInputSubstance),
[hasLocation](#hasLocation),
[hasOutputSubstance](#hasOutputSubstance),
[hasPart](#hasPart),
[hasPoint](#hasPoint),
[hasTag](#hasTag),
[isControlledBy](#isControlledBy),
[isFedBy](#isFedBy),
[isLocationOf](#isLocationOf),
[isMeasuredBy](#isMeasuredBy),
[isPartOf](#isPartOf),
[isPointOf](#isPointOf),
[measures](#measures),
[](ahuRef)
### ahuRef
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#ahuRef`
Range(s) |[brick:AHU](AHU) (c)<br />
[](controls)
### controls
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#controls`
[](feeds)
### feeds
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#feeds`
[](feedsAir)
### feedsAir
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#feedsAir`
Super-properties |[brick:feeds](feeds) (op)<br />
[](hasInputSubstance)
### hasInputSubstance
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#hasInputSubstance`
Range(s) |[brick:Substance](Substance) (c)<br />
[](hasLocation)
### hasLocation
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#hasLocation`
Range(s) |[brick:Location](Location) (c)<br />
[](hasOutputSubstance)
### hasOutputSubstance
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#hasOutputSubstance`
Range(s) |[brick:Substance](Substance) (c)<br />
[](hasPart)
### hasPart
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#hasPart`
[](hasPoint)
### hasPoint
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#hasPoint`
Range(s) |[brick:Point](Point) (c)<br />
[](hasTag)
### hasTag
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#hasTag`
Range(s) |[brick:Tag](Tag) (c)<br />
[](isControlledBy)
### isControlledBy
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#isControlledBy`
[](isFedBy)
### isFedBy
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#isFedBy`
[](isLocationOf)
### isLocationOf
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#isLocationOf`
Domain(s) |[brick:Location](Location) (c)<br />
[](isMeasuredBy)
### isMeasuredBy
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#isMeasuredBy`
Domain(s) |[brick:Substance](Substance) (c)<br />
Range(s) |[brick:Point](Point) (c)<br />
[](isPartOf)
### isPartOf
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#isPartOf`
[](isPointOf)
### isPointOf
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#isPointOf`
Domain(s) |[brick:Point](Point) (c)<br />
[](measures)
### measures
Property | Value
--- | ---
IRI | `https://brickschema.org/schema/1.0.3/Brick#measures`
Domain(s) |[brick:Point](Point) (c)<br />
Range(s) |[brick:Substance](Substance) (c)<br />

## Named Individuals
## Namespaces
* **default (:)**
  * `https://brickschema.org/schema/1.0.3/Brick#`
* **bldg**
  * `https://brickschema.org/schema/1.0.3/ExampleBuilding#`
* **brick**
  * `https://brickschema.org/schema/1.0.3/Brick#`
* **dcterms**
  * `http://purl.org/dc/terms/`
* **owl**
  * `http://www.w3.org/2002/07/owl#`
* **prov**
  * `http://www.w3.org/ns/prov#`
* **rdf**
  * `http://www.w3.org/1999/02/22-rdf-syntax-ns#`
* **rdfs**
  * `http://www.w3.org/2000/01/rdf-schema#`
* **sdo**
  * `http://schema.org/`
* **sdo1**
  * `https://schema.org/`
* **skos**
  * `http://www.w3.org/2004/02/skos/core#`
* **tag**
  * `https://brickschema.org/schema/1.0.3/BrickTag#`
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