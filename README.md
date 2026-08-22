# AI STUDENT ATTENDANCE TRACKER

> **AI-Powered Attendance Monitoring, Analytics, and Student Risk Prediction System**  
> *A Complete Academic College Mini-Project Prototype with User Authentication*

---

## 1. Project Title
**AI Student Attendance Tracker**

---

## 2. Project Overview
The **AI Student Attendance Tracker** is a full-stack, AI-powered web application designed for engineering institutions and colleges. It moves beyond static roll-call records by leveraging dynamic database computations and a trained **Random Forest Machine Learning model** to continuously analyze student attendance patterns, identify consecutive absence streaks, predict detention risks, trigger automated alerts, and provide actionable intervention plans for academic mentors.

> ℹ️ **Academic Demonstration Notice:**  
> *This project uses simulated/demo data for academic demonstration. It can later be integrated with real college attendance systems.*

---

## 3. User Authentication Flow

The application provides a complete, secure authentication workflow:

1. **Register Page (`/register`):**
   - New faculty, mentors, and administrators can register their account.
   - Fields: Full Name, Username, College Email, Academic Role, Department, and Password.
   - Securely stored with password hashing (`werkzeug.security.generate_password_hash`).
   - Automatically redirects to Login with a success confirmation toast upon registration.

2. **Login Page (`/login`):**
   - Clean login card with Username / Email and Password inputs.
   - **⚡ Instant Demo Auto-Fill Button:** Click to automatically populate pre-seeded faculty credentials.
   - Authenticates credentials and sets a secure Flask session.

3. **Pre-Seeded Default Credentials:**
   - **Username:** `admin` *(or `faculty@college.edu`)*
   - **Password:** `admin123`
   - **Role:** `Faculty Advisor`

4. **Logout (`/logout`):**
   - Easily log out at any time from the top navigation bar or sidebar footer.

---

## 4. Problem Statement
In traditional college attendance systems:
- Faculty record daily attendance manually or in isolated spreadsheets.
- Students at risk of falling below the mandatory **75% university eligibility threshold** are often only identified at the end of the semester when it is too late for corrective action.
- Consecutive absence streaks and declining 10-day attendance trends are missed until detention notices are compiled.
- Mentors lack explainable data and early-warning decision-support metrics to guide student counseling.

---

## 5. Objectives
1. **Secure Access:** Faculty & admin authentication (Register & Login) with Flask session control.
2. **Dynamic Tracking:** Record single or batch student attendance across multiple subjects and academic sessions.
3. **Automated Analytics:** Dynamically calculate overall and subject-wise attendance percentages, present/absent ratios, and tier distributions.
4. **Early Risk Prediction:** Use an ML classifier to categorize students into `SAFE`, `AT_RISK`, and `CRITICAL` conditions.
5. **Explainable Metric:** Calculate a composite **Attendance Risk Score (0–100)** to explain prediction factors transparently.
6. **Proactive Alerts:** Automatically generate tiered alerts (`INFO`, `WARNING`, `CRITICAL`) when thresholds are breached.
7. **Reporting & Print:** Provide instant academic semester reports with one-click print/PDF formatting.

---

## 6. Key Features
- 🔐 **Authentication System:** First Register (`/register`) and Login (`/login`) workflow with password hashing and session authorization.
- 📊 **Modern Dashboard:** Live summary metric cards, recent logs, attention list, and Chart.js trend charts.
- 👨‍🎓 **Student Management:** Full student directory with live search, tier filters, progress indicators, and detailed profile modal with subject breakdowns.
- 📝 **Attendance Management:** Dual-mode recording (Single session entry or fast batch roll call) with parameterized database storage.
- 📈 **Dynamic Analytics:** 5 live Chart.js visualizations driven by real-time Flask API queries.
- 🤖 **AI Risk Prediction:** Interactive multi-metric evaluator with confidence rating and structured action recommendations.
- ⚠️ **Alerts Hub:** Live notifications for attendance drops below 75% or 60%, and consecutive absence streaks.
- 📄 **Reports Generation:** Comprehensive institutional reports with clean browser print stylesheets.
- ℹ️ **About Page:** Transparent display of system architecture, database schema, and live calculated ML accuracy.

---

## 7. Technologies Used

