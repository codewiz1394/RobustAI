import os
import json

def initialize_configuration(conf_path):
    """
    Reads a config json file and makes global variables out of the settings.
    :param conf_path:
    :return:
    """

    config_file_path = os.path.join(os.getcwd(), conf_path)
    with open(config_file_path) as file:
        cf = json.load(file)      
    #Set global variable
    globals().update(cf)
    
    return

initialize_configuration("config/config.json")
