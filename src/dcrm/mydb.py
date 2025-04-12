import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="crm-database",
    user="postgres",
    password="password"
)

cursor = conn.cursor()

print("Connection successful ✅")