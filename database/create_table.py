
# mydb.db에 member테이블 만들기

    # DB를 만드는 프로세스
    # 1. DB에 연결
    # 2. 테이블 생성

from libs.db.dbconn import getconn

def create_table():
    conn = getconn()      # dbconn 모듈에서 getconn 호출 (객체 생성)
    cur = conn.cursor()   # db 작업을 하는 객체 (cur)

    # 테이블 생성 - sql언어 DDL
    sql = """
        create table member(
            mem_num int primary key,
            name char(20),
            age int
        )
    """
    cur.execute(sql)

    conn.commit()  # 트렌잭션을 완료했다.
    conn.close()   # 네트워크 종료

if __name__ == "__main__":
    create_table()
