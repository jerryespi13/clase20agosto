import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    tabla_fligh = text(
        """
            CREATE TABLE vuelos(
            id SERIAL PRIMARYKEY,
            origen VARCHAR NOT NULL,
            destino VARCHAR NOT NULL,
            duracion INTEGER NOT NULL
            );
        """
        )
    db.execute(tabla_fligh)
    db.commit()

main()