# FILL THESE VALUES ACCORDINGLY.

from THANOSPRO.config.rishu_config import Config

class Development(Config):
  # get these values from my.telegram.org. 
  APP_ID = 6    # 6 is a placeholder. Fill your 6 digit api id
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"   # replace this with your api hash

  # create any PostgreSQL database.
  # I recommend to use elephantsql and paste that link here
  DB_URI = "Your value"
  ALIVE_NAME = "Your value"
  # After cloning the repo and installing requirements...
  # Do `python string.py` and fill the on screen prompts.
  # String session will be saved in your saved message of telegram.
  # Put that string here.
  THANOSPRO_SESSION = "Your value"

  # Create a bot in @BotFather
  # And fill the following values with bot token and username.
  BOT_TOKEN = "Your value" #token
  #FILL BOT USERNAME WITHOUT @
  BOT_USERNAME = "YOUR VALUE"
  # Custom Command Handler. 
  HANDLER = "."
  #loger I'd
  LOGGER_ID = "Your value"

  # Custom Command Handler for sudo users.
  SUDO_HANDLER = "!"


# end of required config
# THANOSPRO
