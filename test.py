from sqlalchemy import create_engine


DB_USER = 'postgres'
DB_PASSWORD = 'steven'
DB_HOST = 'localhost'  # Gunakan 'localhost' jika PostgreSQL berjalan di lokal
DB_PORT = '5432'
DB_NAME = 'rekdat'


engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
with engine.connect() as connection:
    print("Connection successful!")
