def add_patient(patients, name, age, disease):
    patients.append({"Name": name, "Age": age, "Disease": disease})

def search_patients_by_disease(patients, disease):
    return [patient["Name"] for patient in patients if patient["Disease"] == disease]

# User input
patients = []
num_patients = int(input("Enter the number of patients: "))
for _ in range(num_patients):
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    disease = input("Enter patient disease: ")
    add_patient(patients, name, age, disease)

search_disease = input("Enter disease to search for: ")
found_patients = search