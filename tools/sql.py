import sqlite3
from langchain.tools import Tool
conn = sqlite3.connect("db.sqlite")


def run_sqlite_query(query):
    # execute this query against db
    c = conn.cursor()
    c.execute(query)
    return c.fetchall()

run_query_tool = Tool.from_function(
    name="run_sqlite_query",
    description="Runs a sql query. returns the result",
    func=run_sqlite_query
)