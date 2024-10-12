from models.data import load_data_to_db,init_db

def run():
    init_db()
    load_data_to_db('data/training_data.xlsx')
    