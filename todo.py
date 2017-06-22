import sqlite3
from bottle import route, run,debug,template,request

@route('/todo')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    c.close()
    output = template('make_table', rows=result)
    return output

@route('/classes')
def get_classes():
        classes = []
        classes.append(("Data Streams","Summer 2017","3"))
        classes.append(("Test Methodology","Fall 2017","4"))
        classes.append(("Test Methodology","Fall 2018","5"))
        classes.append(("Test Methodology","Fall 2019","6"))
        classes.append(("Test Methodology","Fall 2020","7"))
        classes.append(("Test Methodology","Fall 2021","8"))
        output = template('make_table', rows=classes)
        return output
        
@route('/new', method='GET')
def new_item():
    if request.GET.save:
        new = request.GET.task.strip()
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new,1))
        new_id = c.lastrowid
        conn.commit()
        c.close()
        return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id
    else:
        return template('new_task.tpl')
debug(True)
run(reloader=True)