| Layer | Technology | Details |
| :--- | :--- | :--- |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript | Custom CSS Grid/Flexbox, Fetch API, no external UI frameworks |
| **Backend** | Python Flask | Lightweight RESTful application server, Jinja2 & Flask Sessions |
| **Machine Learning** | Scikit-Learn, Pandas, NumPy, Joblib | Random Forest Classifier, 80/20 train-test split |
| **Database** | SQLite3 | Local relational storage with Foreign Key constraints & Users table |
| **Visualizations** | Chart.js | Responsive charts rendered via CDN |

---

🚀 Live Demo

AI Student Attendance Tracker is deployed online using Render.
https://ai-student-attendance-tracker-v24t.onrender.com

## 8. System Architecture

```text
               +-------------------------------------------+
               |        User Browser (Faculty/Admin)       |
               +-------------------------------------------+
                     |                          |
                     |  Unauthenticated         |  Authenticated
                     v                          v
               +----------------+        +-----------------------------------+
               | Register/Login |        | Dashboard, Attendance, Analytics, |
               | Pages & APIs   |        | AI Prediction, Alerts, Reports    |
               +----------------+        +-----------------------------------+
                     |                                  |
                     +----------------------------------+
                                     |  HTTP / REST API (Fetch API)
                                     v
               +-------------------------------------------+
               |        Flask Backend (app.py)             |
               +-------------------------------------------+
                   /                       \
                  /                         \
                 v                           v
+-----------------------------+   +------------------------------------+
|  SQLite Database            |   |  Scikit-Learn ML Model Engine      |
|  (database/attendance.db)   |   |  (model/attendance_risk_model.pkl) |
|                             |   |                                    |
|  - users (Auth)             |   |  - Features: Attendance %, Streak, |
|  - students                 |   |    Trend, Marks, Assignments, etc. |
|  - subjects                 |   |  - Output: Prediction + Risk Score |
|  - attendance               |   |  - Confidence & Action Guidelines  |
|  - predictions              |   +------------------------------------+
|  - alerts                   |                      |
+-----------------------------+                      |
                 \                                  /
                  \                                /
                   v                              v
               +-------------------------------------------+
               |  Interactive Dashboard, Alerts & Reports  |
               +-------------------------------------------+
```

---

## 9. AI/ML Methodology
- **Supervised Learning:** Multi-class classification using an ensemble `RandomForestClassifier`.
- **Ensemble Architecture:** 120 decision trees (`n_estimators=120`, `max_depth=9`, `class_weight='balanced'`).
- **Input Features:** 7 continuous and discrete academic indicators.
- **Target Classes:** `SAFE`, `AT_RISK`, `CRITICAL`.
- **Validation:** Stratified 80/20 train/test split evaluated on unseen test data (**99.4% accuracy**).

---

## 10. Dataset Generation
The training dataset is generated via `train_model.py` simulating 2,500 realistic college student academic records:
- High attendance (>75%) with regular marks generates `SAFE` labels.
- Borderline attendance (60%–74%) or recent downward trends generate `AT_RISK` labels.
- Attendance below 60%, consecutive absence streaks &ge; 4, or severe academic lag generate `CRITICAL` labels.

---

## 11. Feature Description

| Feature | Type | Range | Description |
| :--- | :--- | :--- | :--- |
| `attendance_percentage` | Float | 0.0 – 100.0 | Overall cumulative attendance percentage |
| `absent_days` | Integer | 0 – 50 | Total number of absent class sessions |
| `consecutive_absences` | Integer | 0 – 30 | Current unbroken streak of missed classes |
| `attendance_trend` | Float | 0.0 – 100.0 | Recent 10-day moving attendance percentage |
| `internal_marks` | Float | 0.0 – 100.0 | Average continuous internal assessment score |
| `assignment_completion`| Float | 0.0 – 100.0 | Percentage of homework/lab assignments completed |
| `activity_score` | Float | 0.0 – 100.0 | Co-curricular & lab participation score |

---

## 12. Prediction Methodology
1. The user inputs student features manually or selects an enrolled student from the auto-fill menu.
2. Feature vectors are validated for numerical bounds (0 to 100).
3. The loaded Random Forest model predicts class probabilities via `predict_proba()`.
4. The highest-probability class determines the `predicted_condition` and `confidence` score.
5. The record is persisted into the SQLite `predictions` table.

---

## 13. Risk Score Methodology
In addition to categorical classification, the system computes an **Explainable Risk Score (0–100)**:

