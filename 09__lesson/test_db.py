from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = 'postgresql://postgres:Tany1501@localhost:5432/postgres'
db=create_engine(db_connection_string)

def test_insert_subject ():
    sql_body = text("select * from subject")
    len_before = len(db.execute(sql_body).fetchall())
    sql_insert = text("insert into subject (\"subject_title\") values (:new_name)")
    db.execute(sql_insert, new_name = 'SkyPro')
    len_after=len(db.execute(sql_body).fetchall())
    db.execute("delete from subject where subject_title='SkyPro'")
    assert len_after-len_before==1

def test_update_subject ():
    sql_body = text("select * from subject")
    len_before = len(db.execute(sql_body).fetchall())
    sql_insert = text("insert into subject (\"subject_title\") values (:new_name)")
    db.execute(sql_insert, new_name = 'SkyPro')
    sql_update = text("update subject set subject_id=16 where subject_title='SkyPro'")
    db.execute(sql_update)
    len_after=len(db.execute(sql_body).fetchall())
    db.execute("delete from subject where subject_title='SkyPro'")
    assert len_after-len_before==1    


def test_delete_subject ():
    sql_body = text("select * from subject")
    len_before = len(db.execute(sql_body).fetchall())
    sql_insert = text("insert into subject (\"subject_title\") values (:new_name)")
    db.execute(sql_insert, new_name = 'SkyPro')
    sql_update = text("update subject set subject_id=16 where subject_title='SkyPro'")
    db.execute(sql_update) 
    db.execute("delete from subject where subject_id=16")
    len_after=len(db.execute(sql_body).fetchall())
    assert len_after==len_before       