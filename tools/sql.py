import sqlite3
from langchain.tools import Tool
conn = sqlite3.connect("db.sqlite")

def list_tables():
    c = conn.cursor()
    c.execute("SELECT name from sqlite_master WHERE type='table';")
    rows = c.fetchall()
    return "/n".join(row[0] for row in rows if row[0] is not None)


def run_sqlite_query(query):
    # execute this query against db
    c = conn.cursor()
    try:
        c.execute(query)
        return c.fetchall()
    except sqlite3.OperationalError as err:
        return f"The error occured: {str(err)}"

run_query_tool = Tool.from_function(
    name="run_sqlite_query",
    description="Runs a sql query. returns the result",
    func=run_sqlite_query
)

def describe_tables(table_names):
    tables = ", ".join("'" + table + "'" for table in table_names)
    c = conn.cursor()
    rows = c.execute(f"SELECT sql form sqlite_master WHERE type='table' and name IN ({tables});")
    return "\n".join(row[0] for row in rows if row[0] is not None)

describe_tables_tool = Tool.from_function(
    name="describe_tables",
    description="it takes list of table names. and provides the columns with their description for each table",
    func=describe_tables
)