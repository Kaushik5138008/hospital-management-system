# Hospital Management System

This Hospital Management System is a Python-based application that allows for streamlined management of patient information, registration, discharge, and billing. Using CSV files to store and retrieve data, this system simplifies operations like adding new patient records, retrieving details, generating discharge summaries, and producing billing invoices.

## Features

- **Patient Registration**: Add new patients to the system and generate a unique patient ID using UUID.
- **Retrieve Patient Details**: Retrieve details of an existing patient by their unique patient ID.
- **Discharge Summary**: Generate and display a discharge summary for a patient, including their discharge date and any relevant notes.
- **Billing Generation**: Calculate the total bill based on days of stay and tests conducted.
- **Exit**: Safely exits the application.

## Prerequisites

- Python 3.x
- The following Python modules:
  - `csv`: For handling CSV files for data storage.
  - `uuid`: For generating a unique identifier for each patient.
  - `datetime`: For handling and formatting dates.

## How to Run

1. Clone or download the repository to your local machine.
2. Open a terminal in the project directory and run:

    ```bash
    python hospital_management_system.py
    ```

3. The menu will display available operations, where you can choose to:
    - Add a patient
    - Retrieve a patient's details
    - Generate a discharge summary
    - Generate a bill
    - Exit the program

## Project Structure

- `hospital_management_system.py`: Main script that contains the functionality for patient management, billing, and discharge.
- `Patient_Details.csv`: CSV file created by the script where patient records are stored.

## Usage

The program presents the following menu for interaction:

1. **Add a Patient**: Registers a new patient, capturing their name, phone number, email, age, gender, and issue. The patient's ID and admission date are automatically generated.
2. **Retrieve Patient Details**: Searches and displays patient details based on the provided patient ID.
3. **Discharge Summary**: Displays the patient information along with the discharge date, length of stay, and a test summary.
4. **Billing Generation**: Calculates the bill using a standard rate per day and test charges.
5. **Exit**: Closes the program.

### Example Output

```plaintext
Select Operation
1 - ADD A PATIENT
2 - RETRIEVE A PATIENT DETAILS
3 - DISCHARGE SUMMARY
4 - BILL GENERATION
5 - EXIT

### Data Storage Format
The program stores patient data in a CSV format with the following headers:

```csv
Id, Name, Phone_no, Email, Age, Gender, Issue
```
### Future Enhancements
Data Validation: Improve error handling for data entries (e.g., invalid phone numbers, age).
Database Integration: Store data in a relational database for more robust data management.
Enhanced UI: Develop a graphical interface for easier interaction.
License
This project is licensed under the MIT License.

### Acknowledgments
This project is inspired by the need to streamline and digitize hospital record-keeping and billing management. Special thanks to all contributors.
