import model

COUNTER = 0
TABLE_NAME = 'bills_membership'

def genrateId():
    global COUNTER
    COUNTER+=1
    return f'BM-{COUNTER}'

def add_record(data:list):
    data.insert(0,genrateId())
    data = tuple(data)
    model.add_newExpence(TABLE_NAME,data)

def get_records():
    return model.get_records(TABLE_NAME)

def delete_expence(id):
    model.delete_record(id,TABLE_NAME)

def update_expence(id,record):
    model.update_record(TABLE_NAME,id,record)