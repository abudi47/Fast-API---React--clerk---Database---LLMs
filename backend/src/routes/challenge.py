from fastapi import APIRouter, Depends, Request, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session


from ..database.db import (
    get_challenge_quota,
    create_challenge_quota,
    reset_quotas_if_needed,
    get_user_challenges,
    create_challenge,
) 

from ..utils import authenticate_and_get_user_details
from ..database.models import get_db


import json 
from datetime import datetime


router = APIRouter() 


class ChallengeRequest(BaseModel):
    difficulty :str

    class Config:
        json_schema_extra = {"example": {"difficulty": "easy"}}

@router.post("/generate-challenge")
async def generate_challenge(request: Request, challenge_request: ChallengeRequest, db: Session = Depends(get_db)):

    try: 
        user_details = authenticate_and_get_user_details(request)
        user_id = user_details.get("user_id")

        if not user_id:
            raise HTTPException(status_code=401, detail="Unauthorized")

        quota = get_challenge_quota(db, user_id)
        if not quota:
            create_challenge_quota(db, user_id)

        quota = reset_quotas_if_needed(db, quota)

        if quota.remaining_quota <= 0:
            raise HTTPException(status_code=403, detail="Challenge quota exceeded. Please try again later.")

        challenge_data = None



        # Decrement the quota
        quota.remaining_quota -= 1
        db.commit()
        # db.refresh(quota)

        return {"challenge": challenge_data, "quota_remaining": quota.quota_remaining}
    
    
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/my-history")
async def my_history(request :Request ,db: Session = Depends(get_db)):
    user_details = authenticate_and_get_user_details(request)
    user_id = user_details.get("user_id")

    if not user_id:
        raise HTTPException(status_code=401, detail="Unauthorized")
    challenges = get_user_challenges(db, user_id)

    return {"challenges": challenges}

@router.get("/quota")
async def get_quota(request: Request, db: Session = Depends(get_db)):
    user_details = authenticate_and_get_user_details(request)
    user_id = user_details.get("user_id")

    if not user_id:
        raise HTTPException(status_code=401, detail="Unauthorized")


    quota = get_challenge_quota(db, user_id)
    if not quota:
        return {
           "user_id": user_id,
           "quota_remaining": 0,
           "last_reset_date": datetime.now()

        }
    quota =     reset_quotas_if_needed(db, quota)
    return quota

