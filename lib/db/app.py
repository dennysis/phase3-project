

from models import Session, Patient, Doctor

def seed_data():
    session = Session()

  
    patient1 = Patient(name='John  Wick', age=30, status='admitted',heartbeat=72)
    patient2 = Patient(name='Jane Adhiambo', age=25, status='admitted',heartbeat=78)

   
    doctor1 = Doctor(name='Dr. Brown', specialty='Cardiology')
    doctor2 = Doctor(name='Dr. Green', specialty='Neurology')

    session.add_all([patient1, doctor2, doctor1,patient2])
    session.commit()

    session.close()

if __name__ == '__main__':
    seed_data()