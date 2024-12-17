import sqlite3
from faker import Faker
import random

fake = Faker()


def faker_products():
    conn = sqlite3.connect("./back/bdd.sqlite")
    cursor = conn.cursor()

    for i in range(924):
        name = fake.word()
        description = fake.sentence()
        price = round(random.uniform(10, 200), 2)
        rdm = random.randint(1, 1000)
        image_url = f"https://picsum.photos/300/400?random=${rdm}"

        cursor.execute('''
            INSERT INTO products (id, name, description, price, image_url)
            VALUES (?, ?, ?, ?, ?)
        ''', (i, name, description, price, image_url))
        i+=1

    conn.commit()
    conn.close()
