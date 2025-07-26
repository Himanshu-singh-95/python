
order_size = input("Enter the size of your coffee (small, medium, large): ").strip().lower()
extra_shot = input("Do you want an extra shot? (yes/no): ").strip().lower() == 'yes'

if extra_shot:
    coffee = order_size.capitalize() + " Coffee with an extra shot"
else:
    coffee = order_size.capitalize() + " Coffee"

print(f"Order: {coffee}")