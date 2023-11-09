#THIS IS NEW VERSION TO CONNECT TO POSTGRESQL
import psycopg2

conn= psycopg2.connect(host = '127.0.0.1',
                       database = 'products',
                       user = 'postgres',
                       password= '1234567')
cur = conn.cursor()
cur.execute('SELECT superhero_name FROM superhero.superhero LIMIT 5')
usernames = [r[0] for r in cur.fetchall()]
Found= False
while not Found:
    username = input('Введите ваш логин:')
    if username in usernames:
        print('Вы есть в списке')
        Found=True
    else:
        print('К сожалению мы не смогли вас найти!')

conn.commit()
cur.close()
conn.close()