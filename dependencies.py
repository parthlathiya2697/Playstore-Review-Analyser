from fastapi import Header, HTTPException
from utils.private import Creds 

async def get_token_header(x_token: str = Header()):
    if x_token.strip() != Creds.APP_TOKEN.value:
        raise HTTPException(status_code=400, detail="X-Token header invalid")