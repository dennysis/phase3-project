# lib/cli.py

import click
from db.models import Session, Patient, Doctor, Appointment

session = Session()

@click.group()
def cli():
    pass

@cli.command()
@click.argument('name')
@click.argument('age')
def add_patient(name, age):
    """Add a new patient."""
    patient = Patient(name=name, age=int(age), status='admitted')  # Set status to 'admitted' by default
    session.add(patient)
    session.commit()
    click.echo(f'Patient {name} added and admitted.')

@cli.command()
@click.argument('patient_id')
def delete_patient(patient_id):
    """Delete a patient."""
    patient = session.query(Patient).get(patient_id)
    if patient:
        session.delete(patient)
        session.commit()
        click.echo(f'Patient {patient.name} deleted.')
    else:
        click.echo('Patient not found.')

@cli.command()
def list_patients():
    """List all patients."""
    patients = session.query(Patient).all()
    for patient in patients:
        click.echo(f'{patient.id}: {patient.name}, {patient.age} years old, Status: {patient.status}')

@cli.command()
@click.argument('patient_id')
def admit_patient(patient_id):
    """Admit a patient."""
    patient = session.query(Patient).get(patient_id)
    if patient:
        patient.status = 'admitted'
        session.commit()
        click.echo(f'Patient {patient.name} admitted.')
    else:
        click.echo('Patient not found.')

@cli.command()
@click.argument('patient_id')
@click.argument('prescription')
def release_patient(patient_id, prescription):
    """Release a patient with a prescription."""
    patient = session.query(Patient).get(patient_id)
    if patient:
        patient.status = 'released'
        patient.prescription = prescription
        session.commit()
        click.echo(f'Patient {patient.name} released with prescription: {prescription}.')
    else:
        click.echo('Patient not found.')

cli.add_command(add_patient)
cli.add_command(delete_patient)
cli.add_command(list_patients)
cli.add_command(admit_patient)
cli.add_command(release_patient)

if __name__ == '__main__':
    cli()
