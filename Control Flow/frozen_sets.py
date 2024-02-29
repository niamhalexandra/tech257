# Part 1 - Create a frozen set named frozen_set containing elements "hello", "world".
frozen_set = frozenset({"hello", "world"})
print(frozen_set)
# Part 2 - Try to add "!" to frozen_set.
#frozen_set.add("!")
# What happens = it won't let you add the "!", gives attribute error
# Create a normal set (normal_set) containing "let's" "learn"
normal_set = set(["let's", "learn"])
# Try to add frozen_set to normal_set
normal_set.add(frozen_set)
print(normal_set)
# Why does it work = the frozen set itself becomes an element when added to the normal set
# Allowing for frozen sets to be used as elements in collections like sets or lists

# Each time you run the script the items in the frozen set can change order, this is because frozen sets are immutable meaning they have no set order
