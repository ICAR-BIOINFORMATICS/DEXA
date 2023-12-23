# DEXA
A Novel Python-Integrated Model for Advancing the Deciphering of  Differential Gene Expression Patterns

DEXA (Differential Gene Expression Analysis) is a Python-based tool designed for the robust analysis of RNA-seq data, facilitating the identification of differentially expressed genes. This user manual provides a step-by-step guide on how to set up and utilize DEXA effectively.

Step 1: Set Up the Computer System
Ensure that Python is installed on your system. If not, download and install Python from the official website: Python Downloads:         https://www.python.org/downloads/


Step 2: Import Required Python Modules
DEXA relies on a few Python modules for its functionality. You can install these modules using the following commands:
    Pip install pandas
  
    pip install numpy==1.18
    
    pip install scipy==1.1.0
    
    pip install xlrd==1.2.0
    
    pip install openpyxl
    

Note: Python Modules are specified with the versions for the ease of users 
Alternatively, consider installing Anaconda, a distribution that includes many commonly used Python libraries: Anaconda Downloads: https://www.anaconda.com/download


Step 3: Set Working Directory
Navigate to the directory where your input data is located, or where you want the output files to be generated. This can be done using the cd command:
    
      cd /path/to/your/directory

Step 4: Run the DEXA Command Line Tool
Execute the DEXA command-line tool by entering the following command:
  
    python3 DEXA.py <input_file.xlsx>

Replace <input_file.xlsx> with the path to your input Excel file containing the Count matrix data.


# Contact Information
For further assistance or inquiries, please contact:

Dr. Shbana Begam 

Scientist, ICAR-NIPB, New Delhi-110012

Email: shbana.begam@icar.gov.in

Dr. Samarth Godara

Scientist, ICAR-IASRI, New Delhi-110012

Email: samarth.godara@icar.gov.in
