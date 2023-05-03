from .models import employees


def checkRegistration(emp_email):
    data= employees.objects.all()

    for i in data:
        if i.email== emp_email:
            return True
    else:
        return False


