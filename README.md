# AUTHOR
(Dennis.M.Kiguru)

# Date
(13/06/2024)

# Afia Records

## Description
The Medical Record System is a command-line application designed to manage patient and doctor information, as well as schedule and list appointments. This system uses SQLite as the database backend and SQLAlchemy as the ORM (Object Relational Mapper).

## MNP Features
* Add, delete, and list patients.
* Admit and release patients with a prescription.
* Schedule appointments between doctors and patients.
* List all scheduled appointments.


## pre-requiements 
* Python 3.x
* Click library (pip install click)
* SQLAlchemy library (pip install sqlalchemy)*

## usage
Run the command-line interface (CLI) to manage patients and appointments:

(python lib/cli.py)

Upon running the CLI, you will be presented with several options:

1. Add Patient: Add a new patient to the system.
1. Delete Patient: Remove an existing patient from the system.
1. List Patients: Display all patients in the system.
1. Admit Patient: Admit a patient to the system.
1. Release Patient: Release a patient from the system with a prescription.
1. Schedule Appointment: Schedule an appointment for a patient with a doctor.
1. List Appointments: List all scheduled appointments.
1. Exit: Exit the CLI.


# Database Models

#### Patients:

* id: Integer, Primary Key
* name: String
* age: Integer
* heartbeat: Integer
* status: String (e.g., admitted, released)
* prescription: String


#### Doctors:

* id: Integer, Primary Key
* name: String
* specialty: String


#### Appointments:

* id: Integer, Primary Key
* doctor_id: Integer, Foreign Key referencing Doctors.id
* patient_id: Integer, Foreign Key referencing Patients.id
* date: DateTime


#### patient_doctor_association (Association Table):

* patient_id: Integer, Foreign Key referencing Patients.id
* doctor_id: Integer, Foreign Key referencing Doctors.id



# Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

# License
This project is licensed under the MIT License. See the LICENSE file for details.