import streamlit as st

st.title("🔓Google Resembler (Unit Converter)")
st.markdown("### Converts Length, Mass, Time, Temperature, Volume, Area, Fuel Economy, Frequency, Plane Angle Instantly")
st.write("Welcome! Select a category, enter the value and get the converted result in real-time")

category = st.selectbox("Choose a Category",["Length","Mass","Temperature","Time","Volume","Area","Frequency","Fuel Economy","Plane Angle"])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Kilometers to Meters":
            return value * 1000
        elif unit == "Kilometers to Millimeter":
            return value * 1000000
        elif unit == "Kilometers to Centimeter":
            return value * 100000
        elif unit == "Kilometers to Micrometers":
            return value * 1000000000
        elif unit == "Kilometers to Nanometers":
            return value * 1000000000000
        elif unit == "Kilometers to Yards":
            return value * 1093.61
        elif unit == "Kilometers to Foots":
            return value * 3280.84
        elif unit == "Kilometers to Inchs":
            return value * 39370.1
        elif unit == "Kilometers to Nautical miles":
            return value * 0.539957
        elif unit == "Meters to Kilometers":
            return value *0.001
        elif unit == "Meters to Millimeters":
            return value * 1000
        elif unit == "Meters to Centimeters":
            return value * 100
        elif unit == "Meters to Micrometers":
            return value * 1000000
        elif unit == "Meters to Nanometers":
            return value * 1000000000
        elif unit == "Meters to Yards":
            return value * 1.09361
        elif unit == "Meters to Foots":
            return value * 3.28084
        elif unit == "Meters to Inchs":
            return value * 39.37008
        elif unit == "Meters to Nautical miles":
            return value * 0.000539957
        elif unit == "Centimeters to Kilometers":
            return value * 1e-5
        elif unit == "Centimeters to Meters":
            return value * 0.01
        elif unit == "Centimeters to Millimeters":
            return value * 10
        elif unit == "Centimeters to Nanometers":
            return value * 1e+7
        elif unit == "Centimeters to Micrometers":
            return value * 10000
        elif unit == "Centimeters to Miles":
            return value * 6.2137e-6
        elif unit == "Centimeters to Yards":
            return value * 0.0109361
        elif unit == "Centimeters to Foots":
            return value * 0.0328084
        elif unit == "Centimeters to Inchs":
            return value * 0.393701
        elif unit == "Centimeters to Nautical miles":
            return value * 5.3996e-6
        elif unit == "Millimeters to Kilometers":
            return value * 1e-6
        elif unit == "Millimeters to Meters":
            return value * 0.001
        elif unit == "Millimeters to Centimeters":
            return value * 0.1
        elif unit == "Millimeters to Micrometers":
            return value * 1000
        elif unit == "Millimeters to Nanometers":
            return value * 1e+6
        elif unit == "Millimeters to Miles":
            return value * 6.2137e-7
        elif unit == "Millimeters to Yards":
            return value * 0.00109361
        elif unit == "Millimeters to Foots":
            return value * 0.00328084
        elif unit == "Millimeters to Inchs":
            return value * 0.0393701
        elif unit == "Millimeters to Nautical miles":
            return value * 5.3996e-7
        elif unit == "Micrometers to Kilometers":
            return value * 1e-9
        elif unit == "Micrometers to Meters":
            return value * 1e-6
        elif unit == "Micrometers to Centimeters":
            return value * 1e-4
        elif unit == "Micrometers to Millimeters":
            return value * 0.001
        elif unit == "Micrometers to Nanometers":
            return value * 1000
        elif unit == "Micrometers to Miles":
            return value * 6.2137e-10
        elif unit == "Micrometers to Yards":
            return value * 1.0936e-6
        elif unit == "Micrometers to Foots":
            return value * 3.2808e-6
        elif unit == "Micrometers to Inchs":
            return value * 3.2808e-6
        elif unit == "Micrometers to Nautical miles":
            return value * 5.3996e-10
        elif unit == "Nanometers to Kilometers":
            return value * 1e-12
        elif unit == "Nanometers to Meters":
            return value * 1e-9
        elif unit == "Nanometers to Centimeters":
            return value * 1e-7
        elif unit == "Nanometers to Millimeters":
            return value * 1e-6
        elif unit == "Nanometers to Micrometers":
            return value * 0.001
        elif unit == "Nanometers to Miles":
            return value * 6.2137e-13
        elif unit == "Nanometers to Yards":
            return value * 1.0936e-9
        elif unit == "Nanometers to Foots":
            return value * 3.2808e-9
        elif unit == "Nanometers to Inchs":
            return value * 3.937e-8
        elif unit == "Nanometers to Nautical miles":
            return value * 5.3996e-13
        elif unit == "Miles to Kilometers":
            return value * 1.60934
        elif unit == "Miles to Meters":
            return value * 1609.34
        elif unit == "Miles to Centimeters":
            return value * 160934
        elif unit == "Miles to Millimeters":
            return value * 1.609e+6
        elif unit == "Miles to Micrometers":
            return value * 1.609e+9
        elif unit == "Miles to Nanometers":
            return value * 1.609e+12
        elif unit == "Miles to Inchs":
            return value * 63360
        elif unit == "Miles to Foots":
            return value * 5280
        elif unit == "Miles to Yards":
            return value * 1760
        elif unit == "Miles to Nautical miles":
            return value * 0.868976
        elif unit == "Yards to Kilometers":
            return value * 0.0009144
        elif unit == "Yards to Meters":
            return value * 0.9144
        elif unit == "Yards to Centimeters":
            return value * 91.44
        elif unit == "Yards to Millimeters":
            return value * 914.4
        elif unit == "Yards to Micrometers":
            return value * 914400
        elif unit == "Yards to Nanometers":
            return value * 9.144e+8
        elif unit == "Yards to Miles":
            return value * 0.000568182
        elif unit == "Yards to Inchs":
            return value * 36
        elif unit == "Yards to Foots":
            return value * 3
        elif unit == "Yards to Nautical miles":
            return value * 0.000493737
        elif unit == "Foots to Kilometers":
            return value * 0.0003048
        elif unit == "Foots to Meters":
            return value * 0.3048
        elif unit == "Foots to Centimeters":
            return value * 30.48
        elif unit == "Foots to Millimeters":
            return value * 304.8
        elif unit == "Foots to Micrometers":
            return value * 304800
        elif unit == "Foots to Nanometers":
            return value * 3.048e+8
        elif unit == "Foots to Miles":
            return value * 0.000189394
        elif unit == "Foots to Yards":
            return value * 0.333333
        elif unit == "Foots to Inchs":
            return value * 12
        elif unit == "Foots to Nautical miles":
            return value * 0.000164579
        elif unit == "Inches to Kilometers":
            return value * 2.54e-5
        elif unit == "Inches to Meters":
            return value * 0.0254
        elif unit == "Inches to Centimeters":
            return value * 2.54
        elif unit == "Inches to Millimeters":
            return value * 25.4
        elif unit == "Inches to Micrometers":
            return value * 25400
        elif unit == "Inches to Nanometers":
            return value * 2.54e+7
        elif unit == "Inches to Miles":
            return value * 1.5783e-5
        elif unit == "Inches to Yards":
            return value * 0.0277778
        elif unit == "Inches to Foots":
            return value * 0.0833333
        elif unit == "Inches to Nautical miles":
            return value * 1.3715e-5
        elif unit == "Nautical miles to Kilometers":
            return value * 1.852
        elif unit == "Nautical miles to Meters":
            return value * 1852
        elif unit == "Nautical miles to Millimeters":
            return value * 1.852e+6
        elif unit == "Nautical miles to Nanometers":
            return value * 1.852e+12
        elif unit == "Nautical miles to Micrometers":
            return value * 1.852e+9
        elif unit == "Nautical miles to Centimeters":
            return value * 185200
        elif unit == "Nautical miles to Miles":
            return value * 1.15078
        elif unit == "Nautical miles to Yards":
            return value * 2025.37
        elif unit == "Nautical miles to Foots":
            return value * 6076.12
        elif unit == "Nautical miles to Inchs":
            return value * 72913.4
    
    elif category == "Volume":
        if unit == "Liters to US Liquid Gallon":
            return value * 0.264172
        elif unit == "Liters to Liquid Quart":
            return value * 1.05669
        elif unit == "Liters to Liquid Pint":
            return value * 2.11338
        elif unit == "Liters to US Legal cup":
            return value * 4.16667
        elif unit == "Liters to US fluid Ounce":
            return value * 33.814
        elif unit == "Liters to Us Tablespoon":
            return value * 67.628
        elif unit == "Liters to US Teaspoon":
            return value * 202.884
        elif unit == "Liters to Cubic meter":
            return value * 0.001
        elif unit == "Liters to Cubic Foot":
            return value * 0.0353147
        elif unit == "Liters to Cubic Inch":
            return value * 61.0237
        elif unit == "Liters to Imperial Gallon":
            return value * 0.219969
        elif unit == "Liters to Imperial Quart":
            return value * 0.879877
        elif unit == "Liters to Imperial Cups":
            return value * 3.51951
        elif unit == "Liters to Imperial Pints":
            return value * 1.75975
        elif unit == "Liters to Milliliters":
            return value * 1000
        elif unit == "Liters to Imperial Fluid Ounce":
            return value * 35.1951
        elif unit == "Liters to Imperial Tablespoons":
            return value * 56.3121
        elif unit == "Liters to Imperial Teaspoons":
            return value * 168.936
        elif unit == "Gallons to Liters":
            return value * 3.78541
        elif unit == "Gallons to Quarts":
            return value * 0.0378541
        
    elif category == "Area":
        if unit == "Square meters to Square kilometers":
            return value * 1e-6
        elif unit == "Square meters to Square feet":
            return value * 10.7639
        elif unit == "Square meters to Square inches":
            return value * 1550
        elif unit == "Square meters to Square yards":
            return value * 1.19599
        elif unit == "Square meters to Acres":
            return value * 0.000247105
        elif unit == "Square meters to Hectares":
            return value * 0.0001
        elif unit == "Square meters to Square miles":
            return value * 3.86102e-7
        elif unit == "Square feet to Square meters":
            return value / 10.7639
        elif unit == "Square feet to Square inches":
            return value * 144
        elif unit == "Square feet to Acres":
            return value * 0.00092903
        elif unit == "Square kilometer to Square meters":
            return value * 1e+6
        elif unit == "Square kilometer to Square feet":
            return value * 1.076e+7
        elif unit == "Square kilometer to Acres":
            return value * 247.105
        elif unit == "Square Kilometers to Hectares":
            return value * 100
        elif unit == "Square Kilometers to Square inches":
            return value * 1.55e+9
        elif unit == "Square Kilometers to Square yards":
            return value * 1.196e+6
        elif unit == "Square Kilometers to Square miles":
            return value * 0.386102
        elif unit == "Square Miles to Square meters":
            return value * 2.59e+6
        elif unit == "Square Miles to Square feet":
            return value * 2.788e+7
        elif unit == "Square Miles to Acres":
            return value * 640
        elif unit == "Square Miles to Square yards":
            return value * 3.098e+6
        elif unit == "Square Miles to Square kilometers":
            return value * 2.58999
        elif unit == "Square Miles to Square inches":
            return value * 4.014e+9
        elif unit == "Square Miles to Hectares":
            return value * 258.999
        elif unit == "Square Yards to Square kilometers":
            return value * 8.3613e-7
        elif unit == "Square Yards to Square meters":
            return value * 0.836127
        elif unit == "Square Yards to Square miles":
            return value * 3.2283e-7
        elif unit == "Square Yards to Square inches":
            return value * 1296
        elif unit == "Square Yards to Square feet":
            return value * 9
        elif unit == "Square Yards to Acres":
            return value * 0.000206612
        elif unit == "Square Yards to Hectares":
            return value * 8.3613e-5
        elif unit == "Square Feets to Square kilometers":
            return value * 9.2903e-8
        elif unit == "Square Feets to Square meters":
            return value * 0.092903
        elif unit == "Square Feets to Square miles":
            return value * 3.587e-8
        elif unit == "Square Feets to Square yards":
            return value * 0.111111
        elif unit == "Square Feets to Sqaure inches":
            return value * 144
        elif unit == "Square Feets to Hectares":
            return value * 9.2903e-6
        elif unit == "Square Feets to Acres":
            return value * 2.2957e-5
        elif unit == "Square Inches to Square kilometrs":
            return value * 6.4516e-10
        elif unit == "Square Inches to Square meters":
            return value * 0.00064516
        elif unit == "Square Inches to Square yards":
            return value * 0.000771605
        elif unit == "Square Inches to Square miles":
            return value * 2.491e-10
        elif unit == "Square Inches to Square feets":
            return value * 0.00694444
        elif unit == "Square Inches to Acres":
            return value * 1.5942e-7
        elif unit == "Square Inches to Hectares":
            return value * 6.4516e-8
        elif unit == "Hectares to Square kilometers":
            return value * 0.01
        elif unit == "Hectares to Square meters":
            return value * 10000
        elif unit == "Hectares to Square miles":
            return value * 0.00386102
        elif unit == "Hectares to Square inches":
            return value * 1.55e+7
        elif unit == "Hectares to Square feets":
            return value * 107639
        elif unit == "Hectares to Square yards":
            return value * 11959.9
        elif unit == "Hectares to Acres":
            return value * 2.47105
        elif unit == "Acres to Square kilometers":
            return value * 0.00404686
        elif unit == "Acres to Square meters":
            return value * 4046.86
        elif unit == "Acres to Square miles":
            return value * 0.0015625
        elif unit == "Acres to Square yards":
            return value * 4840
        elif unit == "Acres to Square feets":
            return value * 43560
        elif unit == "Acres to Square inches":
            return value * 6.273e+6
        elif unit == "Acres to Hectares":
            return value * 0.404686
        
    elif category == "Frequency":
        if unit == "Hertzs to Kilohertzs":
            return value * 0.001
        elif unit == "Hertzs Megahertzs":
            return value * 1e-6
        elif unit == "Hertzs to Gigahertzs":
            return value * 1e-9
        elif unit == "Kilohertzs to hertzs":
            return value * 1000
        elif unit == "Kilohertzs to Megahertzs":
            return value * 0.001
        elif unit == "Kilohertzs to Gigahertzs":
            return value * 1e-6
        elif unit == "Megahertzs to Hertzs":
            return value * 1e+6
        elif unit == "Megahertzs to Kilohertzs":
            return value * 1e+6
        elif unit == "Megahertzs to Gigahertzs":
            return value * 0.001
        elif unit == "Gigahertzs to Hertzs":
            return value * 1e+9
        elif unit == "Gigahertzs to Kilohertzs":
            return value * 1e+6
        elif unit == "Gigahertzs to Kilohertzs":
            return value * 1000

    elif category == "Plane Angle":
        if unit == "Arcsecond to Degree":
            return value * 0.000277778
        elif unit == "Arcsecond to  Gradian":
            return value * 0.000308642
        elif unit == "Arcsecond to Milliradian":
            return value * 0.00484814
        elif unit == "Arcsecond to Minute of Arc":
            return value * 0.0166667
        elif unit == "Arcsecond to Radian":
            return value * 4.8481e-6
        elif unit == "Degree to Arcsecond":
            return value * 3600
        elif unit == "Degree to Gradian":
            return value * 1.11111
        elif unit == "Degree to Milliradian":
            return value * 17.4533
        elif unit == "Degree to Minute of Arc":
            return value * 60
        elif unit == "Degree to Radian":
            return value * 0.0174533
        elif unit == "Gradian to Arcsecond":
            return value * 3240
        elif unit == "Gradian to Degree":
            return value * 0.9
        elif unit == "Gradian to Milligradian":
            return value * 15.708
        elif unit == "Gradian to Minute of Arc":
            return value * 54
        elif unit == "Gradian to Radian":
            return value *0.015708
        elif unit == "Milliradian to Arcsecond":
            return value * 206.265
        elif unit == "Milliradian to Degree":
            return value * 0.0572958
        elif unit == "Milliradian to Gradian":
            return value * 0.063662
        elif unit == "Milliradian to Minute of Arc":
            return value * 3.43775
        elif unit == "Milliradian to Radian":
            return value * 0.001
        elif unit == "Minute of Arc to Arcsecond":
            return value * 60
        elif unit == "Minute of Arc to Degree":
            return value * 0.0166667
        elif unit == "Minute of Arc to Gradian":
            return value * 0.0185185
        elif unit == "Minute of Arc to Milliradian":
            return value * 0.290888
        elif unit == "Minute of Arc to Radian":
            return value * 0.000290888
        elif unit == "Radian to Arcsecond":
            return value * 206265
        elif unit == "Radian to Degree":
            return value * 57.2958
        elif unit == "Radian to Gradian":
            return value * 63.662
        elif unit == "Radian to Milliradian":
            return value * 1000
        elif unit == "Radian to Minute of Arc":
            return value * 3437.75

    elif category == "Mass":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Kilograms to Ounces":
            return value * 35.274
        elif unit == "Kilograms to Tons":
            return value / 1000
        elif unit == "Kilograms to Grams":
            return value * 1000
        elif unit == "Kilograms to Milligrams":
            return value * 1000000
        elif unit == "Kilograms to Micrograms":
            return value * 1000000000
        elif unit == "Kilograms to US Tons":
            return value * 0.00110231
        elif unit == "Kilograms to Imperial Tons":
            return value * 0.000984207
        elif unit == "Kilograms to Stone":
            return value * 0.157473
        elif unit == "Pounds to Kilograms":
            return value / 2.20462
    
    elif category == "Fuel Economy":
        if unit == "Mile Per Us Gallon to Mile Per Gallon":
            return value * 1.20095
        elif unit == "Mile Per Us Gallon to Kilometre Per Litre":
            return value * 0.425144
        elif unit == "Mile Per Us Gallon to Litre Per 1000 Kilometres":
            return value * 235.215
        elif unit == "Mile Per Gallon to Mile Per Us Gallon":
            return value * 0.832674
        elif unit == "Mile Per Gallon to Kilometre Per Litre":
            return value * 0.354006
        elif unit == "Mile Per Gallon to Litre Per 1000 Kilometres":
            return value * 282.481
        elif unit == "Kilometre Per Litre to Mile Per Us Gallon":
            return value * 2.35215
        elif unit == "Kilometre Per Litre to Mile Per Gallon":
            return value * 2.82481
        elif unit == "Kilometre Per Litre to Litre to 1000 Kilometres":
            return value * 100
        elif unit == "Litre Per 1000 Kilometres to Mile per Us Gallon":
            return value * 235.215
        elif unit == "Litre Per 1000 Kilometres to Mile Per Gallon":
            return value * 282.481
        elif unit == "Litre Per 1000 Kilometres to Kilometre Per Litre":
            return value * 100

    elif category == "Temperature":
        if unit == "Celsius to Fahrenheit":
            return (value * 9/5) + 32
        elif unit == "Fahrenheit to Celsius":
            return (value - 32) * 5/9
        elif unit == "Celsius to Kelvin":
            return value + 273.15
        elif unit == "Kelvin to Celsius":
            return value - 273.15
        elif unit == "Fahrenheit to Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif unit == "Kelvin to Fahrenheit":
            return (value - 273.15) * 9/5 + 32
    
    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24
    return 0        