$$\text{Risk Score} = 0.40 \cdot (100 - \text{Att}) + 0.20 \cdot \min(20, \text{Streak} \times 5) + 0.15 \cdot (100 - \text{Trend}) + 0.08 \cdot (100 - \text{Marks}) + 0.07 \cdot (100 - \text{Assign}) + 0.10 \cdot (100 - \text{Activity})$$

- **0 – 29:** **SAFE** (Good academic standing)
- **30 – 59:** **AT RISK** (Requires faculty check-in and weekly targets)
- **60 – 100:** **CRITICAL** (Urgent mentor intervention & official warning notice)

---

## 14. Database Design (SQLite)

```text
+-------------------+        +--------------------+
|       users       |        |      subjects      |
+-------------------+        +--------------------+
| id (PK)           |        | id (PK)            |
| name              |        | subject_code (UQ)  |<--+
| email (UQ)        |        | subject_name       |   |
| username (UQ)     |        | department         |   |
| password_hash     |        | year               |   |
| role              |        +--------------------+   |
| department        |                                 |
| created_at        |        +--------------------+   |
+-------------------+        |     attendance     |   |
                             +--------------------+   |
+-------------------+        | id (PK)            |   |
|     students      |        | student_id (FK)    |   |
+-------------------+        | subject_id (FK)    |---+
| id (PK)           |        | date               |
| student_id (UQ)   |<--+    | status             |
| name              |   |    | recorded_at        |
| department        |   |    +--------------------+
| year              |   |
| section           |   |    +--------------------+
| email             |   |    |    predictions     |
| created_at        |   |    +--------------------+
+-------------------+   |    | id (PK)            |
                        +--->| student_id         |
                        |    | features...        |
                        |    | predicted_condition|
                        |    | confidence         |
                        |    | risk_score         |
                        |    | recommendation     |
                        |    | created_at         |
                        |    +--------------------+
                        |
                        |    +--------------------+
                        |    |       alerts       |
                        |    +--------------------+
                        |    | id (PK)            |
                        +--->| student_id (FK)    |
                             | alert_type         |
                             | message            |
                             | severity           |
                             | status             |
                             | created_at         |
                             +--------------------+
```

---

## 15. Project Structure

```text
ai_student_attendance_tracker/
│
├── app.py                      # Flask backend, auth routes, database init & REST APIs
├── train_model.py              # ML model trainer (synthetic data generation, RF training, metrics)
├── requirements.txt            # Python dependencies
├── README.md                   # Complete academic documentation
│
├── model/
│   ├── attendance_risk_model.pkl  # Trained Random Forest model (joblib)
│   └── model_metadata.json        # True calculated accuracy (99.4%) and feature weights
│
├── database/
│   └── attendance.db           # SQLite database (auto-generated & seeded on startup)
│
├── templates/
│   ├── register.html           # User registration page
│   ├── login.html              # User login page (with 1-click demo credential filler)
│   ├── base.html               # Master layout (sidebar, navbar, user profile chip, modal)
│   ├── index.html              # Dashboard overview
│   ├── students.html           # Student directory & profile modal
│   ├── attendance.html         # Single & batch attendance recording
│   ├── analytics.html          # Dynamic Chart.js visualizations
│   ├── prediction.html         # AI prediction form & action recommendation card
│   ├── alerts.html             # Multi-tier alert management
│   ├── reports.html            # Attendance standings & print reports
│   └── about.html              # System architecture, DB design & ML metrics
│
└── static/
    ├── css/
    │   └── style.css           # Custom engineering theme (#0B1220, #2563EB, #06B6D4)
    └── js/
        └── script.js           # Vanilla JavaScript API engine, Auth handlers, Chart.js
```

---

## 16. Installation

Ensure Python 3.9+ is installed on your system.

```bash
# 1. Navigate to the project directory
cd "AI ATTENDANCE"

# 2. Install required dependencies
python -m pip install -r requirements.txt
```

---

## 17. Model Training

Train the Random Forest model and generate evaluation metrics:

```bash
python train_model.py
```

*Expected Terminal Output:*
```text
============================================================
AI Student Attendance Tracker - Model Training
============================================================
Generating synthetic student dataset...
Dataset generated successfully. Total records: 2500
Training Random Forest model...
Training completed.
Test Accuracy: 99.4%
Model saved successfully at: model/attendance_risk_model.pkl
Model metadata saved at: model/model_metadata.json
============================================================
```

