import sqlite3
import os.path
#user
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "polling.db")
with sqlite3.connect(db_path) as database:
    db = database.cursor()
#     username = "user"
#     password = "1234"
    db.execute("""CREATE TABLE IF NOT EXISTS `user`
                (`user_id` INTEGER PRIMARY KEY,
                 `username` varchar(100) NOT NULL,
                 `password` varchar(100) NOT NULL
                 )""")
    db.execute("""CREATE TABLE IF NOT EXISTS `admin`
                (`admin_id` INTEGER PRIMARY KEY,
                 `username` varchar(100) NOT NULL,
                 `password` varchar(100) NOT NULL
                 )""")
    db.execute("""CREATE TABLE IF NOT EXISTS `pollcount`
                        (`poll_id` INTEGER PRIMARY KEY NOT NULL,
                         `op1` INTEGER NOT NULL,
                         `op2` INTEGER NOT NULL,
                         `op3` INTEGER NOT NULL,
                         `op4` INTEGER NOT NULL
                         )""")
    db.execute("""CREATE TABLE IF NOT EXISTS `polldata`
                        (`poll_id` INTEGER PRIMARY KEY NOT NULL,
                        `admin_id` INTEGER NOT NULL,
                         `ques` varchar(1000) NOT NULL,
                         `op1` varchar(100) NOT NULL,
                         `op2` varchar(100) NOT NULL,
                         `op3` varchar(100) NOT NULL,
                         `op4` varchar(100) NOT NULL
                         )""")
    db.execute("""CREATE TABLE IF NOT EXISTS `loginpollcount`
                        (`poll_id` INTEGER NOT NULL,
                        `user_id` INTEGER NOT NULL
                         )""")
    # username = "admin"
    # password = "1234"
    # db.execute("INSERT INTO admin(username, password)" " VALUES( :username, :password)",
    #             {"username": username, "password": password})
#     db.execute("INSERT INTO user(username, password)" " VALUES( :username, :password)",
#                 {"username": username, "password": password})
#     database.commit()
#     db.execute("""select * from user""")
    database.commit()
#     rows = db.fetchall()
#     print(rows)


# conn = sqlite3.connect('polling.db')
# c = conn.cursor()
# username = "snmt"
# db=conn.execute("SELECT * FROM user WHERE username = :username ",{"username":username})
# c.execute("""select * from user""")
# c.execute("""CREATE TABLE IF NOT EXISTS `user` ( `username` varchar(100) NOT NULL, `password` varchar(100) NOT NULL )""")
# c.execute("""select * from g_list""")
# c.execute("""INSERT INTO user(username, password)
#                   VALUES("snmt", "1234")""")
# conn.commit()
# rows = c.fetchall()
# print(rows)
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# db_path = os.path.join(BASE_DIR, "polling.db")
# with sqlite3.connect(db_path) as database:
#     db = database.cursor()
    # username = "admin"
    # password = "1234"
    # db.execute("""CREATE TABLE IF NOT EXISTS `admin`
    #             (`admin_id` INTEGER PRIMARY KEY,
    #              `username` varchar(100) NOT NULL,
    #              `password` varchar(100) NOT NULL
    #              )""")
    # db.execute("INSERT INTO admin(username, password)" " VALUES( :username, :password)",
    #             {"username": username, "password": password})
    # database.commit()
    # db.execute("""select * from admin""")
    # database.commit()
    # rows = db.fetchall()
    # print(rows)
#
# #
# conn = sqlite3.connect('polling.db')
# c = conn.cursor()
#
#
# c.execute("""CREATE TABLE IF NOT EXISTS `admin` ( `username` varchar(100) NOT NULL, `password` varchar(100) NOT NULL )""")
# c.execute("""INSERT INTO admin(username, password)
#                      VALUES("admin", "1234")""")
# c.execute("""select * from admin""")
# rows = c.fetchall()
# print(rows)
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# db_path = os.path.join(BASE_DIR, "polling.db")
# with sqlite3.connect(db_path) as database:
#     db = database.cursor()
#     db.execute("""CREATE TABLE IF NOT EXISTS `pollcount`
#                     (`poll_id` INTEGER PRIMARY KEY NOT NULL,
#                      `op1` INTEGER NOT NULL,
#                      `op2` INTEGER NOT NULL,
#                      `op3` INTEGER NOT NULL,
#                      `op4` INTEGER NOT NULL
#                      )""")
#     db.execute("DROP table polldata")
#     db.execute("DROP table pollcount")
    # db.execute("""CREATE TABLE IF NOT EXISTS `admin`
    #                 (`admin_id` INTEGER PRIMARY KEY,
    #                  `username` varchar(100) NOT NULL,
    #                  `password` varchar(100) NOT NULL
    #                  )""")
    # db.execute("""CREATE TABLE IF NOT EXISTS `polldata`
    #                 (`poll_id` INTEGER PRIMARY KEY NOT NULL,
    #                 `admin_id` INTEGER NOT NULL,
    #                  `ques` varchar(1000) NOT NULL,
    #                  `op1` varchar(100) NOT NULL,
    #                  `op2` varchar(100) NOT NULL,
    #                  `op3` varchar(100) NOT NULL,
    #                  `op4` varchar(100) NOT NULL
    #                  )""")
    # db.execute("""INSERT INTO polldata(admin_id,ques,op1,op2,op3,op4)
    #                           VALUES("1", "Favourite Fruit", "Apple", "Banana", "Mango", "Orange")""")
    # database.commit()
    # db.execute("""INSERT INTO pollcount(poll_id,op1,op2,op3,op4)
    #                       VALUES("1", "0", "0", "0", "0")""")
    # db.execute("""UPDATE pollcount set op1 = op1 - 1 where poll_id = 2""")
#     database.commit()
#
conn = sqlite3.connect('polling.db')
c = conn.cursor()
c.execute("""select * from admin""")
rows = c.fetchall()
for row in rows:
    print(row)