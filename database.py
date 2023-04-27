import mariadb
import config

def connect():
    """Connect to the database and return a connection object"""
    try:
        conn = mariadb.connect(
            host=config.DB_HOST,
            port=config.DB_PORT,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            database=config.DB_NAME
        )
        return conn
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB: {e}")
        return None

def create_product_table():
    """Create the product table if it doesn't already exist"""
    conn = connect()
    if conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS product (
                id VARCHAR(10) PRIMARY KEY,
                name VARCHAR(100),
                price DECIMAL(10, 2)
            )
        """)
        conn.commit()
        conn.close()

def get_products():
    """Retrieve all products from the product table"""
    conn = connect()
    if conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM product")
        rows = cur.fetchall()
        conn.close()
        products = []
        for row in rows:
            product = {
                "id": row[0],
                "name": row[1],
                "price": row[2]
            }
            products.append(product)
        return products
    else:
        return []

def add_product(name, price):
    """Add a new product to the product table"""
    conn = connect()
    if conn:
        cur = conn.cursor()
        id = generate_id()
        cur.execute("INSERT INTO product (id, name, price) VALUES (?, ?, ?)", (id, name, price))
        conn.commit()
        conn.close()
        return id
    else:
        return None

def update_product(id, name, price):
    """Update an existing product in the product table"""
    conn = connect()
    if conn:
        cur = conn.cursor()
        cur.execute("UPDATE product SET name = ?, price = ? WHERE id = ?", (name, price, id))
        conn.commit()
        conn.close()

def delete_product(id):
    """Delete an existing product from the product table"""
    conn = connect()
    if conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM product WHERE id = ?", (id,))
        conn.commit()
        conn.close()
