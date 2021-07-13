# 자료 내용 수정/변경 하기

from libs.db.dbconn import getconn

def update_data():
    conn = getconn()
    cur = conn.cursor()

    sql = "update member set name='이몽룡' where mem_num=10004"

    cur.execute(sql)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    update_data()