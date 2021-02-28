# to create a class

class Employee:
    hero = "Superhero"
    villian = "Supervillian"
    pass

# to create objects

sam = Employee()
peter = Employee()
thanos = Employee()
loki = Employee()

# Creating variables for objects

sam.name = "Sam Alexander"
sam.aka = "Nova"
sam.hindiname = "Ulti Balti"

peter.name = "Peter Parker"
peter.aka = "Spider Man"
peter.hindiname = "Makkad Manav"

loki.name = "Loki Odinson"
loki.aka = "Loki"
loki.hindiname = "Lauki"
# to create an instance variable
loki.villian = "Most of the time Supervillian but sometimes as a hero"

thanos.name = "Thanos"
thanos.aka = "The Mad Titan"
thanos.hindiname = "Baigan"

print(f'Employees \n1. {sam.name} aka {sam.aka} is known as "{sam.hindiname}" in Hindi and he works as a {sam.hero}.\n2. {peter.name} aka {peter.aka} is known as "{peter.hindiname}" in Hindi and he works as {peter.hero}.\n3. {loki.name} aka {loki.aka} is known as "{loki.hindiname}" and he works as a {loki.villian}.\n4. {thanos.name} aka {thanos.aka} is known as "{thanos.hindiname}" and works as a {thanos.villian}.')
