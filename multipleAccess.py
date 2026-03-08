import pandas as pd
import random
import glob

files = glob.glob("*.xlsx") # to store all files in one 

for file in files:
    print(f"\nProcessing {file}...")
    df = pd.read_excel(file)

    x = df["A"].tolist() # set according to your filed instead A B and C
    y = df["B"].tolist()
    z = df["C"].tolist()

    def calculation(x, y, z):
        maxValue = float('-inf')
        maxW1 = maxW2 = maxW3 = 0
        maxFormula = ""

        def randomValues():
            w1 = random.random()
            w2 = random.uniform(0, 1 - w1)
            w3 = 1 - w1 - w2
            return w1, w2, w3

        for i in range(len(x)):
            w1, w2, w3 = randomValues()
            formula = w1*x[i] + w2*y[i] + w3*z[i]
            print(f"case{i+1} = {formula:.3f}  (x = {x[i]}, y = {y[i]}, z = {z[i]}) (w1 = {w1:.3f}, w2 = {w2:.3f}, w3 = {w3:.3f})")

            if formula > maxValue:
                maxValue = formula
                maxW1, maxW2, maxW3 = w1, w2, w3
                maxX, maxY, maxZ = x[i], y[i], z[i]
                maxFormula = f"case{i+1}"

   
        print("\nGreatest Value:- ")
        print(f"{maxFormula} = {maxValue:.3f}")
        print(f"x = {maxX}, y = {maxY}, z = {maxZ}")
        print(f"w1 = {maxW1:.3f}, w2 = {maxW2:.3f}, w3 = {maxW3:.3f}")


    calculation(x, y, z)
