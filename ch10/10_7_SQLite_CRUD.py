"""
 날짜 : 2021/03/04
 이름 : 이승환
 내용 : 파이썬 SQLite 실습하기 교재 p291
"""

import sqlite3

try:
    conn = sqlite3.connect("./data/SQLite_db")

    cur = conn.cursor()

    sql = """
            CREATE TABLE IF NOT EXISTS `goods` (
              `code` INTEGER   PRIMARY KEY,
              `name` TEXT(30)  UNIQUE NOT NULL,
              `su`   INTEGER   DEFAULT 0,
              `dan`  REAL      DEFAULT 0.0
            );
          """
          cur.execute(sql)

          cur.execute("INSERT INTO `goods` VALUES (1, '냉장고', 2, 850000)")
          cur.execute("INSERT INTO `goods` VALUES (2, '세탁기', 3, 550000)")
          cur.execute("INSERT INTO `goods` (code, name) VALUES (3, '전자레인지')")
          cur.execute("INSERT INTO `goods` (code, name, dan) VALUES(4, 'HDTV', 15000000)")
          conn.commit()

          sql = "SELECT * FROM `goods`"
          cur.execute(sql)

          code = int(input('code 입력 :'))
          name = input('name 입력 :'))
          code = int(input('su 입력 :'))
          code = int(input('dan 입력 :'))

          sql = f"INSERT INTO `goods` VALUES ({code},{name},{su},{dan})"
          cur.execute(sql)
          conn.commit()

          code = int(input('수정 code 입력 :'))
          code = int(input('수정 su 입력 :'))
          code = int(input('수정 dan 입력 :'))

          sql = f"UPDATE `goods` SET su = {su}, dan = {dan} WHERE code = {code}"
          cur.execute(sql)
          conn.commit()

          code = int(input('삭제 code 입력 :'))
          sql = f"DELETE FROM `goods` WHERE CODE = {code}"
          cur.execute(sql)
          conn.commit()

          sql = "SELECT * FROM `goods`"
          cur.execute(sql)
          rows = cur.fetchall()

except Exception as e:
    print('예외발생')
    conn.rollback()

finally:
    cur.close()
    conn.close()