---

## 18. Running Flask Application

Start the local development server:

```bash
python app.py
```

Access the application in any web browser at:
```text
http://127.0.0.1:5000
```

---

## 19. API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/api/register` | Registers a new faculty / admin account |
| `POST` | `/api/login` | Authenticates user and sets session cookie |
| `GET` | `/api/current_user` | Returns currently logged-in user profile |
| `GET` | `/api/dashboard` | Returns live counts, averages, recent logs, and at-risk students |
| `GET` | `/api/students` | Returns all students with computed attendance % and risk category |
| `GET` | `/api/students/<student_id>` | Returns detailed profile, subject breakdown, and recent history |
| `GET` | `/api/attendance/<student_id>` | Returns complete attendance logs for a student |
| `POST` | `/api/attendance` | Records single or batch attendance sessions with validation |
| `GET` | `/api/analytics` | Returns aggregated metrics for all 5 Chart.js instances |
| `POST` | `/api/predict` | Runs ML risk prediction, computes risk score & returns recommendations |
| `GET` | `/api/predictions` | Retrieves past prediction history records |
| `GET` | `/api/alerts` | Returns system alerts filterable by severity and status |
| `POST` | `/api/alerts/<id>/resolve` | Marks an alert as resolved |
| `GET` | `/api/subjects` | Returns list of academic courses |
| `GET` | `/api/metadata` | Returns true ML model accuracy and system status |

---

## 20. Sample API Requests & Responses

### A. Register Account (`POST /api/register`)
**Request:**
```json
{
  "name": "Prof. Kavin Raj",
  "username": "kavin_faculty",
  "email": "kavin@college.edu",
  "role": "Class Mentor",
  "department": "CSBS",
  "password": "secure_password_123"
}
```
**Response:**
```json
{
  "success": true,
  "message": "Registration successful! You can now log in with your credentials."
}
```

### B. Login Account (`POST /api/login`)
**Request:**
```json
{
  "username": "admin",
  "password": "admin123"
}
```
**Response:**
```json
{
  "success": true,
  "message": "Welcome back, Dr. S. Ramesh!",
  "user": {
    "id": 1,
    "name": "Dr. S. Ramesh",
    "email": "faculty@college.edu",
    "username": "admin",
    "role": "Faculty Advisor",
    "department": "CSBS"
  }
}
```

---

## 21. Screens & Pages Overview
1. **Register Page (`/register`)**: New account registration form for faculty/staff with role and department selection.
2. **Login Page (`/login`)**: Secure login page with 1-click demo credential filler (`admin` / `admin123`).
3. **Overview (`/`)**: Main monitoring dashboard with real-time stat cards, attention alerts, and trend charts.
4. **Students (`/students`)**: Searchable student table with visual attendance progress bars and modal profile viewer.
5. **Attendance (`/attendance`)**: Dual interface for logging single attendance or entire class batch roll calls.
6. **Analytics (`/analytics`)**: 5 Chart.js visualizations covering daily trends, subject averages, tiers, and ratios.
7. **AI Prediction (`/prediction`)**: Risk evaluation tool with student profile auto-fill and structured recommendations.
8. **Alerts (`/alerts`)**: System-wide alert center categorized by `INFO`, `WARNING`, and `CRITICAL`.
9. **Reports (`/reports`)**: Printable semester attendance audit report with institutional sign-off sections.
10. **About (`/about`)**: Technical project documentation and live ML model evaluation metrics.

---

## 22. Future Enhancements
- 📷 **Computer Vision:** Face recognition-based automated classroom attendance using OpenCV.
- 📲 **Instant Notifications:** Automated WhatsApp/SMS gateway alerts to parents when consecutive absences exceed 3 days.
- 💳 **Biometric / RFID Hardware:** Integration with physical RFID scanners for laboratory punch-ins.
- 🔐 **Role-Based Access Control:** Distinct permission levels for Students, Faculty Advisors, and Head of Department.

---

## 23. Limitations
- Uses simulated student attendance distributions for academic demonstration purposes.
- Attendance risk calculations are decision-support guidelines and require faculty verification before official detention.

---

## 24. Academic Disclaimer
*This software is developed solely as a college mini-project prototype for demonstrating AI/ML integration in academic administration. It is designed to be easily extensible for production university ERP integration.*
