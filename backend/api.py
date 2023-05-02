import sqlite3
from datetime import date, datetime
from flask_cors import CORS
from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from config import Config
import os
import pandas as pd

conn = sqlite3.connect('car.db.sqlite')



conn.execute('''CREATE TABLE IF NOT EXISTS yolo
         (image TEXT,
         date DATE,
         time DATETIME,
         ADDRESS VARCHAR(50),
         mac_address VARCHAR(500),
         is_verified INT);''')

TABLE_CREATE = """CREATE TABLE IF NOT EXISTS Users (
    EMAIL VARCHAR(100) UNIQUE,
    USERNAME VARCHAR(50) PRIMARY KEY,
    PASSWORD VARCHAR(500) NOT NULL
);"""
conn.execute(TABLE_CREATE)

conn.commit()
print('table done')
app = Flask(__name__)
CORS(app)
# Returns the current local date
today = date.today()
current_time = datetime.now().strftime("%H:%M:%S")
app.config.from_object(Config)



@app.route('/add/<addr>/<mac>', methods=['GET', 'POST'])
def data_add(addr, mac):
    print(mac)
    if request.method == 'POST':
        print("CALLED")
        file = request.files['file']

        if file.filename == '':
            return jsonify({'detail': "No image selected."})
        elif file:
            filename = secure_filename(file.filename)
            date_time = datetime.now().strftime("%Y%m%d%H%M%S.jpg")
            file.save(os.path.join(Config.UPLOAD_FOLDER, date_time))
            date = datetime.now().strftime("%Y-%m-%d")
            time = datetime.now().strftime("%H:%M:%S")
            conn = sqlite3.connect('car.db.sqlite')
            qry = f"""INSERT INTO yolo VALUES
                ("{date_time}", "{date}", "{time}", "{addr}", "{mac}", 0)"""
            print(qry)
            conn.execute(qry)
            conn.commit()
            return jsonify({"detail": 'Image has been successfully uploaded'})
        else:
            return jsonify({"detail": 'Allowed media types are - png, jpg, jpeg, gif'})

    return jsonify({'Date': today, 'time': current_time})


@app.route('/delete_all', methods=['GET', 'POST', 'DELETE'])
def deleteall_data():
    conn = sqlite3.connect('car.db.sqlite')
    query = 'DELETE FROM yolo where is_verified = 2'
    conn.execute(query)
    conn.commit()
    return "data deleted"


@app.route('/delete_row/<id>', methods=['GET', 'POST', 'DELETE'])
def deleteall_row(id):
    conn = sqlite3.connect('car.db.sqlite')
    query = f'DELETE FROM yolo WHERE image = "{id}"'
    conn.execute(query)
    conn.commit()
    return f"data of {id} row deleted"


@app.route('/fetch/<area>', methods=['GET'])
def get_data(area):
    if area == 'admin':
        conn = sqlite3.connect('car.db.sqlite')
        query='select * from yolo where is_verified = 0'
        temp=conn.execute(query).fetchall()
        conn.commit()
    else:
        conn = sqlite3.connect('car.db.sqlite')
        query=f"""select * from yolo where is_verified = 0 AND ADDRESS = '{area}'"""
        temp=conn.execute(query).fetchall()
        conn.commit()

    data=[]
    print(len(temp))
    for i in temp:
        print(i[0])
        dict={"iamge_path":i[0],"date":i[1],"time":i[2],"location":i[3],"mac_address":i[4],"approved":i[5]}
        data.append(dict)
    return jsonify({'data':data,'count':len(temp)})

@app.route('/fetch_all', methods=['GET'])
def get_fetchall():
    conn = sqlite3.connect('car.db.sqlite')
    query=f"""select * from yolo """
    temp=conn.execute(query).fetchall()
    conn.commit()
    data=[]
    print(len(temp))
    for i in temp:
        print(i[0])
        dict={"iamge_path":i[0],"date":i[1],"time":i[2],"location":i[3],"mac_address":i[4],"approved":i[5]}
        data.append(dict)
    return jsonify({'data':data,'count':len(temp)})

@app.route('/count/<area>',methods=['GET'])
# def get_count():
#     conn = sqlite3.connect('car.db.sqlite')
#     query='select * from yolo where is_verified = 0'
#     temp=conn.execute(query).fetchall()
#     conn.commit()
#     print(len(temp))
#     return jsonify({'count':len(temp)})



def get_count(area):
    if area == 'admin':
        conn = sqlite3.connect('car.db.sqlite')
        query='select * from yolo where is_verified = 0'
        temp=conn.execute(query).fetchall()
        conn.commit()
    else:
        conn = sqlite3.connect('car.db.sqlite')
        query=f"""select * from yolo where is_verified = 0 AND ADDRESS = '{area}'"""
        temp=conn.execute(query).fetchall()
        conn.commit()

    data=[]
    print(len(temp))
    
    return jsonify({'count':len(temp)})


