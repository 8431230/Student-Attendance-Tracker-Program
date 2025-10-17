classes_held = int(input("Enter total classes held: "))
classes_attended = int(input("Enter total classes attended: "))

attendance = (classes_attended / classes_held) * 100

print("Classes Held:", classes_held)
print("Classes Attended:", classes_attended)
print("Attendance:", round(attendance, 2), "%")

if attendance >= 75:
    print("Status: Eligible for exams")
else:
    print("Status: Not eligible for exams")
