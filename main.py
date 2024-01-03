from modules.adversarial_attacks import simulate_attack
from modules.defence_strategies import develop_defense_strategy
from modules.monitoring import monitor
import os
import logging
import utils.config as cf
import datetime as dt


#Setup Directory
curr_dirr = os.getcwd()
dirs_to_make = ['logs/', 'results/']
for dir in dirs_to_make:
    if not os.path.exists(os.path.join(curr_dirr, dir)):
        os.makedirs(os.path.join(curr_dirr, dir))

#Logging setup
START_TIME = dt.datetime.strftime(dt.datetime.utcnow(), '%Y-%m-%d--%H-%M-%S').replace('-','_')
logfile='logs/robust_ai_%s.log' % START_TIME
fh = logging.FileHandler(logfile)
logger = logging.getLogger('main')
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)
logger.addHandler(ch)
logger.addHandler(fh)
logger.setLevel(logging.INFO)

logger.info('Started Logging')
logger.info('robust ai experiment: Starting...')


def main():
    # Example of how to use the modules
    simulate_attack()
    develop_defense_strategy()
    monitor()

if __name__ == "__main__":
    main()