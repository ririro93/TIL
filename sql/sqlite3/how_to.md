# sqlite3

## 특징
- case-sensitive
- has only 5 data types
  1. NULL
  2. INTEGER
  3. REAL : decimal
  4. TEXT
  5. BLOB : image, mp3 file etc.

## 확장자명이 .db도 있고 .sqlite3도 있다 차이는?
-> database파일은 확장자명이 중요하지 않다. 어떤 확장자명이어도 안에 있는 내용이 같으면 다 읽을 수 있다 <br>
-> sqlite3파일은 밑에 있는 특정 sequence of bytes로 시작하는 특징이 있긴 하다 <br>
-> `0x53 0x51 0x4c 0x69 0x74 0x65 0x20 0x66 0x6f 0x72 0x6d 0x61 0x74 0x20 0x33 0x00`

<br>

## using sqlite3 with python 
### table 내용 보는 방법
- SQLite extension에서 open database하면 explorer에 새로운 SQLite Explorer 탭이 뜬다
  - 여기서 우클릭 -> show table

<br>

### getting started
```python 
import sqlite3

# connect to db
conn = sqlite3.connect('times.db')

# create cursor
cursor = conn.cursor()

# create table -> 다 한 줄에 들어가야 돼서 doctring 쓰는거
cursor.execute("""CREATE TABLE customers (
  first_name text,
  last_name text,
  email text
)""")

# commit to db
conn.commit()

# close connection
conn.close()
```
