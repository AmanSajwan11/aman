             #  Hospital Management 
from datetime import datetime

class Hospital:
     # Initialize the patients and doctors lists
    def __init__(self): 
        self.patients = []
        self.doctors = []

    # Method to add a patient to the patients list
    def add_patient(self, name, age, illness):
        self.patients.append({"name": name, "age": age, "illness": illness, "medical_records": []})

     # Method to add a doctor to the doctors list
    def add_doctor(self, name, specialization, availability=None):
        if availability is None:
            availability = []
        self.doctors.append({"name": name, "specialization": specialization, "availability": availability})

    # Method to print all patients' detail
    def get_patients(self):
        for patient in self.patients:
            print(f"Patient Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")
  
    # Method to print all doctors' details
    def get_doctors(self):
        for doctor in self.doctors:
            print(f"Doctor Name: {doctor['name']}, Specialization: {doctor['specialization']}")

    def schedule_appointment(self, patient_name, doctor_name, date_time):
        for doctor in self.doctors:
            if doctor['name'] == doctor_name:
                if date_time in doctor['availability']:
                    for patient in self.patients:
                        if patient['name'] == patient_name:
                            print(f"Appointment scheduled for {patient_name} with {doctor_name} at {date_time}")
                            doctor['availability'].remove(date_time)
                            patient['medical_records'].append({"doctor": doctor_name, "date_time": date_time})
                            return
                    print(f"Patient {patient_name} not found.")
                    return
        print(f"No available slots for {doctor_name} at {date_time}")

    def set_doctor_availability(self, doctor_name, availability):
        for doctor in self.doctors:
            if doctor['name'] == doctor_name:
                doctor['availability'] = availability
                print(f"Availability set for {doctor_name}")

    def get_doctor_schedule(self, doctor_name):
        for doctor in self.doctors:
            if doctor['name'] == doctor_name:
                print(f"Doctor {doctor_name} Availability:")
                for slot in doctor['availability']:
                    print(slot)



hospital = Hospital()

while True:
    print("1. Add Patient")
    print("2. Add Doctor")
    print("3. Get Patients")
    print("4. Get Doctors")
    print("5. Schedule Appointment")
    print("6. Set Doctor Availability")
    print("7. Get Doctor Schedule")
    print("8. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter Patient Name: ")
        age = int(input("Enter Patient Age: "))
        illness = input("Enter Patient Illness: ")
        hospital.add_patient(name, age, illness)
    elif choice == 2:
        name = input("Enter Doctor Name: ")
        specialization = input("Enter Doctor Specialization: ")
        hospital.add_doctor(name, specialization)
    elif choice == 3:
        hospital.get_patients()
    elif choice == 4:
        hospital.get_doctors()
    elif choice == 5:
        patient_name = input("Enter Patient Name: ")
        doctor_name = input("Enter Doctor Name: ")
        date_time = input("Enter Appointment Date and Time (YYYY-MM-DD HH:MM): ")
        hospital.schedule_appointment(patient_name, doctor_name, date_time)
    elif choice == 6:
        doctor_name = input("Enter Doctor Name: ")
        availability = input("Enter Doctor Availability (comma-separated date-time strings): ").split(",")
        hospital.set_doctor_availability(doctor_name, availability)
    elif choice == 7:
        doctor_name = input("Enter Doctor Name: ")
        hospital.get_doctor_schedule(doctor_name)
    elif choice == 8:
        break
 
      # EXIT THE PROGRAM