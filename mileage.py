print("How many kilometers did you run today?")
kms = input()
miles = round(float(kms)/1.60934, 2)
print(f"Your {kms} run was {miles} miles today.")
