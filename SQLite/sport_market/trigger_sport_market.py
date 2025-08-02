import sqlite3 as s
with s.connect('SQLite/sport_market/market.db') as file:
    cursor = file.cursor()
    cursor.execute('''
CREATE TRIGGER add_history_deal
BEFORE INSERT ON main.deal
FOR EACH ROW
BEGIN
INSERT INTO history_deal(id_product, sale, quantity, date, id_worker, id_client)
VALUES(NEW.id_product, NEW.sale, NEW.quantity, NEW.date, NEW.id_worker, NEW.id_client);
END;
''')
    cursor.execute('''
INSERT INTO deal(id_product, sale, quantity, date, id_worker, id_client) VALUES (1, 7, 1, '08-07-2025', 1, 1)
''')
    cursor.execute('''SELECT * FROM deal, history_deal''')
    data = cursor.fetchall()
    print(data)

#super_joe@mail
    cursor.execute('''
CREATE TRIGGER prevent_duplicate_email_update
BEFORE UPDATE ON client
FOR EACH ROW
BEGIN
    SELECT
    CASE
        WHEN EXISTS (
            SELECT * FROM client WHERE email = NEW.email AND OLD.id != id
        ) THEN
            RAISE(ABORT, 'Email уже существует')
    END;
END;
''')
