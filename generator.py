import csv
from faker import Faker
import random
import datetime



with open('City_parkings.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=':',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    faker = Faker('pl_PL')
    types = ['rownolegle', 'prostopadle', 'ukosnie', 'inaczej']

    for i in range(250):
        rand_type = types[random.randrange(len(types))]
        spamwriter.writerow([str(i)] + [rand_type] + [str(random.randint(0, 1))]
                            )

with open('Park_rides.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=':',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    faker = Faker('pl_PL')

    for i in range(250):
        rand_type = types[random.randrange(len(types))]
        spamwriter.writerow([str(250+i)] + [str(random.randint(0, 1))] + [faker.cryptocurrency_name()]
                            )

with open('Kiss_rides.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=':',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    faker = Faker('pl_PL')

    for i in range(250):
        rand_type = types[random.randrange(len(types))]
        spamwriter.writerow([str(500+i)] + [str(random.randint(0, 30))] + [str(random.randint(0, 1))]
                            )
faker = Faker('pl_PL')
losu_losu = [faker.company()]
for i in range(500):
    losu_losu.append(faker.company())

with open('Estates.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=':',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    faker = Faker('pl_PL')

    for i in range(500):
        spamwriter.writerow([losu_losu[i]]
                            )

with open('Estate_parkings.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=':',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    faker = Faker('pl_PL')

    for i in range(250):
        rand_estate = losu_losu[random.randrange(len(losu_losu))]
        spamwriter.writerow([str(750+i)] + [rand_estate]
                            )


class Location:

    latitude = 1.00
    longitute = 1.00


losu_losu_loc = [Location()]
for i in range(1000):
    loc = Location()
    loc.latitude = faker.latitude()
    loc.longitute = faker.longitude()

    if loc not in losu_losu_loc:
        losu_losu_loc.append(loc)
    else:
        i=i-1

with open('Locations.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=':',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

    faker = Faker('pl_PL')

    for i in range(1001):
        rand_loc = losu_losu_loc[i]
        spamwriter.writerow([str(i)] + [str(rand_loc.latitude).replace(".", ",")] + [str(rand_loc.longitute).replace(".", ",")]
                            )


with open('Parkings.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=':',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    faker = Faker('pl_PL')

    for i in range(1000):
        rand_loc = losu_losu_loc[i]
        spamwriter.writerow([str(i)]
                            + [str(random.randint(1, 100))]
                            + [str(random.randint(0, 4))]
                            + [str(random.randint(0, 1))]
                            + [str(random.randint(0, 1))]
                            + [faker.date_between_dates(date_start=datetime.date(2017, 12, 3), date_end=datetime.date(2018, 12, 3))]
                            + [str(random.randint(3500, 8000))]
                            + [str(random.randint(150, 450))]
                            + [str(random.randint(0, 1000))]
                            )

with open('Parks.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter='|',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    faker = Faker('pl_PL')
    vehicle_id_array = list(range(0, 10000))
    random.shuffle(vehicle_id_array)

    for i in range(10000):
        spamwriter.writerow([faker.iso8601(tzinfo=None, end_datetime=None)]
                            + [str(vehicle_id_array[i])] #vehicle id
                            + [str(random.randint(0, 1000))]
                            )


with open('Engines.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=':',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    faker = Faker('pl_PL')
    engine = ['petrol', 'diesel', 'LNG', 'LPG', 'Electric',
             'Hybrid', 'Mild Hybrid']

    for i in range(len(engine)):

        spamwriter.writerow([engine[i]]
                            )

with open('Vehicle.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=':',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    faker = Faker('pl_PL')
    engine = ['petrol', 'diesel', 'LNG', 'LPG', 'Electric',
             'Hybrid', 'Mild Hybrid']

    for i in range(10000):
        rand_engine = engine[random.randrange(len(engine))]
        spamwriter.writerow([str(i)]+[faker.license_plate()] + [str(random.randint(1500, 8000))]
                            + [str(random.randint(100, 450))]
                            + [rand_engine] + [str(random.randint(0, 4999))]
                            )


with open('User.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=':',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    faker = Faker('pl_PL')
    card_number_array = list(range(0, 5000))
    random.shuffle(card_number_array)

    for i in range(5000):
        spamwriter.writerow([str(i)] + [faker.name().split(" ")[0]] + [faker.name().split(" ")[-1]]
                            + [faker.phone_number()] + [str(card_number_array[i])] + [str(random.randint(0, 5000))]
                            )


with open('Cards.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=':',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    faker = Faker('pl_PL')

    for i in range(5000):
        spamwriter.writerow([str(i)] + [faker.date_between_dates(date_start=datetime.date(2018, 12, 5), date_end=datetime.date(2025, 12, 5))]
                           )


class Country:
    country_name = faker.country()
    iso_code = faker.country_code(representation="alpha-2")


losu_losu_country = [Country()]

for i in range(10):
    country = Country()
    country.country_name = faker.country()
    country.iso_code = faker.country_code(representation="alpha-2")
    losu_losu_country.append(country)


with open('Countries.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=':',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

    faker = Faker('pl_PL')

    for i in range(10):
        spamwriter.writerow([losu_losu_country[i].country_name]
                             + [losu_losu_country[i].iso_code]
                            )

with open('Addresses.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=':',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

    faker = Faker('pl_PL')

    for i in range(5000):
        rand_country = losu_losu_country[random.randrange(len(losu_losu_country))]
        spamwriter.writerow([str(i)]
                            + [faker.city()] + [faker.postcode()]
                            + [faker.street_name()]
                            + [str(random.randint(1, 199))]
                            + [rand_country.country_name]
                            )

losu_losu_dept = [faker.company()]

for i in range(20):
    losu_losu_dept.append(faker.company())

with open('Departments.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=':',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

    faker = Faker('pl_PL')

    for i in range(20):
        spamwriter.writerow([losu_losu_dept[i]]
                            )


with open('Employees.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=':',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

    faker = Faker('pl_PL')

    for i in range(500):
        rand_dept = losu_losu_dept[random.randrange(len(losu_losu_dept))]
        spamwriter.writerow([str(i)] + [faker.name().split(" ")[0]] + [faker.name().split(" ")[-1]]
                            + [random.randint(1800, 5800)] + [rand_dept] + [str(random.randint(0, 1000))] + [str(random.randint(0, 1000))]
                            )
