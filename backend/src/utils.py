from clerk_backend_api import Clerk , AuthenticateRequestOptions
from fastapi import HTTPException
from dotenv import load_dotenv
import os


clerk_sdk = Clerk(bearer_token=os.getenv("CLERK_API_KEY"))

def authenticate_and_get_user_details(request):
    try:
        request_state = clerk_sdk.authenticate_request(
            request,
            AuthenticateRequestOptions(
                authorized_parties=[os.getenv("CLERK_FRONTEND_API")],
                jwt_key=os.getenv("JWT_KEY"),

            )
        )

        if not request_state.is_signed_in:
            raise HTTPException(status_code=401, detail="Invalid token")
        user_id = request_state.payload.get("sub")

        return {"user_id": user_id}

    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid credentials")