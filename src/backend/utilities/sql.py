import psycopg2
from typing import Dict, List, Tuple


class PgSql:
    """Apply methods to a PG database."""

    def __init__(self, database: str, user: str, password: str, host: str, port: str):
        """Init"""
        self.conn = psycopg2.connect(
            database=database, user=user, host=host, password=password, port=port
        )
        self.cursor = self.conn.cursor()

    def create_database(self, database: str):
        """Create a database."""
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()

        check = f"SELECT 1 FROM pg_database WHERE datname = '{database}';"
        self.cursor.execute(check)
        exists = self.cursor.fetchone()

        if exists:
            raise psycopg2.Error(f"Database {database} already exists.")
        else:
            self.cursor.execute(f"CREATE DATABASE {database};")

        self.conn.autocommit = False

    def execute_query(self, query: str) -> List[Tuple]:
        """Execute a query and return results."""
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.conn.commit()
        return rows

    def insert_row(table: str, **kwargs: Dict[str, str]) -> bool:
        """
        Insert a row into a table
        """
        conn, cur = db_conn()

        fields = fields = "(" + ", ".join(tuple(kwargs.keys())) + ")"
        placeholders = ", ".join(["%s"] * len(kwargs))
        values = tuple(kwargs.values())

        query = f"INSERT INTO {table} {fields} VALUES({placeholders});"
        cur.execute(query, values)

        conn.commit()
        cur.close()
        conn.close()
        return True

    def close_conn(self):
        """Close connection"""
        self.conn.close()
