# from fastapi_users.authentication import JWTAuthentication
# from fastapi_users.db import SQLAlchemyUserDatabase
# from core.db import database
# from .models import User
# from .schemas import UserDB


# users = User.__table__
# user_db = SQLAlchemyUserDatabase(UserDB, database, users)

# SECRET = "283rnjr9wekfkoaeief8efmsd9p8fsddjif9dofnkdsfwejfke"

# auth_backends = [
#     JWTAuthentication(secret=SECRET, lifetime_seconds=3600),
# ]