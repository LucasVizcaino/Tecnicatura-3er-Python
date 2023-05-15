import psycopg2 # Esto es para conectarnos a la base de datos de Postgre

conexion = psycopg2.connect(
    user="postgres",
    password="sarmiento",
    host="127.0.0.1",
    port="5432",
    database="test_bd"
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = '' 
            valores = ()
            cursor.execute(sentencia, valores) 
            registros_insertados = cursor.rowcount
            print(f'Los registros insertados son: {registros_insertados}')

except Exception as e:
    print(f'Ocurrio un error {e}')
finally:
    conexion.close()