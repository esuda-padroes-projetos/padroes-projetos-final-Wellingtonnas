from app.models.user import User

class UserFactory:
    @staticmethod
    def create(name="Usuário Teste", email="user@email.com", registration="0001"):
        return User(
            name=name,
            email=email,
            registration=registration
        )
