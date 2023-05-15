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
            sentence = 'SELECT * FROM persona WHERE id_persona = %s' #PlaceHolder
            id_persona =  input('Digite un id: ')
            cursor.execute(sentence, (id_persona,))
            registros = cursor.fetchone()

            print(registros)
except Exception as e:
    print(f'Ocurrio un error {e}')
finally:
    conexion.close()