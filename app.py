import streamlit as st
import pandas as pd
from backend.db_helper import get_db_connection, register_member

# 1. Advanced Page Configurations & Global Dark Styling
st.set_page_config(
    page_title="RNSIT Gym Intelligence Terminal", 
    layout="wide", 
    page_icon="🏋️‍♂️",
    initial_sidebar_state="expanded"
)

# Custom CSS injection for a professional, dashboard-centric vibe
st.markdown("""
    <style>
    .main-title { font-size: 2.6rem; font-weight: 800; color: #FF4B4B; margin-bottom: 0.2rem; }
    .sub-title { font-size: 1rem; color: #A0AEC0; margin-bottom: 2rem; }
    .kpi-card { background-color: #1A202C; padding: 1.5rem; border-radius: 0.75rem; border-left: 5px solid #FF4B4B; }
    </style>
""", unsafe_allow_html=True)

# ====================================================================
# 2. SIDEBAR INTERACTIVE CONTROL NAVIGATION
# ====================================================================
with st.sidebar:
    st.image("https://www.rnsit.ac.in/wp-content/uploads/2022/12/RNSIT_LOGO.png", width=120)
    st.markdown("### 🧬 Navigation Control")
    page = s_menu = st.radio(
        "Select Operational Terminal:",
        ["Dashboard Overview", "New Member Onboarding", "Financial Audit Ledger"]
    )
    st.write("---")
    st.markdown("🔧 **System Telemetry**")
    st.caption("Database Node: **PostgreSQL (Localhost)**")
    st.caption("Environment: **Development Target**")
    st.caption("Course Framework: **BCS402 Mini-Project**")

# ====================================================================
# TERMINAL VIEW 1: PREMIUM DASHBOARD OVERVIEW
# ====================================================================
if page == "Dashboard Overview":
    st.markdown("<div class='main-title'>🏋️‍♂️ GYM EXECUTIVE INTELLIGENCE TERMINAL</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Real-time operational metrics, multi-table relation states, and capacity heatmaps.</div>", unsafe_allow_html=True)
    
    conn = get_db_connection()
    if conn:
        cur = conn.cursor()
        
        # Aggregate complex statistical summaries for analytical KPI block
        cur.execute("SELECT COUNT(*) FROM Members;")
        total_members = cur.fetchone()[0]
        
        cur.execute("SELECT COUNT(*) FROM Trainers;")
        total_trainers = cur.fetchone()[0]
        
        cur.execute("SELECT SUM(Amount) FROM Payments WHERE Status = 'Paid';")
        revenue = cur.fetchone()[0] or 0.0
        
        # High-impact visual metric cards
        kpi1, kpi2, kpi3 = st.columns(3)
        with kpi1:
            st.metric(label="👥 Registered Member Base", value=total_members, delta="Active Subscriptions")
        with kpi2:
            st.metric(label="💪 Certified Professional Staff", value=total_trainers, delta="Allocated Instructors")
        with kpi3:
            st.metric(label="💰 Gross Realized Revenue", value=f"₹{revenue:,.2f}", delta="Processed Logs")
            
        st.write("---")
        
        # Interactive Grid Data display
        st.subheader("📋 Active Cross-Table Client Assignment Matrix")
        df_join = pd.read_sql_query(
            """SELECT m.MemberID as "ID", m.Name AS "Member Name", m.Phone as "Contact", 
                      COALESCE(t.Name, 'No Personal Trainer') AS "Assigned Trainer", p.PlanName as "Subscription Tier"
               FROM Members m 
               LEFT JOIN Trainers t ON m.TrainerID = t.TrainerID 
               JOIN Plans p ON m.PlanID = p.PlanID ORDER BY m.MemberID ASC;""", conn
        )
        st.dataframe(df_join, use_container_width=True, hide_index=True)
        cur.close()

