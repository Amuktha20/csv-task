import csv
with open("employeedata.csv","r",newline="") as file:
    reader=csv.reader(file)
    header=next(reader)
    rows=[]
    for row in reader:
        year=row[3][:4]
        if year=="2024":
            salary=float(row[2])
            salary=salary+(salary*20/100)
            row[2]=str(salary)
        rows.append(row)
with open("updated_employees_salary.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(header)
    writer.writerows(rows)

print("Employee salaries updated successfully!")

