from dataclasses import dataclass


class Book:
    def __init__(self):
        self.title: str
        self.author: str
        self.publication_date: str