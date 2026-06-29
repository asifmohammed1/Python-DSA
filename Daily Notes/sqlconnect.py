# pip install sqlalchemy psycopg2

from sqlalchemy import create_engine, text

Host = "postgresql+psycopg2://<Username>:<Password>@ep-white-rain-379558-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require"
engine = create_engine(Host, pool_pre_ping=True)
conn = engine.connect()

result = conn.execute(text("SELECT * FROM users;"))
for row in result:
    print(row)

# conn.commit() # use this only while update or create a rows or table
conn.close()

import pandas as pd
df = pd.read_sql("SELECT * FROM users;", engine)
print(df)

engine.dispose()

