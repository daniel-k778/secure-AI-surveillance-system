#pip install pymysql
#pip install sqlalchemy
#pip install cryptography (for sha256)


from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class userdata(Base):
    __tablename__ = 'userdata'
    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)

sqlite_engine = create_engine('sqlite:///userdata.db')
mysql_engine = create_engine('mysql+pymysql://root:password@localhost:3306/userdata')#replace 'password' for MySQL password

SQLite_Session = sessionmaker(bind=sqlite_engine)
sqlite_session = SQLite_Session()

MySQL_Session = sessionmaker(bind=mysql_engine)
mysql_session = MySQL_Session()

Base.metadata.create_all(mysql_engine)

for table in [userdata]:
    records = sqlite_session.query(table).all()
    for record in records:
        mysql_session.merge(record)

mysql_session.commit()

sqlite_session.close()
mysql_session.close()