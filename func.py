from datetime import datetime

def today():
    today = datetime.now()
    return today

def verify_date(date):
    for fmt in ("%d-%m-%Y", "%d/%m/%Y"):
        try:
            return datetime.strptime(date, fmt)
        except ValueError:
            continue
    raise ValueError("Formato de data inválido. Use DD-MM-AAAA ou DD/MM/AAAA.")

def verify_due(date_ref):
    due_date = verify_date(date_ref)
    return today() > due_date