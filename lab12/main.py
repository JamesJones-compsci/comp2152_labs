# import mammal
from mammal import Mammal
from person import Person
from tick import Tick
from puma import Puma

m = Mammal(10)
print(m)
d = str(m)
print(d)
# d = m.__str__()
# print(d)

m.speak()
# Mammal.speak(m)  # Is the same thing as above

p = Person("John Doe", 20, 6)
p.speak()
print(p)
p.heart.beat()
print(p.heart)

print(m.heart == p.heart)


t = Tick()
t.suck_blood()

pm = Puma(5, t)
pm.tick.suck_blood()

print(pm)
pm.claw()

pm2 = Puma(3)
pm2.claw()