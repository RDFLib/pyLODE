Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE) 2.8.10

# Brick

## Metadata
* **URI**
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
URI | `https://brickschema.org/schema/1.0.3/Brick#AHU`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#HVAC](https://brickschema.org/schema/1.0.3/Brick#HVAC) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Rooftop_Unit](https://brickschema.org/schema/1.0.3/Brick#Rooftop_Unit) (c)<br />
In range of |[https://brickschema.org/schema/1.0.3/Brick#ahuRef](https://brickschema.org/schema/1.0.3/Brick#ahuRef) (op)<br />
Has members |[https://brickschema.org/schema/1.0.3/ExampleBuilding#AHU1](https://brickschema.org/schema/1.0.3/ExampleBuilding#AHU1)<br />
### Absorption_Chiller
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Absorption_Chiller`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Chiller](https://brickschema.org/schema/1.0.3/Brick#Chiller) (c)<br />
### Active_Power
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Active_Power`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Electric_Power](https://brickschema.org/schema/1.0.3/Brick#Electric_Power) (c)<br />
### Air
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Air`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Gas](https://brickschema.org/schema/1.0.3/Brick#Gas) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Mixed_Air](https://brickschema.org/schema/1.0.3/Brick#Mixed_Air) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Supply_Air](https://brickschema.org/schema/1.0.3/Brick#Supply_Air) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Outside_Air](https://brickschema.org/schema/1.0.3/Brick#Outside_Air) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air](https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Return_Air](https://brickschema.org/schema/1.0.3/Brick#Return_Air) (c)<br />
### Air_Enthalpy_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Air_Enthalpy_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Enthalpy_Sensor](https://brickschema.org/schema/1.0.3/Brick#Enthalpy_Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Enthalpy_Sensor](https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Enthalpy_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Return_Air_Enthalpy_Sensor](https://brickschema.org/schema/1.0.3/Brick#Return_Air_Enthalpy_Sensor) (c)<br />
### Air_Flow_Dead_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Dead_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Dead_Band_Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Stack_Flow_Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Stack_Flow_Dead_Band_Setpoint) (c)<br />
### Air_Flow_Demand_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Demand_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Demand_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Demand_Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Flow_Demand_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Flow_Demand_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Flow_Demand_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Flow_Demand_Setpoint) (c)<br />
### Air_Flow_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Flow_Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Flow_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Return_Air_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Return_Air_Flow_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Fan_Air_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Fan_Air_Flow_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Bypass_Air_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Bypass_Air_Flow_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Fume_Hood_Air_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Fume_Hood_Air_Flow_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Flow_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Flow_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Flow_Sensor) (c)<br />
Has members |[https://brickschema.org/schema/1.0.3/ExampleBuilding#AFS1](https://brickschema.org/schema/1.0.3/ExampleBuilding#AFS1)<br />
### Air_Flow_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Flow_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Flow_Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Fan_Air_Flow_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Fan_Air_Flow_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Flow_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Flow_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Flow_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Flow_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Flow_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Flow_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Demand_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Demand_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Flow_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Flow_Setpoint) (c)<br />
### Air_Flow_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Limit](https://brickschema.org/schema/1.0.3/Brick#Limit) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Max_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Air_Flow_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Min_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Air_Flow_Setpoint_Limit) (c)<br />
### Air_Grains_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Air_Grains_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Sensor](https://brickschema.org/schema/1.0.3/Brick#Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Return_Air_Grains_Sensor](https://brickschema.org/schema/1.0.3/Brick#Return_Air_Grains_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Grains_Sensor](https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Grains_Sensor) (c)<br />
### Air_Handler_Unit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Air_Handler_Unit`
Description | <p>Assembly consisting of sections containing a fan or fans and other necessary equipment to perform one or more of the following functions: circulating, filtration, heating, cooling, heat recovery, humidifying, dehumidifying, and mixing of air. Is usually connected to an air-distribution system.</p>
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#HVAC](https://brickschema.org/schema/1.0.3/Brick#HVAC) (c)<br />
### Air_Humidity_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Air_Humidity_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Humidity_Sensor](https://brickschema.org/schema/1.0.3/Brick#Humidity_Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Relative_Humidity_Sensor:](https://brickschema.org/schema/1.0.3/Brick#Relative_Humidity_Sensor:) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Humidity_Sensor:](https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Humidity_Sensor:) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Humidity_Sensor:](https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Humidity_Sensor:) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Humidity_Sensor:](https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Humidity_Sensor:) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Return_Air_Humidity_Sensor:](https://brickschema.org/schema/1.0.3/Brick#Return_Air_Humidity_Sensor:) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Humidity_Sensor:](https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Humidity_Sensor:) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Zone_Humidity_Sensor:](https://brickschema.org/schema/1.0.3/Brick#Zone_Humidity_Sensor:) (c)<br />
### Air_Quality
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Air_Quality`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Quantity](https://brickschema.org/schema/1.0.3/Brick#Quantity) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#TVOC](https://brickschema.org/schema/1.0.3/Brick#TVOC) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#PM10](https://brickschema.org/schema/1.0.3/Brick#PM10) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#CO2](https://brickschema.org/schema/1.0.3/Brick#CO2) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#PM25](https://brickschema.org/schema/1.0.3/Brick#PM25) (c)<br />
### Air_Static_Pressure_Increase_Decrease_Step_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Air_Static_Pressure_Increase_Decrease_Step_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Increase_Decrease_Step_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Increase_Decrease_Step_Setpoint) (c)<br />
### Air_Temperature_Increase_Decrease_Step_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Air_Temperature_Increase_Decrease_Step_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Temperature_Increase_Decrease_Step_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Temperature_Increase_Decrease_Step_Setpoint) (c)<br />
### Air_Temperature_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Air_Temperature_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Temperature_Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Zone_Air_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Zone_Air_Temperature_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Temperature_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Return_Air_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Return_Air_Temperature_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Mixed_Air_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Mixed_Air_Temperature_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Temperature_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Sensor) (c)<br />
Has members |[https://brickschema.org/schema/1.0.3/ExampleBuilding#TS2](https://brickschema.org/schema/1.0.3/ExampleBuilding#TS2)<br />
### Air_Temperature_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Air_Temperature_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Temperature_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Temperature_Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Mixed_Air_Temperature_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Mixed_Air_Temperature_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Room_Air_Temperature_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Room_Air_Temperature_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Temperature_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Temperature_Setpoint) (c)<br />
### Alternating_Current_Frequency
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Alternating_Current_Frequency`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Frequency](https://brickschema.org/schema/1.0.3/Brick#Frequency) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Electric_Current](https://brickschema.org/schema/1.0.3/Brick#Electric_Current) (c)<br />
### Angle_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Angle_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Sensor](https://brickschema.org/schema/1.0.3/Brick#Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Solar_Azimuth_Angle_Sensor](https://brickschema.org/schema/1.0.3/Brick#Solar_Azimuth_Angle_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Solar_Zenith_Angle_Sensor](https://brickschema.org/schema/1.0.3/Brick#Solar_Zenith_Angle_Sensor) (c)<br />
### Apparent_Power
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Apparent_Power`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Electric_Power](https://brickschema.org/schema/1.0.3/Brick#Electric_Power) (c)<br />
### Atmospheric_Pressure
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Atmospheric_Pressure`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Pressure](https://brickschema.org/schema/1.0.3/Brick#Pressure) (c)<br />
### Average_Discharge_Air_Flow_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Average_Discharge_Air_Flow_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Flow_Sensor) (c)<br />
### Average_Exhaust_Air_Static_Pressure_Sensor:
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Average_Exhaust_Air_Static_Pressure_Sensor:`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Static_Pressure_Sensor:](https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Static_Pressure_Sensor:) (c)<br />
### Average_Supply_Air_Flow_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Average_Supply_Air_Flow_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Flow_Sensor) (c)<br />
### Average_Zone_Temperature_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Average_Zone_Temperature_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Zone_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Zone_Temperature_Sensor) (c)<br />
### Basement
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Basement`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Location](https://brickschema.org/schema/1.0.3/Brick#Location) (c)<br />
### Battery_Voltage_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Battery_Voltage_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Voltage_Sensor](https://brickschema.org/schema/1.0.3/Brick#Voltage_Sensor) (c)<br />
### Blowdown_Water
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Blowdown_Water`
Description | <p>Water expelled from a system to remove mineral build up</p>
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Water](https://brickschema.org/schema/1.0.3/Brick#Water) (c)<br />
### Boiler
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Boiler`
Description | <p>A closed, pressure vessel that uses fuel or electricity for heating water or other fluids to supply steam or hot water for heating, humidification, or other applications.</p>
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#HVAC](https://brickschema.org/schema/1.0.3/Brick#HVAC) (c)<br />
### Booster_Fan
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Booster_Fan`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Supply_Fan](https://brickschema.org/schema/1.0.3/Brick#Supply_Fan) (c)<br />
### Booster_Fan_Air_Flow_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Booster_Fan_Air_Flow_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Fan_Air_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Fan_Air_Flow_Sensor) (c)<br />
### Building
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Building`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Location](https://brickschema.org/schema/1.0.3/Brick#Location) (c)<br />
### Building_Static_Pressure_Sensor:
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Building_Static_Pressure_Sensor:`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Sensor](https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Sensor) (c)<br />
### Building_Static_Pressure_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Building_Static_Pressure_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Setpoint) (c)<br />
### Bypass_Air_Flow_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Bypass_Air_Flow_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Sensor) (c)<br />
### CO2
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#CO2`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Quality](https://brickschema.org/schema/1.0.3/Brick#Air_Quality) (c)<br />
### CO2_Differential_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#CO2_Differential_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#CO2_Sensor](https://brickschema.org/schema/1.0.3/Brick#CO2_Sensor) (c)<br />
### CO2_Level_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#CO2_Level_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#CO2_Sensor](https://brickschema.org/schema/1.0.3/Brick#CO2_Sensor) (c)<br />
Has members |[https://brickschema.org/schema/1.0.3/ExampleBuilding#co2s1](https://brickschema.org/schema/1.0.3/ExampleBuilding#co2s1)<br />
### CO2_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#CO2_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Sensor](https://brickschema.org/schema/1.0.3/Brick#Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Outside_Air_CO2_Sensor](https://brickschema.org/schema/1.0.3/Brick#Outside_Air_CO2_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#CO2_Level_Sensor](https://brickschema.org/schema/1.0.3/Brick#CO2_Level_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Return_Air_CO2_Sensor](https://brickschema.org/schema/1.0.3/Brick#Return_Air_CO2_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#CO2_Differential_Sensor](https://brickschema.org/schema/1.0.3/Brick#CO2_Differential_Sensor) (c)<br />
### CO2_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#CO2_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Setpoint](https://brickschema.org/schema/1.0.3/Brick#Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Return_Air_CO2_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Return_Air_CO2_Setpoint) (c)<br />
### CRAC
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#CRAC`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#HVAC](https://brickschema.org/schema/1.0.3/Brick#HVAC) (c)<br />
### Capacity
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Capacity`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Quantity](https://brickschema.org/schema/1.0.3/Brick#Quantity) (c)<br />
### Capacity_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Capacity_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Sensor](https://brickschema.org/schema/1.0.3/Brick#Sensor) (c)<br />
### Centrifugal_Chiller
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Centrifugal_Chiller`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Chiller](https://brickschema.org/schema/1.0.3/Brick#Chiller) (c)<br />
### Chilled_Water
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water`
Description | <p>water used as a cooling medium (particularly in air-conditioning systems or in processes) at below ambient temperature.</p>
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Water](https://brickschema.org/schema/1.0.3/Brick#Water) (c)<br />
### Chilled_Water_Differential_Pressure_Dead_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Pressure_Dead_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Dead_Band_Setpoint) (c)<br />
### Chilled_Water_Differential_Pressure_Increase_Decrease_Step_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Pressure_Increase_Decrease_Step_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Increase_Decrease_Step_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Increase_Decrease_Step_Setpoint) (c)<br />
### Chilled_Water_Differential_Pressure_Integral_Time_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Pressure_Integral_Time_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Integral_Time_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Integral_Time_Setpoint) (c)<br />
### Chilled_Water_Differential_Pressure_Load_Shed_Reset_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Pressure_Load_Shed_Reset_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Load_Shed_Status](https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Load_Shed_Status) (c)<br />
### Chilled_Water_Differential_Pressure_Load_Shed_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Pressure_Load_Shed_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Load_Shed_Differential_Pressure_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Load_Shed_Differential_Pressure_Setpoint) (c)<br />
### Chilled_Water_Differential_Pressure_Load_Shed_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Pressure_Load_Shed_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Load_Shed_Status](https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Load_Shed_Status) (c)<br />
### Chilled_Water_Differential_Pressure_Proportional_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Pressure_Proportional_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Proportional_Band_Setpoint) (c)<br />
### Chilled_Water_Differential_Pressure_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Pressure_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Sensor](https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Sensor) (c)<br />
### Chilled_Water_Differential_Pressure_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Pressure_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Setpoint) (c)<br />
### Chilled_Water_Differential_Temperature_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Temperature_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Temperature_Sensor) (c)<br />
### Chilled_Water_Discharge_Flow_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Discharge_Flow_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Flow_Sensor) (c)<br />
### Chilled_Water_Pump
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Pump`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Water_Pump](https://brickschema.org/schema/1.0.3/Brick#Water_Pump) (c)<br />
### Chilled_Water_Pump_Differential_Pressure_Dead_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Pump_Differential_Pressure_Dead_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Dead_Band_Setpoint) (c)<br />
### Chilled_Water_Pump_Differential_Pressure_Integration_Time_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Pump_Differential_Pressure_Integration_Time_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Integral_Time](https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Integral_Time) (c)<br />
### Chilled_Water_Return_Temperature_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Return_Temperature_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Return_Water_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Return_Water_Temperature_Sensor) (c)<br />
### Chilled_Water_Static_Pressure_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Static_Pressure_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Setpoint) (c)<br />
### Chilled_Water_Supply_Flow_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Supply_Flow_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Flow_Sensor) (c)<br />
### Chilled_Water_Supply_Temperature_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Supply_Temperature_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Temperature_Sensor) (c)<br />
### Chilled_Water_System
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_System`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Water_System](https://brickschema.org/schema/1.0.3/Brick#Water_System) (c)<br />
### Chilled_Water_Temperature_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Temperature_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Water_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Water_Temperature_Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Supply_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Supply_Temperature_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Temperature_Sensor) (c)<br />
### Chilled_Water_Valve
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Valve`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Water_Valve](https://brickschema.org/schema/1.0.3/Brick#Water_Valve) (c)<br />
### Chiller
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Chiller`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#HVAC](https://brickschema.org/schema/1.0.3/Brick#HVAC) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Centrifugal_Chiller](https://brickschema.org/schema/1.0.3/Brick#Centrifugal_Chiller) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Absorption_Chiller](https://brickschema.org/schema/1.0.3/Brick#Absorption_Chiller) (c)<br />
Has members |[https://brickschema.org/schema/1.0.3/ExampleBuilding#CH1](https://brickschema.org/schema/1.0.3/ExampleBuilding#CH1)<br />
### City
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#City`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Location](https://brickschema.org/schema/1.0.3/Brick#Location) (c)<br />
### Cloudage
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Cloudage`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Quantity](https://brickschema.org/schema/1.0.3/Brick#Quantity) (c)<br />
### Coil
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Coil`
Description | <p>Exchanger that transfers heat from an exhaust airstream to a separated supply airstream.</p>
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#HVAC](https://brickschema.org/schema/1.0.3/Brick#HVAC) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Cooling_Coil](https://brickschema.org/schema/1.0.3/Brick#Cooling_Coil) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Heating_Coil](https://brickschema.org/schema/1.0.3/Brick#Heating_Coil) (c)<br />
### Cold_Box
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Cold_Box`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Laboratory](https://brickschema.org/schema/1.0.3/Brick#Laboratory) (c)<br />
### Complex_Power
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Complex_Power`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Electric_Power](https://brickschema.org/schema/1.0.3/Brick#Electric_Power) (c)<br />
### Compressor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Compressor`
Description | <p>(1) device for mechanically increasing the pressure of a gas. (2) often described as being either open, hermetic, or semihermetic to describe how the compressor and motor drive is situated in relation to the gas or vapor being compressed. Types include centrifugal, axial flow, reciprocating, rotary screw, rotary vane, scroll, or diaphragm. 1. device for mechanically increasing the pressure of a gas. 2. specific machine, with or without accessories, for compressing refrigerant vapor.</p>
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#HVAC](https://brickschema.org/schema/1.0.3/Brick#HVAC) (c)<br />
### Computer_Room_Air_Conditioning
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Computer_Room_Air_Conditioning`
Description | <p>A device that monitors and maintains the temperature, air distribution and humidity in a network room or data center. </p>
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#HVAC](https://brickschema.org/schema/1.0.3/Brick#HVAC) (c)<br />
### Condenser
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Condenser`
Description | <p>A heat exchanger in which the primary heat transfer vapor changes its state to a liquid phase.</p>
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#HVAC](https://brickschema.org/schema/1.0.3/Brick#HVAC) (c)<br />
### Condenser_Heat_Exchanger
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Condenser_Heat_Exchanger`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Heat_Exchanger](https://brickschema.org/schema/1.0.3/Brick#Heat_Exchanger) (c)<br />
### Condenser_Water
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Condenser_Water`
Description | <p>Water used used to remove heat through condensation</p>
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Water](https://brickschema.org/schema/1.0.3/Brick#Water) (c)<br />
### Condenser_Water_Pump
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Condenser_Water_Pump`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Water_Pump](https://brickschema.org/schema/1.0.3/Brick#Water_Pump) (c)<br />
### Conductivity
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Conductivity`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Quantity](https://brickschema.org/schema/1.0.3/Brick#Quantity) (c)<br />
### Conductivity_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Conductivity_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Sensor](https://brickschema.org/schema/1.0.3/Brick#Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Deionised_Water_Conductivity_Sensor](https://brickschema.org/schema/1.0.3/Brick#Deionised_Water_Conductivity_Sensor) (c)<br />
### Cooling_Coil
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Cooling_Coil`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Coil](https://brickschema.org/schema/1.0.3/Brick#Coil) (c)<br />
### Cooling_Coil_Discharge_Air_Temperature_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Cooling_Coil_Discharge_Air_Temperature_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Sensor) (c)<br />
### Cooling_Demand_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Cooling_Demand_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Demand_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Demand_Setpoint) (c)<br />
### Cooling_Discharge_Air_Flow_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Cooling_Discharge_Air_Flow_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Flow_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Flow_Setpoint) (c)<br />
### Cooling_Discharge_Air_Temperature_Dead_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Cooling_Discharge_Air_Temperature_Dead_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Dead_Band_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Dead_Band_Setpoint) (c)<br />
### Cooling_Discharge_Air_Temperature_Integral_Time_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Cooling_Discharge_Air_Temperature_Integral_Time_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Integral_Time_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Integral_Time_Setpoint) (c)<br />
### Cooling_Discharge_Air_Temperature_Proportional_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Cooling_Discharge_Air_Temperature_Proportional_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Proportional_Band_Setpoint) (c)<br />
### Cooling_On_Off_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Cooling_On_Off_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#On_Off_Status](https://brickschema.org/schema/1.0.3/Brick#On_Off_Status) (c)<br />
### Cooling_Request_Percent_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Cooling_Request_Percent_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Demand_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Demand_Setpoint) (c)<br />
### Cooling_Request_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Cooling_Request_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Demand_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Demand_Setpoint) (c)<br />
### Cooling_Supply_Air_Flow_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Cooling_Supply_Air_Flow_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Flow_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Flow_Setpoint) (c)<br />
### Cooling_Supply_Air_Temperature_Dead_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Cooling_Supply_Air_Temperature_Dead_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Temperature_Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Temperature_Dead_Band_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Dead_Band_Setpoint) (c)<br />
### Cooling_Supply_Air_Temperature_Integral_Time_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Cooling_Supply_Air_Temperature_Integral_Time_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Integral_Time_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Integral_Time_Setpoint) (c)<br />
### Cooling_Supply_Air_Temperature_Proportional_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Cooling_Supply_Air_Temperature_Proportional_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Proportional_Band_Setpoint) (c)<br />
### Cooling_Tower_Fan
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Cooling_Tower_Fan`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Fan](https://brickschema.org/schema/1.0.3/Brick#Fan) (c)<br />
### Current
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Current`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Quantity](https://brickschema.org/schema/1.0.3/Brick#Quantity) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Electric_Current](https://brickschema.org/schema/1.0.3/Brick#Electric_Current) (c)<br />
### Current_Angle
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Current_Angle`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Electric_Current](https://brickschema.org/schema/1.0.3/Brick#Electric_Current) (c)<br />
### Current_Imbalance
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Current_Imbalance`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Electric_Current](https://brickschema.org/schema/1.0.3/Brick#Electric_Current) (c)<br />
### Current_Magnitude
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Current_Magnitude`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Electric_Current](https://brickschema.org/schema/1.0.3/Brick#Electric_Current) (c)<br />
### Current_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Current_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Sensor](https://brickschema.org/schema/1.0.3/Brick#Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Motor_Current_Sensor](https://brickschema.org/schema/1.0.3/Brick#Motor_Current_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Photovoltaic_Current_Output_Sensor](https://brickschema.org/schema/1.0.3/Brick#Photovoltaic_Current_Output_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Load_Current_Sensor](https://brickschema.org/schema/1.0.3/Brick#Load_Current_Sensor) (c)<br />
### Current_Total_Harmonic_Distortion
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Current_Total_Harmonic_Distortion`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Electric_Current](https://brickschema.org/schema/1.0.3/Brick#Electric_Current) (c)<br />
### DC_Bus_Voltage_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#DC_Bus_Voltage_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Voltage_Sensor](https://brickschema.org/schema/1.0.3/Brick#Voltage_Sensor) (c)<br />
### Damper
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Damper`
Description | <p>Element inserted into an air-distribution system or element of an air-distribution system permitting modification of the air resistance of the system and consequently changing the airflow rate or shutting off the airflow.</p>
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#HVAC](https://brickschema.org/schema/1.0.3/Brick#HVAC) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Economizer_Damper](https://brickschema.org/schema/1.0.3/Brick#Economizer_Damper) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Outside_Damper](https://brickschema.org/schema/1.0.3/Brick#Outside_Damper) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Return_Damper](https://brickschema.org/schema/1.0.3/Brick#Return_Damper) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Exhaust_Damper](https://brickschema.org/schema/1.0.3/Brick#Exhaust_Damper) (c)<br />
### Damper_Position_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Damper_Position_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Limit](https://brickschema.org/schema/1.0.3/Brick#Limit) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Max_Damper_Position_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Damper_Position_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Min_Damper_Position_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Damper_Position_Setpoint_Limit) (c)<br />
### Damper_Position_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Damper_Position_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Sensor](https://brickschema.org/schema/1.0.3/Brick#Sensor) (c)<br />
### Damper_Position_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Damper_Position_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Setpoint](https://brickschema.org/schema/1.0.3/Brick#Setpoint) (c)<br />
### Daytime
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Daytime`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Quantity](https://brickschema.org/schema/1.0.3/Brick#Quantity) (c)<br />
### Dead_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Dead_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Setpoint](https://brickschema.org/schema/1.0.3/Brick#Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Pressure_Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Pressure_Dead_Band_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Dead_Band_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Dead_Band_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Differential_Pressure_Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Differential_Pressure_Dead_Band_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Temperature_Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Temperature_Dead_Band_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Cooling_Supply_Air_Temperature_Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Cooling_Supply_Air_Temperature_Dead_Band_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Cooling_Discharge_Air_Temperature_Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Cooling_Discharge_Air_Temperature_Dead_Band_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Dead_Band_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Temperature_Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Temperature_Dead_Band_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Temperature_Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Temperature_Dead_Band_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Dead_Band_Setpoint) (c)<br />
### Dehumidification_On_Off_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Dehumidification_On_Off_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#On_Off_Status](https://brickschema.org/schema/1.0.3/Brick#On_Off_Status) (c)<br />
### Deionised_Water_Conductivity_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Deionised_Water_Conductivity_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Conductivity_Sensor](https://brickschema.org/schema/1.0.3/Brick#Conductivity_Sensor) (c)<br />
### Deionised_Water_Level_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Deionised_Water_Level_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Water_Level_Sensor](https://brickschema.org/schema/1.0.3/Brick#Water_Level_Sensor) (c)<br />
### Demand_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Demand_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Sensor](https://brickschema.org/schema/1.0.3/Brick#Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Peak_Power_Demand_Sensor](https://brickschema.org/schema/1.0.3/Brick#Peak_Power_Demand_Sensor) (c)<br />
### Demand_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Demand_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Setpoint](https://brickschema.org/schema/1.0.3/Brick#Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Heating_Request_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Heating_Request_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Demand_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Demand_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Cooling_Request_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Cooling_Request_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Cooling_Request_Percent_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Cooling_Request_Percent_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Heating_Request_Percent_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Heating_Request_Percent_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Heating_Demand_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Heating_Demand_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Preheat_Demand_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Preheat_Demand_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Cooling_Demand_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Cooling_Demand_Setpoint) (c)<br />
### Dew_Point_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Dew_Point_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Setpoint](https://brickschema.org/schema/1.0.3/Brick#Setpoint) (c)<br />
### Dewpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Dewpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Quantity](https://brickschema.org/schema/1.0.3/Brick#Quantity) (c)<br />
### Dewpoint_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Dewpoint_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Sensor](https://brickschema.org/schema/1.0.3/Brick#Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Return_Air_Dewpoint_Sensor](https://brickschema.org/schema/1.0.3/Brick#Return_Air_Dewpoint_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Dewpoint_Sensor](https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Dewpoint_Sensor) (c)<br />
### Differential_Pressure_Dead_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Dead_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Dead_Band_Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Pump_Differential_Pressure_Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Pump_Differential_Pressure_Dead_Band_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Differential_Pressure_Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Differential_Pressure_Dead_Band_Setpoint) (c)<br />
### Differential_Pressure_Increase_Decrease_Step_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Increase_Decrease_Step_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Increase_Decrease_Step_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Increase_Decrease_Step_Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Pressure_Increase_Decrease_Step_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Pressure_Increase_Decrease_Step_Setpoint) (c)<br />
### Differential_Pressure_Integral_Time
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Integral_Time`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Integral_Time_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Integral_Time_Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Pump_Differential_Pressure_Integration_Time_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Pump_Differential_Pressure_Integration_Time_Setpoint) (c)<br />
### Differential_Pressure_Integral_Time_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Integral_Time_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Integral_Time_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Integral_Time_Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Differential_Pressure_Integral_Time_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Differential_Pressure_Integral_Time_Setpoint) (c)<br />
### Differential_Pressure_Load_Shed_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Load_Shed_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Load_Shed_Status](https://brickschema.org/schema/1.0.3/Brick#Load_Shed_Status) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Pressure_Load_Shed_Reset_Status](https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Pressure_Load_Shed_Reset_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Pressure_Load_Shed_Status](https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Pressure_Load_Shed_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Supply_Temperature_Load_Shed_Status](https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Supply_Temperature_Load_Shed_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Discharge_Temperature_Load_Shed_Status](https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Discharge_Temperature_Load_Shed_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Differential_Pressure_Load_Shed_Status](https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Differential_Pressure_Load_Shed_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Differential_Pressure_Load_Shed_Reset_Status](https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Differential_Pressure_Load_Shed_Reset_Status) (c)<br />
### Differential_Pressure_Proportional_Band
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Proportional_Band`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Proportional_Band_Setpoint) (c)<br />
### Differential_Pressure_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Pressure_Sensor](https://brickschema.org/schema/1.0.3/Brick#Pressure_Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Pressure_Sensor](https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Pressure_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Heat_Wheel_Differential_Pressure_Sensor](https://brickschema.org/schema/1.0.3/Brick#Heat_Wheel_Differential_Pressure_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Filter_Differential_Pressure_Sensor](https://brickschema.org/schema/1.0.3/Brick#Filter_Differential_Pressure_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Differential_Pressure_Sensor](https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Differential_Pressure_Sensor) (c)<br />
### Differential_Pressure_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Pressure_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Pressure_Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Pressure_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Pressure_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Differential_Pressure_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Differential_Pressure_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Load_Shed_Differential_Pressure_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Load_Shed_Differential_Pressure_Setpoint) (c)<br />
### Differential_Pressure_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Limit](https://brickschema.org/schema/1.0.3/Brick#Limit) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Min_Chilled_Water_Differential_Pressure_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Chilled_Water_Differential_Pressure_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Min_Hot_Water_Differential_Pressure_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Hot_Water_Differential_Pressure_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Max_Chilled_Water_Differential_Pressure_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Chilled_Water_Differential_Pressure_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Max_Hot_Water_Differential_Pressure_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Hot_Water_Differential_Pressure_Setpoint_Limit) (c)<br />
### Differential_Speed_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Differential_Speed_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Speed_Sensor](https://brickschema.org/schema/1.0.3/Brick#Speed_Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Heat_Wheel_Speed_Sensor](https://brickschema.org/schema/1.0.3/Brick#Heat_Wheel_Speed_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Return_Fan_Differential_Speed_Sensor](https://brickschema.org/schema/1.0.3/Brick#Return_Fan_Differential_Speed_Sensor) (c)<br />
### Differential_Speed_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Differential_Speed_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Speed_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Speed_Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Return_Discharge_Fan_Differential_Speed_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Return_Discharge_Fan_Differential_Speed_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Return_Supply_Fan_Differential_Speed_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Return_Supply_Fan_Differential_Speed_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Return_Fan_Differential_Speed_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Return_Fan_Differential_Speed_Setpoint) (c)<br />
### Dimmer
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Dimmer`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Switch](https://brickschema.org/schema/1.0.3/Brick#Switch) (c)<br />
### Direction
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Direction`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Quantity](https://brickschema.org/schema/1.0.3/Brick#Quantity) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Wind_Direction](https://brickschema.org/schema/1.0.3/Brick#Wind_Direction) (c)<br />
### Direction_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Direction_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Sensor](https://brickschema.org/schema/1.0.3/Brick#Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Wind_Direction_Sensor](https://brickschema.org/schema/1.0.3/Brick#Wind_Direction_Sensor) (c)<br />
### Direction_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Direction_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Status](https://brickschema.org/schema/1.0.3/Brick#Status) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Motor_Direction_Status](https://brickschema.org/schema/1.0.3/Brick#Motor_Direction_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Run_Direction_Status](https://brickschema.org/schema/1.0.3/Brick#Run_Direction_Status) (c)<br />
### Disable_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Disable_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Status](https://brickschema.org/schema/1.0.3/Brick#Status) (c)<br />
### Discharge_Air_Duct_Pressure_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Duct_Pressure_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Pressure_Status](https://brickschema.org/schema/1.0.3/Brick#Pressure_Status) (c)<br />
### Discharge_Air_Flow_Demand_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Flow_Demand_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Flow_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Flow_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Demand_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Demand_Setpoint) (c)<br />
### Discharge_Air_Flow_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Flow_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Average_Supply_Air_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Average_Supply_Air_Flow_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Average_Discharge_Air_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Average_Discharge_Air_Flow_Sensor) (c)<br />
### Discharge_Air_Flow_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Flow_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Flow_Demand_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Flow_Demand_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Cooling_Discharge_Air_Flow_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Cooling_Discharge_Air_Flow_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Heating_Discharge_Air_Flow_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Heating_Discharge_Air_Flow_Setpoint) (c)<br />
### Discharge_Air_Humidity_Sensor:
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Humidity_Sensor:`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Humidity_Sensor](https://brickschema.org/schema/1.0.3/Brick#Air_Humidity_Sensor) (c)<br />
### Discharge_Air_Static_Pressure_Integral_Time_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Static_Pressure_Integral_Time_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Integral_Time_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Integral_Time_Setpoint) (c)<br />
### Discharge_Air_Static_Pressure_Proportional_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Static_Pressure_Proportional_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Proportional_Band_Setpoint) (c)<br />
### Discharge_Air_Static_Pressure_Sensor:
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Static_Pressure_Sensor:`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Sensor](https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Sensor) (c)<br />
### Discharge_Air_Static_Pressure_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Static_Pressure_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Setpoint) (c)<br />
### Discharge_Air_Temperature_Cooling_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Cooling_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Setpoint) (c)<br />
### Discharge_Air_Temperature_Dead_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Dead_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Dead_Band_Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Cooling_Discharge_Air_Temperature_Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Cooling_Discharge_Air_Temperature_Dead_Band_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Heating_Discharge_Air_Temperature_Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Heating_Discharge_Air_Temperature_Dead_Band_Setpoint) (c)<br />
### Discharge_Air_Temperature_Heating_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Heating_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Setpoint) (c)<br />
### Discharge_Air_Temperature_Proportional_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Proportional_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Proportional_Band_Setpoint) (c)<br />
### Discharge_Air_Temperature_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Air_Temperature_Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Preheat_Discharge_Air_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Preheat_Discharge_Air_Temperature_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Heat_Wheel_Discharge_Air_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Heat_Wheel_Discharge_Air_Temperature_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Cooling_Coil_Discharge_Air_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Cooling_Coil_Discharge_Air_Temperature_Sensor) (c)<br />
### Discharge_Air_Temperature_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Temperature_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Air_Temperature_Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Heating_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Heating_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Cooling_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Cooling_Setpoint) (c)<br />
### Discharge_Air_Velocity_Pressure_Sensor:
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Velocity_Pressure_Sensor:`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Velocity_Pressure_Sensor:](https://brickschema.org/schema/1.0.3/Brick#Velocity_Pressure_Sensor:) (c)<br />
### Discharge_Fan_Air_Flow_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Discharge_Fan_Air_Flow_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Fan_Air_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Fan_Air_Flow_Sensor) (c)<br />
### Domestic_Hot_Water_Supply_Temperature_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Domestic_Hot_Water_Supply_Temperature_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Supply_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Supply_Temperature_Sensor) (c)<br />
### Domestic_Hot_Water_Valve
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Domestic_Hot_Water_Valve`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Heating_Valve](https://brickschema.org/schema/1.0.3/Brick#Heating_Valve) (c)<br />
### Domestic_Water
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Domestic_Water`
Description | <p>Tap water for drinking, washing, cooking, and flushing of toliets</p>
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Water](https://brickschema.org/schema/1.0.3/Brick#Water) (c)<br />
### Drive_Ready_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Drive_Ready_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Status](https://brickschema.org/schema/1.0.3/Brick#Status) (c)<br />
### Dual_Band_Mode_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Dual_Band_Mode_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Mode_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Mode_Setpoint) (c)<br />
### Duration_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Duration_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Sensor](https://brickschema.org/schema/1.0.3/Brick#Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Run_Time_Sensor](https://brickschema.org/schema/1.0.3/Brick#Run_Time_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Rain_Duration_Sensor](https://brickschema.org/schema/1.0.3/Brick#Rain_Duration_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#On_Timer_Sensor](https://brickschema.org/schema/1.0.3/Brick#On_Timer_Sensor) (c)<br />
### EconCycle_On_Off_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#EconCycle_On_Off_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#On_Off_Status](https://brickschema.org/schema/1.0.3/Brick#On_Off_Status) (c)<br />
### Economizer
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Economizer`
Description | <p>Device that, on proper variable sensing, initiates control signals or actions to conserve energy. A control system that reduces the mechanical heating and cooling requirement.</p>
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#HVAC](https://brickschema.org/schema/1.0.3/Brick#HVAC) (c)<br />
### Economizer_Damper
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Economizer_Damper`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Damper](https://brickschema.org/schema/1.0.3/Brick#Damper) (c)<br />
### Electric_Current
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Electric_Current`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Current](https://brickschema.org/schema/1.0.3/Brick#Current) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Current_Magnitude](https://brickschema.org/schema/1.0.3/Brick#Current_Magnitude) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Current_Angle](https://brickschema.org/schema/1.0.3/Brick#Current_Angle) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Alternating_Current_Frequency](https://brickschema.org/schema/1.0.3/Brick#Alternating_Current_Frequency) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Current_Total_Harmonic_Distortion](https://brickschema.org/schema/1.0.3/Brick#Current_Total_Harmonic_Distortion) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Current_Imbalance](https://brickschema.org/schema/1.0.3/Brick#Current_Imbalance) (c)<br />
### Electric_Energy
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Electric_Energy`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Energy](https://brickschema.org/schema/1.0.3/Brick#Energy) (c)<br />
### Electric_Power
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Electric_Power`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Power](https://brickschema.org/schema/1.0.3/Brick#Power) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Active_Power](https://brickschema.org/schema/1.0.3/Brick#Active_Power) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Complex_Power](https://brickschema.org/schema/1.0.3/Brick#Complex_Power) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Apparent_Power](https://brickschema.org/schema/1.0.3/Brick#Apparent_Power) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Reactive_Power](https://brickschema.org/schema/1.0.3/Brick#Reactive_Power) (c)<br />
### Electric_Voltage
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Electric_Voltage`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Voltage](https://brickschema.org/schema/1.0.3/Brick#Voltage) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Voltage_Angle](https://brickschema.org/schema/1.0.3/Brick#Voltage_Angle) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Voltage_Imbalance](https://brickschema.org/schema/1.0.3/Brick#Voltage_Imbalance) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Voltage_Magnitude](https://brickschema.org/schema/1.0.3/Brick#Voltage_Magnitude) (c)<br />
### Elevator
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Elevator`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Equipment](https://brickschema.org/schema/1.0.3/Brick#Equipment) (c)<br />
### Emergency_Air_Flow_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Emergency_Air_Flow_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Status](https://brickschema.org/schema/1.0.3/Brick#Status) (c)<br />
### Emergency_Generator_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Emergency_Generator_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Status](https://brickschema.org/schema/1.0.3/Brick#Status) (c)<br />
### Emergency_Power_Off_Activated_By_High_Temperature_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Emergency_Power_Off_Activated_By_High_Temperature_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Emergency_Power_Off_Status](https://brickschema.org/schema/1.0.3/Brick#Emergency_Power_Off_Status) (c)<br />
### Emergency_Power_Off_Activated_By_Leak_Detection_System_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Emergency_Power_Off_Activated_By_Leak_Detection_System_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Emergency_Power_Off_Status](https://brickschema.org/schema/1.0.3/Brick#Emergency_Power_Off_Status) (c)<br />
### Emergency_Power_Off_Enable_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Emergency_Power_Off_Enable_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Emergency_Power_Off_Status](https://brickschema.org/schema/1.0.3/Brick#Emergency_Power_Off_Status) (c)<br />
### Emergency_Power_Off_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Emergency_Power_Off_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Status](https://brickschema.org/schema/1.0.3/Brick#Status) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Emergency_Power_Off_Activated_By_High_Temperature_Status](https://brickschema.org/schema/1.0.3/Brick#Emergency_Power_Off_Activated_By_High_Temperature_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Emergency_Power_Off_Activated_By_Leak_Detection_System_Status](https://brickschema.org/schema/1.0.3/Brick#Emergency_Power_Off_Activated_By_Leak_Detection_System_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Emergency_Power_Off_System_Enable_Status](https://brickschema.org/schema/1.0.3/Brick#Emergency_Power_Off_System_Enable_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Emergency_Power_Off_Enable_Status](https://brickschema.org/schema/1.0.3/Brick#Emergency_Power_Off_Enable_Status) (c)<br />
### Emergency_Power_Off_System_Enable_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Emergency_Power_Off_System_Enable_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Emergency_Power_Off_Status](https://brickschema.org/schema/1.0.3/Brick#Emergency_Power_Off_Status) (c)<br />
### Emergency_Push_Button_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Emergency_Push_Button_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Status](https://brickschema.org/schema/1.0.3/Brick#Status) (c)<br />
### Enable_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Enable_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Status](https://brickschema.org/schema/1.0.3/Brick#Status) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Heat_Exchanger_System_Enable_Status](https://brickschema.org/schema/1.0.3/Brick#Heat_Exchanger_System_Enable_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Run_Enable_Status](https://brickschema.org/schema/1.0.3/Brick#Run_Enable_Status) (c)<br />
### Energy
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Energy`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Quantity](https://brickschema.org/schema/1.0.3/Brick#Quantity) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Electric_Energy](https://brickschema.org/schema/1.0.3/Brick#Electric_Energy) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Thermal_Energy](https://brickschema.org/schema/1.0.3/Brick#Thermal_Energy) (c)<br />
### Energy_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Energy_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Sensor](https://brickschema.org/schema/1.0.3/Brick#Sensor) (c)<br />
### Energy_Storage
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Energy_Storage`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Equipment](https://brickschema.org/schema/1.0.3/Brick#Equipment) (c)<br />
### Entering_Water_Temperature_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Entering_Water_Temperature_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Water_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Water_Temperature_Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Ice_Tank_Entering_Water_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Ice_Tank_Entering_Water_Temperature_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Coil_Entering_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Coil_Entering_Temperature_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#PreHeat_Coil_Entering_Air_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#PreHeat_Coil_Entering_Air_Temperature_Sensor) (c)<br />
### Entering_Water_Temperature_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Entering_Water_Temperature_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Water_Temperature_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Water_Temperature_Setpoint) (c)<br />
### Enthalpy
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Enthalpy`
Description | <p>(also known as heat content), thermodynamic quantity equal to the sum of the internal energy of a system plus the product of the pressure volume work done on the system. H = E + pv, where H = enthalpy or total heat content, E = internal energy of the system, p = pressure, and v = volume. (Compare to [[specific enthalpy]].)</p>
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Quantity](https://brickschema.org/schema/1.0.3/Brick#Quantity) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Substance](https://brickschema.org/schema/1.0.3/Brick#Substance) (c)<br />
### Enthalpy_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Enthalpy_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Sensor](https://brickschema.org/schema/1.0.3/Brick#Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Enthalpy_Sensor](https://brickschema.org/schema/1.0.3/Brick#Air_Enthalpy_Sensor) (c)<br />
### Enthalpy_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Enthalpy_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Setpoint](https://brickschema.org/schema/1.0.3/Brick#Setpoint) (c)<br />
### Environment_Box
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Environment_Box`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Laboratory](https://brickschema.org/schema/1.0.3/Brick#Laboratory) (c)<br />
### Equipment
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Equipment`
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Water_System](https://brickschema.org/schema/1.0.3/Brick#Water_System) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Meter](https://brickschema.org/schema/1.0.3/Brick#Meter) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#PlugStrip](https://brickschema.org/schema/1.0.3/Brick#PlugStrip) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Shading_System](https://brickschema.org/schema/1.0.3/Brick#Shading_System) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#HVAC](https://brickschema.org/schema/1.0.3/Brick#HVAC) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Heating_Ventilation_Air_Conditioning_System](https://brickschema.org/schema/1.0.3/Brick#Heating_Ventilation_Air_Conditioning_System) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Solar_Panel](https://brickschema.org/schema/1.0.3/Brick#Solar_Panel) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Steam_System](https://brickschema.org/schema/1.0.3/Brick#Steam_System) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Weather](https://brickschema.org/schema/1.0.3/Brick#Weather) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Lighting_System](https://brickschema.org/schema/1.0.3/Brick#Lighting_System) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Power_System](https://brickschema.org/schema/1.0.3/Brick#Power_System) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Elevator](https://brickschema.org/schema/1.0.3/Brick#Elevator) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Fire_Safety_System](https://brickschema.org/schema/1.0.3/Brick#Fire_Safety_System) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Furniture](https://brickschema.org/schema/1.0.3/Brick#Furniture) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Energy_Storage](https://brickschema.org/schema/1.0.3/Brick#Energy_Storage) (c)<br />
### Evaporative_Heat_Exchanger
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Evaporative_Heat_Exchanger`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Heat_Exchanger](https://brickschema.org/schema/1.0.3/Brick#Heat_Exchanger) (c)<br />
### Even_Month_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Even_Month_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Status](https://brickschema.org/schema/1.0.3/Brick#Status) (c)<br />
### Exhaust_Air
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air`
Description | <p>air that must be removed from a space due to contaminants, regardless of pressurization</p>
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air](https://brickschema.org/schema/1.0.3/Brick#Air) (c)<br />
### Exhaust_Air_Flow_Integral_Time_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Flow_Integral_Time_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Integral_Time_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Integral_Time_Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Stack_Flow_Integral_Time_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Stack_Flow_Integral_Time_Setpoint) (c)<br />
### Exhaust_Air_Flow_Proportional_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Flow_Proportional_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Proportional_Band_Setpoint) (c)<br />
### Exhaust_Air_Flow_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Flow_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Stack_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Stack_Flow_Sensor) (c)<br />
### Exhaust_Air_Flow_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Flow_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Stack_Flow_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Stack_Flow_Setpoint) (c)<br />
### Exhaust_Air_Humidity_Sensor:
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Humidity_Sensor:`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Humidity_Sensor](https://brickschema.org/schema/1.0.3/Brick#Air_Humidity_Sensor) (c)<br />
### Exhaust_Air_Stack_Flow_Dead_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Stack_Flow_Dead_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Dead_Band_Setpoint) (c)<br />
### Exhaust_Air_Stack_Flow_Integral_Time_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Stack_Flow_Integral_Time_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Flow_Integral_Time_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Flow_Integral_Time_Setpoint) (c)<br />
### Exhaust_Air_Stack_Flow_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Stack_Flow_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Flow_Sensor) (c)<br />
### Exhaust_Air_Stack_Flow_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Stack_Flow_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Flow_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Flow_Setpoint) (c)<br />
### Exhaust_Air_Static_Pressure_Proportional_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Static_Pressure_Proportional_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Proportional_Band_Setpoint) (c)<br />
### Exhaust_Air_Static_Pressure_Sensor:
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Static_Pressure_Sensor:`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Sensor](https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Average_Exhaust_Air_Static_Pressure_Sensor:](https://brickschema.org/schema/1.0.3/Brick#Average_Exhaust_Air_Static_Pressure_Sensor:) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Lowest_Exhaust_Air_Static_Pressure_Sensor:](https://brickschema.org/schema/1.0.3/Brick#Lowest_Exhaust_Air_Static_Pressure_Sensor:) (c)<br />
### Exhaust_Air_Static_Pressure_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Static_Pressure_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Setpoint) (c)<br />
### Exhaust_Air_Temperature_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Temperature_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Air_Temperature_Sensor) (c)<br />
### Exhaust_Air_Velocity_Pressure_Sensor:
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Velocity_Pressure_Sensor:`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Velocity_Pressure_Sensor:](https://brickschema.org/schema/1.0.3/Brick#Velocity_Pressure_Sensor:) (c)<br />
### Exhaust_Damper
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Exhaust_Damper`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Damper](https://brickschema.org/schema/1.0.3/Brick#Damper) (c)<br />
### Exhaust_Fan
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Exhaust_Fan`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Fan](https://brickschema.org/schema/1.0.3/Brick#Fan) (c)<br />
### Fan
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Fan`
Description | <p>Any device with two or more blades or vanes attached to a rotating shaft used to produce an airflow for the purpose of comfort, ventilation, exhaust, heating, cooling, or any other gaseous transport.</p>
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#HVAC](https://brickschema.org/schema/1.0.3/Brick#HVAC) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Standby_Fan](https://brickschema.org/schema/1.0.3/Brick#Standby_Fan) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Exhaust_Fan](https://brickschema.org/schema/1.0.3/Brick#Exhaust_Fan) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Supply_Fan](https://brickschema.org/schema/1.0.3/Brick#Supply_Fan) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Cooling_Tower_Fan](https://brickschema.org/schema/1.0.3/Brick#Cooling_Tower_Fan) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Return_Fan](https://brickschema.org/schema/1.0.3/Brick#Return_Fan) (c)<br />
### Fan_Air_Flow_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Fan_Air_Flow_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Supply_Fan_Air_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Supply_Fan_Air_Flow_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Return_Fan_Air_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Return_Fan_Air_Flow_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Booster_Fan_Air_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Booster_Fan_Air_Flow_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Discharge_Fan_Air_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Discharge_Fan_Air_Flow_Sensor) (c)<br />
### Fan_Air_Flow_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Fan_Air_Flow_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Setpoint) (c)<br />
### Fan_Coil_Unit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Fan_Coil_Unit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Terminal_Unit](https://brickschema.org/schema/1.0.3/Brick#Terminal_Unit) (c)<br />
### Fan_Start_Stop_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Fan_Start_Stop_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Start_Stop_Status](https://brickschema.org/schema/1.0.3/Brick#Start_Stop_Status) (c)<br />
### Fan_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Fan_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Status](https://brickschema.org/schema/1.0.3/Brick#Status) (c)<br />
### Fault_Indicator_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Fault_Indicator_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Status](https://brickschema.org/schema/1.0.3/Brick#Status) (c)<br />
### Fault_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Fault_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Status](https://brickschema.org/schema/1.0.3/Brick#Status) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Humidifier_Fault_Status](https://brickschema.org/schema/1.0.3/Brick#Humidifier_Fault_Status) (c)<br />
### Filter
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Filter`
Description | <p>Device to remove gases from a mixture of gases</p>
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#HVAC](https://brickschema.org/schema/1.0.3/Brick#HVAC) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Mixed_Air_Filter](https://brickschema.org/schema/1.0.3/Brick#Mixed_Air_Filter) (c)<br />
### Filter_Differential_Pressure_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Filter_Differential_Pressure_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Sensor](https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Sensor) (c)<br />
### Filter_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Filter_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Status](https://brickschema.org/schema/1.0.3/Brick#Status) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Pre_Filter_Status](https://brickschema.org/schema/1.0.3/Brick#Pre_Filter_Status) (c)<br />
### Fire_Safety_System
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Fire_Safety_System`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Equipment](https://brickschema.org/schema/1.0.3/Brick#Equipment) (c)<br />
### Fire_Zone
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Fire_Zone`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Zone](https://brickschema.org/schema/1.0.3/Brick#Zone) (c)<br />
### Floor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Floor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Location](https://brickschema.org/schema/1.0.3/Brick#Location) (c)<br />
### Flow
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Flow`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Quantity](https://brickschema.org/schema/1.0.3/Brick#Quantity) (c)<br />
### Flow_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Flow_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Sensor](https://brickschema.org/schema/1.0.3/Brick#Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Water_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Water_Flow_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Sensor) (c)<br />
### Flow_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Flow_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Setpoint](https://brickschema.org/schema/1.0.3/Brick#Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Setpoint) (c)<br />
### Fluid
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Fluid`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Substance](https://brickschema.org/schema/1.0.3/Brick#Substance) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Liquid](https://brickschema.org/schema/1.0.3/Brick#Liquid) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Gas](https://brickschema.org/schema/1.0.3/Brick#Gas) (c)<br />
### Freeze_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Freeze_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Status](https://brickschema.org/schema/1.0.3/Brick#Status) (c)<br />
### Freezer
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Freezer`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Laboratory](https://brickschema.org/schema/1.0.3/Brick#Laboratory) (c)<br />
### Frequency
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Frequency`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Quantity](https://brickschema.org/schema/1.0.3/Brick#Quantity) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Alternating_Current_Frequency](https://brickschema.org/schema/1.0.3/Brick#Alternating_Current_Frequency) (c)<br />
### Frequency_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Frequency_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Sensor](https://brickschema.org/schema/1.0.3/Brick#Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Output_Frequency_Sensor](https://brickschema.org/schema/1.0.3/Brick#Output_Frequency_Sensor) (c)<br />
### Frost
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Frost`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Solid](https://brickschema.org/schema/1.0.3/Brick#Solid) (c)<br />
### Frost_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Frost_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Sensor](https://brickschema.org/schema/1.0.3/Brick#Sensor) (c)<br />
### Fuel_Oil
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Fuel_Oil`
Description | <p>Petroleum based oil burned for energy</p>
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Oil](https://brickschema.org/schema/1.0.3/Brick#Oil) (c)<br />
### Fume_Hood
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Fume_Hood`
Description | <p>A fume-collection device mounted over a work space, table, or shelf and serving to conduct unwanted gases away from the area enclosed.</p>
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#HVAC](https://brickschema.org/schema/1.0.3/Brick#HVAC) (c)<br />
### Fume_Hood_Air_Flow_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Fume_Hood_Air_Flow_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Sensor) (c)<br />
### Furniture
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Furniture`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Equipment](https://brickschema.org/schema/1.0.3/Brick#Equipment) (c)<br />
### Gas
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Gas`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Fluid](https://brickschema.org/schema/1.0.3/Brick#Fluid) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Steam](https://brickschema.org/schema/1.0.3/Brick#Steam) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Air](https://brickschema.org/schema/1.0.3/Brick#Air) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Natural_Gas](https://brickschema.org/schema/1.0.3/Brick#Natural_Gas) (c)<br />
### Gasoline
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Gasoline`
Description | <p>Petroleum derived liquid used as a fuel source</p>
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Liquid](https://brickschema.org/schema/1.0.3/Brick#Liquid) (c)<br />
### Grains
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Grains`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Quantity](https://brickschema.org/schema/1.0.3/Brick#Quantity) (c)<br />
### HVAC
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#HVAC`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Equipment](https://brickschema.org/schema/1.0.3/Brick#Equipment) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Fume_Hood](https://brickschema.org/schema/1.0.3/Brick#Fume_Hood) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#VFD](https://brickschema.org/schema/1.0.3/Brick#VFD) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Pump](https://brickschema.org/schema/1.0.3/Brick#Pump) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Fan](https://brickschema.org/schema/1.0.3/Brick#Fan) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Heat_Exchanger](https://brickschema.org/schema/1.0.3/Brick#Heat_Exchanger) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Terminal_Unit](https://brickschema.org/schema/1.0.3/Brick#Terminal_Unit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Condenser](https://brickschema.org/schema/1.0.3/Brick#Condenser) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#AHU](https://brickschema.org/schema/1.0.3/Brick#AHU) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Thermostat](https://brickschema.org/schema/1.0.3/Brick#Thermostat) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Space_Heater](https://brickschema.org/schema/1.0.3/Brick#Space_Heater) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#CRAC](https://brickschema.org/schema/1.0.3/Brick#CRAC) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Compressor](https://brickschema.org/schema/1.0.3/Brick#Compressor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Computer_Room_Air_Conditioning](https://brickschema.org/schema/1.0.3/Brick#Computer_Room_Air_Conditioning) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Economizer](https://brickschema.org/schema/1.0.3/Brick#Economizer) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Chiller](https://brickschema.org/schema/1.0.3/Brick#Chiller) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Coil](https://brickschema.org/schema/1.0.3/Brick#Coil) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Filter](https://brickschema.org/schema/1.0.3/Brick#Filter) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Boiler](https://brickschema.org/schema/1.0.3/Brick#Boiler) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Air_Handler_Unit](https://brickschema.org/schema/1.0.3/Brick#Air_Handler_Unit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Variable_Frequency_Drive](https://brickschema.org/schema/1.0.3/Brick#Variable_Frequency_Drive) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Valve](https://brickschema.org/schema/1.0.3/Brick#Valve) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Damper](https://brickschema.org/schema/1.0.3/Brick#Damper) (c)<br />
### HVAC_Zone
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#HVAC_Zone`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Zone](https://brickschema.org/schema/1.0.3/Brick#Zone) (c)<br />
### Hail
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Hail`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Solid](https://brickschema.org/schema/1.0.3/Brick#Solid) (c)<br />
### Hail_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Hail_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Sensor](https://brickschema.org/schema/1.0.3/Brick#Sensor) (c)<br />
### Hand_Auto_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Hand_Auto_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Status](https://brickschema.org/schema/1.0.3/Brick#Status) (c)<br />
### Heat_Exchanger
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Heat_Exchanger`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#HVAC](https://brickschema.org/schema/1.0.3/Brick#HVAC) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Condenser_Heat_Exchanger](https://brickschema.org/schema/1.0.3/Brick#Condenser_Heat_Exchanger) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Evaporative_Heat_Exchanger](https://brickschema.org/schema/1.0.3/Brick#Evaporative_Heat_Exchanger) (c)<br />
### Heat_Exchanger_Discharge_Water_Temperature_Proportional_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Heat_Exchanger_Discharge_Water_Temperature_Proportional_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Temperature_Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Temperature_Proportional_Band_Setpoint) (c)<br />
### Heat_Exchanger_Supply_Water_Temperature_Dead_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Heat_Exchanger_Supply_Water_Temperature_Dead_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Temperature_Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Temperature_Dead_Band_Setpoint) (c)<br />
### Heat_Exchanger_Supply_Water_Temperature_Proportional_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Heat_Exchanger_Supply_Water_Temperature_Proportional_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Temperature_Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Temperature_Proportional_Band_Setpoint) (c)<br />
### Heat_Exchanger_Supply_Water_Temperature_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Heat_Exchanger_Supply_Water_Temperature_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Water_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Water_Temperature_Sensor) (c)<br />
### Heat_Exchanger_System_Enable_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Heat_Exchanger_System_Enable_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Enable_Status](https://brickschema.org/schema/1.0.3/Brick#Enable_Status) (c)<br />
### Heat_Wheel_Differential_Pressure_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Heat_Wheel_Differential_Pressure_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Sensor](https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Sensor) (c)<br />
### Heat_Wheel_Discharge_Air_Temperature_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Heat_Wheel_Discharge_Air_Temperature_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Sensor) (c)<br />
### Heat_Wheel_Speed_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Heat_Wheel_Speed_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Differential_Speed_Sensor](https://brickschema.org/schema/1.0.3/Brick#Differential_Speed_Sensor) (c)<br />
### Heat_Wheel_VFD
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Heat_Wheel_VFD`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#VFD](https://brickschema.org/schema/1.0.3/Brick#VFD) (c)<br />
### Heat_Wheel_Voltage_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Heat_Wheel_Voltage_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Voltage_Sensor](https://brickschema.org/schema/1.0.3/Brick#Voltage_Sensor) (c)<br />
### Heating_Coil
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Heating_Coil`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Coil](https://brickschema.org/schema/1.0.3/Brick#Coil) (c)<br />
Has members |[https://brickschema.org/schema/1.0.3/ExampleBuilding#Coil_1](https://brickschema.org/schema/1.0.3/ExampleBuilding#Coil_1)<br />
### Heating_Demand_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Heating_Demand_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Demand_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Demand_Setpoint) (c)<br />
### Heating_Discharge_Air_Flow_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Heating_Discharge_Air_Flow_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Flow_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Flow_Setpoint) (c)<br />
### Heating_Discharge_Air_Temperature_Dead_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Heating_Discharge_Air_Temperature_Dead_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Dead_Band_Setpoint) (c)<br />
### Heating_Discharge_Air_Temperature_Integral_Time_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Heating_Discharge_Air_Temperature_Integral_Time_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Integral_Time_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Integral_Time_Setpoint) (c)<br />
### Heating_Discharge_Air_Temperature_Proportional_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Heating_Discharge_Air_Temperature_Proportional_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Proportional_Band_Setpoint) (c)<br />
### Heating_On_Off_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Heating_On_Off_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#On_Off_Status](https://brickschema.org/schema/1.0.3/Brick#On_Off_Status) (c)<br />
### Heating_Request_Percent_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Heating_Request_Percent_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Demand_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Demand_Setpoint) (c)<br />
### Heating_Request_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Heating_Request_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Demand_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Demand_Setpoint) (c)<br />
### Heating_Supply_Air_Flow_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Heating_Supply_Air_Flow_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Flow_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Flow_Setpoint) (c)<br />
### Heating_Supply_Air_Temperature_Dead_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Heating_Supply_Air_Temperature_Dead_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Temperature_Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Temperature_Dead_Band_Setpoint) (c)<br />
### Heating_Supply_Air_Temperature_Integral_Time_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Heating_Supply_Air_Temperature_Integral_Time_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Integral_Time_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Integral_Time_Setpoint) (c)<br />
### Heating_Supply_Air_Temperature_Proportional_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Heating_Supply_Air_Temperature_Proportional_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Proportional_Band_Setpoint) (c)<br />
### Heating_Valve
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Heating_Valve`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Valve](https://brickschema.org/schema/1.0.3/Brick#Valve) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Reheat_Valve](https://brickschema.org/schema/1.0.3/Brick#Reheat_Valve) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Domestic_Hot_Water_Valve](https://brickschema.org/schema/1.0.3/Brick#Domestic_Hot_Water_Valve) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Preheat_Hot_Water_Valve](https://brickschema.org/schema/1.0.3/Brick#Preheat_Hot_Water_Valve) (c)<br />
### Heating_Ventilation_Air_Conditioning_System
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Heating_Ventilation_Air_Conditioning_System`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Equipment](https://brickschema.org/schema/1.0.3/Brick#Equipment) (c)<br />
### High_Humidity_Alarm_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#High_Humidity_Alarm_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Humidity_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Humidity_Setpoint) (c)<br />
### High_Outside_Air_Lockout_Temperature_Differential_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#High_Outside_Air_Lockout_Temperature_Differential_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Lockout_Temperature_Differential_Sensor](https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Lockout_Temperature_Differential_Sensor) (c)<br />
### High_Static_Pressure_Cutout_Limit_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#High_Static_Pressure_Cutout_Limit_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Setpoint) (c)<br />
### High_Temperature_Hot_Water_Supply_Temperature_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#High_Temperature_Hot_Water_Supply_Temperature_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Supply_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Supply_Temperature_Sensor) (c)<br />
### Highest_Zone_Temperature_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Highest_Zone_Temperature_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Zone_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Zone_Temperature_Sensor) (c)<br />
### Hold_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Hold_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Status](https://brickschema.org/schema/1.0.3/Brick#Status) (c)<br />
### Hot_Box
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Hot_Box`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Laboratory](https://brickschema.org/schema/1.0.3/Brick#Laboratory) (c)<br />
### Hot_Water
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Hot_Water`
Description | <p>Hot water used for HVAC heating or supply to hot taps</p>
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Water](https://brickschema.org/schema/1.0.3/Brick#Water) (c)<br />
### Hot_Water_Coil_Entering_Temperature_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Coil_Entering_Temperature_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Entering_Water_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Entering_Water_Temperature_Sensor) (c)<br />
### Hot_Water_Differential_Pressure_Dead_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Differential_Pressure_Dead_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Dead_Band_Setpoint) (c)<br />
### Hot_Water_Differential_Pressure_Integral_Time_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Differential_Pressure_Integral_Time_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Integral_Time_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Integral_Time_Setpoint) (c)<br />
### Hot_Water_Differential_Pressure_Load_Shed_Reset_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Differential_Pressure_Load_Shed_Reset_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Load_Shed_Status](https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Load_Shed_Status) (c)<br />
### Hot_Water_Differential_Pressure_Load_Shed_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Differential_Pressure_Load_Shed_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Load_Shed_Status](https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Load_Shed_Status) (c)<br />
### Hot_Water_Differential_Pressure_Proportional_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Differential_Pressure_Proportional_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Proportional_Band_Setpoint) (c)<br />
### Hot_Water_Differential_Pressure_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Differential_Pressure_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Sensor](https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Medium_Temperature_Hot_Water_Differential_Pressure_Sensor](https://brickschema.org/schema/1.0.3/Brick#Medium_Temperature_Hot_Water_Differential_Pressure_Sensor) (c)<br />
### Hot_Water_Differential_Pressure_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Differential_Pressure_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Setpoint) (c)<br />
### Hot_Water_Discharge_Temperature_Load_Shed_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Discharge_Temperature_Load_Shed_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Load_Shed_Status](https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Load_Shed_Status) (c)<br />
### Hot_Water_Pump
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Pump`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Water_Pump](https://brickschema.org/schema/1.0.3/Brick#Water_Pump) (c)<br />
### Hot_Water_Return_Temperature_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Return_Temperature_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Return_Water_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Return_Water_Temperature_Sensor) (c)<br />
### Hot_Water_Static_Pressure_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Static_Pressure_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Setpoint) (c)<br />
### Hot_Water_Supply_Temperature_Load_Shed_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Supply_Temperature_Load_Shed_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Load_Shed_Status](https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Load_Shed_Status) (c)<br />
### Hot_Water_Supply_Temperature_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Supply_Temperature_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Water_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Water_Temperature_Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Medium_Temperature_Hot_Water_Supply_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Medium_Temperature_Hot_Water_Supply_Temperature_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#High_Temperature_Hot_Water_Supply_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#High_Temperature_Hot_Water_Supply_Temperature_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Domestic_Hot_Water_Supply_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Domestic_Hot_Water_Supply_Temperature_Sensor) (c)<br />
### Hot_Water_System
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Hot_Water_System`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Water_System](https://brickschema.org/schema/1.0.3/Brick#Water_System) (c)<br />
### Humidification_On_Off_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Humidification_On_Off_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#On_Off_Status](https://brickschema.org/schema/1.0.3/Brick#On_Off_Status) (c)<br />
### Humidifier_Fault_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Humidifier_Fault_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Fault_Status](https://brickschema.org/schema/1.0.3/Brick#Fault_Status) (c)<br />
### Humidity
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Humidity`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Quantity](https://brickschema.org/schema/1.0.3/Brick#Quantity) (c)<br />
### Humidity_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Humidity_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Sensor](https://brickschema.org/schema/1.0.3/Brick#Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Humidity_Sensor](https://brickschema.org/schema/1.0.3/Brick#Air_Humidity_Sensor) (c)<br />
### Humidity_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Humidity_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Setpoint](https://brickschema.org/schema/1.0.3/Brick#Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Low_Humidity_Alarm_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Low_Humidity_Alarm_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#High_Humidity_Alarm_Setpoint](https://brickschema.org/schema/1.0.3/Brick#High_Humidity_Alarm_Setpoint) (c)<br />
### Ice
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Ice`
Description | <p>Water in its solid form</p>
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Solid](https://brickschema.org/schema/1.0.3/Brick#Solid) (c)<br />
### Ice_Tank_Entering_Water_Temperature_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Ice_Tank_Entering_Water_Temperature_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Entering_Water_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Entering_Water_Temperature_Sensor) (c)<br />
### Ice_Tank_Leaving_Water_Temperature_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Ice_Tank_Leaving_Water_Temperature_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Leaving_Water_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Leaving_Water_Temperature_Sensor) (c)<br />
### Illuminance
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Illuminance`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Quantity](https://brickschema.org/schema/1.0.3/Brick#Quantity) (c)<br />
### Increase_Decrease_Step_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Increase_Decrease_Step_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Setpoint](https://brickschema.org/schema/1.0.3/Brick#Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Increase_Decrease_Step_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Increase_Decrease_Step_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Increase_Decrease_Step_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Increase_Decrease_Step_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Temperature_Increase_Decrease_Step_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Temperature_Increase_Decrease_Step_Setpoint) (c)<br />
### Integral_Gain_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Integral_Gain_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Setpoint](https://brickschema.org/schema/1.0.3/Brick#Setpoint) (c)<br />
### Integral_Time_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Integral_Time_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Setpoint](https://brickschema.org/schema/1.0.3/Brick#Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Static_Pressure_Integral_Time_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Static_Pressure_Integral_Time_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Flow_Integral_Time_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Flow_Integral_Time_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Integral_Time](https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Integral_Time) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Heating_Supply_Air_Temperature_Integral_Time_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Heating_Supply_Air_Temperature_Integral_Time_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Differential_Pressure_Integral_Time_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Differential_Pressure_Integral_Time_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Pressure_Integral_Time_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Pressure_Integral_Time_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Integral_Time_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Integral_Time_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Integral_Time_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Integral_Time_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Temperature_Integral_Time_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Temperature_Integral_Time_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Cooling_Discharge_Air_Temperature_Integral_Time_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Cooling_Discharge_Air_Temperature_Integral_Time_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Cooling_Supply_Air_Temperature_Integral_Time_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Cooling_Supply_Air_Temperature_Integral_Time_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Heating_Discharge_Air_Temperature_Integral_Time_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Heating_Discharge_Air_Temperature_Integral_Time_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Static_Pressure_Integral_Time_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Static_Pressure_Integral_Time_Setpoint) (c)<br />
### Interface
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Interface`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Lighting_System](https://brickschema.org/schema/1.0.3/Brick#Lighting_System) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Switch](https://brickschema.org/schema/1.0.3/Brick#Switch) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Touchpanel](https://brickschema.org/schema/1.0.3/Brick#Touchpanel) (c)<br />
### Irradiance
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Irradiance`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Quantity](https://brickschema.org/schema/1.0.3/Brick#Quantity) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Solar_Irradiance](https://brickschema.org/schema/1.0.3/Brick#Solar_Irradiance) (c)<br />
### Isolation_Valve
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Isolation_Valve`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Valve](https://brickschema.org/schema/1.0.3/Brick#Valve) (c)<br />
### Laboratory
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Laboratory`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Room](https://brickschema.org/schema/1.0.3/Brick#Room) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Freezer](https://brickschema.org/schema/1.0.3/Brick#Freezer) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Hot_Box](https://brickschema.org/schema/1.0.3/Brick#Hot_Box) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Environment_Box](https://brickschema.org/schema/1.0.3/Brick#Environment_Box) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Cold_Box](https://brickschema.org/schema/1.0.3/Brick#Cold_Box) (c)<br />
### Last_Fault_Code_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Last_Fault_Code_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Status](https://brickschema.org/schema/1.0.3/Brick#Status) (c)<br />
### Lead_Lag_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Lead_Lag_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Status](https://brickschema.org/schema/1.0.3/Brick#Status) (c)<br />
### Leaving_Water_Temperature_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Leaving_Water_Temperature_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Water_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Water_Temperature_Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Ice_Tank_Leaving_Water_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Ice_Tank_Leaving_Water_Temperature_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#PreHeat_Coil_Leaving_Air_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#PreHeat_Coil_Leaving_Air_Temperature_Sensor) (c)<br />
### Leaving_Water_Temperature_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Leaving_Water_Temperature_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Water_Temperature_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Water_Temperature_Setpoint) (c)<br />
### Level
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Level`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Quantity](https://brickschema.org/schema/1.0.3/Brick#Quantity) (c)<br />
### Lighting
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Lighting`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Lighting_System](https://brickschema.org/schema/1.0.3/Brick#Lighting_System) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Luminaire_Driver](https://brickschema.org/schema/1.0.3/Brick#Luminaire_Driver) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Luminaire](https://brickschema.org/schema/1.0.3/Brick#Luminaire) (c)<br />
### Lighting_System
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Lighting_System`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Equipment](https://brickschema.org/schema/1.0.3/Brick#Equipment) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Lighting](https://brickschema.org/schema/1.0.3/Brick#Lighting) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Interface](https://brickschema.org/schema/1.0.3/Brick#Interface) (c)<br />
### Lighting_Zone
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Lighting_Zone`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Zone](https://brickschema.org/schema/1.0.3/Brick#Zone) (c)<br />
### Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Point](https://brickschema.org/schema/1.0.3/Brick#Point) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Max_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Speed_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Speed_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Min_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Damper_Position_Limit](https://brickschema.org/schema/1.0.3/Brick#Damper_Position_Limit) (c)<br />
### Liquid
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Liquid`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Fluid](https://brickschema.org/schema/1.0.3/Brick#Fluid) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Water](https://brickschema.org/schema/1.0.3/Brick#Water) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Oil](https://brickschema.org/schema/1.0.3/Brick#Oil) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Gasoline](https://brickschema.org/schema/1.0.3/Brick#Gasoline) (c)<br />
### Load_Current_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Load_Current_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Current_Sensor](https://brickschema.org/schema/1.0.3/Brick#Current_Sensor) (c)<br />
### Load_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Load_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Setpoint](https://brickschema.org/schema/1.0.3/Brick#Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Max_Load_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Max_Load_Setpoint) (c)<br />
### Load_Shed_Differential_Pressure_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Load_Shed_Differential_Pressure_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Medium_Temperature_Hot_Water_Differential_Pressure_Load_Shed_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Medium_Temperature_Hot_Water_Differential_Pressure_Load_Shed_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Pressure_Load_Shed_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Pressure_Load_Shed_Setpoint) (c)<br />
### Load_Shed_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Load_Shed_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Status](https://brickschema.org/schema/1.0.3/Brick#Status) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Load_Shed_Status](https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Load_Shed_Status) (c)<br />
### Locally_On_Off_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Locally_On_Off_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#On_Off_Status](https://brickschema.org/schema/1.0.3/Brick#On_Off_Status) (c)<br />
### Location
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Location`
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Roof](https://brickschema.org/schema/1.0.3/Brick#Roof) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Floor](https://brickschema.org/schema/1.0.3/Brick#Floor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Space](https://brickschema.org/schema/1.0.3/Brick#Space) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#City](https://brickschema.org/schema/1.0.3/Brick#City) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Building](https://brickschema.org/schema/1.0.3/Brick#Building) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Basement](https://brickschema.org/schema/1.0.3/Brick#Basement) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Wing](https://brickschema.org/schema/1.0.3/Brick#Wing) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Room](https://brickschema.org/schema/1.0.3/Brick#Room) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Zone](https://brickschema.org/schema/1.0.3/Brick#Zone) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Outside](https://brickschema.org/schema/1.0.3/Brick#Outside) (c)<br />
In domain of |[https://brickschema.org/schema/1.0.3/Brick#isLocationOf](https://brickschema.org/schema/1.0.3/Brick#isLocationOf) (op)<br />
In range of |[https://brickschema.org/schema/1.0.3/Brick#hasLocation](https://brickschema.org/schema/1.0.3/Brick#hasLocation) (op)<br />
### Low_Humidity_Alarm_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Low_Humidity_Alarm_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Humidity_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Humidity_Setpoint) (c)<br />
### Low_Outside_Air_Lockout_Temperature_Differential_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Low_Outside_Air_Lockout_Temperature_Differential_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Lockout_Temperature_Differential_Sensor](https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Lockout_Temperature_Differential_Sensor) (c)<br />
### Low_Outside_Air_Temperature_Enable_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Low_Outside_Air_Temperature_Enable_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Temperature_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Temperature_Setpoint) (c)<br />
### Lowest_Exhaust_Air_Static_Pressure_Sensor:
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Lowest_Exhaust_Air_Static_Pressure_Sensor:`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Static_Pressure_Sensor:](https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Static_Pressure_Sensor:) (c)<br />
### Lowest_Zone_Temperature_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Lowest_Zone_Temperature_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Zone_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Zone_Temperature_Sensor) (c)<br />
### Luminaire
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Luminaire`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Lighting](https://brickschema.org/schema/1.0.3/Brick#Lighting) (c)<br />
### Luminaire_Driver
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Luminaire_Driver`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Lighting](https://brickschema.org/schema/1.0.3/Brick#Lighting) (c)<br />
### Luminance
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Luminance`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Quantity](https://brickschema.org/schema/1.0.3/Brick#Quantity) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Substance](https://brickschema.org/schema/1.0.3/Brick#Substance) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Luminous_Flux](https://brickschema.org/schema/1.0.3/Brick#Luminous_Flux) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Luminous_Intensity](https://brickschema.org/schema/1.0.3/Brick#Luminous_Intensity) (c)<br />
### Luminance_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Luminance_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Sensor](https://brickschema.org/schema/1.0.3/Brick#Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Outside_Luminance_Sensor](https://brickschema.org/schema/1.0.3/Brick#Outside_Luminance_Sensor) (c)<br />
### Luminance_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Luminance_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Setpoint](https://brickschema.org/schema/1.0.3/Brick#Setpoint) (c)<br />
### Luminous_Flux
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Luminous_Flux`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Luminance](https://brickschema.org/schema/1.0.3/Brick#Luminance) (c)<br />
### Luminous_Intensity
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Luminous_Intensity`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Luminance](https://brickschema.org/schema/1.0.3/Brick#Luminance) (c)<br />
### Makeup_Water
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Makeup_Water`
Description | <p>Water used used to makeup water loss through leaks, evaporation, or blowdown</p>
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Water](https://brickschema.org/schema/1.0.3/Brick#Water) (c)<br />
### Manual_Auto_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Manual_Auto_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Status](https://brickschema.org/schema/1.0.3/Brick#Status) (c)<br />
### Max_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Max_Air_Flow_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Max_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Limit) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Max_Heating_Discharge_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Heating_Discharge_Air_Flow_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Max_Heating_Supply_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Heating_Supply_Air_Flow_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Max_Cooling_Supply_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Cooling_Supply_Air_Flow_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Max_Cooling_Discharge_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Cooling_Discharge_Air_Flow_Setpoint_Limit) (c)<br />
### Max_Chilled_Water_Differential_Pressure_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Max_Chilled_Water_Differential_Pressure_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Max_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Limit) (c)<br />
### Max_Cooling_Discharge_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Max_Cooling_Discharge_Air_Flow_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Max_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Air_Flow_Setpoint_Limit) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Max_Occupied_Cooling_Discharge_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Occupied_Cooling_Discharge_Air_Flow_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Max_Unoccupied_Cooling_Discharge_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Unoccupied_Cooling_Discharge_Air_Flow_Setpoint_Limit) (c)<br />
### Max_Cooling_Supply_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Max_Cooling_Supply_Air_Flow_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Max_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Air_Flow_Setpoint_Limit) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Max_Unoccupied_Cooling_Supply_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Unoccupied_Cooling_Supply_Air_Flow_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Max_Occupied_Cooling_Supply_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Occupied_Cooling_Supply_Air_Flow_Setpoint_Limit) (c)<br />
### Max_Damper_Position_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Max_Damper_Position_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Damper_Position_Limit](https://brickschema.org/schema/1.0.3/Brick#Damper_Position_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Max_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Limit) (c)<br />
### Max_Discharge_Air_Static_Pressure_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Max_Discharge_Air_Static_Pressure_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Max_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Max_Static_Pressure_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Static_Pressure_Setpoint_Limit) (c)<br />
### Max_Heating_Discharge_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Max_Heating_Discharge_Air_Flow_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Max_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Air_Flow_Setpoint_Limit) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Max_Unoccupied_Heating_Discharge_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Unoccupied_Heating_Discharge_Air_Flow_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Max_Occupied_Heating_Discharge_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Occupied_Heating_Discharge_Air_Flow_Setpoint_Limit) (c)<br />
### Max_Heating_Supply_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Max_Heating_Supply_Air_Flow_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Max_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Air_Flow_Setpoint_Limit) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Max_Unoccupied_Heating_Supply_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Unoccupied_Heating_Supply_Air_Flow_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Max_Occupied_Heating_Supply_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Occupied_Heating_Supply_Air_Flow_Setpoint_Limit) (c)<br />
### Max_Hot_Water_Differential_Pressure_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Max_Hot_Water_Differential_Pressure_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Max_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Setpoint_Limit) (c)<br />
### Max_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Max_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Limit](https://brickschema.org/schema/1.0.3/Brick#Limit) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Max_Discharge_Air_Static_Pressure_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Discharge_Air_Static_Pressure_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Max_Static_Pressure_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Static_Pressure_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Max_Damper_Position_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Damper_Position_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Max_Supply_Air_Static_Pressure_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Supply_Air_Static_Pressure_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Max_Hot_Water_Differential_Pressure_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Hot_Water_Differential_Pressure_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Max_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Air_Flow_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Max_Chilled_Water_Differential_Pressure_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Chilled_Water_Differential_Pressure_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Max_Speed_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Speed_Setpoint_Limit) (c)<br />
### Max_Load_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Max_Load_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Load_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Load_Setpoint) (c)<br />
### Max_Occupied_Cooling_Discharge_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Max_Occupied_Cooling_Discharge_Air_Flow_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Max_Cooling_Discharge_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Cooling_Discharge_Air_Flow_Setpoint_Limit) (c)<br />
### Max_Occupied_Cooling_Supply_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Max_Occupied_Cooling_Supply_Air_Flow_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Max_Cooling_Supply_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Cooling_Supply_Air_Flow_Setpoint_Limit) (c)<br />
### Max_Occupied_Heating_Discharge_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Max_Occupied_Heating_Discharge_Air_Flow_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Max_Heating_Discharge_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Heating_Discharge_Air_Flow_Setpoint_Limit) (c)<br />
### Max_Occupied_Heating_Supply_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Max_Occupied_Heating_Supply_Air_Flow_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Max_Heating_Supply_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Heating_Supply_Air_Flow_Setpoint_Limit) (c)<br />
### Max_Return_Air_CO2_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Max_Return_Air_CO2_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Return_Air_CO2_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Return_Air_CO2_Setpoint) (c)<br />
### Max_Speed_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Max_Speed_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Speed_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Speed_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Max_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Limit) (c)<br />
### Max_Static_Pressure_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Max_Static_Pressure_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Max_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Setpoint_Limit) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Max_Supply_Air_Static_Pressure_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Supply_Air_Static_Pressure_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Max_Discharge_Air_Static_Pressure_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Discharge_Air_Static_Pressure_Setpoint_Limit) (c)<br />
### Max_Supply_Air_Static_Pressure_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Max_Supply_Air_Static_Pressure_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Max_Static_Pressure_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Static_Pressure_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Max_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Limit) (c)<br />
### Max_Unoccupied_Cooling_Discharge_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Max_Unoccupied_Cooling_Discharge_Air_Flow_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Max_Cooling_Discharge_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Cooling_Discharge_Air_Flow_Setpoint_Limit) (c)<br />
### Max_Unoccupied_Cooling_Supply_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Max_Unoccupied_Cooling_Supply_Air_Flow_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Max_Cooling_Supply_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Cooling_Supply_Air_Flow_Setpoint_Limit) (c)<br />
### Max_Unoccupied_Heating_Discharge_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Max_Unoccupied_Heating_Discharge_Air_Flow_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Max_Heating_Discharge_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Heating_Discharge_Air_Flow_Setpoint_Limit) (c)<br />
### Max_Unoccupied_Heating_Supply_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Max_Unoccupied_Heating_Supply_Air_Flow_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Max_Heating_Supply_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Heating_Supply_Air_Flow_Setpoint_Limit) (c)<br />
### Medium_Temperature_Hot_Water_Differential_Pressure_Load_Shed_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Medium_Temperature_Hot_Water_Differential_Pressure_Load_Shed_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Load_Shed_Differential_Pressure_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Load_Shed_Differential_Pressure_Setpoint) (c)<br />
### Medium_Temperature_Hot_Water_Differential_Pressure_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Medium_Temperature_Hot_Water_Differential_Pressure_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Differential_Pressure_Sensor](https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Differential_Pressure_Sensor) (c)<br />
### Medium_Temperature_Hot_Water_Supply_Temperature_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Medium_Temperature_Hot_Water_Supply_Temperature_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Supply_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Supply_Temperature_Sensor) (c)<br />
### Meter
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Meter`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Equipment](https://brickschema.org/schema/1.0.3/Brick#Equipment) (c)<br />
### Min_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Min_Air_Flow_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Min_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Setpoint_Limit) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Min_Cooling_Discharge_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Cooling_Discharge_Air_Flow_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Min_Heating_Discharge_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Heating_Discharge_Air_Flow_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Min_Cooling_Supply_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Cooling_Supply_Air_Flow_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Min_Heating_Supply_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Heating_Supply_Air_Flow_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Min_Outside_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Outside_Air_Flow_Setpoint_Limit) (c)<br />
### Min_Chilled_Water_Differential_Pressure_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Min_Chilled_Water_Differential_Pressure_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Min_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Limit) (c)<br />
### Min_Cooling_Discharge_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Min_Cooling_Discharge_Air_Flow_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Min_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Air_Flow_Setpoint_Limit) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Min_Occupied_Cooling_Discharge_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Occupied_Cooling_Discharge_Air_Flow_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Min_Unoccupied_Cooling_Discharge_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Unoccupied_Cooling_Discharge_Air_Flow_Setpoint_Limit) (c)<br />
### Min_Cooling_Supply_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Min_Cooling_Supply_Air_Flow_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Min_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Air_Flow_Setpoint_Limit) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Min_Occupied_Cooling_Supply_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Occupied_Cooling_Supply_Air_Flow_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Min_Unoccupied_Cooling_Supply_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Unoccupied_Cooling_Supply_Air_Flow_Setpoint_Limit) (c)<br />
### Min_Damper_Position_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Min_Damper_Position_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Min_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Damper_Position_Limit](https://brickschema.org/schema/1.0.3/Brick#Damper_Position_Limit) (c)<br />
### Min_Discharge_Air_Static_Pressure_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Min_Discharge_Air_Static_Pressure_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Min_Static_Pressure_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Static_Pressure_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Min_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Limit) (c)<br />
### Min_Heating_Discharge_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Min_Heating_Discharge_Air_Flow_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Min_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Air_Flow_Setpoint_Limit) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Min_Occupied_Heating_Discharge_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Occupied_Heating_Discharge_Air_Flow_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Min_Unoccupied_Heating_Discharge_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Unoccupied_Heating_Discharge_Air_Flow_Setpoint_Limit) (c)<br />
### Min_Heating_Supply_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Min_Heating_Supply_Air_Flow_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Min_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Air_Flow_Setpoint_Limit) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Min_Unoccupied_Heating_Supply_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Unoccupied_Heating_Supply_Air_Flow_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Min_Occupied_Heating_Supply_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Occupied_Heating_Supply_Air_Flow_Setpoint_Limit) (c)<br />
### Min_Hot_Water_Differential_Pressure_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Min_Hot_Water_Differential_Pressure_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Min_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Limit) (c)<br />
### Min_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Min_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Limit](https://brickschema.org/schema/1.0.3/Brick#Limit) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Min_Discharge_Air_Static_Pressure_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Discharge_Air_Static_Pressure_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Min_Static_Pressure_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Static_Pressure_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Min_Damper_Position_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Damper_Position_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Min_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Air_Flow_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Min_Hot_Water_Differential_Pressure_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Hot_Water_Differential_Pressure_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Min_Speed_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Speed_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Min_Supply_Air_Static_Pressure_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Supply_Air_Static_Pressure_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Min_Chilled_Water_Differential_Pressure_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Chilled_Water_Differential_Pressure_Setpoint_Limit) (c)<br />
### Min_Occupied_Cooling_Discharge_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Min_Occupied_Cooling_Discharge_Air_Flow_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Min_Cooling_Discharge_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Cooling_Discharge_Air_Flow_Setpoint_Limit) (c)<br />
### Min_Occupied_Cooling_Supply_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Min_Occupied_Cooling_Supply_Air_Flow_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Min_Cooling_Supply_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Cooling_Supply_Air_Flow_Setpoint_Limit) (c)<br />
### Min_Occupied_Heating_Discharge_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Min_Occupied_Heating_Discharge_Air_Flow_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Min_Heating_Discharge_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Heating_Discharge_Air_Flow_Setpoint_Limit) (c)<br />
### Min_Occupied_Heating_Supply_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Min_Occupied_Heating_Supply_Air_Flow_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Min_Heating_Supply_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Heating_Supply_Air_Flow_Setpoint_Limit) (c)<br />
### Min_Outside_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Min_Outside_Air_Flow_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Min_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Air_Flow_Setpoint_Limit) (c)<br />
### Min_Speed_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Min_Speed_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Speed_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Speed_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Min_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Limit) (c)<br />
### Min_Static_Pressure_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Min_Static_Pressure_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Min_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Setpoint_Limit) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Min_Discharge_Air_Static_Pressure_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Discharge_Air_Static_Pressure_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Min_Supply_Air_Static_Pressure_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Supply_Air_Static_Pressure_Setpoint_Limit) (c)<br />
### Min_Supply_Air_Static_Pressure_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Min_Supply_Air_Static_Pressure_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Min_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Min_Static_Pressure_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Static_Pressure_Setpoint_Limit) (c)<br />
### Min_Unoccupied_Cooling_Discharge_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Min_Unoccupied_Cooling_Discharge_Air_Flow_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Min_Cooling_Discharge_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Cooling_Discharge_Air_Flow_Setpoint_Limit) (c)<br />
### Min_Unoccupied_Cooling_Supply_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Min_Unoccupied_Cooling_Supply_Air_Flow_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Min_Cooling_Supply_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Cooling_Supply_Air_Flow_Setpoint_Limit) (c)<br />
### Min_Unoccupied_Heating_Discharge_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Min_Unoccupied_Heating_Discharge_Air_Flow_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Min_Heating_Discharge_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Heating_Discharge_Air_Flow_Setpoint_Limit) (c)<br />
### Min_Unoccupied_Heating_Supply_Air_Flow_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Min_Unoccupied_Heating_Supply_Air_Flow_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Min_Heating_Supply_Air_Flow_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Heating_Supply_Air_Flow_Setpoint_Limit) (c)<br />
### Mixed_Air
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Mixed_Air`
Description | <p>(1) air that contains two or more streams of air. (2) combined outdoor air and recirculated air.</p>
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air](https://brickschema.org/schema/1.0.3/Brick#Air) (c)<br />
### Mixed_Air_Filter
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Mixed_Air_Filter`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Filter](https://brickschema.org/schema/1.0.3/Brick#Filter) (c)<br />
### Mixed_Air_Temperature_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Mixed_Air_Temperature_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Air_Temperature_Sensor) (c)<br />
### Mixed_Air_Temperature_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Mixed_Air_Temperature_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Temperature_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Air_Temperature_Setpoint) (c)<br />
### Mode_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Mode_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Setpoint](https://brickschema.org/schema/1.0.3/Brick#Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Dual_Band_Mode_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Dual_Band_Mode_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Unoccupied_Mode_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Unoccupied_Mode_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Occupied_Mode_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Occupied_Mode_Setpoint) (c)<br />
### Mode_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Mode_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Status](https://brickschema.org/schema/1.0.3/Brick#Status) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Occupied_Mode_Status](https://brickschema.org/schema/1.0.3/Brick#Occupied_Mode_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#System_Mode_Status](https://brickschema.org/schema/1.0.3/Brick#System_Mode_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Operating_Mode_Status](https://brickschema.org/schema/1.0.3/Brick#Operating_Mode_Status) (c)<br />
### Motion_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Motion_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Sensor](https://brickschema.org/schema/1.0.3/Brick#Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#PIR_Sensor](https://brickschema.org/schema/1.0.3/Brick#PIR_Sensor) (c)<br />
### Motor_Current_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Motor_Current_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Current_Sensor](https://brickschema.org/schema/1.0.3/Brick#Current_Sensor) (c)<br />
### Motor_Direction_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Motor_Direction_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Direction_Status](https://brickschema.org/schema/1.0.3/Brick#Direction_Status) (c)<br />
### Motor_Speed_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Motor_Speed_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Speed_Sensor](https://brickschema.org/schema/1.0.3/Brick#Speed_Sensor) (c)<br />
### Motor_Start_Stop_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Motor_Start_Stop_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Start_Stop_Status](https://brickschema.org/schema/1.0.3/Brick#Start_Stop_Status) (c)<br />
### Motor_Torque_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Motor_Torque_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Torque_Sensor](https://brickschema.org/schema/1.0.3/Brick#Torque_Sensor) (c)<br />
### Natural_Gas
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Natural_Gas`
Description | <p>Fossil fuel energy source consisting largely of methane and other hydrocarbons</p>
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Gas](https://brickschema.org/schema/1.0.3/Brick#Gas) (c)<br />
### Occupancy_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Occupancy_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Sensor](https://brickschema.org/schema/1.0.3/Brick#Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#PIR_Sensor](https://brickschema.org/schema/1.0.3/Brick#PIR_Sensor) (c)<br />
### Occupancy_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Occupancy_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Status](https://brickschema.org/schema/1.0.3/Brick#Status) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Temporary_Occupancy_Status](https://brickschema.org/schema/1.0.3/Brick#Temporary_Occupancy_Status) (c)<br />
### Occupied_Cooling_Supply_Air_Flow_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Occupied_Cooling_Supply_Air_Flow_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Occupied_Supply_Air_Flow_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Occupied_Supply_Air_Flow_Setpoint) (c)<br />
### Occupied_Cooling_Temperature_Dead_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Occupied_Cooling_Temperature_Dead_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Temperature_Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Temperature_Dead_Band_Setpoint) (c)<br />
### Occupied_Heating_Supply_Air_Flow_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Occupied_Heating_Supply_Air_Flow_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Occupied_Supply_Air_Flow_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Occupied_Supply_Air_Flow_Setpoint) (c)<br />
### Occupied_Heating_Temperature_Dead_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Occupied_Heating_Temperature_Dead_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Temperature_Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Temperature_Dead_Band_Setpoint) (c)<br />
### Occupied_Mode_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Occupied_Mode_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Mode_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Mode_Setpoint) (c)<br />
### Occupied_Mode_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Occupied_Mode_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Mode_Status](https://brickschema.org/schema/1.0.3/Brick#Mode_Status) (c)<br />
### Occupied_Supply_Air_Flow_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Occupied_Supply_Air_Flow_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Flow_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Flow_Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Occupied_Heating_Supply_Air_Flow_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Occupied_Heating_Supply_Air_Flow_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Occupied_Cooling_Supply_Air_Flow_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Occupied_Cooling_Supply_Air_Flow_Setpoint) (c)<br />
### Off_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Off_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Status](https://brickschema.org/schema/1.0.3/Brick#Status) (c)<br />
### Oil
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Oil`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Liquid](https://brickschema.org/schema/1.0.3/Brick#Liquid) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Fuel_Oil](https://brickschema.org/schema/1.0.3/Brick#Fuel_Oil) (c)<br />
### On_Off_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#On_Off_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Status](https://brickschema.org/schema/1.0.3/Brick#Status) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Standby_Unit_On_Off_Status](https://brickschema.org/schema/1.0.3/Brick#Standby_Unit_On_Off_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Heating_On_Off_Status](https://brickschema.org/schema/1.0.3/Brick#Heating_On_Off_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Locally_On_Off_Status](https://brickschema.org/schema/1.0.3/Brick#Locally_On_Off_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Cooling_On_Off_Status](https://brickschema.org/schema/1.0.3/Brick#Cooling_On_Off_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Remotely_On_Off_Status](https://brickschema.org/schema/1.0.3/Brick#Remotely_On_Off_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#EconCycle_On_Off_Status](https://brickschema.org/schema/1.0.3/Brick#EconCycle_On_Off_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Standby_Glycool_Unit_On_Off_Status](https://brickschema.org/schema/1.0.3/Brick#Standby_Glycool_Unit_On_Off_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Humidification_On_Off_Status](https://brickschema.org/schema/1.0.3/Brick#Humidification_On_Off_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Dehumidification_On_Off_Status](https://brickschema.org/schema/1.0.3/Brick#Dehumidification_On_Off_Status) (c)<br />
### On_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#On_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Status](https://brickschema.org/schema/1.0.3/Brick#Status) (c)<br />
### On_Timer_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#On_Timer_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Duration_Sensor](https://brickschema.org/schema/1.0.3/Brick#Duration_Sensor) (c)<br />
### Open_Heating_Valve_Outside_Air_Temperature_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Open_Heating_Valve_Outside_Air_Temperature_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Temperature_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Temperature_Setpoint) (c)<br />
### Operating_Mode_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Operating_Mode_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Mode_Status](https://brickschema.org/schema/1.0.3/Brick#Mode_Status) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Vent_Operating_Mode_Status](https://brickschema.org/schema/1.0.3/Brick#Vent_Operating_Mode_Status) (c)<br />
### Operative_Temperature
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Operative_Temperature`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Temperature](https://brickschema.org/schema/1.0.3/Brick#Temperature) (c)<br />
### Output_Frequency_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Output_Frequency_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Frequency_Sensor](https://brickschema.org/schema/1.0.3/Brick#Frequency_Sensor) (c)<br />
### Output_Voltage_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Output_Voltage_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Voltage_Sensor](https://brickschema.org/schema/1.0.3/Brick#Voltage_Sensor) (c)<br />
### Outside
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Outside`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Location](https://brickschema.org/schema/1.0.3/Brick#Location) (c)<br />
### Outside_Air
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Outside_Air`
Description | <p>air external to a defined zone (e.g., corridors).</p>
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air](https://brickschema.org/schema/1.0.3/Brick#Air) (c)<br />
### Outside_Air_CO2_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Outside_Air_CO2_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#CO2_Sensor](https://brickschema.org/schema/1.0.3/Brick#CO2_Sensor) (c)<br />
### Outside_Air_Dewpoint_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Dewpoint_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Dewpoint_Sensor](https://brickschema.org/schema/1.0.3/Brick#Dewpoint_Sensor) (c)<br />
### Outside_Air_Enthalpy_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Enthalpy_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Enthalpy_Sensor](https://brickschema.org/schema/1.0.3/Brick#Air_Enthalpy_Sensor) (c)<br />
### Outside_Air_Flow_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Flow_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Sensor) (c)<br />
### Outside_Air_Flow_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Flow_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Setpoint) (c)<br />
### Outside_Air_Grains_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Grains_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Grains_Sensor](https://brickschema.org/schema/1.0.3/Brick#Air_Grains_Sensor) (c)<br />
### Outside_Air_Humidity_Sensor:
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Humidity_Sensor:`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Humidity_Sensor](https://brickschema.org/schema/1.0.3/Brick#Air_Humidity_Sensor) (c)<br />
### Outside_Air_Lockout_Temperature_Differential_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Lockout_Temperature_Differential_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Temperature_Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#High_Outside_Air_Lockout_Temperature_Differential_Sensor](https://brickschema.org/schema/1.0.3/Brick#High_Outside_Air_Lockout_Temperature_Differential_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Low_Outside_Air_Lockout_Temperature_Differential_Sensor](https://brickschema.org/schema/1.0.3/Brick#Low_Outside_Air_Lockout_Temperature_Differential_Sensor) (c)<br />
### Outside_Air_Lockout_Temperature_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Lockout_Temperature_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Temperature_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Temperature_Setpoint) (c)<br />
### Outside_Air_Temperature_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Temperature_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Air_Temperature_Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Lockout_Temperature_Differential_Sensor](https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Lockout_Temperature_Differential_Sensor) (c)<br />
### Outside_Air_Temperature_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Temperature_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Temperature_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Air_Temperature_Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Lockout_Temperature_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Outside_Air_Lockout_Temperature_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Low_Outside_Air_Temperature_Enable_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Low_Outside_Air_Temperature_Enable_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Open_Heating_Valve_Outside_Air_Temperature_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Open_Heating_Valve_Outside_Air_Temperature_Setpoint) (c)<br />
### Outside_Damper
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Outside_Damper`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Damper](https://brickschema.org/schema/1.0.3/Brick#Damper) (c)<br />
### Outside_Luminance_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Outside_Luminance_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Luminance_Sensor](https://brickschema.org/schema/1.0.3/Brick#Luminance_Sensor) (c)<br />
### Overridden_Off_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Overridden_Off_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Overridden_Status](https://brickschema.org/schema/1.0.3/Brick#Overridden_Status) (c)<br />
### Overridden_On_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Overridden_On_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Overridden_Status](https://brickschema.org/schema/1.0.3/Brick#Overridden_Status) (c)<br />
### Overridden_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Overridden_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Status](https://brickschema.org/schema/1.0.3/Brick#Status) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Overridden_On_Status](https://brickschema.org/schema/1.0.3/Brick#Overridden_On_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Overridden_Off_Status](https://brickschema.org/schema/1.0.3/Brick#Overridden_Off_Status) (c)<br />
### PIR_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#PIR_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Occupancy_Sensor](https://brickschema.org/schema/1.0.3/Brick#Occupancy_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Motion_Sensor](https://brickschema.org/schema/1.0.3/Brick#Motion_Sensor) (c)<br />
### PM10
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#PM10`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Quality](https://brickschema.org/schema/1.0.3/Brick#Air_Quality) (c)<br />
### PM25
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#PM25`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Quality](https://brickschema.org/schema/1.0.3/Brick#Air_Quality) (c)<br />
### Peak_Power_Demand_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Peak_Power_Demand_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Demand_Sensor](https://brickschema.org/schema/1.0.3/Brick#Demand_Sensor) (c)<br />
### Photovoltaic_Current_Output_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Photovoltaic_Current_Output_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Current_Sensor](https://brickschema.org/schema/1.0.3/Brick#Current_Sensor) (c)<br />
### Piezoelectric_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Piezoelectric_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Sensor](https://brickschema.org/schema/1.0.3/Brick#Sensor) (c)<br />
### PlugStrip
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#PlugStrip`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Equipment](https://brickschema.org/schema/1.0.3/Brick#Equipment) (c)<br />
### Point
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Point`
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Limit](https://brickschema.org/schema/1.0.3/Brick#Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Status](https://brickschema.org/schema/1.0.3/Brick#Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Setpoint](https://brickschema.org/schema/1.0.3/Brick#Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Sensor](https://brickschema.org/schema/1.0.3/Brick#Sensor) (c)<br />
In domain of |[https://brickschema.org/schema/1.0.3/Brick#isPointOf](https://brickschema.org/schema/1.0.3/Brick#isPointOf) (op)<br />[https://brickschema.org/schema/1.0.3/Brick#measures](https://brickschema.org/schema/1.0.3/Brick#measures) (op)<br />
In range of |[https://brickschema.org/schema/1.0.3/Brick#hasPoint](https://brickschema.org/schema/1.0.3/Brick#hasPoint) (op)<br />[https://brickschema.org/schema/1.0.3/Brick#isMeasuredBy](https://brickschema.org/schema/1.0.3/Brick#isMeasuredBy) (op)<br />
### Power
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Power`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Quantity](https://brickschema.org/schema/1.0.3/Brick#Quantity) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Electric_Power](https://brickschema.org/schema/1.0.3/Brick#Electric_Power) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Thermal_Power](https://brickschema.org/schema/1.0.3/Brick#Thermal_Power) (c)<br />
### Power_Factor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Power_Factor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Quantity](https://brickschema.org/schema/1.0.3/Brick#Quantity) (c)<br />
### Power_System
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Power_System`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Equipment](https://brickschema.org/schema/1.0.3/Brick#Equipment) (c)<br />
### PreHeat_Coil_Entering_Air_Temperature_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#PreHeat_Coil_Entering_Air_Temperature_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Entering_Water_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Entering_Water_Temperature_Sensor) (c)<br />
### PreHeat_Coil_Leaving_Air_Temperature_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#PreHeat_Coil_Leaving_Air_Temperature_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Leaving_Water_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Leaving_Water_Temperature_Sensor) (c)<br />
### Pre_Filter_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Pre_Filter_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Filter_Status](https://brickschema.org/schema/1.0.3/Brick#Filter_Status) (c)<br />
### Precipitation
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Precipitation`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Quantity](https://brickschema.org/schema/1.0.3/Brick#Quantity) (c)<br />
### Preheat_Demand_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Preheat_Demand_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Demand_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Demand_Setpoint) (c)<br />
### Preheat_Discharge_Air_Temperature_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Preheat_Discharge_Air_Temperature_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Sensor) (c)<br />
### Preheat_Hot_Water_Valve
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Preheat_Hot_Water_Valve`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Heating_Valve](https://brickschema.org/schema/1.0.3/Brick#Heating_Valve) (c)<br />
### Preheat_Valve_VFD
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Preheat_Valve_VFD`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#VFD](https://brickschema.org/schema/1.0.3/Brick#VFD) (c)<br />
### Pressure
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Pressure`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Quantity](https://brickschema.org/schema/1.0.3/Brick#Quantity) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Static_Pressure](https://brickschema.org/schema/1.0.3/Brick#Static_Pressure) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Atmospheric_Pressure](https://brickschema.org/schema/1.0.3/Brick#Atmospheric_Pressure) (c)<br />
### Pressure_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Pressure_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Sensor](https://brickschema.org/schema/1.0.3/Brick#Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Velocity_Pressure_Sensor:](https://brickschema.org/schema/1.0.3/Brick#Velocity_Pressure_Sensor:) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Sensor](https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Sensor](https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Sensor) (c)<br />
### Pressure_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Pressure_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Setpoint](https://brickschema.org/schema/1.0.3/Brick#Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Velocity_Pressure_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Velocity_Pressure_Setpoint) (c)<br />
### Pressure_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Pressure_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Status](https://brickschema.org/schema/1.0.3/Brick#Status) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Duct_Pressure_Status](https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Duct_Pressure_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Duct_Pressure_Status](https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Duct_Pressure_Status) (c)<br />
### Proportional_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Proportional_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Setpoint](https://brickschema.org/schema/1.0.3/Brick#Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Proportional_Band_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Heating_Supply_Air_Temperature_Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Heating_Supply_Air_Temperature_Proportional_Band_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Pressure_Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Differential_Pressure_Proportional_Band_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Differential_Pressure_Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Differential_Pressure_Proportional_Band_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Proportional_Band](https://brickschema.org/schema/1.0.3/Brick#Differential_Pressure_Proportional_Band) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Flow_Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Flow_Proportional_Band_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Static_Pressure_Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Static_Pressure_Proportional_Band_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Static_Pressure_Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Static_Pressure_Proportional_Band_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Differential_Pressure_Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Differential_Pressure_Proportional_Band_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Cooling_Supply_Air_Temperature_Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Cooling_Supply_Air_Temperature_Proportional_Band_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Cooling_Discharge_Air_Temperature_Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Cooling_Discharge_Air_Temperature_Proportional_Band_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Temperature_Proportional_Band_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Temperature_Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Temperature_Proportional_Band_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Temperature_Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Temperature_Proportional_Band_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Heating_Discharge_Air_Temperature_Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Heating_Discharge_Air_Temperature_Proportional_Band_Setpoint) (c)<br />
### Pump
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Pump`
Description | <p>Machine for imparting energy to a fluid, causing it to do work, drawing a fluid into itself through an entrance port, and forcing the fluid out through an exhaust port.</p>
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#HVAC](https://brickschema.org/schema/1.0.3/Brick#HVAC) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Water_Pump](https://brickschema.org/schema/1.0.3/Brick#Water_Pump) (c)<br />
### Pump_Start_Stop_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Pump_Start_Stop_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Start_Stop_Status](https://brickschema.org/schema/1.0.3/Brick#Start_Stop_Status) (c)<br />
### Quantity
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Quantity`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Quantity](https://brickschema.org/schema/1.0.3/Brick#Quantity) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Enthalpy](https://brickschema.org/schema/1.0.3/Brick#Enthalpy) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Speed](https://brickschema.org/schema/1.0.3/Brick#Speed) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Quantity](https://brickschema.org/schema/1.0.3/Brick#Quantity) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Dewpoint](https://brickschema.org/schema/1.0.3/Brick#Dewpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Frequency](https://brickschema.org/schema/1.0.3/Brick#Frequency) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Flow](https://brickschema.org/schema/1.0.3/Brick#Flow) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Precipitation](https://brickschema.org/schema/1.0.3/Brick#Precipitation) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Energy](https://brickschema.org/schema/1.0.3/Brick#Energy) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Luminance](https://brickschema.org/schema/1.0.3/Brick#Luminance) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Temperature](https://brickschema.org/schema/1.0.3/Brick#Temperature) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Current](https://brickschema.org/schema/1.0.3/Brick#Current) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Voltage](https://brickschema.org/schema/1.0.3/Brick#Voltage) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Level](https://brickschema.org/schema/1.0.3/Brick#Level) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Humidity](https://brickschema.org/schema/1.0.3/Brick#Humidity) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Weather_Condition](https://brickschema.org/schema/1.0.3/Brick#Weather_Condition) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Conductivity](https://brickschema.org/schema/1.0.3/Brick#Conductivity) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Capacity](https://brickschema.org/schema/1.0.3/Brick#Capacity) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Pressure](https://brickschema.org/schema/1.0.3/Brick#Pressure) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Daytime](https://brickschema.org/schema/1.0.3/Brick#Daytime) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Cloudage](https://brickschema.org/schema/1.0.3/Brick#Cloudage) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Irradiance](https://brickschema.org/schema/1.0.3/Brick#Irradiance) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Air_Quality](https://brickschema.org/schema/1.0.3/Brick#Air_Quality) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Power_Factor](https://brickschema.org/schema/1.0.3/Brick#Power_Factor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Power](https://brickschema.org/schema/1.0.3/Brick#Power) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Illuminance](https://brickschema.org/schema/1.0.3/Brick#Illuminance) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Direction](https://brickschema.org/schema/1.0.3/Brick#Direction) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Grains](https://brickschema.org/schema/1.0.3/Brick#Grains) (c)<br />
### Radiant_Temperature
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Radiant_Temperature`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Temperature](https://brickschema.org/schema/1.0.3/Brick#Temperature) (c)<br />
### Rain_Duration_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Rain_Duration_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Rain_Sensor](https://brickschema.org/schema/1.0.3/Brick#Rain_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Duration_Sensor](https://brickschema.org/schema/1.0.3/Brick#Duration_Sensor) (c)<br />
### Rain_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Rain_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Sensor](https://brickschema.org/schema/1.0.3/Brick#Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Rain_Duration_Sensor](https://brickschema.org/schema/1.0.3/Brick#Rain_Duration_Sensor) (c)<br />
### Reactive_Power
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Reactive_Power`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Electric_Power](https://brickschema.org/schema/1.0.3/Brick#Electric_Power) (c)<br />
### Reheat_Valve
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Reheat_Valve`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Heating_Valve](https://brickschema.org/schema/1.0.3/Brick#Heating_Valve) (c)<br />
### Relative_Humidity_Sensor:
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Relative_Humidity_Sensor:`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Humidity_Sensor](https://brickschema.org/schema/1.0.3/Brick#Air_Humidity_Sensor) (c)<br />
### Remotely_On_Off_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Remotely_On_Off_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#On_Off_Status](https://brickschema.org/schema/1.0.3/Brick#On_Off_Status) (c)<br />
### Reset_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Reset_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Setpoint](https://brickschema.org/schema/1.0.3/Brick#Setpoint) (c)<br />
### Return_Air
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Return_Air`
Description | <p>air removed from a space to be recirculated or exhausted. Air extracted from a space and totally or partially returned to an air conditioner, furnace, or other heating, cooling, or ventilating system.</p>
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air](https://brickschema.org/schema/1.0.3/Brick#Air) (c)<br />
### Return_Air_CO2_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Return_Air_CO2_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#CO2_Sensor](https://brickschema.org/schema/1.0.3/Brick#CO2_Sensor) (c)<br />
### Return_Air_CO2_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Return_Air_CO2_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#CO2_Setpoint](https://brickschema.org/schema/1.0.3/Brick#CO2_Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Max_Return_Air_CO2_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Max_Return_Air_CO2_Setpoint) (c)<br />
### Return_Air_Dewpoint_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Return_Air_Dewpoint_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Dewpoint_Sensor](https://brickschema.org/schema/1.0.3/Brick#Dewpoint_Sensor) (c)<br />
### Return_Air_Enthalpy_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Return_Air_Enthalpy_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Enthalpy_Sensor](https://brickschema.org/schema/1.0.3/Brick#Air_Enthalpy_Sensor) (c)<br />
### Return_Air_Flow_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Return_Air_Flow_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Sensor) (c)<br />
### Return_Air_Grains_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Return_Air_Grains_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Grains_Sensor](https://brickschema.org/schema/1.0.3/Brick#Air_Grains_Sensor) (c)<br />
### Return_Air_Humidity_Sensor:
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Return_Air_Humidity_Sensor:`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Humidity_Sensor](https://brickschema.org/schema/1.0.3/Brick#Air_Humidity_Sensor) (c)<br />
### Return_Air_Temperature_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Return_Air_Temperature_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Air_Temperature_Sensor) (c)<br />
### Return_Damper
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Return_Damper`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Damper](https://brickschema.org/schema/1.0.3/Brick#Damper) (c)<br />
### Return_Discharge_Fan_Differential_Speed_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Return_Discharge_Fan_Differential_Speed_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Differential_Speed_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Differential_Speed_Setpoint) (c)<br />
### Return_Fan
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Return_Fan`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Fan](https://brickschema.org/schema/1.0.3/Brick#Fan) (c)<br />
### Return_Fan_Air_Flow_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Return_Fan_Air_Flow_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Fan_Air_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Fan_Air_Flow_Sensor) (c)<br />
### Return_Fan_Differential_Speed_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Return_Fan_Differential_Speed_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Differential_Speed_Sensor](https://brickschema.org/schema/1.0.3/Brick#Differential_Speed_Sensor) (c)<br />
### Return_Fan_Differential_Speed_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Return_Fan_Differential_Speed_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Differential_Speed_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Differential_Speed_Setpoint) (c)<br />
### Return_Supply_Fan_Differential_Speed_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Return_Supply_Fan_Differential_Speed_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Differential_Speed_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Differential_Speed_Setpoint) (c)<br />
### Return_Water_Temperature_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Return_Water_Temperature_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Water_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Water_Temperature_Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Return_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Return_Temperature_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Return_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Return_Temperature_Sensor) (c)<br />
### Roof
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Roof`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Location](https://brickschema.org/schema/1.0.3/Brick#Location) (c)<br />
### Rooftop_Unit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Rooftop_Unit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#AHU](https://brickschema.org/schema/1.0.3/Brick#AHU) (c)<br />
### Room
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Room`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Location](https://brickschema.org/schema/1.0.3/Brick#Location) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Server_Room](https://brickschema.org/schema/1.0.3/Brick#Server_Room) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Laboratory](https://brickschema.org/schema/1.0.3/Brick#Laboratory) (c)<br />
### Room_Air_Temperature_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Room_Air_Temperature_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Temperature_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Air_Temperature_Setpoint) (c)<br />
### Run_Direction_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Run_Direction_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Direction_Status](https://brickschema.org/schema/1.0.3/Brick#Direction_Status) (c)<br />
### Run_Enable_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Run_Enable_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Enable_Status](https://brickschema.org/schema/1.0.3/Brick#Enable_Status) (c)<br />
### Run_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Run_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Start_Stop_Status](https://brickschema.org/schema/1.0.3/Brick#Start_Stop_Status) (c)<br />
### Run_Time_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Run_Time_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Duration_Sensor](https://brickschema.org/schema/1.0.3/Brick#Duration_Sensor) (c)<br />
### Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Point](https://brickschema.org/schema/1.0.3/Brick#Point) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Water_Level_Sensor](https://brickschema.org/schema/1.0.3/Brick#Water_Level_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Solar_Radiance_Sensor](https://brickschema.org/schema/1.0.3/Brick#Solar_Radiance_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Frost_Sensor](https://brickschema.org/schema/1.0.3/Brick#Frost_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Duration_Sensor](https://brickschema.org/schema/1.0.3/Brick#Duration_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Air_Grains_Sensor](https://brickschema.org/schema/1.0.3/Brick#Air_Grains_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Rain_Sensor](https://brickschema.org/schema/1.0.3/Brick#Rain_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#CO2_Sensor](https://brickschema.org/schema/1.0.3/Brick#CO2_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Torque_Sensor](https://brickschema.org/schema/1.0.3/Brick#Torque_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Flow_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Current_Sensor](https://brickschema.org/schema/1.0.3/Brick#Current_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Humidity_Sensor](https://brickschema.org/schema/1.0.3/Brick#Humidity_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Piezoelectric_Sensor](https://brickschema.org/schema/1.0.3/Brick#Piezoelectric_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Voltage_Sensor](https://brickschema.org/schema/1.0.3/Brick#Voltage_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Capacity_Sensor](https://brickschema.org/schema/1.0.3/Brick#Capacity_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Luminance_Sensor](https://brickschema.org/schema/1.0.3/Brick#Luminance_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Damper_Position_Sensor](https://brickschema.org/schema/1.0.3/Brick#Damper_Position_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Frequency_Sensor](https://brickschema.org/schema/1.0.3/Brick#Frequency_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Enthalpy_Sensor](https://brickschema.org/schema/1.0.3/Brick#Enthalpy_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Motion_Sensor](https://brickschema.org/schema/1.0.3/Brick#Motion_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Occupancy_Sensor](https://brickschema.org/schema/1.0.3/Brick#Occupancy_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Temperature_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Pressure_Sensor](https://brickschema.org/schema/1.0.3/Brick#Pressure_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Demand_Sensor](https://brickschema.org/schema/1.0.3/Brick#Demand_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Dewpoint_Sensor](https://brickschema.org/schema/1.0.3/Brick#Dewpoint_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Direction_Sensor](https://brickschema.org/schema/1.0.3/Brick#Direction_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Hail_Sensor](https://brickschema.org/schema/1.0.3/Brick#Hail_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Angle_Sensor](https://brickschema.org/schema/1.0.3/Brick#Angle_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Energy_Sensor](https://brickschema.org/schema/1.0.3/Brick#Energy_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Trace_Heat_Sensor](https://brickschema.org/schema/1.0.3/Brick#Trace_Heat_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Speed_Sensor](https://brickschema.org/schema/1.0.3/Brick#Speed_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Conductivity_Sensor](https://brickschema.org/schema/1.0.3/Brick#Conductivity_Sensor) (c)<br />
### Server_Room
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Server_Room`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Room](https://brickschema.org/schema/1.0.3/Brick#Room) (c)<br />
### Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Point](https://brickschema.org/schema/1.0.3/Brick#Point) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Proportional_Band_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Temperature_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Temperature_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#CO2_Setpoint](https://brickschema.org/schema/1.0.3/Brick#CO2_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Load_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Load_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Mode_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Mode_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Dead_Band_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Humidity_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Humidity_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Speed_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Speed_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Pressure_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Pressure_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Dew_Point_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Dew_Point_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Enthalpy_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Enthalpy_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Integral_Gain_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Integral_Gain_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Increase_Decrease_Step_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Increase_Decrease_Step_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Luminance_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Luminance_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Flow_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Flow_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Damper_Position_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Damper_Position_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Reset_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Reset_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Demand_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Demand_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Integral_Time_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Integral_Time_Setpoint) (c)<br />
### Shading_System
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Shading_System`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Equipment](https://brickschema.org/schema/1.0.3/Brick#Equipment) (c)<br />
### Solar_Azimuth_Angle_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Solar_Azimuth_Angle_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Angle_Sensor](https://brickschema.org/schema/1.0.3/Brick#Angle_Sensor) (c)<br />
### Solar_Irradiance
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Solar_Irradiance`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Irradiance](https://brickschema.org/schema/1.0.3/Brick#Irradiance) (c)<br />
### Solar_Panel
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Solar_Panel`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Equipment](https://brickschema.org/schema/1.0.3/Brick#Equipment) (c)<br />
### Solar_Radiance_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Solar_Radiance_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Sensor](https://brickschema.org/schema/1.0.3/Brick#Sensor) (c)<br />
### Solar_Zenith_Angle_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Solar_Zenith_Angle_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Angle_Sensor](https://brickschema.org/schema/1.0.3/Brick#Angle_Sensor) (c)<br />
### Solid
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Solid`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Substance](https://brickschema.org/schema/1.0.3/Brick#Substance) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Frost](https://brickschema.org/schema/1.0.3/Brick#Frost) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Ice](https://brickschema.org/schema/1.0.3/Brick#Ice) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Hail](https://brickschema.org/schema/1.0.3/Brick#Hail) (c)<br />
### Space
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Space`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Location](https://brickschema.org/schema/1.0.3/Brick#Location) (c)<br />
### Space_Heater
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Space_Heater`
Description | <p>A heater used to warm the air in an enclosed area, such as a room or office</p>
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#HVAC](https://brickschema.org/schema/1.0.3/Brick#HVAC) (c)<br />
### Speed
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Speed`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Quantity](https://brickschema.org/schema/1.0.3/Brick#Quantity) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Wind_Speed](https://brickschema.org/schema/1.0.3/Brick#Wind_Speed) (c)<br />
### Speed_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Speed_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Sensor](https://brickschema.org/schema/1.0.3/Brick#Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Differential_Speed_Sensor](https://brickschema.org/schema/1.0.3/Brick#Differential_Speed_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Wind_Speed_Sensor](https://brickschema.org/schema/1.0.3/Brick#Wind_Speed_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Motor_Speed_Sensor](https://brickschema.org/schema/1.0.3/Brick#Motor_Speed_Sensor) (c)<br />
### Speed_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Speed_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Setpoint](https://brickschema.org/schema/1.0.3/Brick#Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Differential_Speed_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Differential_Speed_Setpoint) (c)<br />
### Speed_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Speed_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Limit](https://brickschema.org/schema/1.0.3/Brick#Limit) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Max_Speed_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Speed_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Min_Speed_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Speed_Setpoint_Limit) (c)<br />
### Speed_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Speed_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Status](https://brickschema.org/schema/1.0.3/Brick#Status) (c)<br />
### Stages_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Stages_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Status](https://brickschema.org/schema/1.0.3/Brick#Status) (c)<br />
### Standby_Fan
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Standby_Fan`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Fan](https://brickschema.org/schema/1.0.3/Brick#Fan) (c)<br />
### Standby_Glycool_Unit_On_Off_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Standby_Glycool_Unit_On_Off_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#On_Off_Status](https://brickschema.org/schema/1.0.3/Brick#On_Off_Status) (c)<br />
### Standby_Unit_On_Off_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Standby_Unit_On_Off_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#On_Off_Status](https://brickschema.org/schema/1.0.3/Brick#On_Off_Status) (c)<br />
### Start_Stop_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Start_Stop_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Status](https://brickschema.org/schema/1.0.3/Brick#Status) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Run_Status](https://brickschema.org/schema/1.0.3/Brick#Run_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Fan_Start_Stop_Status](https://brickschema.org/schema/1.0.3/Brick#Fan_Start_Stop_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Pump_Start_Stop_Status](https://brickschema.org/schema/1.0.3/Brick#Pump_Start_Stop_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Motor_Start_Stop_Status](https://brickschema.org/schema/1.0.3/Brick#Motor_Start_Stop_Status) (c)<br />
### Static_Pressure
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Static_Pressure`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Pressure](https://brickschema.org/schema/1.0.3/Brick#Pressure) (c)<br />
### Static_Pressure_Dead_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Dead_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Dead_Band_Setpoint) (c)<br />
### Static_Pressure_Increase_Decrease_Step_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Increase_Decrease_Step_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Increase_Decrease_Step_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Increase_Decrease_Step_Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Static_Pressure_Increase_Decrease_Step_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Air_Static_Pressure_Increase_Decrease_Step_Setpoint) (c)<br />
### Static_Pressure_Integral_Time_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Integral_Time_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Integral_Time_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Integral_Time_Setpoint) (c)<br />
### Static_Pressure_Proportional_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Proportional_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Proportional_Band_Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Static_Pressure_Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Static_Pressure_Proportional_Band_Setpoint) (c)<br />
### Static_Pressure_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Pressure_Sensor](https://brickschema.org/schema/1.0.3/Brick#Pressure_Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Static_Pressure_Sensor:](https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Static_Pressure_Sensor:) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Building_Static_Pressure_Sensor:](https://brickschema.org/schema/1.0.3/Brick#Building_Static_Pressure_Sensor:) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Static_Pressure_Sensor:](https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Static_Pressure_Sensor:) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Static_Pressure_Sensor:](https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Static_Pressure_Sensor:) (c)<br />
### Static_Pressure_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Pressure_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Pressure_Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Static_Pressure_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Static_Pressure_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Static_Pressure_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Static_Pressure_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Static_Pressure_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Static_Pressure_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Static_Pressure_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Static_Pressure_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Building_Static_Pressure_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Building_Static_Pressure_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Static_Pressure_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Static_Pressure_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#High_Static_Pressure_Cutout_Limit_Setpoint](https://brickschema.org/schema/1.0.3/Brick#High_Static_Pressure_Cutout_Limit_Setpoint) (c)<br />
### Static_Pressure_Setpoint_Limit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Setpoint_Limit`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Limit](https://brickschema.org/schema/1.0.3/Brick#Limit) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Min_Static_Pressure_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Min_Static_Pressure_Setpoint_Limit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Max_Static_Pressure_Setpoint_Limit](https://brickschema.org/schema/1.0.3/Brick#Max_Static_Pressure_Setpoint_Limit) (c)<br />
### Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Point](https://brickschema.org/schema/1.0.3/Brick#Point) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Emergency_Generator_Status](https://brickschema.org/schema/1.0.3/Brick#Emergency_Generator_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#On_Status](https://brickschema.org/schema/1.0.3/Brick#On_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Fault_Status](https://brickschema.org/schema/1.0.3/Brick#Fault_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Occupancy_Status](https://brickschema.org/schema/1.0.3/Brick#Occupancy_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Turn_Off_Status](https://brickschema.org/schema/1.0.3/Brick#Turn_Off_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Lead_Lag_Status](https://brickschema.org/schema/1.0.3/Brick#Lead_Lag_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Stages_Status](https://brickschema.org/schema/1.0.3/Brick#Stages_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Off_Status](https://brickschema.org/schema/1.0.3/Brick#Off_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Emergency_Power_Off_Status](https://brickschema.org/schema/1.0.3/Brick#Emergency_Power_Off_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Hold_Status](https://brickschema.org/schema/1.0.3/Brick#Hold_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Emergency_Push_Button_Status](https://brickschema.org/schema/1.0.3/Brick#Emergency_Push_Button_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Disable_Status](https://brickschema.org/schema/1.0.3/Brick#Disable_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Last_Fault_Code_Status](https://brickschema.org/schema/1.0.3/Brick#Last_Fault_Code_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Manual_Auto_Status](https://brickschema.org/schema/1.0.3/Brick#Manual_Auto_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Pressure_Status](https://brickschema.org/schema/1.0.3/Brick#Pressure_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Direction_Status](https://brickschema.org/schema/1.0.3/Brick#Direction_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Load_Shed_Status](https://brickschema.org/schema/1.0.3/Brick#Load_Shed_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Enable_Status](https://brickschema.org/schema/1.0.3/Brick#Enable_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Emergency_Air_Flow_Status](https://brickschema.org/schema/1.0.3/Brick#Emergency_Air_Flow_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#System_Status](https://brickschema.org/schema/1.0.3/Brick#System_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Hand_Auto_Status](https://brickschema.org/schema/1.0.3/Brick#Hand_Auto_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Start_Stop_Status](https://brickschema.org/schema/1.0.3/Brick#Start_Stop_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#System_Shutdown_Status](https://brickschema.org/schema/1.0.3/Brick#System_Shutdown_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Fan_Status](https://brickschema.org/schema/1.0.3/Brick#Fan_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Speed_Status](https://brickschema.org/schema/1.0.3/Brick#Speed_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Overridden_Status](https://brickschema.org/schema/1.0.3/Brick#Overridden_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#On_Off_Status](https://brickschema.org/schema/1.0.3/Brick#On_Off_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Fault_Indicator_Status](https://brickschema.org/schema/1.0.3/Brick#Fault_Indicator_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Drive_Ready_Status](https://brickschema.org/schema/1.0.3/Brick#Drive_Ready_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Filter_Status](https://brickschema.org/schema/1.0.3/Brick#Filter_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Freeze_Status](https://brickschema.org/schema/1.0.3/Brick#Freeze_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Mode_Status](https://brickschema.org/schema/1.0.3/Brick#Mode_Status) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Even_Month_Status](https://brickschema.org/schema/1.0.3/Brick#Even_Month_Status) (c)<br />
### Steam
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Steam`
Description | <p>water in the vapor phase.</p>
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Gas](https://brickschema.org/schema/1.0.3/Brick#Gas) (c)<br />
### Steam_System
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Steam_System`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Equipment](https://brickschema.org/schema/1.0.3/Brick#Equipment) (c)<br />
### Substance
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Substance`
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Solid](https://brickschema.org/schema/1.0.3/Brick#Solid) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Fluid](https://brickschema.org/schema/1.0.3/Brick#Fluid) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Enthalpy](https://brickschema.org/schema/1.0.3/Brick#Enthalpy) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Luminance](https://brickschema.org/schema/1.0.3/Brick#Luminance) (c)<br />
In domain of |[https://brickschema.org/schema/1.0.3/Brick#isMeasuredBy](https://brickschema.org/schema/1.0.3/Brick#isMeasuredBy) (op)<br />
In range of |[https://brickschema.org/schema/1.0.3/Brick#hasOutputSubstance](https://brickschema.org/schema/1.0.3/Brick#hasOutputSubstance) (op)<br />[https://brickschema.org/schema/1.0.3/Brick#hasInputSubstance](https://brickschema.org/schema/1.0.3/Brick#hasInputSubstance) (op)<br />[https://brickschema.org/schema/1.0.3/Brick#measures](https://brickschema.org/schema/1.0.3/Brick#measures) (op)<br />
### Supply_Air
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Air`
Description | <p>(1) air delivered by mechanical or natural ventilation to a space, composed of any combination of outdoor air, recirculated air, or transfer air. (2) air entering a space from an air-conditioning, heating, or ventilating apparatus for the purpose of comfort conditioning. Supply air is generally filtered, fan forced, and either heated, cooled, humidified, or dehumidified as necessary to maintain specified conditions. Only the quantity of outdoor air within the supply airflow may be used as replacement air.</p>
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air](https://brickschema.org/schema/1.0.3/Brick#Air) (c)<br />
### Supply_Air_Duct_Pressure_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Duct_Pressure_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Pressure_Status](https://brickschema.org/schema/1.0.3/Brick#Pressure_Status) (c)<br />
### Supply_Air_Flow_Demand_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Flow_Demand_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Demand_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Demand_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Flow_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Flow_Setpoint) (c)<br />
### Supply_Air_Flow_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Flow_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Sensor) (c)<br />
### Supply_Air_Flow_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Flow_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Air_Flow_Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Heating_Supply_Air_Flow_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Heating_Supply_Air_Flow_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Flow_Demand_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Flow_Demand_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Occupied_Supply_Air_Flow_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Occupied_Supply_Air_Flow_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Cooling_Supply_Air_Flow_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Cooling_Supply_Air_Flow_Setpoint) (c)<br />
### Supply_Air_Humidity_Sensor:
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Humidity_Sensor:`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Humidity_Sensor](https://brickschema.org/schema/1.0.3/Brick#Air_Humidity_Sensor) (c)<br />
### Supply_Air_Static_Pressure_Integral_Time_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Static_Pressure_Integral_Time_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Integral_Time_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Integral_Time_Setpoint) (c)<br />
### Supply_Air_Static_Pressure_Proportional_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Static_Pressure_Proportional_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Proportional_Band_Setpoint) (c)<br />
### Supply_Air_Static_Pressure_Sensor:
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Static_Pressure_Sensor:`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Sensor](https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Sensor) (c)<br />
### Supply_Air_Static_Pressure_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Static_Pressure_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Static_Pressure_Setpoint) (c)<br />
### Supply_Air_Temperature_Dead_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Temperature_Dead_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Dead_Band_Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Cooling_Supply_Air_Temperature_Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Cooling_Supply_Air_Temperature_Dead_Band_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Heating_Supply_Air_Temperature_Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Heating_Supply_Air_Temperature_Dead_Band_Setpoint) (c)<br />
### Supply_Air_Temperature_Proportional_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Temperature_Proportional_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Proportional_Band_Setpoint) (c)<br />
### Supply_Air_Velocity_Pressure_Sensor:
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Velocity_Pressure_Sensor:`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Velocity_Pressure_Sensor:](https://brickschema.org/schema/1.0.3/Brick#Velocity_Pressure_Sensor:) (c)<br />
### Supply_Fan
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Fan`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Fan](https://brickschema.org/schema/1.0.3/Brick#Fan) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Booster_Fan](https://brickschema.org/schema/1.0.3/Brick#Booster_Fan) (c)<br />
### Supply_Fan_Air_Flow_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Fan_Air_Flow_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Fan_Air_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Fan_Air_Flow_Sensor) (c)<br />
### Supply_Water_Differential_Pressure_Dead_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Differential_Pressure_Dead_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Dead_Band_Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Thermal_Energy_Storage_Supply_Water_Differential_Pressure_Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Thermal_Energy_Storage_Supply_Water_Differential_Pressure_Dead_Band_Setpoint) (c)<br />
### Supply_Water_Differential_Pressure_Integral_Time_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Differential_Pressure_Integral_Time_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Integral_Time_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Integral_Time_Setpoint) (c)<br />
### Supply_Water_Differential_Pressure_Proportional_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Differential_Pressure_Proportional_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Proportional_Band_Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Thermal_Energy_Storage_Discharge_Water_Differential_Pressure_ProportionalBandSetpoint](https://brickschema.org/schema/1.0.3/Brick#Thermal_Energy_Storage_Discharge_Water_Differential_Pressure_ProportionalBandSetpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Thermal_Energy_Storage_Supply_Water_Differential_Pressure_Proportional_BandSetpoint](https://brickschema.org/schema/1.0.3/Brick#Thermal_Energy_Storage_Supply_Water_Differential_Pressure_Proportional_BandSetpoint) (c)<br />
### Supply_Water_Flow_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Flow_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Water_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Water_Flow_Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Discharge_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Discharge_Flow_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Supply_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Supply_Flow_Sensor) (c)<br />
### Supply_Water_Temperature_Dead_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Temperature_Dead_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Dead_Band_Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Heat_Exchanger_Supply_Water_Temperature_Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Heat_Exchanger_Supply_Water_Temperature_Dead_Band_Setpoint) (c)<br />
### Supply_Water_Temperature_Integral_Time_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Temperature_Integral_Time_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Integral_Time_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Integral_Time_Setpoint) (c)<br />
### Supply_Water_Temperature_Proportional_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Temperature_Proportional_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Proportional_Band_Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Heat_Exchanger_Discharge_Water_Temperature_Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Heat_Exchanger_Discharge_Water_Temperature_Proportional_Band_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Heat_Exchanger_Supply_Water_Temperature_Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Heat_Exchanger_Supply_Water_Temperature_Proportional_Band_Setpoint) (c)<br />
### Switch
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Switch`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Interface](https://brickschema.org/schema/1.0.3/Brick#Interface) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Dimmer](https://brickschema.org/schema/1.0.3/Brick#Dimmer) (c)<br />
### System_Mode_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#System_Mode_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Mode_Status](https://brickschema.org/schema/1.0.3/Brick#Mode_Status) (c)<br />
### System_Shutdown_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#System_Shutdown_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Status](https://brickschema.org/schema/1.0.3/Brick#Status) (c)<br />
### System_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#System_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Status](https://brickschema.org/schema/1.0.3/Brick#Status) (c)<br />
### TVOC
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#TVOC`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Quality](https://brickschema.org/schema/1.0.3/Brick#Air_Quality) (c)<br />
### Tag
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Tag`
In range of |[https://brickschema.org/schema/1.0.3/Brick#hasTag](https://brickschema.org/schema/1.0.3/Brick#hasTag) (op)<br />
Has members |[https://brickschema.org/schema/1.0.3/BrickTag#Medium](https://brickschema.org/schema/1.0.3/BrickTag#Medium)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Frost](https://brickschema.org/schema/1.0.3/BrickTag#Frost)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Meter](https://brickschema.org/schema/1.0.3/BrickTag#Meter)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Run](https://brickschema.org/schema/1.0.3/BrickTag#Run)<br />[https://brickschema.org/schema/1.0.3/BrickTag#HVAC](https://brickschema.org/schema/1.0.3/BrickTag#HVAC)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Steam](https://brickschema.org/schema/1.0.3/BrickTag#Steam)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Time](https://brickschema.org/schema/1.0.3/BrickTag#Time)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Percent](https://brickschema.org/schema/1.0.3/BrickTag#Percent)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Isolation](https://brickschema.org/schema/1.0.3/BrickTag#Isolation)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Hand](https://brickschema.org/schema/1.0.3/BrickTag#Hand)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Equip](https://brickschema.org/schema/1.0.3/BrickTag#Equip)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Load](https://brickschema.org/schema/1.0.3/BrickTag#Load)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Gas](https://brickschema.org/schema/1.0.3/BrickTag#Gas)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Last](https://brickschema.org/schema/1.0.3/BrickTag#Last)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Generator](https://brickschema.org/schema/1.0.3/BrickTag#Generator)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Fan](https://brickschema.org/schema/1.0.3/BrickTag#Fan)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Direction](https://brickschema.org/schema/1.0.3/BrickTag#Direction)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Bandsetpoint](https://brickschema.org/schema/1.0.3/BrickTag#Bandsetpoint)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Luminance](https://brickschema.org/schema/1.0.3/BrickTag#Luminance)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Hot](https://brickschema.org/schema/1.0.3/BrickTag#Hot)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Outside](https://brickschema.org/schema/1.0.3/BrickTag#Outside)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Proportional](https://brickschema.org/schema/1.0.3/BrickTag#Proportional)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Cool](https://brickschema.org/schema/1.0.3/BrickTag#Cool)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Dewpoint](https://brickschema.org/schema/1.0.3/BrickTag#Dewpoint)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Limit](https://brickschema.org/schema/1.0.3/BrickTag#Limit)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Zone](https://brickschema.org/schema/1.0.3/BrickTag#Zone)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Push](https://brickschema.org/schema/1.0.3/BrickTag#Push)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Open](https://brickschema.org/schema/1.0.3/BrickTag#Open)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Temperature](https://brickschema.org/schema/1.0.3/BrickTag#Temperature)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Mixed](https://brickschema.org/schema/1.0.3/BrickTag#Mixed)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Stop](https://brickschema.org/schema/1.0.3/BrickTag#Stop)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Unit](https://brickschema.org/schema/1.0.3/BrickTag#Unit)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Temporary](https://brickschema.org/schema/1.0.3/BrickTag#Temporary)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Max](https://brickschema.org/schema/1.0.3/BrickTag#Max)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Setpoint](https://brickschema.org/schema/1.0.3/BrickTag#Setpoint)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Month](https://brickschema.org/schema/1.0.3/BrickTag#Month)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Occupied](https://brickschema.org/schema/1.0.3/BrickTag#Occupied)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Static](https://brickschema.org/schema/1.0.3/BrickTag#Static)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Operating](https://brickschema.org/schema/1.0.3/BrickTag#Operating)<br />[https://brickschema.org/schema/1.0.3/BrickTag#CO2](https://brickschema.org/schema/1.0.3/BrickTag#CO2)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Thermal](https://brickschema.org/schema/1.0.3/BrickTag#Thermal)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Fuel](https://brickschema.org/schema/1.0.3/BrickTag#Fuel)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Position](https://brickschema.org/schema/1.0.3/BrickTag#Position)<br />[https://brickschema.org/schema/1.0.3/BrickTag#PIR](https://brickschema.org/schema/1.0.3/BrickTag#PIR)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Mode](https://brickschema.org/schema/1.0.3/BrickTag#Mode)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Loc](https://brickschema.org/schema/1.0.3/BrickTag#Loc)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Pre](https://brickschema.org/schema/1.0.3/BrickTag#Pre)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Level](https://brickschema.org/schema/1.0.3/BrickTag#Level)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Drive](https://brickschema.org/schema/1.0.3/BrickTag#Drive)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Damper](https://brickschema.org/schema/1.0.3/BrickTag#Damper)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Supply](https://brickschema.org/schema/1.0.3/BrickTag#Supply)<br />[https://brickschema.org/schema/1.0.3/BrickTag#On](https://brickschema.org/schema/1.0.3/BrickTag#On)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Liquid](https://brickschema.org/schema/1.0.3/BrickTag#Liquid)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Hold](https://brickschema.org/schema/1.0.3/BrickTag#Hold)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Hood](https://brickschema.org/schema/1.0.3/BrickTag#Hood)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Alarm](https://brickschema.org/schema/1.0.3/BrickTag#Alarm)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Conductivity](https://brickschema.org/schema/1.0.3/BrickTag#Conductivity)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Cooling](https://brickschema.org/schema/1.0.3/BrickTag#Cooling)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Standby](https://brickschema.org/schema/1.0.3/BrickTag#Standby)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Indicator](https://brickschema.org/schema/1.0.3/BrickTag#Indicator)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Stack](https://brickschema.org/schema/1.0.3/BrickTag#Stack)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Discharge](https://brickschema.org/schema/1.0.3/BrickTag#Discharge)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Current](https://brickschema.org/schema/1.0.3/BrickTag#Current)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Vent](https://brickschema.org/schema/1.0.3/BrickTag#Vent)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Speed](https://brickschema.org/schema/1.0.3/BrickTag#Speed)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Valve](https://brickschema.org/schema/1.0.3/BrickTag#Valve)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Storage](https://brickschema.org/schema/1.0.3/BrickTag#Storage)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Decrease](https://brickschema.org/schema/1.0.3/BrickTag#Decrease)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Turn](https://brickschema.org/schema/1.0.3/BrickTag#Turn)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Entering](https://brickschema.org/schema/1.0.3/BrickTag#Entering)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Gasoline](https://brickschema.org/schema/1.0.3/BrickTag#Gasoline)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Energy](https://brickschema.org/schema/1.0.3/BrickTag#Energy)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Pir](https://brickschema.org/schema/1.0.3/BrickTag#Pir)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Wind](https://brickschema.org/schema/1.0.3/BrickTag#Wind)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Emergency](https://brickschema.org/schema/1.0.3/BrickTag#Emergency)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Differential](https://brickschema.org/schema/1.0.3/BrickTag#Differential)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Point](https://brickschema.org/schema/1.0.3/BrickTag#Point)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Hail](https://brickschema.org/schema/1.0.3/BrickTag#Hail)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Preheat](https://brickschema.org/schema/1.0.3/BrickTag#Preheat)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Request](https://brickschema.org/schema/1.0.3/BrickTag#Request)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Lighting](https://brickschema.org/schema/1.0.3/BrickTag#Lighting)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Solar](https://brickschema.org/schema/1.0.3/BrickTag#Solar)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Capacity](https://brickschema.org/schema/1.0.3/BrickTag#Capacity)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Bus](https://brickschema.org/schema/1.0.3/BrickTag#Bus)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Exhaust](https://brickschema.org/schema/1.0.3/BrickTag#Exhaust)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Lockout](https://brickschema.org/schema/1.0.3/BrickTag#Lockout)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Shade](https://brickschema.org/schema/1.0.3/BrickTag#Shade)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Locally](https://brickschema.org/schema/1.0.3/BrickTag#Locally)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Unoccupied](https://brickschema.org/schema/1.0.3/BrickTag#Unoccupied)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Dual](https://brickschema.org/schema/1.0.3/BrickTag#Dual)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Condenser](https://brickschema.org/schema/1.0.3/BrickTag#Condenser)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Relative](https://brickschema.org/schema/1.0.3/BrickTag#Relative)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Coil](https://brickschema.org/schema/1.0.3/BrickTag#Coil)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Building](https://brickschema.org/schema/1.0.3/BrickTag#Building)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Domestic](https://brickschema.org/schema/1.0.3/BrickTag#Domestic)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Humidity](https://brickschema.org/schema/1.0.3/BrickTag#Humidity)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Exchanger](https://brickschema.org/schema/1.0.3/BrickTag#Exchanger)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Occupancy](https://brickschema.org/schema/1.0.3/BrickTag#Occupancy)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Step](https://brickschema.org/schema/1.0.3/BrickTag#Step)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Return](https://brickschema.org/schema/1.0.3/BrickTag#Return)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Radiance](https://brickschema.org/schema/1.0.3/BrickTag#Radiance)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Leaving](https://brickschema.org/schema/1.0.3/BrickTag#Leaving)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Velocity](https://brickschema.org/schema/1.0.3/BrickTag#Velocity)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Integral](https://brickschema.org/schema/1.0.3/BrickTag#Integral)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Azimuth](https://brickschema.org/schema/1.0.3/BrickTag#Azimuth)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Motion](https://brickschema.org/schema/1.0.3/BrickTag#Motion)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Econcycle](https://brickschema.org/schema/1.0.3/BrickTag#Econcycle)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Gain](https://brickschema.org/schema/1.0.3/BrickTag#Gain)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Blowdown](https://brickschema.org/schema/1.0.3/BrickTag#Blowdown)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Freeze](https://brickschema.org/schema/1.0.3/BrickTag#Freeze)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Lead](https://brickschema.org/schema/1.0.3/BrickTag#Lead)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Piezoelectric](https://brickschema.org/schema/1.0.3/BrickTag#Piezoelectric)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Code](https://brickschema.org/schema/1.0.3/BrickTag#Code)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Ice](https://brickschema.org/schema/1.0.3/BrickTag#Ice)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Humidification](https://brickschema.org/schema/1.0.3/BrickTag#Humidification)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Proportionalbandsetpoint](https://brickschema.org/schema/1.0.3/BrickTag#Proportionalbandsetpoint)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Low](https://brickschema.org/schema/1.0.3/BrickTag#Low)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Shed](https://brickschema.org/schema/1.0.3/BrickTag#Shed)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Output](https://brickschema.org/schema/1.0.3/BrickTag#Output)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Water](https://brickschema.org/schema/1.0.3/BrickTag#Water)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Bypass](https://brickschema.org/schema/1.0.3/BrickTag#Bypass)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Flow](https://brickschema.org/schema/1.0.3/BrickTag#Flow)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Pump](https://brickschema.org/schema/1.0.3/BrickTag#Pump)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Lowest](https://brickschema.org/schema/1.0.3/BrickTag#Lowest)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Status](https://brickschema.org/schema/1.0.3/BrickTag#Status)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Deionised](https://brickschema.org/schema/1.0.3/BrickTag#Deionised)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Heat](https://brickschema.org/schema/1.0.3/BrickTag#Heat)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Ready](https://brickschema.org/schema/1.0.3/BrickTag#Ready)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Highest](https://brickschema.org/schema/1.0.3/BrickTag#Highest)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Natural](https://brickschema.org/schema/1.0.3/BrickTag#Natural)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Start](https://brickschema.org/schema/1.0.3/BrickTag#Start)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Dehumidification](https://brickschema.org/schema/1.0.3/BrickTag#Dehumidification)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Heating](https://brickschema.org/schema/1.0.3/BrickTag#Heating)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Air](https://brickschema.org/schema/1.0.3/BrickTag#Air)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Demand](https://brickschema.org/schema/1.0.3/BrickTag#Demand)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Duration](https://brickschema.org/schema/1.0.3/BrickTag#Duration)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Fluid](https://brickschema.org/schema/1.0.3/BrickTag#Fluid)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Increase](https://brickschema.org/schema/1.0.3/BrickTag#Increase)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Average](https://brickschema.org/schema/1.0.3/BrickTag#Average)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Battery](https://brickschema.org/schema/1.0.3/BrickTag#Battery)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Tank](https://brickschema.org/schema/1.0.3/BrickTag#Tank)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Enthalpy](https://brickschema.org/schema/1.0.3/BrickTag#Enthalpy)<br />[https://brickschema.org/schema/1.0.3/BrickTag#System](https://brickschema.org/schema/1.0.3/BrickTag#System)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Torque](https://brickschema.org/schema/1.0.3/BrickTag#Torque)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Min](https://brickschema.org/schema/1.0.3/BrickTag#Min)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Solid](https://brickschema.org/schema/1.0.3/BrickTag#Solid)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Makeup](https://brickschema.org/schema/1.0.3/BrickTag#Makeup)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Band](https://brickschema.org/schema/1.0.3/BrickTag#Band)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Humidifier](https://brickschema.org/schema/1.0.3/BrickTag#Humidifier)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Plugstrip](https://brickschema.org/schema/1.0.3/BrickTag#Plugstrip)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Zenith](https://brickschema.org/schema/1.0.3/BrickTag#Zenith)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Voltage](https://brickschema.org/schema/1.0.3/BrickTag#Voltage)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Duct](https://brickschema.org/schema/1.0.3/BrickTag#Duct)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Oil](https://brickschema.org/schema/1.0.3/BrickTag#Oil)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Co2](https://brickschema.org/schema/1.0.3/BrickTag#Co2)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Dc](https://brickschema.org/schema/1.0.3/BrickTag#Dc)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Off](https://brickschema.org/schema/1.0.3/BrickTag#Off)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Frequency](https://brickschema.org/schema/1.0.3/BrickTag#Frequency)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Fault](https://brickschema.org/schema/1.0.3/BrickTag#Fault)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Shutdown](https://brickschema.org/schema/1.0.3/BrickTag#Shutdown)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Room](https://brickschema.org/schema/1.0.3/BrickTag#Room)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Photovoltaic](https://brickschema.org/schema/1.0.3/BrickTag#Photovoltaic)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Reheat](https://brickschema.org/schema/1.0.3/BrickTag#Reheat)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Weather](https://brickschema.org/schema/1.0.3/BrickTag#Weather)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Remotely](https://brickschema.org/schema/1.0.3/BrickTag#Remotely)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Power](https://brickschema.org/schema/1.0.3/BrickTag#Power)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Manual](https://brickschema.org/schema/1.0.3/BrickTag#Manual)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Disable](https://brickschema.org/schema/1.0.3/BrickTag#Disable)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Fume](https://brickschema.org/schema/1.0.3/BrickTag#Fume)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Sensor](https://brickschema.org/schema/1.0.3/BrickTag#Sensor)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Reset](https://brickschema.org/schema/1.0.3/BrickTag#Reset)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Lag](https://brickschema.org/schema/1.0.3/BrickTag#Lag)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Auto](https://brickschema.org/schema/1.0.3/BrickTag#Auto)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Peak](https://brickschema.org/schema/1.0.3/BrickTag#Peak)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Booster](https://brickschema.org/schema/1.0.3/BrickTag#Booster)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Integration](https://brickschema.org/schema/1.0.3/BrickTag#Integration)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Filter](https://brickschema.org/schema/1.0.3/BrickTag#Filter)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Rain](https://brickschema.org/schema/1.0.3/BrickTag#Rain)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Even](https://brickschema.org/schema/1.0.3/BrickTag#Even)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Pressure](https://brickschema.org/schema/1.0.3/BrickTag#Pressure)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Button](https://brickschema.org/schema/1.0.3/BrickTag#Button)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Angle](https://brickschema.org/schema/1.0.3/BrickTag#Angle)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Glycool](https://brickschema.org/schema/1.0.3/BrickTag#Glycool)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Chilled](https://brickschema.org/schema/1.0.3/BrickTag#Chilled)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Grains](https://brickschema.org/schema/1.0.3/BrickTag#Grains)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Motor](https://brickschema.org/schema/1.0.3/BrickTag#Motor)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Overridden](https://brickschema.org/schema/1.0.3/BrickTag#Overridden)<br />[https://brickschema.org/schema/1.0.3/BrickTag#High](https://brickschema.org/schema/1.0.3/BrickTag#High)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Cutout](https://brickschema.org/schema/1.0.3/BrickTag#Cutout)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Timer](https://brickschema.org/schema/1.0.3/BrickTag#Timer)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Trace](https://brickschema.org/schema/1.0.3/BrickTag#Trace)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Dead](https://brickschema.org/schema/1.0.3/BrickTag#Dead)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Wheel](https://brickschema.org/schema/1.0.3/BrickTag#Wheel)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Stages](https://brickschema.org/schema/1.0.3/BrickTag#Stages)<br />[https://brickschema.org/schema/1.0.3/BrickTag#Enable](https://brickschema.org/schema/1.0.3/BrickTag#Enable)<br />
### Temperature
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Temperature`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Quantity](https://brickschema.org/schema/1.0.3/Brick#Quantity) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Operative_Temperature](https://brickschema.org/schema/1.0.3/Brick#Operative_Temperature) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Radiant_Temperature](https://brickschema.org/schema/1.0.3/Brick#Radiant_Temperature) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Wet_Bulb_Temperature](https://brickschema.org/schema/1.0.3/Brick#Wet_Bulb_Temperature) (c)<br />
### Temperature_Dead_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Temperature_Dead_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Dead_Band_Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Occupied_Heating_Temperature_Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Occupied_Heating_Temperature_Dead_Band_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Occupied_Cooling_Temperature_Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Occupied_Cooling_Temperature_Dead_Band_Setpoint) (c)<br />
### Temperature_Increase_Decrease_Step_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Temperature_Increase_Decrease_Step_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Increase_Decrease_Step_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Increase_Decrease_Step_Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Temperature_Increase_Decrease_Step_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Air_Temperature_Increase_Decrease_Step_Setpoint) (c)<br />
### Temperature_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Temperature_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Sensor](https://brickschema.org/schema/1.0.3/Brick#Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Water_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Water_Temperature_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Zone_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Zone_Temperature_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Air_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Air_Temperature_Sensor) (c)<br />
Has members |[https://brickschema.org/schema/1.0.3/ExampleBuilding#TS1](https://brickschema.org/schema/1.0.3/ExampleBuilding#TS1)<br />[https://brickschema.org/schema/1.0.3/ExampleBuilding#standalone](https://brickschema.org/schema/1.0.3/ExampleBuilding#standalone)<br />
### Temperature_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Temperature_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Setpoint](https://brickschema.org/schema/1.0.3/Brick#Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Water_Temperature_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Water_Temperature_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Air_Temperature_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Air_Temperature_Setpoint) (c)<br />
### Temporary_Occupancy_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Temporary_Occupancy_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Occupancy_Status](https://brickschema.org/schema/1.0.3/Brick#Occupancy_Status) (c)<br />
### Terminal_Unit
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Terminal_Unit`
Description | <p>A device that regulates the volumetric flow rate and/or the temperature of the controlled medium.</p>
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#HVAC](https://brickschema.org/schema/1.0.3/Brick#HVAC) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Fan_Coil_Unit](https://brickschema.org/schema/1.0.3/Brick#Fan_Coil_Unit) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Variable_Air_Volume_Box](https://brickschema.org/schema/1.0.3/Brick#Variable_Air_Volume_Box) (c)<br />
### Thermal_Energy
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Thermal_Energy`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Energy](https://brickschema.org/schema/1.0.3/Brick#Energy) (c)<br />
### Thermal_Energy_Storage_Discharge_Water_Differential_Pressure_ProportionalBandSetpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Thermal_Energy_Storage_Discharge_Water_Differential_Pressure_ProportionalBandSetpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Differential_Pressure_Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Differential_Pressure_Proportional_Band_Setpoint) (c)<br />
### Thermal_Energy_Storage_Supply_Water_Differential_Pressure_Dead_Band_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Thermal_Energy_Storage_Supply_Water_Differential_Pressure_Dead_Band_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Differential_Pressure_Dead_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Differential_Pressure_Dead_Band_Setpoint) (c)<br />
### Thermal_Energy_Storage_Supply_Water_Differential_Pressure_Proportional_BandSetpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Thermal_Energy_Storage_Supply_Water_Differential_Pressure_Proportional_BandSetpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Differential_Pressure_Proportional_Band_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Differential_Pressure_Proportional_Band_Setpoint) (c)<br />
### Thermal_Power
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Thermal_Power`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Power](https://brickschema.org/schema/1.0.3/Brick#Power) (c)<br />
### Thermostat
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Thermostat`
Description | <p>An automatic control device used to maintain temperature at a fixed or adjustable setpoint.</p>
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#HVAC](https://brickschema.org/schema/1.0.3/Brick#HVAC) (c)<br />
### Torque_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Torque_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Sensor](https://brickschema.org/schema/1.0.3/Brick#Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Motor_Torque_Sensor](https://brickschema.org/schema/1.0.3/Brick#Motor_Torque_Sensor) (c)<br />
### Touchpanel
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Touchpanel`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Interface](https://brickschema.org/schema/1.0.3/Brick#Interface) (c)<br />
### Trace_Heat_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Trace_Heat_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Sensor](https://brickschema.org/schema/1.0.3/Brick#Sensor) (c)<br />
### Turn_Off_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Turn_Off_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Status](https://brickschema.org/schema/1.0.3/Brick#Status) (c)<br />
### Unoccupied_Mode_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Unoccupied_Mode_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Mode_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Mode_Setpoint) (c)<br />
### VFD
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#VFD`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#HVAC](https://brickschema.org/schema/1.0.3/Brick#HVAC) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Preheat_Valve_VFD](https://brickschema.org/schema/1.0.3/Brick#Preheat_Valve_VFD) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Heat_Wheel_VFD](https://brickschema.org/schema/1.0.3/Brick#Heat_Wheel_VFD) (c)<br />
### Valve
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Valve`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#HVAC](https://brickschema.org/schema/1.0.3/Brick#HVAC) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Heating_Valve](https://brickschema.org/schema/1.0.3/Brick#Heating_Valve) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Isolation_Valve](https://brickschema.org/schema/1.0.3/Brick#Isolation_Valve) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Water_Valve](https://brickschema.org/schema/1.0.3/Brick#Water_Valve) (c)<br />
### Variable_Air_Volume_Box
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Variable_Air_Volume_Box`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Terminal_Unit](https://brickschema.org/schema/1.0.3/Brick#Terminal_Unit) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Variable_Air_Volume_Box_With_Reheat](https://brickschema.org/schema/1.0.3/Brick#Variable_Air_Volume_Box_With_Reheat) (c)<br />
### Variable_Air_Volume_Box_With_Reheat
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Variable_Air_Volume_Box_With_Reheat`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Variable_Air_Volume_Box](https://brickschema.org/schema/1.0.3/Brick#Variable_Air_Volume_Box) (c)<br />
### Variable_Frequency_Drive
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Variable_Frequency_Drive`
Description | <p>Electronic device that varies its output frequency to vary the rotating speed of a motor, given a fixed input frequency. Used with fans or pumps to vary the flow in the system as a function of a maintained pressure.</p>
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#HVAC](https://brickschema.org/schema/1.0.3/Brick#HVAC) (c)<br />
### Velocity_Pressure_Sensor:
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Velocity_Pressure_Sensor:`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Pressure_Sensor](https://brickschema.org/schema/1.0.3/Brick#Pressure_Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Velocity_Pressure_Sensor:](https://brickschema.org/schema/1.0.3/Brick#Discharge_Air_Velocity_Pressure_Sensor:) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Velocity_Pressure_Sensor:](https://brickschema.org/schema/1.0.3/Brick#Exhaust_Air_Velocity_Pressure_Sensor:) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Velocity_Pressure_Sensor:](https://brickschema.org/schema/1.0.3/Brick#Supply_Air_Velocity_Pressure_Sensor:) (c)<br />
### Velocity_Pressure_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Velocity_Pressure_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Pressure_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Pressure_Setpoint) (c)<br />
### Vent_Operating_Mode_Status
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Vent_Operating_Mode_Status`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Operating_Mode_Status](https://brickschema.org/schema/1.0.3/Brick#Operating_Mode_Status) (c)<br />
### Voltage
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Voltage`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Quantity](https://brickschema.org/schema/1.0.3/Brick#Quantity) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Electric_Voltage](https://brickschema.org/schema/1.0.3/Brick#Electric_Voltage) (c)<br />
### Voltage_Angle
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Voltage_Angle`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Electric_Voltage](https://brickschema.org/schema/1.0.3/Brick#Electric_Voltage) (c)<br />
### Voltage_Imbalance
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Voltage_Imbalance`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Electric_Voltage](https://brickschema.org/schema/1.0.3/Brick#Electric_Voltage) (c)<br />
### Voltage_Magnitude
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Voltage_Magnitude`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Electric_Voltage](https://brickschema.org/schema/1.0.3/Brick#Electric_Voltage) (c)<br />
### Voltage_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Voltage_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Sensor](https://brickschema.org/schema/1.0.3/Brick#Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Output_Voltage_Sensor](https://brickschema.org/schema/1.0.3/Brick#Output_Voltage_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#DC_Bus_Voltage_Sensor](https://brickschema.org/schema/1.0.3/Brick#DC_Bus_Voltage_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Heat_Wheel_Voltage_Sensor](https://brickschema.org/schema/1.0.3/Brick#Heat_Wheel_Voltage_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Battery_Voltage_Sensor](https://brickschema.org/schema/1.0.3/Brick#Battery_Voltage_Sensor) (c)<br />
### Water
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Water`
Description | <p>transparent, odorless, tasteless liquid; a compound of hydrogen and oxygen (H2O), containing 11.188% hydrogen and 88.812% oxygen by mass; freezing at 32°F (0°C); boiling near 212°F (100°C).</p>
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Liquid](https://brickschema.org/schema/1.0.3/Brick#Liquid) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Hot_Water](https://brickschema.org/schema/1.0.3/Brick#Hot_Water) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Chilled_Water](https://brickschema.org/schema/1.0.3/Brick#Chilled_Water) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Makeup_Water](https://brickschema.org/schema/1.0.3/Brick#Makeup_Water) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Domestic_Water](https://brickschema.org/schema/1.0.3/Brick#Domestic_Water) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Blowdown_Water](https://brickschema.org/schema/1.0.3/Brick#Blowdown_Water) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Condenser_Water](https://brickschema.org/schema/1.0.3/Brick#Condenser_Water) (c)<br />
### Water_Flow_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Water_Flow_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Flow_Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Flow_Sensor](https://brickschema.org/schema/1.0.3/Brick#Supply_Water_Flow_Sensor) (c)<br />
### Water_Level_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Water_Level_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Sensor](https://brickschema.org/schema/1.0.3/Brick#Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Deionised_Water_Level_Sensor](https://brickschema.org/schema/1.0.3/Brick#Deionised_Water_Level_Sensor) (c)<br />
### Water_Pump
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Water_Pump`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Pump](https://brickschema.org/schema/1.0.3/Brick#Pump) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Pump](https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Pump) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Condenser_Water_Pump](https://brickschema.org/schema/1.0.3/Brick#Condenser_Water_Pump) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Pump](https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Pump) (c)<br />
### Water_System
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Water_System`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Equipment](https://brickschema.org/schema/1.0.3/Brick#Equipment) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_System](https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_System) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Hot_Water_System](https://brickschema.org/schema/1.0.3/Brick#Hot_Water_System) (c)<br />
### Water_Temperature_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Water_Temperature_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Temperature_Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Return_Water_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Return_Water_Temperature_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Temperature_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Heat_Exchanger_Supply_Water_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Heat_Exchanger_Supply_Water_Temperature_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Supply_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Hot_Water_Supply_Temperature_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Leaving_Water_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Leaving_Water_Temperature_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Entering_Water_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Entering_Water_Temperature_Sensor) (c)<br />
### Water_Temperature_Setpoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Water_Temperature_Setpoint`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Temperature_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Temperature_Setpoint) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Leaving_Water_Temperature_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Leaving_Water_Temperature_Setpoint) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Entering_Water_Temperature_Setpoint](https://brickschema.org/schema/1.0.3/Brick#Entering_Water_Temperature_Setpoint) (c)<br />
### Water_Valve
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Water_Valve`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Valve](https://brickschema.org/schema/1.0.3/Brick#Valve) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Valve](https://brickschema.org/schema/1.0.3/Brick#Chilled_Water_Valve) (c)<br />
### Weather
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Weather`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Equipment](https://brickschema.org/schema/1.0.3/Brick#Equipment) (c)<br />
### Weather_Condition
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Weather_Condition`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Quantity](https://brickschema.org/schema/1.0.3/Brick#Quantity) (c)<br />
### Wet_Bulb_Temperature
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Wet_Bulb_Temperature`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Temperature](https://brickschema.org/schema/1.0.3/Brick#Temperature) (c)<br />
### Wind_Direction
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Wind_Direction`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Direction](https://brickschema.org/schema/1.0.3/Brick#Direction) (c)<br />
### Wind_Direction_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Wind_Direction_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Direction_Sensor](https://brickschema.org/schema/1.0.3/Brick#Direction_Sensor) (c)<br />
### Wind_Speed
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Wind_Speed`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Speed](https://brickschema.org/schema/1.0.3/Brick#Speed) (c)<br />
### Wind_Speed_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Wind_Speed_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Speed_Sensor](https://brickschema.org/schema/1.0.3/Brick#Speed_Sensor) (c)<br />
### Wing
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Wing`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Location](https://brickschema.org/schema/1.0.3/Brick#Location) (c)<br />
### Zone
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Zone`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Location](https://brickschema.org/schema/1.0.3/Brick#Location) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Fire_Zone](https://brickschema.org/schema/1.0.3/Brick#Fire_Zone) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Lighting_Zone](https://brickschema.org/schema/1.0.3/Brick#Lighting_Zone) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#HVAC_Zone](https://brickschema.org/schema/1.0.3/Brick#HVAC_Zone) (c)<br />
### Zone_Air_Temperature_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Zone_Air_Temperature_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Air_Temperature_Sensor) (c)<br />
### Zone_Humidity_Sensor:
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Zone_Humidity_Sensor:`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Air_Humidity_Sensor](https://brickschema.org/schema/1.0.3/Brick#Air_Humidity_Sensor) (c)<br />
### Zone_Temperature_Sensor
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#Zone_Temperature_Sensor`
Super-classes |[https://brickschema.org/schema/1.0.3/Brick#Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Temperature_Sensor) (c)<br />
Sub-classes |[https://brickschema.org/schema/1.0.3/Brick#Average_Zone_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Average_Zone_Temperature_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Lowest_Zone_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Lowest_Zone_Temperature_Sensor) (c)<br />[https://brickschema.org/schema/1.0.3/Brick#Highest_Zone_Temperature_Sensor](https://brickschema.org/schema/1.0.3/Brick#Highest_Zone_Temperature_Sensor) (c)<br />

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
URI | `https://brickschema.org/schema/1.0.3/Brick#ahuRef`
Range(s) |[https://brickschema.org/schema/1.0.3/Brick#AHU](https://brickschema.org/schema/1.0.3/Brick#AHU) (c)<br />
[](controls)
### controls
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#controls`
[](feeds)
### feeds
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#feeds`
[](feedsAir)
### feedsAir
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#feedsAir`
Description | Passes air
Super-properties |[https://brickschema.org/schema/1.0.3/Brick#feeds](https://brickschema.org/schema/1.0.3/Brick#feeds) (op)<br />
[](hasInputSubstance)
### hasInputSubstance
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#hasInputSubstance`
Range(s) |[https://brickschema.org/schema/1.0.3/Brick#Substance](https://brickschema.org/schema/1.0.3/Brick#Substance) (c)<br />
[](hasLocation)
### hasLocation
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#hasLocation`
Range(s) |[https://brickschema.org/schema/1.0.3/Brick#Location](https://brickschema.org/schema/1.0.3/Brick#Location) (c)<br />
[](hasOutputSubstance)
### hasOutputSubstance
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#hasOutputSubstance`
Range(s) |[https://brickschema.org/schema/1.0.3/Brick#Substance](https://brickschema.org/schema/1.0.3/Brick#Substance) (c)<br />
[](hasPart)
### hasPart
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#hasPart`
[](hasPoint)
### hasPoint
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#hasPoint`
Range(s) |[https://brickschema.org/schema/1.0.3/Brick#Point](https://brickschema.org/schema/1.0.3/Brick#Point) (c)<br />
[](hasTag)
### hasTag
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#hasTag`
Range(s) |[https://brickschema.org/schema/1.0.3/Brick#Tag](https://brickschema.org/schema/1.0.3/Brick#Tag) (c)<br />
[](isControlledBy)
### isControlledBy
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#isControlledBy`
[](isFedBy)
### isFedBy
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#isFedBy`
[](isLocationOf)
### isLocationOf
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#isLocationOf`
Domain(s) |[https://brickschema.org/schema/1.0.3/Brick#Location](https://brickschema.org/schema/1.0.3/Brick#Location) (c)<br />
[](isMeasuredBy)
### isMeasuredBy
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#isMeasuredBy`
Domain(s) |[https://brickschema.org/schema/1.0.3/Brick#Substance](https://brickschema.org/schema/1.0.3/Brick#Substance) (c)<br />
Range(s) |[https://brickschema.org/schema/1.0.3/Brick#Point](https://brickschema.org/schema/1.0.3/Brick#Point) (c)<br />
[](isPartOf)
### isPartOf
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#isPartOf`
[](isPointOf)
### isPointOf
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#isPointOf`
Domain(s) |[https://brickschema.org/schema/1.0.3/Brick#Point](https://brickschema.org/schema/1.0.3/Brick#Point) (c)<br />
[](measures)
### measures
Property | Value
--- | ---
URI | `https://brickschema.org/schema/1.0.3/Brick#measures`
Domain(s) |[https://brickschema.org/schema/1.0.3/Brick#Point](https://brickschema.org/schema/1.0.3/Brick#Point) (c)<br />
Range(s) |[https://brickschema.org/schema/1.0.3/Brick#Substance](https://brickschema.org/schema/1.0.3/Brick#Substance) (c)<br />

## Named Individuals
## Namespaces
* **dct**
  * `http://purl.org/dc/terms/`
* **owl**
  * `http://www.w3.org/2002/07/owl#`
* **prov**
  * `http://www.w3.org/ns/prov#`
* **rdf**
  * `http://www.w3.org/1999/02/22-rdf-syntax-ns#`
* **rdfs**
  * `http://www.w3.org/2000/01/rdf-schema#`
* **schema**
  * `http://schema.org/`
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