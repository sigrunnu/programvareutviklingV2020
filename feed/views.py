# testing search
import sqlite3
from sqlite3 import Error

from django.shortcuts import render

from .models import Exercise


# Create your views here.
def home(request):
    latest_exercises = Exercise.objects.all()

    context = {
        'exercises': latest_exercises
    }

    return render(request, 'feed/feed.html', context)


def search(request):
    """
    :param request:
    :type request: 
    :return: render:
    :rtype: HttpResponse:
    """
    search_word = request.GET['search_field']
    print(search_word)

    # testing search
    conn = create_connection('db.sqlite3')
    select_all_tasks(conn, search_word)

    return render(request, 'feed/search.html', {'search_content': search_word})


# testing search
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


# fetching data from feed_exercise
def select_all_tasks(conn, search_word):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    # cur.execute("SELECT * FROM feed_exercise")
    cur.execute("SELECT * FROM feed_exercise WHERE exerciseTitle=?",
                (search_word,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


'''Not in use yet tester for bare select_all i første omgang - her går de 
etter priority som er definert som tall def select_task_by_priority(conn, 
priority): """ Query tasks by priority :param conn: the Connection object 
:param priority: :return: """ cur = conn.cursor() cur.execute("SELECT * FROM 
tasks WHERE priority=?", (priority,)) 

        rows = cur.fetchall()

        for row in rows:
            print(row)


def main(self):
        database = r"C:\sqlite\db\pythonsqlite.db"

        # create a database connection
        conn = create_connection(database)
        with conn:
            #tester for bare select_all
            #print("1. Query task by priority:")
            #select_task_by_priority(conn, 1)

            print("2. Query all exercises")
            select_all_tasks(conn)

if __name__ == '__main__':
        main()
'''
