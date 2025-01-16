from app import db
from datetime import datetime
import pytz
import re

"""
    Modelo que representa a tabela `user` no banco de dados.
"""
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    created_at = db.Column(db.DateTime,default=lambda: datetime.now(pytz.timezone("America/Sao_Paulo")))
    updated_at = db.Column(db.DateTime,onupdate=lambda: datetime.now(pytz.timezone("America/Sao_Paulo")))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S") if self.created_at else None,
            "updated_at": self.updated_at.strftime("%Y-%m-%d %H:%M:%S") if self.updated_at else None
        }
          
    @staticmethod
    def validate_user(data, is_update=False):
        """
        Função de validação do usuário. 
        """
        errors = []

        # Validar nome
        name = data.get('name')
        if not is_update and (not name or not (1 <= len(name) <= 80)):
            errors.append("Name is required and must be between 1 and 80 characters.")
        elif is_update and name is not None and not (1 <= len(name) <= 80):
            errors.append("Name must be between 1 and 80 characters if provided.")

        # Validar email
        email = data.get('email')
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not is_update and not email:
            errors.append("Email is required and must be no longer than 50 characters.")
        elif email:
            if len(email) > 50:
                errors.append("Email must be no longer than 50 characters.")
            elif not re.match(email_regex, email):
                errors.append("Invalid email format.")

        return errors


