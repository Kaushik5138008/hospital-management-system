import csv           #for importing comma separated values
import uuid           #universally unique identifier as randomizer for patient id
import datetime    #importing the date time module for assigning the current date of patient admission




def add_patient():
    print('***************PATIENT REGISTRATION***************')
    opening_a_file=open("Patient_Details.csv","a+",newline="")  #creating a new file named Patients_Details.csv
    write_in_file=csv.writer(opening_a_file)  #writing in that created file
    headers=["Id","Name"," Phone_no","Email","Age","Gender","Issue"]   #format of csv file
    write_in_file.writerow(headers)          #for writing it as a csv file
    inp1=int(input("Enter how many Patient Details You want To Insert: "))
    user=1
    for i in range(inp1):
        print(f"please enter user {user} details: ")
        Name = input("Enter Your Name: ")
        Phone_no = int(input("Enter your Phn no.: "))
        Email = input("Enter Your Email: ")
        Age = int(input("Enter Your Age: "))
        Gender = input("Enter Your Gender: ")
        Issue = input("Enter Your Issue: ")
        today= datetime.date.today()
        Admission_date= print("Admission date: ",today.strftime("%Y, %m, %d"))
        Id = (str(uuid.uuid4())[0:3])  #using uuid for generating a rndom unique patient id of 3 digit number
        print("Your Patient ID is:", Id)
        write_in_file.writerow([Id,Name,Phone_no,Email,Age,Gender,Issue])  #format of the csv file to be written
        user+=1
        print()
    opening_a_file.close() #closing a file

def retrieve_patient_details():
    print('***************PATIENT RESERVATION***************')
    opening_a_file2=open("patient_Details.csv","r")    #0pening the 1st file with the help of second file
    reading=csv.reader(opening_a_file2)     #reading the file
    inp1=input("enter your patient id-")
    coun1=0
    for row in reading: 
        if row[coun1]==inp1:
            print(["Id","Name"," Phone_no","Email","Age","Gender","Issue"])
            print(row[0:]) #to print existing rows
            break
        else:
            print("Patient details:")

def discharge_report():
    print('***************DISCHARGE SUMMARY***************')
    opening_a_file2=open("patient_Details.csv","r")    #to open the existing file of the patient
    reading=csv.reader(opening_a_file2)
    inp1=input("enter your patient id-")
    coun1=0
    for row in reading:
        if row[coun1]==inp1:
            print(["Id","Name"," Phone_no","Email","Age","Gender","Issue"])
            print(row[0:])  #to print existing rows
            break
        else:
            print("Patient details: ")
    today= datetime.date.today()   #defining function
    Discharge_date= print("Discharge date: ",today.strftime("%Y, %m, %d"))   #format to print datetime
    days_of_stay= int(input("Enter your days of stay: "))
    test_report= input("Following is the report of your tests: ")
    
def bill_generation():
    print('***************TOTAL BILL***************')
    opening_a_file2=open("patient_Details.csv","r")
    reading=csv.reader(opening_a_file2)
    inp1=input("enter your patient id-")
    coun1=0
    for row in reading:
        if row[coun1]==inp1:
            print(["Id","Name"," Phone_no","Email","Age","Gender","Issue"])   #format to be printed
            print(row[0:])
            break
        else:
            print("Patient details: ")
    days_of_stay=int(input("Enter your days of stay: "))
    print("Days of stay: ",days_of_stay)
    No_of_tests_held=int(input("No of tests held: "))
    print("Cost per day= Rs.",5000)  #defined amount
    print("Charges per test= Rs.",300)  #defined amount
    print("Amount charged= Rs.",((days_of_stay*5000)+(No_of_tests_held*300)))  #the bill structure generation
    
def exit():
    print("Thank you for visiting our hospital")
    
    
print("Select Operation\n 1-ADD A PATIENT,\n 2-RETRIEVE A PATIENT DETAILS,\n 3-DISCHARGE SUMMARY,\n 4-BILL GENERATION,\n 5-EXIT")
while True:
    option=input("Enter the S. No of the Operation you wish to carry out (1/2/3/4/5):")  #to select the operation to do.
    if option not in ('1','2','3','4','5'):
        print("invalid entry")
    else:
        if option=='1':
            add_patient()
        elif option =='2':
            retrieve_patient_details()
        elif option=='3':
            discharge_report()
        elif option=='4':
            bill_generation()
        elif option=='5':
            exit()
        else:
            print("invalid")
    a=input("WANT TO CONTINUE FOR NEXT OPERATION,\n press [1] for YES or [0] for NO:     ")
    if a=="0":
        break