from ninja import Router
from .services import check_user_credentials
from .schemas import CredentialsSchema


router = Router()


@router.post("token/")
def token(request, credentials: CredentialsSchema):
    token = check_user_credentials(credentials.email, credentials.password)
    return {"token": token.key}
    