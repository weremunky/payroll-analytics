# Payroll Analytics Tool

A Python implementation of an automated payroll and order billing analytics solution for a moving business. Built to demonstrate a systematic approach to business operations, reporting, and data-driven efficiency.

---

## What This Does

This project processes employee timesheets and customer orders to automate payroll calculation (including overtime), link employee work logs to customer billing, and generate clear summary reports and visualizations. I used sample business data to simulate real-world business analytics and process improvement.

> **Note:**  
> This code is a recreation of an internal tool I originally developed for my previous job to automate payroll and order analytics at a moving business.  
> The CSV files provided in this repository are for demonstration and testing purposes only, to illustrate how the code works with example data.

---

## Key Features

- **Real data ingestion:** Uses pandas to load actual employee and order CSV files
- **Payroll automation:** Calculates pay, including overtime rules
- **Order linking:** Connects customer billing directly to employee work logs
- **Summary reporting:** Outputs results as both CSV and Excel files
- **Risk checks:** Warns of missing files, excessive hours, or missing values
- **Visual analysis:** Generates a bar chart of total pay by employee

---

## Setup & Installation

You'll need Python 3.7+ and a few libraries.  
Install dependencies with:

```bash
pip3 install pandas matplotlib openpyxl
```

That’s it. No special accounts or paid tools required.

---
## Universal Usage & Customization

This script is plug-and-play for any business with similar CSV data.
Set your own filenames, pay rates, and overtime rules from the command line:

```bash
python3 main.py --employees my_employees.csv --orders my_orders.csv --base_pay 25 --ot_multiplier 2.0
```

- `--employees`: Employee data CSV (default: employees.csv)
- `--orders`: Orders/billing CSV (default: orders.csv)
- `--base_pay`: Base pay per hour (default: 20)
- `--ot_multiplier`: Overtime multiplier (default: 1.5)

---

## How to Run

Just run the main script with your CSV data files in the same folder:

```bash
python3 main.py
```

The program will:

    Load employee and order data from CSVs

    Calculate payroll and link to billing

    Output summary reports as CSV and Excel

    Print warnings for any suspicious or missing data

    Show a bar chart of total pay by employee

---

## Understanding the Results

The output gives you several key deliverables:

    payroll_summary.csv: Total hours and pay per employee

    employee_summary.csv / .xlsx: Combined payroll and billing details per employee

    pay_by_employee.png: Visual chart comparing total pay by employee

The script also warns you if an employee is logged for over 16 hours/day, or if there are missing fields in your data.
What I Learned

---

## This project taught me a lot about:

- Automating real-world business reporting and payroll

- Handling operational data with Python and pandas

- Performing basic error checking on business data

- Creating professional reports and business visuals

While this payroll tool is not complex software, it reflects the backbone of business analytics work in any company.
Next Steps & Improvements

---

## Some ideas I’m considering for future versions:

- Add custom pay rates and overtime rules per job/employee

- Export management dashboards with richer visuals

- Integrate with Google Sheets or business databases

- Implement user authentication for sensitive payroll access

This project gave me hands-on experience with the kind of operational automation that’s standard in real-world analytics and data roles, and I’m excited to expand on it.

---
Ian Angel, 2024
