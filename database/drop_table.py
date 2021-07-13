#

from libs.db.dbconn import getconn

def drop_table():
    conn = getconn()       # 네트워크(DB) 연결 객체
    cur = conn.cursor()
    sql = "drop table member"  # 테이블 삭제 ---> SQL : DDL
    cur.execute(sql)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    drop_table()