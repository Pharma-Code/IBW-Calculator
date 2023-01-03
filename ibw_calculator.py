import sys
import os

def main():
    #Display Title and Instructions
    print("Pharma-Code: Ideal Body Weight Calculator")
    print("Input the Weight (kg), Height (m), Select the Gender and Formula to Calculate Ideal Body Weight.")

    #Receive Inputs
    weight = input("Input the Weight (kg): ")
    height = input("Input the Height (m): ")

    gender = input('''Select the Gender
    1. Male
    2. Female
    Input the number that corresponds to the gender: ''')

    formula = input('''Select the Formula
    1. Common Formula
    2. GJ Hamwi's Formula (1964)
    3. BJ Devine's Formula (1974)
    4. JD Robinson's Formula (1983)
    5. DR Miller's Formula (1983)
    Input the number that corresponds to the formula: ''')

    #Convert to Numeric Formats
    weight = convert_to_float(weight)
    height = convert_to_float(height)
    gender = convert_to_int(gender)
    formula = convert_to_int(formula)

    #Validate Inputs
    if gender not in range(1, 3):
        print("Invalid Input! Input does not correspond with any gender.")
        sys.exit()

    if formula not in range(1, 6):
        print("Invalid Input! Input does not correspond with any formula.")
        sys.exit()

    #Match the Formula
    match formula:
        case 1:
            common_formula(weight, height, gender)
        case 2:
            hamwi_formula(weight, height, gender)
        case 3:
            devine_formula(weight, height, gender)
        case 4:
            robinson_formula(weight, height, gender)
        case 5:
            miller_formula(weight, height, gender)

    #Prevent Script from Closing
    os.system("PAUSE")

def convert_to_float(value):
    try:
        return float(value)
    except:
        print("Please, input numeric values only.")
        sys.exit()

def convert_to_int(value):
    try:
        return int(value)
    except:
        print("Please, input numeric values only.")
        sys.exit()

def common_formula(weight, height, gender):
    multiplier = 0.0

    #Male
    if gender == 1:
        multiplier = height ** 2
    #Female
    else:
        multiplier = (height - 0.1) ** 2

    ibw = 22 * multiplier
    ibw = round(ibw, 1)

    display_results(weight, ibw)

def hamwi_formula(weight, height, gender):
    addition_factor = 0.0
    multiplier = 0.0

    #Male
    if gender == 1:
        addition_factor = 48.0
        multiplier = 2.7
    #Female
    else:
        addition_factor = 45.5
        multiplier = 2.2

    height_ft = convert_to_ft(height)

    ibw = addition_factor + (multiplier * (height_ft - 5))
    ibw = round(ibw, 1)

    display_results(weight, ibw)

def devine_formula(weight, height, gender):
    addition_factor = 0.0
    multiplier = 2.3

    #Male
    if gender == 1:
        addition_factor = 50.0
    #Female
    else:
        addition_factor = 45.5

    height_ft = convert_to_ft(height)

    ibw = addition_factor + (multiplier * (height_ft - 5))
    ibw = round(ibw, 1)

    display_results(weight, ibw)

def robinson_formula(weight, height, gender):
    addition_factor = 0.0
    multiplier = 0.0

    #Male
    if gender == 1:
        addition_factor = 52.0
        multiplier = 1.9
    #Female
    else:
        addition_factor = 49.0
        multiplier = 1.7

    height_ft = convert_to_ft(height)

    ibw = addition_factor + (multiplier * (height_ft - 5))
    ibw = round(ibw, 1)

    display_results(weight, ibw)

def miller_formula(weight, height, gender):
    addition_factor = 0.0
    multiplier = 0.0

    #Male
    if gender == 1:
        addition_factor = 56.2
        multiplier = 1.4
    #Female
    else:
        addition_factor = 53.1
        multiplier = 1.36

    height_ft = convert_to_ft(height)

    ibw = addition_factor + (multiplier * (height_ft - 5))
    ibw = round(ibw, 1)

    display_results(weight, ibw)

def convert_to_ft(value):
    return value * 3.28084

def display_results(weight, ibw):
    indication = ""
    percentage_difference = ((weight - ibw) / ibw) * 100
    percentage_difference = round(percentage_difference, 1)

    if percentage_difference > 30:
        indication = "Obese"
    else:
        indication = "Normal"

    print(f"Ideal Body Weight: {ibw}kg")
    print(f"Percentage Difference: {percentage_difference}%")
    print(f"Indication: {indication}")

if __name__ == "__main__":
    main()
