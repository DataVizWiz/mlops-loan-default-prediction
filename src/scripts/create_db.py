"""Create database for Model tracking."""

from os import environ
from backend.utilities.sql import PgSql

if __name__ == "__main__":
    un = environ["DB_USER"]
    pw = environ["DB_PASSWORD"]

    pg = PgSql("postgres", un, pw, "localhost", 5432)
    print(pg.conn)
    print(pg.cursor)
    pg.create_database("logs")
