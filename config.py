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
  THANOSPRO_SESSION = "BQCeB-rsjigMcY7NggO76A4Fy2PNMjkznqV0bEXOFanj6Fdsmq_PZ2hOcmt-T03GAGOnc8OiUCxNw7T3eouzGgBrXFwvPDgmswfW-yyWO3z9g8Oqrkc5veeq615EBd-Zaze-9gRZThsHNsNDS8x75P1Bdpb8LyuAe8ilmiXQWBYpcZAzHzrEr-eVtwK5wyE99Na5VPlw4mPDBsNgt0BF5zCv6Egka-azqZlbY9AdegHUEzNj2Qqs8chWb6Xn_A790xEEhylm_wmGP0YmON3nrkpK0Wa7LpuaFC39JhB0CxJg_X2ApVOwvJhSwIlLJzW0jMdvykk8FpiaL0iBgSqVdfp1AAAAAVMuvcAA"

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
