from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста

PGUSER = env.str("PGUSER")
PGPASS = env.str("PGPASS")
DATABASE = env.str("DATABASE")

POSTGRESS_URI = f"postgresql://{PGUSER}:{PGPASS}@{IP}/{DATABASE}"

banned_users = [123123312, 123123455]
channels = [-1001687582826]
allowed_users = []

# DB_USER = env.str("DB_USER")
# DB_PASS = env.str("DB_PASS")
# DB_HOST = env.str("DB_HOST")
# DB_NAME = env.str("DB_NAME")



