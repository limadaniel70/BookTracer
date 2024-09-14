import sqlite3


class Database:
    def __init__(self, db_name: str) -> None:
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_book_table()
        self.create_user_table()
        self.create_transaction_table()

    def close_connection(self) -> None:
        self.conn.close()

    def create_user_table(self) -> None:
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Users(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT,
            phone TEXT,
            creation_date TEXT
            )
            """
        )

    def create_book_table(self) -> None:
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Books(
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            publication_date TEXT NOT NULL,
            publisher TEXT NOT NULL,
            edition INTEGER NOT NULL
            )
            """
        )

    def create_transaction_table(self) -> None:
        self.cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Transactions(
        transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        book_id INTEGER NOT NULL,
        transaction_date TEXT NOT NULL,
        expiration_date TEXT NOT NULL,
        status TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES Users(user_id),
        FOREIGN KEY (book_id) REFERENCES Books(book_id)
        )
        """
    )
        
    # TODO: adicionar metodos CRUD para cada entidade.

if __name__ == "__main__":
    db = Database("test.db")