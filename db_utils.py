import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
from mysql.connector import Error
from sqlalchemy import MetaData, Table, Column, Integer, String, Boolean, Text, BigInteger, Float, TIMESTAMP, Enum


def create_connection(host_name, user_name, user_password, db_name=None):
    """
    Creates a connection to the MySQL database.

    Args:
        host_name (str): The hostname of the MySQL server.
        user_name (str): The username to authenticate with.
        user_password (str): The password to authenticate with.
        db_name (str, optional): The name of the database to connect to. Defaults to None.

    Returns:
        mysql.connector.connection_cext.CMySQLConnection: The connection object to the MySQL database.
    """

    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            port=3306,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def create_sqlalchemy_engine(user, password, host, db):
    """
    Creates a SQLAlchemy engine for connecting to the MySQL database.

    Args:
        user (str): The username to authenticate with.
        password (str): The password to authenticate with.
        host (str): The hostname of the MySQL server.
        db (str): The name of the database to connect to.

    Returns:
        sqlalchemy.engine.Engine: The SQLAlchemy engine connected to the MySQL database.
    """

    url = f'mysql+mysqlconnector://{user}:{password}@{host}/{db}'
    engine = create_engine(url)
    return engine


def execute_query(conn, query):
    """
    Executes a SQL query on the MySQL database.

    Args:
        connection (mysql.connector.connection_cext.CMySQLConnection): The connection object to the MySQL database.
        query (str): The SQL query to execute.

    Returns:
        None
    """

    cursor = conn.cursor()
    try:
        cursor.execute(query)
        conn.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def query_to_df(conn, query):
    """
    Executes a SQL SELECT query and returns the result as a pandas DataFrame.

    Args:
        connection (mysql.connector.connection_cext.CMySQLConnection): The connection object to the MySQL database.
        query (str): The SQL SELECT query to execute.

    Returns:
        pandas.DataFrame: A DataFrame containing the query results.
    """
    
    try:
        df = pd.read_sql(query, conn)
        return df
    except Error as e:
        print(f"The error '{e}' occurred")
        return None
