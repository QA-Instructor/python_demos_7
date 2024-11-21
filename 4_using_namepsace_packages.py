import sys

print(sys.path)

sys.path.append('namespacepackageA')
sys.path.append('namespacepackageB')

print(sys.path)

# namespaces can be spread across multiple directories
# if multiple directories have a sub-directory with the same name.
# Both namespacepackageA and B have a subdir called subpackageA.
# It's the subdirectory name that is used for the namespace.

from subpackageA.restaurant import Restaurant
from subpackageA.delivery_driver import DeliveryDriver

r1 = Restaurant()
print(r1.get_name())

d1 = DeliveryDriver("Bob")
print(d1.get_name())

# __name__ shows the name of a module
print(r1.get_module_name())