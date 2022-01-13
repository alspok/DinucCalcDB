'''Create table using BASE'''
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

'''Enter database and table name when instanting class+'''
class SeqMetaDB():
    def __init__(self, database, table) -> None:
        self.database = database
        self.table = table

    '''
    Dinuc frequencies in two different frames.
    aa, ac, ag, .... columns contains strig.
    1st item - dinuc frq in 1st frame,
    2nd item - dinuc frq in 2nd frame,
    3rd item - abs value of dinuc in frames differencies.
    '''        
    def initTable(self):
        meta = MetaData()    
        self.table = Table(
                    self.table, meta,
                    Column('id', Integer, primary_key = True),
                    Column('seq_name', String),
                    Column('description', String),
                    Column('seq_length', String),
                    Column('gc_percent', String),
                    Column('di_diff', String),
                    #Column('mono_shuffle_diff', String),
                    Column('di_shuffle_diff', String),
                    #Column('tri_shuffle_diff', String),
                    Column('aa', String),
                    Column('aa', String),
                    Column('aa', String),
                    Column('ac', String),
                    Column('ag', String),
                    Column('at', String),
                    Column('ca', String),
                    Column('cc', String),
                    Column('cg', String),
                    Column('ct', String),
                    Column('ga', String),
                    Column('gc', String),
                    Column('gg', String),
                    Column('gt', String),
                    Column('ta', String),
                    Column('tc', String),
                    Column('tg', String),
                    Column('tt', String),
                    )
        
        engine = create_engine(f"sqlite:///{self.database}")
        meta.create_all(engine)
        
class SQLQuery():
    def __init__(self, database: str, table: str) -> None:
        self.database = database
        self.table = table
        self.engine = create_engine(f"sqlite:///{self.database}")
    
    '''INSERT INTO table (colums) VALUES (values);'''
    def insert(self, columns: str, values: str) -> None:
        query = f"INSERT INTO {self.table} ({columns}) VALUES ({values})"
        with self.engine.connect() as conn:
            conn.execute(query)
            
    '''Insert dictionary into table'''            
    def insertDict(self, dict) -> None:
        columns = ', '.join(dict.keys())
        values = [f':{e}, ' for e in dict.keys()]
        values = ''.join(values)
        values = values[:-2]
        query = f"INSERT INTO {self.table} ({columns}) VALUES ({values})"
        try:
            with self.engine.connect() as conn:
                conn.execute(query, dict)
        except Exception as e:
            print(e)
            
    '''SELECT colums FROM table WHERE condition; condition - column == (<, <=, ...) value '''
    def select(self, columns: str, condition: str) -> list:
        res = []
        with self.engine.connect() as conn:
            query = f"SELECT {columns} FROM {self.table} WHERE {condition}"
            result = conn.execute(query)
            [res.append(r) for r in result]
        return res
                
                
    '''UPDATE table SET column=value WHERE condition;'''
    def update(self, columns: str, condition: str) -> None:
        with self.engine.connect() as conn:
            query = f"UPDATE {self.table} SET {columns} WHERE {condition}"
            conn.execute(query)
            
    '''DELETE FROM table WHERE condition; condition - column == (<, <=, ...) value'''
    def delete(self, condition: str) -> None:
        query = f"DELETE FROM {self.table} WHERE {condition}"
        with self.engine.connect() as conn:
            conn.execute(query)
