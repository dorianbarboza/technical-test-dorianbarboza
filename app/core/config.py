import os
from dotenv import load_dotenv

load_dotenv()



SECRET_KEY = os.getenv("SECRET_KEY", None)

ALGORITHM = os.getenv("ALGORITHM", None)

ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", None))

POSTGRESQL_DATABASE_URI = os.getenv("POSTGRESQL_DATABASE_URI", None)

POSTGRESQL_DATABASE_NAME = os.getenv("POSTGRESQL_DATABASE_NAME", None)

AWS_REGION = os.getenv("AWS_REGION", "us-east-2")

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", "AKIARO3HCVLDIVH5TWUA")

AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", "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")

# EMAIL
EMAIL_ADMIN = os.getenv("EMAIL_ADMIN", "dorianbarbozazebrands@gmail.com").split(",")

EMAIL_ADMIN_PWD = os.getenv("EMAIL_ADMIN_PWD", None)

EMAIL_SENDER = os.getenv("EMAIL_SENDER", "dorianbarboza@gmail.com")



