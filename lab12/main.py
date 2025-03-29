# import mammal
from mammal import Mammal
from person import Person

m = Mammal(10)
m.speak()
# Mammal.speak(m)  # Is the same thing as above

p = Person("John Doe", 20, 6)
p.speak()