import sqlite3
import server.SensorHat as SensorHat

conn = sqlite3.connect('database.db')

c = conn.cursor()

c.execute("""
--sql
CREATE TABLE Sensors(
Temperature blob
Humidity blob
Orientation text
)
;
""")

c.executemany("""
--sql
SELECT 
;
""")