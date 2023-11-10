#THIS IS NEW VERSION TO CONNECT TO POSTGRESQL
import psycopg2

conn= psycopg2.connect(host = 'localhost',
                       database = 'assignment5',
                       user = 'postgres'
                       )
cur = conn.cursor()
cur.execute('SELECT superhero_name FROM superhero.superhero ORDER BY superhero_name ASC LIMIT 15')
usernames = [r[0] for r in cur.fetchall()]
# Found= False
# while not Found:
#     username = input('Введите ваш логин:')
#     if username in usernames:
#         print('Вы есть в списке')
#         Found=True
#     else:
#         print('К сожалению мы не смогли вас найти!')
''' СОЗДАТЬ ФУНКЦИЮ БИНАРНОГО ПОИСКА ВХОЖДЕНИЯ ПАРАМЕТРА В СПИСОК usernames'''
def binary_search(username):
    # ЕСЛИ ОН ЕСТЬ С СПИСКЕ
    return True
    # ЕСЛИ ЕГО НЕТ С СПИСКЕ
    return False


conn.commit()
cur.close()
conn.close()