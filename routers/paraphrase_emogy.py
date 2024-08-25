from fastapi import APIRouter, Depends
from utils.open_ai import paraphrase, emojify

# custom
from dependencies import get_token_header


# Creating the router instance
router = APIRouter(dependencies= [
                                    Depends(get_token_header)
                                 ],
                    tags= ["AI Services"]
                   )


# Defining the routes
@router.get("/paraphrase")
async def paraphrase_(text: str):
    return paraphrase(text)


@router.get("/emojify")
async def emojify_(text: str):
    return emojify(text)


@router.get("/paraphrase_and_emojify")
async def paraphrase_emojify_(text: str):
    text_ret = emojify( paraphrase( text) )
    return {"data" : text_ret}
