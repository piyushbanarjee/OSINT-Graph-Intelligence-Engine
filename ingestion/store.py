import sqlite3

db = sqlite3.connect('data/intelligence.db')
cursor = db.cursor()

cursor.execute('pragma foreign_keys = ON;')

cursor.execute('''create table if not exists documents(
            document_id integer primary key autoincrement,
            filename text,
            raw_text text,
            created_at timestamp default current_timestamp);''')
db.commit()


cursor.execute('''create table if not exists entities(
                entity_id integer primary key autoincrement,
                document_id int,
                name text,
                role text,
                created_at timestamp default current_timestamp,
                foreign key (document_id) references documents(document_id) on delete cascade,
                UNIQUE(document_id, name)
               );''')
db.commit()

cursor.execute('''create table if not exists relationships(
                relation_id integer primary key autoincrement,
                document_id int,
                origin text,
                destination text,
                label text,
                created_at timestamp default current_timestamp,
                foreign key (document_id) references documents(document_id) on delete cascade);''')
db.commit()


def save_document(filename, raw_text):
    cursor.execute("""insert into documents (filename, raw_text)
                       values (?, ?)""", (filename, raw_text))
    db.commit()
    return cursor.lastrowid

def save_entites(document_id, name, role):
    cursor.execute(""" 
    insert or ignore into entities (document_id, name, role)
    values (?,?,?)""", (document_id, name, role))
    db.commit()



def save_relationships(document_id, origin, destination, label):
    cursor.execute(""" 
    insert into relationships (document_id, origin, destination, label)
    values (?,?,?,?)""", (document_id, origin, destination, label))
    db.commit()

def entities_doc_id(name)-> list:
    cursor.execute("select document_id from entities where name = ?", (name,))
    rows = cursor.fetchall()
    docs = [row[0] for row in rows]
    return docs

def get_all_entity_data():
    cursor.execute("select distinct name, role from entities ")
    rows = cursor.fetchall()
    names = [row[0] for row in rows]
    roles = [row[1] for row in rows]
    return names, roles

def get_all_relationship_data():
    cursor.execute("select distinct origin, destination, label from relationships ")
    rows = cursor.fetchall()
    origin = [row[0] for row in rows]
    destination = [row[1] for row in rows]
    label = [row[2] for row in rows]
    return origin, destination, label
    
if __name__ == "__main__":
    pass