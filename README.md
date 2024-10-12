## Excel to PDF Invoice Generator
This python scripts convert Excel files into individual pdf invoices using following libraries:
1. glob: To locate all Excel files.
2. Pandas: To read Excel files and extract invoice data.
3. FPDF: To generate PDFs.
4. pathlib: To handle file paths and extract filenames


## How it Works
1.The script uses glob to search for all Excel files in the specified directory.
2.For each Excel file , the script reads the data using pandas and extract invoice details.
3.The FPDF library is used to generate a PDF for each Invoice.
4. The pdf files are named based on the Excel File name (Without the Extension) and saved the output in directory.

   

