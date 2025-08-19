# Sales Reporting Pipeline

This project automates the process of reading, cleaning, analyzing, and reporting sales data using Python and pandas.

---

## Features

- Reads sales data from CSV files  
- Cleans data by parsing dates and handling missing values  
- Aggregates sales by city (total and average)  
- Identifies top sales transactions  
- Generates Excel reports (`summary.xlsx` and `top_sales.xlsx`)  
- Includes error handling and logging (e.g., missing files, malformed rows)  
- Can be run easily via command line  

---

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sky2d2/sales-reporting-pipeline.git
   cd sales-reporting-pipeline
   ```

2. **Create and activate a virtual environment**:

   **On macOS/Linux**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   **On Windows**:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Place your sales CSV file inside the `data/` folder (you can use or modify the provided sample).

Run the reporting script by specifying the CSV file path:

```bash
python sales_report.py data/sales.csv
```

---

## Input Data Format

The CSV file should have at least the following columns:

- `date` — date of the sale (any standard format is supported)  
- `city` — city where the sale occurred (optional, missing values filled as `"Unknown"`)  
- `amount` — numeric sales amount (rows missing this are ignored)  

**Example:**
```csv
date,city,amount
2025-08-01,New York,100
2025-08-02,Los Angeles,200
2025-08-03,,150
```

---

## Output

- `summary.xlsx` — Excel file aggregating total and average sales by city  
- `top_sales.xlsx` — Excel file listing the top 5 sales transactions by amount  
- `sales_report.log` — Log file capturing workflow information and errors  

---

## Project Structure

```
sales-reporting-pipeline/
├── data/                # Input sales CSV files
├── sales_report.py      # Main reporting script
├── requirements.txt     # Dependencies
└── README.md            # Documentation
```
