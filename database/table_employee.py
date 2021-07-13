
from libs.db.dbconn import getconn

def select_emp():
    conn = getconn()
    cur = conn.cursor()
    # SQL - select
    sql = "select * from employee"
    cur.execute(sql)

    rs = cur.fetchall()   # 데이터 목록 리스트형으로 반환
    for i in rs:
        print(i)
    conn.close()

#한개 찾기

def select_one():
    conn = getconn()
    cur = conn.cursor()
    sql = "select * from employee where emp_id=?"
    cur.execute(sql, ('e103',))  # --> 한개 매핑을 경우 튜플 자료구조 ,를 꼭 넣을것.
    rs = cur.fetchone()
    print(rs)
    conn.commit()

# 추가
'''
def insert_emp():
    conn = getconn()
    cur = conn.cursor()
    sql = "insert into employee(emp_id, name, age, salary) values (?, ?, ?, ?)"
    cur.execute(sql, ('e104', '강산', 22, 1000))
    conn.commit()
    conn.close()
'''
# 수정
def update_emp():
    conn = getconn()
    cur = conn.cursor()
    sql = "update employee set salary = ? where emp_id=?"
    cur.execute(sql,(200, 'e103'))
    conn.commit()
    conn.close()

#삭제
def delete_emp():
    conn = getconn()
    cur = conn.cursor()
    sql = "delete from employee where emp_id=?"
    cur.execute(sql, ('e103',))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    #insert_emp()
    #update_emp()
    delete_emp()
    select_emp()
    #select_one()
