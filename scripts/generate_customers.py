from faker import Faker
import csv

fake = Faker('en_US')
Faker.seed(42)

with open('fixtures/customers.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'email', 'phone', 'ssn', 'address', 'city', 'state', 'zip', 'dob', 'income'])
    
    for _ in range(1000):
        writer.writerow([
            fake.name(),
            fake.email(),
            fake.phone_number(),
            fake.ssn(),
            fake.street_address(),
            fake.city(),
            fake.state_abbr(),
            fake.zipcode().zfill(5),  # Ensure 5 digits with leading zeros
            fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d'),
            fake.random_int(min=20000, max=250000)
        ])

print('Generated 1000 rows of customer data')

