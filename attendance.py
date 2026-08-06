import json
import csv
import os
import time
import random
from datetime import datetime

# ---------- Load Student Database ----------

with open("students.json", "r") as file:
    students = json.load(file)

attendance_file = "attendance.csv"

if not os.path.exists(attendance_file):
    with open(attendance_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "ID",
            "Name",
            "Department",
            "Date",
            "Time",
            "Confidence",
            "Liveness",
            "Mask",
            "Status"
        ])

marked = set()

# ---------- Boot Screen ----------

print("\n")
print("╔══════════════════════════════════════════════╗")
print("║      AI SMART ATTENDANCE AGENT v2.0         ║")
print("║    Facial Recognition Simulation Engine     ║")
print("╚══════════════════════════════════════════════╝")

modules = [
    "Camera Module",
    "Face Recognition Engine",
    "Student Database",
    "Attendance Database",
    "AI Decision Module"
]

for module in modules:
    print(f"Loading {module}...")
    time.sleep(0.8)

print("\nSystem Status : ONLINE")
print("-" * 55)

# ---------- Main Loop ----------

while True:

    print("\nScanning Classroom...")
    time.sleep(1)

    print("Face Detected\n")

    name = input("Enter Detected Student Name (or exit): ")

    if name.lower() == "exit":
        break

    student = None

    for s in students:
        if s["name"].lower() == name.lower():
            student = s
            break

    if student:

        if student["id"] in marked:

            print("\nDuplicate Entry Detected")
            print("Attendance already recorded.\n")
            continue

        confidence = round(random.uniform(95, 99.9), 2)

        liveness = random.choice(["PASS", "PASS", "PASS", "PASS"])

        mask = random.choice(["No Mask", "Mask Detected"])

        print("\nSearching Database...")
        time.sleep(1)

        print("\nMatch Found\n")

        print("Student Information")
        print("-----------------------------")
        print("ID          :", student["id"])
        print("Name        :", student["name"])
        print("Department  :", student["department"])
        print("Year        :", student["year"])

        print("\nAI Analysis")
        print("-----------------------------")
        print("Confidence      :", confidence, "%")
        print("Liveness        :", liveness)
        print("Mask Detection  :", mask)

        print("\nDecision")
        print("-----------------------------")

        now = datetime.now()

        date = now.strftime("%d-%m-%Y")
        current_time = now.strftime("%H:%M:%S")

        with open(attendance_file, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                student["id"],
                student["name"],
                student["department"],
                date,
                current_time,
                confidence,
                liveness,
                mask,
                "Present"
            ])

        marked.add(student["id"])

        print("Attendance Accepted")

    else:

        print("\nWARNING")
        print("-----------------------------")
        print("Unknown Face")
        print("Attendance Denied")

# ---------- Dashboard ----------

print("\n")
print("=" * 45)
print("TODAY'S ATTENDANCE DASHBOARD")
print("=" * 45)

for sid in marked:
    for s in students:
        if s["id"] == sid:
            print("✓", s["name"])

print("\nTotal Students :", len(students))
print("Present        :", len(marked))
print("Absent         :", len(students) - len(marked))

percentage = (len(marked) / len(students)) * 100

print("Attendance %   :", round(percentage, 2), "%")

print("\nAttendance Saved Successfully")
print("System Closed")