import pandas as pd
df=pd.read_csv('SanFranciscoAPI.csv')
df
df2=pd.read_csv('RhodeIsland.csv')
df2
from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:hellosql@localhost:5432/postgres')
df.to_sql('SanFranciscoPoliceStops', engine, if_exists='replace', index=False)
df2.to_sql('RhodeIslandPoliceStops', engine, if_exists='replace', index=False)