import os
import pandas as pd
import matplotlib.pyplot as plt

BASE_PAY = 20
OT_MULTIPLIER = 1.5

#Verify data files exist
required_files = ['employees.csv', 'orders.csv']
missing = [f for f in required_files if not os.path.exists(f)]
if missing:
    print(f"ERROR: Missing file(s): {', '.join(missing)}.")
    exit(1)

employees = pd.read_csv('employees.csv')
orders = pd.read_csv('orders.csv')

#Data validation
if employees.isnull().any().any():
    print("WARNING: Null values detected in employees.csv.")
if orders.isnull().any().any():
    print("WARNING: Null values detected in orders.csv.")
if (employees['hours_worked'] > 16).any():
    print("WARNING: One or more employees logged over 16 hours in a day. Check your data.")

def calc_pay(row):
    hrs = row['hours_worked']
    overtime = max(0, hrs - 8)
    return 8 * BASE_PAY + overtime * BASE_PAY * OT_MULTIPLIER if overtime else hrs * BASE_PAY

employees['pay'] = employees.apply(calc_pay, axis=1)

payroll = (
    employees.groupby(['employee_id', 'name'], as_index=False)
    .agg({'hours_worked': 'sum', 'pay': 'sum'})
)

billing = (
    orders.groupby(['employee_id', 'customer'], as_index=False)
    .agg({'amount_billed': 'sum'})
)

summary = pd.merge(payroll, billing, on='employee_id', how='left')

print("\nPayroll Summary:\n", payroll)
print("\nOrder Billing Summary:\n", billing)
print("\nEmployee Summary:\n", summary)

payroll.to_csv('payroll_summary.csv', index=False)
summary.to_csv('employee_summary.csv', index=False)
summary.to_excel('employee_summary.xlsx', index=False)
print("\nReports exported: payroll_summary.csv, employee_summary.csv, employee_summary.xlsx")

#Visualization: Total Pay by Employee
plt.figure(figsize=(8, 5))
plt.bar(payroll['name'], payroll['pay'], color='#4682b4')
plt.title('Total Pay by Employee')

plt.xlabel('Employee')
plt.ylabel('Total Pay (USD)')

plt.tight_layout()
plt.savefig('pay_by_employee.png')
plt.close()
print("Pay chart saved as pay_by_employee.png")
