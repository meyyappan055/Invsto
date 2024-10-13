from models.data import load_data_to_db,init_db
from models.analysis import df as analysis_df , generate_signals , calculate_moving_averages
from models.testing import testing_strategy

def run():
    try:
        init_db()
        load_data_to_db('data/training_data.xlsx')
        signals = generate_signals(calculate_moving_averages())
        testing_strategy(analysis_df, 1000)
        
    except Exception as e:
        print(f"An error occurred: {e}")