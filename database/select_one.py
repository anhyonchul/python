# 특정한 회원 검색하기

from libs.db.dbconn import getconn

def select_one():
    conn = getconn()
    cur = conn.cursor()

    #1명 검색
    sql = "select * from member where mem_num=10002"
    cur.execute(sql)
    print("회원번호로 검색")

    # rs = cur.fetchmany(num)
    rs = cur.fetchone()
    '''
    for i in rs:
        print(i)
    '''
    print(rs)
    conn.close()

if __name__ =="__main__":
    select_one()