# ====================================================================
# TERMINAL VIEW 2: HIGH-END ONBOARDING WORKSPACE
# ====================================================================
elif page == "New Member Onboarding":
    st.markdown("<div class='main-title'>📝 MEMBER REGISTRATION WORKSPACE</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Onboard assets and compile contractual relationship attributes securely.</div>", unsafe_allow_html=True)
    
    conn = get_db_connection()
    if conn:
        cur = conn.cursor()
        cur.execute("SELECT TrainerID, Name FROM Trainers;")
        trainers = {name: tid for tid, name in cur.fetchall()}
        trainers["No Personal Trainer Assigned"] = 0
        
        cur.execute("SELECT PlanID, PlanName FROM Plans;")
        plans = {name: pid for pid, name in cur.fetchall()}
        
        # Using layout columns to split input parameters cleanly
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("### 📋 Customer Profile Specifications")
            with st.form("onboarding_form_clean", clear_on_submit=True):
                name = st.text_input("Full Name", placeholder="e.g., Rahul Sharma")
                phone = st.text_input("Mobile Contact Fields (Unique Constraint)", placeholder="e.g., 9876543210")
                selected_trainer = st.selectbox("Assign Dedicated Fitness Expert", list(trainers.keys()))
                selected_plan = st.selectbox("Assign Pricing Bracket System", list(plans.keys()))
                
                st.write("\n")
                submit = st.form_submit_button("🚀 Commit Profile to Storage Disk")
                
                if submit:
                    if name.strip() == "" or phone.strip() == "":
                        st.error("⚠️ Core Integrity Violation: Input variables cannot be null.")
                    else:
                        success = register_member(name, phone, trainers[selected_trainer], plans[selected_plan])
                        if success:
                            st.success(f"✨ Safe Insertion Confirmed: {name} mapped successfully to the ledger matrix.")
        
        with col2:
            st.markdown("### 🔍 Validation Guardrails")
            st.info("💡 **Relational Cascade Rules:** Registering a profile here automatically initiates a matching invoice inside the relational Payments ledger structure.")
            st.warning("⚠️ **Unique Checks:** Enforces unique parameter matching rules on mobile values to filter duplicate entries out of the buffer schema.")
        cur.close()

# ====================================================================
# TERMINAL VIEW 3: ACCOUNTING AND DEFICIT TRACKER
# ====================================================================
elif page == "Financial Audit Ledger":
    st.markdown("<div class='main-title'>💰 AUDIT & ARREARS ACCOUNTING POOL</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Monitor subscription default statuses and evaluate localized stream revenues.</div>", unsafe_allow_html=True)
    
    conn = get_db_connection()
    if conn:
        grid1, grid2 = st.columns(2)
        
        with grid1:
            st.error("🚨 Outstanding Subscription Defaulters")
            df_defaulters = pd.read_sql_query(
                """SELECT m.Name AS "Defaulter Name", m.Phone AS "Contact", p.Amount AS "Balance Due", p.Status 
                   FROM Payments p 
                   JOIN Members m ON p.MemberID = m.MemberID 
                   WHERE p.Status = 'Pending';""", conn
            )
            st.dataframe(df_defaulters, use_container_width=True, hide_index=True)
                
        with grid2:
            st.success("📊 Revenue Apportionment per Membership Class")
            df_revenue = pd.read_sql_query(
                """SELECT p.PlanName AS "Membership Plan", COUNT(m.MemberID) AS "Subscribers", SUM(pay.Amount) AS "Total Revenue" 
                   FROM Plans p 
                   JOIN Members m ON p.PlanID = m.PlanID 
                   JOIN Payments pay ON m.MemberID = pay.MemberID 
                   WHERE pay.Status = 'Paid' 
                   GROUP BY p.PlanName 
                   ORDER BY "Total Revenue" DESC;""", conn
            )
            st.dataframe(df_revenue, use_container_width=True, hide_index=True)
            
        st.write("---")
        st.subheader("🏋️‍♂️ Instructor Workload Distribution Analysis")
        df_load = pd.read_sql_query(
            """SELECT t.TrainerID as "ID", t.Name AS "Instructor", t.Specialization as "Specialty", COUNT(m.MemberID) AS "Total Active Clients" 
               FROM Trainers t 
               JOIN Members m ON t.TrainerID = m.TrainerID 
               GROUP BY t.TrainerID, t.Name, t.Specialization 
               HAVING COUNT(m.MemberID) > 1 
               ORDER BY "Total Active Clients" DESC;""", conn
        )
        st.dataframe(df_load, use_container_width=True, hide_index=True)