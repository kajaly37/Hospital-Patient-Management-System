# 🏥 Hospital Patient Management System

A simple and user-friendly web-based application developed using **Python, Flask, SQLite, HTML, CSS, and JavaScript** to manage hospital patient records efficiently.

## 📌 About the Project

The Hospital Patient Management System is designed to simplify the process of managing patient information in a hospital.

It provides an easy-to-use dashboard where users can add, view, update, delete, and search patient records.

The project uses SQLite to store patient information securely in a local database.

## ✨ Features

- **Dashboard:** View total patients and gender-wise patient statistics.
- **Add Patient:** Register new patients with their personal and medical details.
- **View Patients:** Display all registered patient records.
- **Edit Patient:** Update existing patient information.
- **Delete Patient:** Remove patient records.
- **Search Patients:** Search patients by name, phone number, disease, or blood group.
- **Patient Details:** View complete information about an individual patient.
- **SQLite Database:** Store patient records locally.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web framework |
| SQLite | Database management |
| HTML | Web page structure |
| CSS | Styling and layout |
| JavaScript | Basic frontend functionality |
| Git & GitHub | Version control and project hosting |

## 📂 Project Structure

```text
Hospital-Patient-Management-System/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── patients.html
│   ├── add_patient.html
│   ├── edit_patient.html
│   └── patient_details.html
│
└── static/
    ├── css/
    │   └── style.css
    │
    └── js/
        └── script.js
```

**Note:** The SQLite database file (`database.db`) is generated automatically when the application runs.

## ⚙️ Installation and Setup

Follow these steps to run the project on your computer.

### 1. Clone the Repository

```bash
git clone https://github.com/kajaly37/Hospital-Patient-Management-System.git
```

### 2. Open the Project Folder

```bash
cd Hospital-Patient-Management-System
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
flask --app app run --debug
```

### 7. Open in Browser

Visit:

```text
http://127.0.0.1:5000
```

The Hospital Patient Management System should now be running locally.

## 🗄️ Database

The project uses **SQLite** for storing patient records.

Patient information includes:

- Patient ID
- Name
- Age
- Gender
- Phone Number
- Address
- Blood Group
- Disease
- Admission Date

## 🎯 Project Objective

The main objective of this project is to develop a beginner-friendly hospital patient management application that demonstrates the practical use of Python, Flask, database connectivity, and web development.

## 🚀 Future Improvements

- User authentication and login system.
- Patient report generation.
- Export patient records to PDF or Excel.
- Improved data validation.
- Role-based access control.

## 👩‍💻 Author

**Kajal Yadav**

Engineering Student | Artificial Intelligence & Data Science

## 📜 Disclaimer

This project is developed for educational purposes. Use fictional patient information for testing. It is not intended to store or manage real patient medical records.