from controllers import data_controller
from views.visualize import plot_data
from models.analysis import df as analysis_df


if __name__ == '__main__':
    data_controller.run()
    plot_data(analysis_df)