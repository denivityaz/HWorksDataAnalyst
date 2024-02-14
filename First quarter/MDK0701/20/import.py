import psycopg2
import fiona  # работа с геоданными формата shapefile


con = psycopg2.connect('host=127.0.0.1 port=5432 user=postgres password=2693 dbname=lab20')

shp = fiona.open('ne_10m_coastline.shp')


i = 0

for feature in shp:
    # Получение координат объекта
    arr = feature['geometry']['coordinates']
    # Вывод номера объекта и количества координат
    print(i, len(arr))
    sql = 'insert into data.shape (polygon, segment, latitude, longitude) values'

    for j in range(0, len(arr)):
        pt = arr[j]
        # Добавление координат в SQL запрос
        sql = sql + f' ({i}, {j}, {pt[1]}, {pt[0]}),'

 
    i = i + 1
    # Удаление последней запятой из SQL запроса
    sql = sql[:-1]

    # Выполнение SQL запроса
    cur = con.cursor()
    cur.execute(sql)
    cur.close()

    con.commit()


con.close()