if category == "Length":
    unit = st.selectbox("Select Conversation",["Miles to Kilometers","Kilometers to Miles","Kilometers to Meters","Kilometers to Centimeters","Kilometers to Millimeters","Kilometers to Micrometers","Kilometers to Nanometers","Kilometers to Inches","Kilometers to Foots","Kilometers to Yards","Kilometers to Nautical miles","Meters to Kilometers","Meters to Miles","Meters to Centimeters","Meters to Millimeters","Meters to Micrometers","Meters to Nanometers","Meters to Inches","Meters to Foots","Meters to Yards","Meters to Nautical miles","Centimeters to Kilometers","Centimeters to Miles","Centimeters to Meters","Centimeters to Millimeters","Centimeters to Micrometers","Centimeters to Nanometers","Centimeters to Inches","Centimeters to Foots","Centimeters to Yards","Centimeters to Nautical miles","Millimeters to Kilometers","Millimeters to Miles","Millimeters to Meters","Millimeters to Centimeters","Millimeters to Micrometers","Millimeters to Nanometers","Milli to Inches","Millimeters to Foots","Millimeters to Yards","Millimeters to Nautical miles","Micrometers to Kilometers","Micrometers to Miles","Micrometers to Meters","Micrometers to Centimeters","Micrometers to Millimeters","Micrometers to Nanometers","Micrometers to Inches","Micrometers to Foots","Micrometers to Yards","Micrometers to Nautical miles","Nanometers to Kilometers","Nanometers to Meters","Nanometers to Centimeters","Nanometers to Millimeters","Nanometers to Micrometers","Nanometers to Inches","Nanometers to Foots","Nanometers to Yards","Nanometers to Nautical miles","Nanometers to Miles","Inches to Kilometers","Inches to Miles","Inches to Meters","Inches to Centimeters","Inches to Millimeters","Inches to Micrometers","Inches to Nanometers","Inches to Foots","Inches to Yards","Inches to Nautical miles","Nautical miles to Kilometers","Nautical miles to Miles","Nautical miles to Meters","Nautical miles to Centimeters","Nautical miles to Millimeters","Nautical miles to Micrometers","Nautical miles to Nanometers","Nautical miles to Inches","Nautical miles to Foots","Nautical miles to Yards","Yards to Kilometers","Yards to Miles","Yards to Centimeters","Yards to Millimeters","Yards to Micrometers","Yards to Nanometers","Yards to Inches","Yards to Foots","Yards to Nautical miles","Foots to Kilometers","Foots to Miles","Foots to Meters","Foots to Centimeters","Foots to Millimeters","Foots to Micrometers","Foots to Nanometers","Foots to Inches","Foot to Yards","Foots to Nautical miles","Miles to Meters","Miles to Centimeters","Miles to Millimeters","Miles to Micrometers","Miles to Nanometers","Miles to Inches","Miles to Foots","Miles to Nautical miles","Miles to Yards"])

