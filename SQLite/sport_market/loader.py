import sqlite3 as sql
with sql.connect('SQLite/sport_market/market.db') as db:
    cursor = db.cursor()
#■ о товарах: название товара, вид товара (одежда, обувь,
#и т.д.), количество товара в наличии, себестоимость,
#производитель, цена продажи;
    cursor.execute('''
CREATE TABLE IF NOT EXISTS product(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
type_product TEXT NOT NULL,
quantity INTEGER NOT NULL CHECK(quantity >= 0),
purchase REAL NOT NULL CHECK(purchase >= 0),
maker TEXT NOT NULL,
sale REAL NOT NULL CHECK(sale >= 0))
''')
#■ о сотрудниках: ФИО сотрудника, должность, дата
#приёма на работу, пол, зарплата;
    cursor.execute('''
CREATE TABLE IF NOT EXISTS worker(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
role TEXT NOT NULL,
data_to_start TEXT NOT NULL,
sex TEXT NOT NULL,
salary REAL NOT NULL CHECK(salary >= 0))
''')
#■ о клиентах: ФИО клиента, email, контактный телефон,
#пол, история заказов, процент скидки, дата регистрации, подписан ли на почтовую рассылку
    cursor.execute('''
CREATE TABLE IF NOT EXISTS client(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
email TEXT NOT NULL,
phone TEXT NOT NULL,
sex TEXT NOT NULL,
history TEXT,
procent_discount INTEGER, 
data TEXT NOT NULL,
check_spam INTEGER NOT NULL DEFAULT (0))
''')
    
#■ о продажах: название проданного товара, цена продажи, количество, дата продажи, информация о продавце (ФИО сотрудника, выполнившего продажу),
#информация о покупателе (ФИО покупателя, если
#купил зарегистрированный покупатель);    
    cursor.execute('''
CREATE TABLE IF NOT EXISTS deal(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
id_product INTEGER,
sale REAL NOT NULL CHECK(sale >= 0),
quantity INTEGER NOT NULL CHECK(quantity >= 0),
date TEXT NOT NULL,
id_worker INTEGER,
id_client INTEGER NOT NULL,
FOREIGN KEY (id_product) REFERENCES product(id),
FOREIGN KEY (id_worker) REFERENCES worker(id),
FOREIGN KEY (id_client) REFERENCES client(id) )                
                   ''')
    
    cursor.execute('''
CREATE TABLE IF NOT EXISTS history_deal(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
id_product INTEGER,
sale REAL NOT NULL CHECK(sale >= 0),
quantity INTEGER NOT NULL CHECK(quantity >= 0),
date TEXT NOT NULL,
id_worker INTEGER,
id_client INTEGER NOT NULL,
FOREIGN KEY (id_product) REFERENCES product(id),
FOREIGN KEY (id_worker) REFERENCES worker(id),
FOREIGN KEY (id_client) REFERENCES client(id))
''')
    
    cursor.execute('''
CREATE TABLE IF NOT EXISTS archive(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
id_product INTEGER,
sale REAL NOT NULL CHECK(sale >= 0),
quantity INTEGER NOT NULL CHECK(quantity >= 0),
date TEXT NOT NULL,
FOREIGN KEY (id_product) REFERENCES product(id))
''')     

