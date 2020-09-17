from ninja import Schema


class CredentialsSchema(Schema):
    email: str
    password: str
