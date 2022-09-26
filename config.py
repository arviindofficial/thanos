# FILL THESE VALUES ACCORDINGLY.

from THANOSPRO.config.rishu_config import Config

class Development(Config):
  # get these values from my.telegram.org. 
  APP_ID = 16358545    # 6 is a placeholder. Fill your 6 digit api id
  API_HASH = "fe7833907fec3cba426017706e2551e9"   # replace this with your api hash

  # create any PostgreSQL database.
  # I recommend to use elephantsql and paste that link here
  DB_URI = "postgres://ebnnwvck:NVdxRdRK5BtwdyeEmEmlBj4937L8OlCu@jelani.db.elephantsql.com/ebnnwvck"
  ALIVE_NAME = "Suryansh"
  # After cloning the repo and installing requirements...
  # Do `python string.py` and fill the on screen prompts.
  # String session will be saved in your saved message of telegram.
  # Put that string here.
  THANOSPRO_SESSION = "1BVtsOH4Bu5HMc9t4O60Sz81o87VU2_aFtdDYbbO4AUMUCe_dIdMN-LrxGIfWZZ19Mdf95mcT6JAwajbgLu7TTFjjTMX3cfP7bIP155dO1d4tGzqnG-drzElmHbHIGbPWH9yBqxw1m7h3RD2XjQ9trNnCNpQ5iHzxxwI2OD0QfvsMcCzteiEzGNcVan2VG15j46mxVa0ye8eh35p2umXAGisC99J3JLUYxPdMQVNDVTvIohbfA7LbmoaBE4BLWLcdTcFIxjbWPwt8iHZNsLM6KeCqRxBjvJugrVCbCEzg8zjo4xk8BWVF6gUfZMX3QkPIw_KrXHMsvKDeGQlciq5VuCAVMh-cSjQ="

  # Create a bot in @BotFather
  # And fill the following values with bot token and username.
  BOT_TOKEN = "5672371530:AAE2OzQFvwf5DjWJDP7tMuuYhI2DLU11AQ0" #token
  #FILL BOT USERNAME WITHOUT @
  BOT_USERNAME = "CHEAPEST_INDIAN_SMM_BOT"
  # Custom Command Handler. 
  HANDLER = "."
 

  # Custom Command Handler for sudo users.
  SUDO_HANDLER = "!"


# end of required config
# THANOSPRO