elif category == "Mass":
    unit = st.selectbox("Select Conversation",["Kilograms to Pounds","Kilograms to Ounces","Kilograms to Tons","Kilograms to Grams","Kilograms to Milligrams","Kilograms to Micrograms","Kilograms to US Tons","Kilograms to Imperial Tons","Kilograms to Stone","Pounds to Kilograms"])

elif category == "Area":
    unit = st.selectbox("Select Conversation",["Square Kilometers to Square miles","Square Miles to Square kilometers","Square Miles to Square meters","Square Miles to Square feets ","Square Miles to Hectares","Square Miles to Square Inches","Square Miles to Square Yards","Square Miles to Acres","Square Kilometers to Square inches","Square Kilometers to Square yards","Square Kilometers to Acres","Square Kilometers to Square feets","Square Kilometers to Square meters","Square Kilometers to Hectares","Square Inches to Square meters","Square Inches to Square feets","Square Inches to Hecatares","Square Inches to Square Miles","Square Inches to Square Kilometers","Square Inches to Square Yards","Square Inches to Acres","Square Yards to Square meters","Square Yards to Square feets","Square Yards to Hectares","Square Yards to Square Miles","Square Yards to Square Kilometers","Square Yards to Square Inches","Square Yards to Acres","Acres to Square meters","Acres to Square feets","Acres to Hectares","Acres to Square Miles","Acres to Square Kilometers","Acres to Square Inches","Acres to Square Yards","Square Meters to Square kilometers","Square Meters to Square yards","Square Meters to Square feets","Square Meters to Square inches","Square Meters to Hecaters","Square Meters to Acres","Square Meters to Square miles","Square Feets to Square kilometers","Square Feets to Square meters","Square Feets to Square yards","Square Feets to Square inches","Square Feets to Arces","Square Feets to Hectares","Square Feets to Square miles"])

