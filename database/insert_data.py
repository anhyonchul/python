
# 자료를 삽입하는 코드

from libs.db.dbconn import getconn

def insert_data():
    conn = getconn()
    cur = conn.cursor()

    # 자료추가 - SQL언어
    cur.execute("insert into member values (10003, '황진이', 25)")
    cur.execute("insert into member values (10004, '성춘향', 22)")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    insert_data()
