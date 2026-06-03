# 🏋️‍♂️ Gym Membership Management System
> **DBMS Mini-Project Terminal (Course Code: BCS402)** > Developed by: Amrit Raj, Ankit Kumar, Anushka Shrivastava, Ashish Raj, and Devasya Tiwari.

An enterprise-grade, relational database application engineered to automate the logistical, staff, and financial workflows of a fitness center. Moving away from manual logbooks and flat spreadsheets, this system implements a normalized PostgreSQL backend paired with an interactive Python Streamlit user interface to maintain strict data integrity and real-time operational transparency.

---

## 🧬 System Architecture & DBMS Highlights

The core of this project centers heavily on fundamental Relational Database Management System (RDBMS) design patterns:

### 1. Database Schema Model (ER Layout)
The relational schema comprises four highly integrated tables meticulously structured to achieve high-order normalization form:
* `Trainers`: Captures trainer skillsets and professional specialization metrics.
* `Plans`: Organizes subscription package attributes, pricing structures, and duration limits.
* `Members`: Links clients securely to both their chosen plan tier and assigned fitness coach.
* `Payments`: Operates as a system financial ledger monitoring transaction lifecycles.

### 2. Advanced DB Engineering Concepts Implemented
* **Data Integrity Safeguards:** Enforces strict `PRIMARY KEY`, `NOT NULL`, and `UNIQUE` constraints to stop duplicate entries (e.g., matching phone records) right at the compiler layer.
* **Cascading Maintenance Protocols:** Configured with relational constraints like `ON DELETE SET NULL` on staff relationships (protecting members if a trainer leaves) and `ON DELETE CASCADE` on payments (ensuring no orphan invoices linger if a account profile is deleted).
* **Multi-Table Joins & Dynamic Aggregations:** Complex in-flight queries aggregate live member analytics, measure staff capacity loads (`GROUP BY` & `HAVING`), and isolate outstanding deficit metrics.
* **State Mutators (Data Modification):** Natively runs parameterized, transactional `INSERT` and `UPDATE` SQL streams straight from the UI to safely modify persistent storage fields on disk.

---

## 🖥️ Application Features & User Interface

The frontend web application drops basic, flat configurations for a premium dark-themed corporate administration console layout split across three focused workspaces:

1. **🖥️ Executive Command Center:** Displays high-level graphical summary KPIs (Roster counts, staff configurations, and gross realized capital) paired with an interactive directory search terminal to filter database records live by name strings.
2. **📝 Member Onboarding Terminal:** A clean data-entry form parsing user details. Submitting an asset runs a compound transactional write block—onboarding the user profile to `Members` while simultaneously instantiating a pending invoice item in the `Payments` table.
3. **📊 Financial Audit & Desk Control:** An active operational module that displays ledger statistics alongside an **Interactive Settle Balance Action**. Administrators can select any real-time outstanding arrear balance account from a dynamic dropdown and settle it natively, firing a live database state mutation override.

---

## 💻 Technical Stack

* **Frontend Interface:** Streamlit (Python Core Dashboard Framework)
* **Database Engine:** PostgreSQL 18
* **Database Adapter:** Psycopg2 (Advanced PostgreSQL binary connector)
* **Data Structuring:** Pandas & DataFrames

---

## ⚙️ Installation & Local Setup Workflow

### Prerequisites
Ensure your host machine has **Python 3.x** and **PostgreSQL** engine environments configured natively.

### 1. Clone the Cloud Workspace
Open your **Git Bash** terminal window on your laptop and clone down your repository branches:
```bash
git clone [https://github.com/YOUR_GITHUB_USERNAME/GYM-MANAGEMENT-SYSTEM.git](https://github.com/YOUR_GITHUB_USERNAME/GYM-MANAGEMENT-SYSTEM.git)
cd GYM-MANAGEMENT-SYSTEM
