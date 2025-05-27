
class doctor:
    def __init__(self,name,availabe_date,specialty):
        self.name=name
        self.availabe_date=availabe_date
        self.specialty=specialty   


    def patient(self,name,preffered_date,medical_case):
        self.name=name
        self.preffered_date=preffered_date
        self.medical_case=medical_case
    
    def schedule_appointment(doctor,patient):
        if doctor.self.specialty.lower() in patient.self.medical_case.lower():
            if patient(self.preffered_date) == doctor(self.availabe_date) and doctor(self.specialty)==patient(self.medical_case):
                return f"Make appointment schedule with Dr. {doctor.name} on {patient.preffered_date} for {patient.name}'s {patient.medical_case} case."
            elif self.preffered_date != self.availabe_date:
                return f"Dr. {doctor.name} is not available on {patient.preffered_date}. would you like to schedule for a different date? available date: {', '.join(doctor.availabe_date)}"
            elif "emergence" in patient(self.medical_case).lower() != doctor(self.specialty) and doctor(self.availabe_date)==patient(self.preffered_date):
                return f"emergence appointment schedule with Dr. {doctor.name}"
            else:
                return f"Dr. {doctor.name} is not specialized in {patient.medical_case}. Please consult a different doctor."