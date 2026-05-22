temperature = float(input("Enter the temperature: ").strip())

if temperature < 0:
    print("Freezing Cold")
elif temperature <= 10:
    print("Very Cold")
elif temperature <= 20:
    print("Cold")
elif temperature <= 30:
    print("Pleasant")
elif temperature <= 40:
    print("Hot")
else:
    print("Very Hot")