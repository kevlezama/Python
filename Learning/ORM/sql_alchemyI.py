from sqlalchemy import create_engine, URL, text
import logging

FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
FILE = "basic.log"

logging.basicConfig(
        level=logging.INFO,
        format=FORMAT,
        datefmt="%Y-%m-%d %H:%M:%S",
        filename=FILE
    ) 

# URL Object

url_object = URL.create(

    "postgresql+psycopg2",
    username="postgres",
    password="admin",  # plain (unescaped) text
    host="localhost",
    database="test_1_db",
)

'''

The value passed to create_engine() may be an instance of URL, instead of a plain string,
which bypasses the need for string parsing to be used, and therefore does not need an escaped URL string to be provided.
The URL object is created using the URL.create() constructor method, passing all fields individually.
Special characters such as those within passwords may be passed without any modification:

'''

try:
    engine = create_engine(url_object)
    logging.info(engine)
    logging.info(f"Connection to {url_object.database} successfully done")
    engine_conn = engine.connect()
    logging.info(engine_conn)
    # engine_conn.close()

except Exception as e:
    logging.error(e)


try:
    result_query = engine_conn.execute(text("SELECT * FROM public.employees"))
    
    for row in result_query:
        print(row)


except Exception as e:
    logging.error(e)


engine_conn.close()





