import pandas as pd
# glob module is use to retrieve files or dic
#that matches a specipic pattern
import glob
from fpdf import FPDF 
from pathlib import Path


filepaths=glob.glob("Invoices/*.xlsx")

for filepath in filepaths:
    df=pd.read_excel(filepath,sheet_name="Sheet 1")
    #Create a pdf object with potrait orientation
    pdf=FPDF(orientation="P",unit="mm",format="A4")
    # Add a new page 
    pdf.add_page()
    filename=Path(filepath).stem
    invoice_nr,date=filename.split("-")
    pdf.set_font(family="Times",size=18,style="B")
    pdf.cell(w=60, h=10,txt=f"Invoice nr.{invoice_nr}",ln=1)
    pdf.set_font(family="Times",size=18,style="B")
    pdf.cell(w=60, h=10,txt=f"Date:{date}")
    
    pdf.output(f"Pdfs/{filename}.pdf")
    
    
    
    