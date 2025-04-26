import csv
from collections import defaultdict

def analyze_grades(csv_file_path, threshold):
    """
    Analyze a CSV file and print names of students whose average grade is above the threshold.

    """
    student_grades = defaultdict(list)

    # Read CSV
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['name']
            grade = float(row['grade'])
            student_grades[name].append(grade)

    print(f"\nStudents with average grade above {threshold}:")
    
    for name, grades in student_grades.items():
        avg_grade = sum(grades) / len(grades)
        if avg_grade > threshold:
            print(f" - {name} (Average Grade: {avg_grade:.2f})")

def main():
    csv_file_path = 'students.csv'
    threshold = 80

    analyze_grades(csv_file_path, threshold)

if __name__ == "__main__":
    main()

