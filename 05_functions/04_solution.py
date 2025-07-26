# Circle Statistics
import math

def circle_stats(radius):
    area = round(math.pi * radius ** 2, 2)
    circumference = round(2 * math.pi * radius, 2)
    return area, circumference

# Usage - Unpacking multiple return values
area, circumference = circle_stats(3)
print(f"Area: {area}")
print(f"Circumference: {circumference}")