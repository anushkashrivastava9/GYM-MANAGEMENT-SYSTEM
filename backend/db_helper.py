import psycopg2
import streamlit as st

@st.cache_resource
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="GYM-MANAGEMENT-SYSTEM",
            user="postgres",       
            password="Jaimahakaal@2028"  
        )
        return conn
    except Exception as e:
        st.error(f"❌ Database connection failed: {e}")
        return None

def register_member(name, phone, trainer_id, plan_id):
    conn = get_db_connection()
    if conn is None: return False
    cur = conn.cursor()
    try:
        t_id = None if trainer_id == 0 else trainer_id
        cur.execute(
            "INSERT INTO Members (Name, Phone, TrainerID, PlanID) VALUES (%s, %s, %s, %s) RETURNING MemberID;",
            (name, phone, t_id, plan_id)
        )
        member_id = cur.fetchone()[0]
        
        cur.execute("SELECT Price FROM Plans WHERE PlanID = %s;", (plan_id,))
        price = cur.fetchone()[0]
        
        cur.execute(
            "INSERT INTO Payments (MemberID, Amount, Status) VALUES (%s, %s, 'Pending');",
            (member_id, price)
        )
        conn.commit()
        cur.close()
        return True
    except Exception as e:
        conn.rollback()
        cur.close()
        st.error(f"Transaction Fault: {e}")
        return False