elif category == "Temperature":
    unit = st.selectbox("Select Conversation",["Celsius to Fahrenheit","Fahrenheit to Celsius","Celsius to Kelvin","Kelvin to Celsius","Fahrenheit to Kelvin","Kelvin to Fahrenheit"])

elif category == "Frequency":
    unit = st.selectbox("Select Conversation",["Hertzs to Kilohertzs","Hertzs to Megahertzs","Hertzs to Gigahertzs","Kilohertzs to Hertzs","Kilohertzs to Megahertzs","Megahertzs to Hertzs","Megahertzs to Kilohertzs","Megahertzs to Gigahertzs","Kilohertzs to Gigahertzs","Gigahertzs to Hertzs","Gigahertzs to Kilohertzs","Gigahertzs to Megahertzs"])

elif category == "Plane Angle":
    unit = st.selectbox("Select Conversation",["Arcsecond to Degree","Arcsecond to Gradian","Arcsecond to Milligradian","Arcsecond to Minute of Arc","Arcsecond to Radian","Degree to Arcsecond","Degree to Gradian","Degree to Milligradian","Degree to Minute of Arc","Degree to Radian","Gradian to Arcsecond","Gradian to Degree","Gradian to Milliradian","Gradian to Minute of Arc","Gradian to Radian","Milligradian to Arcsecond","Milligradian to Degree","Milligradian to Gradian","Milligradian to Arc of second","Milligradian to Radian","Minute of Arc to Arcsecond","Minute of Arc to Degree","Minute of Arc to Gradian","Minute of Arc to Milligradian","Minute of Arc to Radian","Radian to Arcsecond","Radian to Degree","Radian to Gradian","Radian to Milligradian","Radian to Arc of second"])

elif category == "Fuel Economy":
    unit = st.selectbox("Select Converstaion",["Mile Per Us Gallon to Mile Per Gallon","Mile Per Us Gallon to Kilometre Per Litre","Mile Per Us Gallon to Litre Per 1000 Kilometres","Mile Per Gallon to Mile Per Us Gallon","Mile Per Gallon to Kilometre Per Litre","Mile Per Gallon to Litre Per 1000 Kilomtres","Kilometre Per Litre to Mile Per Us Gallon","Kilometre Per Litre to Mile Per Gallon","Kilometre Per Litre to Litre Per 1000 Kilometres","Litre Per 1000 Kilometres to Mile Per Us Gallon","Litre Per 1000 Kilometres to Mile Per Gallon","Litre Per 1000 Kilometres to Kilometre Per Litre"])

elif category == "Time":
    unit = st.selectbox("Select Converstaion",["Seconds to Minutes","Minutes to Seconds","Minutes to Hours","Hours to Minutes","Hours to Days","Days to Hours"])

value = st.number_input("Enter the Value to Convert")

if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The result is {result:.2f}")