import sqlite3

DB_PATH = 'exmple'

def db_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn



def create_tables():
    queries = [
        """ 
        CREATE TABLE IF NOT EXISTS bills_membership(
            id VARCHAR,
            date DATE,
            place VARCHAR,
            usage VARCHAR
            amount INTEGER,
        )
        """,

        """ 
        CREATE TABLE IF NOT EXISTS miscellanious_expence(
            id VARCHAR,
            date DATE,
            place VARCHAR,
            usage VARCHAR,
            amount INTEGER
        )
        """,

        """ 
        CREATE TABLE IF NOT EXISTS upskill_learning(
            id VARCHAR,
            date DATE,
            place VARCHAR,
            usage VARCHAR,
            amount INTEGER
        )
        """,

        """ 
        CREATE TABLE IF NOT EXISTS necessary_expence(
            id VARCHAR,
            date DATE,
            name VARCHAR,
            amount INTEGER,
            importance VARCHAR,
            frequency VARCHAR
        )
        """,

        """ 
        CREATE TABLE IF NOT EXISTS investments_savings(
            id VARCHAR,
            date DATE,
            type VARCHAR,
            interest REAL,
            amount INTEGER,
            duration INTEGER,
            starting_date DATE,
            maturity_date DATE
        )
        """,

        """ 
        CREATE TABLE IF NOT EXISTS loan_emi(
            id VARCHAR,
            date DATE,
            type VARCHAR,
            interest REAL,
            amount INTEGER,
            duration INTEGER,
            outstanding_amount INTEGER,
            starting_date DATE,  
            end_date DATE,  
            paid_instalment INTEGER,
            remaining_instalment INTEGER
        )
        """, 
    ]
    try:
        conn = db_connection()
        cursor = conn.cursor()
        for query in queries:
            cursor.execute(query)
        conn.commit()
    except Exception as e:
        print("Some error may occure...")
        print(e)
    finally:
        conn.close()

def get_records(table_name:str):
    try:
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM {table_name}')
        records = cursor.fetchall()
        return records
    except Exception as e:
        print("Some error may occure...")
        print(e)
    finally:
        conn.close()

def delete_record(id:str,table_name:str):
    try:
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute(f'''DELETE FROM {table_name} WHERE id=?''',(id))
        conn.commit()
        print('record deleted.')
    except Exception as e:
        print("Some error may occure...")
        print(e)
    finally:
        conn.close()

def add_newExpence(table_name:str,record:tuple):
    try:
        conn = db_connection()
        cursor = conn.cursor()
        if table_name in ('bills_membership','miscellanious_expence','upskill_learning'):
            cursor.execute(F'''INSERT INTO {table_name} VALUES (?,?,?,?,?)''',record)
            conn.commit()
        elif table_name == 'necessary_expence':
            cursor.execute(F'''INSERT INTO {table_name} VALUES (?,?,?,?,?,?)''',record)
            conn.commit()
        elif table_name == 'investments_savings':
            cursor.execute(F'''INSERT INTO {table_name} VALUES (?,?,?,?,?,?,?,?)''',record)
            conn.commit()
        elif table_name == 'loan_emi':
            cursor.execute(F'''INSERT INTO {table_name} VALUES (?,?,?,?,?,?,?,?,?,?,?)''',record)
            conn.commit()
        else:
            print('No table exists.')
    except Exception as e:
        print("Some error may occure.")
        print(e)
    finally:
        conn.close()

def update_record(table_name:str, id:str, record:tuple):
    try:
        conn = db_connection()
        cursor = conn.cursor()
        if table_name in ('bills_membership','miscellanious_expence','upskill_learning'):
            cursor.execute(F'''UPDATE {table_name} SET place=?,usage=?,amount=? WHERE id = ?''',(*record, id))          
            conn.commit()
        elif table_name == 'necessary_expence':
            cursor.execute(f'UPDATE {table_name} SET name=?,amount=?,importance=?,frequency=? WHERE id=?',(*record,id))
            conn.commit()
        elif table_name == 'investments_savings':
            cursor.execute(f'UPDATE {table_name} SET type=?,interest=?,amount=?,duration=? WHERE id=?',(*record,id))
            conn.commit()
        elif table_name == 'loan_emi':
            cursor.execute(f'UPDATE {table_name} SET type=?,interest=?,amount=?,duration=?,outstanding_amount=? WHERE id=?',(*record,id))
            conn.commit()
        else:
            print('No table exists.')
    except Exception as e:
        print("Some error may occure...")
        print(e)
    finally:
        conn.close()
