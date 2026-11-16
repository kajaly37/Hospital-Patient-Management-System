from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "hospital-management-secret-key"

DATABASE = "database.db"


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            phone TEXT NOT NULL,
            address TEXT,
            blood_group TEXT,
            disease TEXT,
            admission_date TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def dashboard():
    conn = get_db_connection()

    total_patients = conn.execute(
        "SELECT COUNT(*) FROM patients"
    ).fetchone()[0]

    recent_patients = conn.execute(
        "SELECT * FROM patients ORDER BY id DESC LIMIT 5"
    ).fetchall()

    conn.close()

    return render_template(
        "dashboard.html",
        total_patients=total_patients,
        recent_patients=recent_patients
    )


@app.route("/patients")
def patients():

    search = request.args.get("search", "").strip()

    conn = get_db_connection()

    if search:
        patients = conn.execute("""
            SELECT * FROM patients
            WHERE name LIKE ?
               OR phone LIKE ?
               OR disease LIKE ?
               OR blood_group LIKE ?
            ORDER BY id DESC
        """, (
            f"%{search}%",
            f"%{search}%",
            f"%{search}%",
            f"%{search}%"
        )).fetchall()
    else:
        patients = conn.execute(
            "SELECT * FROM patients ORDER BY id DESC"
        ).fetchall()

    conn.close()

    return render_template(
        "patients.html",
        patients=patients,
        search=search
    )

@app.route("/add-patient", methods=["GET", "POST"])
def add_patient():

    if request.method == "POST":

        name = request.form["name"]
        age = request.form["age"]
        gender = request.form["gender"]
        phone = request.form["phone"]
        address = request.form["address"]
        blood_group = request.form["blood_group"]
        disease = request.form["disease"]
        admission_date = request.form["admission_date"]

        conn = get_db_connection()

        conn.execute("""
            INSERT INTO patients
            (name, age, gender, phone, address, blood_group, disease, admission_date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            name,
            age,
            gender,
            phone,
            address,
            blood_group,
            disease,
            admission_date
        ))

        conn.commit()
        conn.close()

        flash("Patient added successfully!")

        return redirect(url_for("patients"))

    return render_template("add_patient.html")


@app.route("/edit-patient/<int:id>", methods=["GET", "POST"])
def edit_patient(id):

    conn = get_db_connection()

    patient = conn.execute(
        "SELECT * FROM patients WHERE id = ?",
        (id,)
    ).fetchone()

    if not patient:
        conn.close()
        return "Patient not found", 404

    if request.method == "POST":

        name = request.form["name"]
        age = request.form["age"]
        gender = request.form["gender"]
        phone = request.form["phone"]
        address = request.form["address"]
        blood_group = request.form["blood_group"]
        disease = request.form["disease"]
        admission_date = request.form["admission_date"]

        conn.execute("""
            UPDATE patients
            SET name = ?,
                age = ?,
                gender = ?,
                phone = ?,
                address = ?,
                blood_group = ?,
                disease = ?,
                admission_date = ?
            WHERE id = ?
        """, (
            name,
            age,
            gender,
            phone,
            address,
            blood_group,
            disease,
            admission_date,
            id
        ))

        conn.commit()
        conn.close()

        flash("Patient updated successfully!")

        return redirect(url_for("patients"))

    conn.close()

    return render_template("edit_patient.html", patient=patient)


@app.route("/delete-patient/<int:id>")
def delete_patient(id):

    conn = get_db_connection()

    conn.execute(
        "DELETE FROM patients WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()

    flash("Patient deleted successfully!")

    return redirect(url_for("patients"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)