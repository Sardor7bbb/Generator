from Database import Database_db


def task_1(name):
    query = f"""SELECT * FROM film WHERE title LIKE '{name}%'"""
    return Database_db.connect(query)


def task_2(name):
    query = f"""SELECT * FROM customer WHERE first_name LIKE '{name}%'"""
    return Database_db.connect(query)


def task_3(name):
    query = f"""SELECT * FROM actor WHERE first_name LIKE '{name}%' """
    return Database_db.connect(query)


def main():
    name = input("Qidiruv: ")
    yield task_1(name)

    yield task_2(name)
    yield task_3(name)
    return main()

if __name__ == '__main__':
    natija = 0
    qiymat = 0
    for result in main():
        natija += 1
        for row in result:
            qiymat += 1
            print(row)

    print(f"""==========================================================================================================
    {natija} ta tablitsadan 
    {qiymat} ta malumot topildi.""")
