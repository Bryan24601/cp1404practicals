"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))
if score < 0:
    status = "Invalid Score"
elif score < 50:
    status = "Bad"
elif score < 90:
    status = "Passable"
elif score < 100:
    status = "Excellent"
else:
    status = "Invalid Score"
print(status)
