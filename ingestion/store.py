import sqlite3

db = sqlite3.connect('data/intelligence.db')
cursor = db.cursor()


cursor.execute('''create table if not exists documents(
            id integer primary key autoincrement,
            filename varchar(50),
            raw_text varchar(500000),
            created_at timestamp default current_timestamp);''')
db.commit()



cursor.execute('pragma foreign_keys= ON;')
cursor.execute('''create table if not exists entity_candidates(
                id integer primary key autoincrement,
                document_id int,
                entity_type varchar(50),
                entity_name varchar(50),
                created_at timestamp default current_timestamp,
                foreign key (document_id) references documents(id) on delete cascade); ''')
db.commit()

    
def save_document(filename, raw_text):
    cursor.execute(""" insert into documents (filename, raw_text)
                   values (?, ?) """, (filename, raw_text))
    db.commit()
    return cursor.lastrowid


if __name__ == "__main__":
    pass