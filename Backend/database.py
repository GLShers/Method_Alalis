import databases
from sqlalchemy import create_engine, MetaData

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:rawqer22@localhost/mydb"

database = databases.Database(SQLALCHEMY_DATABASE_URL)#представляет собой подключение к базе данных. Этот объект будет использоваться для выполнения асинхронных операций
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

metadata = MetaData()



