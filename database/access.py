
from config import Config
from database.database import Database

botly = Database(Config.DATABASE_URL, Config.SESSION_NAME)
