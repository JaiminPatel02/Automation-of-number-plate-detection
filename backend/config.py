import os
import sqlite3

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOAD_FOLDER = os.path.join(basedir, 'core/media')

conn = sqlite3.connect('garbage.db.sqlite')

conn.execute('''CREATE TABLE IF NOT EXISTS yolo
         (image TEXT,
         date DATE,
         time DATETIME,
         ADDRESS VARCHAR(50),
         mac_address VARCHAR(500),
         is_verified INT);''')




         