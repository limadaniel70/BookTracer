class Transaction:
    def __init__(self, user: int, book: int, transaction_date: str, expiration_date: str, status: str) -> None:
        self.user_id = user,
        self.book_id = book,
        self.transaction_date = transaction_date
        self.expiration_date = expiration_date
        self.status = status