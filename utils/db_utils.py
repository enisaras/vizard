from sqlalchemy import create_engine
import pandas as pd

def connect_mysql(user, password, host, port, schema):
    connection_string = f"mysql+pymysql://{user}:{password}@{host}:{port}/{schema}"
    engine = create_engine(connection_string)
    return engine


def connect_oracle(user, password, host, port, service_name):
    connection_string = f"oracle+cx_oracle://{user}:{password}@{host}:{port}/?service_name={service_name}"
    engine = create_engine(connection_string)
    return engine


def connect_postgres(user, password, host, port, dbname):
    connection_string = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
    engine = create_engine(connection_string)
    return engine


def get_table(engine, table_name):
    query = f"SELECT * FROM {table_name}"
    table = pd.read_sql_query(query, engine)
    return table
