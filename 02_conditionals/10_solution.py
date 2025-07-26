# "Recommend a type of food for a pet based on species and age."
# Requirements:

# For Dogs:

# Less than 2 years old → Puppy food
# 2 years and above → Adult food


# For Cats:

# Above 5 years → Senior cat food
# 5 years and below → Junior cat food

pet_species = input("Enter pet species (dog/cat): ").strip().lower()
pet_age = int(input("Enter pet age in years: "))

if pet_species == "dog":
    if pet_age < 2:
        food = "Puppy food"
    else:
        food = "Adult food"
elif pet_species == "cat":
    if pet_age > 5:
        food = "Senior cat food"
    else:
        food = "Junior cat food"
else:
    food = "Unknown species"

print(f"Recommended food: {food}")