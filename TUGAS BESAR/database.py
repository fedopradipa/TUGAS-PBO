import mysql.connector


def create_database_connection():
    return mysql.connector.connect(
        host="sql.freedb.tech",
        user="freedb_admin_warnet",
        password="c%A&bxN4vJ#P$Ug",
        database="freedb_warnet"
    )


def create_tables():
    connection = create_database_connection()
    cursor = connection.cursor()

    try:
        # Tabel Pengguna
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                fullname VARCHAR(255),
                gender VARCHAR(10),
                age INT,
                username VARCHAR(50) UNIQUE,
                password VARCHAR(255)
            )
        """)

        # Tabel Penyewaan
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS rentals (
                id INT AUTO_INCREMENT PRIMARY KEY,
                id_pesan INT, 
                name VARCHAR(50),
                computer VARCHAR(10),
                duration INT,
                price INT,
                order_time TIME,
                end_time TIME,
                order_date DATE,
                status_pembayaran ENUM('LUNAS', 'BELUM LUNAS') DEFAULT 'BELUM LUNAS'
              
            )
        """)

        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    create_tables()