@app.route('/fetchv/<area>',methods=['GET'])
def get_datav(area):

    if area == "admin":
        conn = sqlite3.connect('car.db.sqlite')
        query='select * from yolo where is_verified = 1'
        temp=conn.execute(query).fetchall()
        conn.commit()
  
    else:
        conn = sqlite3.connect('car.db.sqlite')
        query=f'select * from yolo where is_verified = 1 AND ADDRESS = "{area}"'
        temp=conn.execute(query).fetchall()
        conn.commit()
    data=[]

    # print(temp)
    for i in temp:
        print(i[0])
        dict={"iamge_path":i[0],"date":i[1],"time":i[2],"location":i[3],"mac_address":i[4],"approved":i[5]}
        data.append(dict)
    return jsonify({'data':data})


@app.route("/media/<path>", methods=['GET'])
def media(path):
    print(path)
    return send_from_directory(
        directory=app.config['UPLOAD_FOLDER'], path=path
    )
@app.route('/verify/<id>/<area>', methods=['GET', 'POST'])
def verify_update(id, area):
    conn = sqlite3.connect('car.db.sqlite')
    query1 = f'select is_verified from yolo WHERE image = "{id}"'
    temp = conn.execute(query1).fetchall()
    temp = temp[0][0]
    if temp == 0:
        pass
    query = f'UPDATE yolo SET is_verified=1 WHERE image = "{id}"'

    if temp == 1:
        query = f'UPDATE yolo SET is_verified=0 WHERE image = "{id}"'

    conn.execute(query)
    conn.commit()
    # notification(area)
    print(temp)
    return f"data of {id} where {temp}row updated ,message sent to {area}"


@app.route('/temp_delete/<id>',methods=['GET','POST'])
def temp_delete(id):
    conn = sqlite3.connect('car.db.sqlite')
    query1 = f'select is_verified from yolo WHERE image = "{id}"'
    temp = conn.execute(query1).fetchall()
    temp=temp[0][0]
    if temp==0:
        pass
    query = f'UPDATE yolo SET is_verified=2 WHERE image = "{id}"'

    if temp==2:
        query = f'UPDATE yolo SET is_verified=0 WHERE image = "{id}"'

    conn.execute(query)
    conn.commit()
    return f"data of {id} where {temp}row send to temp_delete page"


@app.route('/fetch_delete/<area>',methods=['GET'])
def get_delete(area):
   
    data=[]

    if area == "admin":
        conn = sqlite3.connect('car.db.sqlite')
        query=f"select * from yolo where is_verified = 2"
        temp=conn.execute(query).fetchall()
        conn.commit()

    else:
        conn = sqlite3.connect('car.db.sqlite')
        query=f"select * from yolo where is_verified = 2 AND ADDRESS = '{area}'"
        temp=conn.execute(query).fetchall()
        conn.commit()
    # print(temp)
    for i in temp:
        print(i[0])
        dict={"iamge_path":i[0],"date":i[1],"time":i[2],"location":i[3],"mac_address":i[4],"approved":i[5]}
        data.append(dict)
    return jsonify({'data':data})


#    login 
@app.route('/add_user/<name>/<email>/<passw>')
def add_user(name,email,passw):
    conn=sqlite3.connect('car.db.sqlite')
    qry = f"""INSERT INTO Users VALUES
                    ("{email}", "{name}", "{passw}")"""
    conn.execute(qry)
    conn.commit()
    return 'data added'

@app.route('/fetch_login')
def fetch_login():
    conn = sqlite3.connect('car.db.sqlite')
    query = 'select * from Users'
    temp = conn.execute(query).fetchall()
    conn.commit()
    data = []
    print(temp)
    # for i in temp:
    #     print(i[0])
    #     dict = {"iamge_path": i[0], "date": i[1], "time": i[2],
    #             "location": i[3], "mac_address": i[4], "approved": i[5]}
    #     data.append(dict)
    return jsonify({'data':temp})
# @app.route('/loginsucess')
# def sucess():
#     if "user_id" in session:
#         return 'Login sucessful'
#     else:
#         return 'not'




@app.route('/valid/<name>/<passw>')
def login_validate(name,passw):
    conn = sqlite3.connect('car.db.sqlite')
    query=f"""SELECT * from Users where USERNAME ='{name}' AND PASSWORD='{passw}' """
    temp = conn.execute(query).fetchall()
    conn.commit()
    if len(temp)>0:
        # session['user_id']=temp[0][1]
        return jsonify({'Username':temp[0][1],'status':"Yes"})
    else:
       return jsonify({'Username':"",'status':"No"})
    # return jsonify({'data':temp})

@app.route("/delete_user/<username>")
def deleteuser(username):
    conn = sqlite3.connect('car.db.sqlite')
    query = f"DELETE FROM Users where USERNAME = '{username}'"
    conn.execute(query)
    conn.commit()
    return f"user delete {username} "

if __name__ =="__main__":
    app.run(debug=True)