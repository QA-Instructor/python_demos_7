import sys

print("This is Python's path where it looks for modules:")
print(sys.path)

print("\nAs individual items:")
for place in sys.path:
    print(place)

print("\nYou can add locations to this path:")
sys.path.append('./demomodules')

for place in sys.path:
    print(place)
