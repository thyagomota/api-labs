import sqlite3

def get_entity_name(table):
    s = ''
    for w in table.split('_'):
        s += w.capitalize()
    return s

conn = sqlite3.connect('db/quotes.db')
if conn: 

    # yaml header 
    print('''openapi: 3.0.0
info:
    title: Quotes API
    version: "1.0"
components: 
    schemas:''')

    # db introspection: get tables metadata
    cur = conn.cursor()
    sql = """
        SELECT * FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'
    """
    cur.execute(sql)
    tables = []
    for row in cur.fetchall():
        tables.append(row[1])
    
    for table in tables:
        entity_name = get_entity_name(table)
        sql = f"""
            PRAGMA table_info({table})
        """
        print(f'        {entity_name}:')
        cur.execute(sql)
        required = '            required:\n'
        properties = '            type: object\n            properties:\n'
        for row in cur.fetchall():
            column, type, null, pkey = row[1], row[2], row[3], row[5]
            if type.startswith('INT'):
                type = 'integer'
            elif type.startswith('VARCHAR'):
                type = 'string'
            elif type.startswith('FLOAT'):
                type = 'number'
            if null == 1 or pkey:
                required += f'                - {column}\n'
            properties += f'                {column}:\n                    type: {type}\n'
        print(required, end='')
        print(properties, end='')
    
    conn.close()