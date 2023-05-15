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
            sentencia = 'INSERT INTO persona (nombre, apellido, email)VALUES (%s, %s, %s)' 
            valores = (
                ('Carlos', 'Perez', 'carlosperez777@gmail.com'),
                ('Marcos ', 'Canto', 'mcanto@gmail.com'),
                ('Marcelo', 'Cuenca', 'marceloCuenca@gmail.com'),
                ) #Es una tupla de tuplas
            cursor.executemany(sentencia, valores) 
            #conexion.commit() Esto se utiliza para guardar cambios en la base de datos
            registros_insertados = cursor.rowcount
            print(f'Los registros insertados son: {registros_insertados}')

except Exception as e:
    print(f'Ocurrio un error {e}')
finally:
    conexion.close()