import pandas as pd
import logging
import argparse

# Setup logging configuration
logging.basicConfig(
    filename='sales_report.log',
    format='%(asctime)s %(levelname)s %(message)s',
    level=logging.INFO
)

def read_and_clean_data(filepath):
    """
    Read sales CSV file and clean the data:
    - Parse 'date' column to datetime (invalid dates become NaT)
    - Drop rows missing 'amount'
    - Fill missing 'city' values with 'Unknown'
    """
    try:
        df = pd.read_csv(filepath)
        logging.info(f"Loaded data from {filepath}")
        
        # Parse dates safely
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        
        # Drop rows where 'amount' is missing or invalid
        df = df.dropna(subset=["amount"])
        
        # Fill missing 'city' with a default value
        df = df.fillna({"city": "Unknown"})
        
        return df
    
    except Exception as e:
        logging.error(f"Error reading or cleaning data: {e}")
        raise

def generate_summary(df):
    """
    Group sales by 'city' and calculate total and average sales.
    Returns a summary DataFrame with columns: city, total (sum), avg (mean).
    """
    summary = (
        df.groupby("city", as_index=False)["amount"]
        .agg(total="sum", avg="mean")
    )
    return summary

def save_reports(df, summary):
    """
    Save sales summary and top sales reports to Excel files.
    - summary.xlsx: City-level total and average sales
    - top_sales.xlsx: Top 5 sales by amount
    """
    try:
        summary.to_excel("summary.xlsx", index=False)
        logging.info("Summary report saved to summary.xlsx")
        
        top_sales = df.nlargest(5, "amount")
        top_sales.to_excel("top_sales.xlsx", index=False)
        logging.info("Top sales report saved to top_sales.xlsx")
    
    except Exception as e:
        logging.error(f"Error saving reports: {e}")
        raise

def main(args):
    """
    Main workflow:
    - Read and clean sales data
    - Generate summary stats
    - Merge summary stats back to the main dataframe
    - Save reports
    """
    df = read_and_clean_data(args.input)
    summary = generate_summary(df)
    
    # Merge summaries to enrich original data if needed
    merged = df.merge(summary, on="city", suffixes=("", "_city"))
    
    save_reports(merged, summary)
    logging.info("Sales reporting pipeline completed successfully.")

if __name__ == "__main__":
    # Command-line argument parsing
    parser = argparse.ArgumentParser(description="Sales reporting pipeline")
    parser.add_argument("input", help="Path to sales CSV file")
    args = parser.parse_args()
    
    main(args)
