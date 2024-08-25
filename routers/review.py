from fastapi import APIRouter, Depends

# custom
from dependencies import get_token_header
from utils.scrap import get_reviews, get_all_content


# Creating the router instance
router = APIRouter(dependencies= [
                                    Depends(get_token_header)
                                 ],
                    tags= ["Google Play Reviews"]
                   )


# Defining the routes
@router.get("/reviews")
async def reviews_(package_name: str):
    return get_reviews(package_name)


@router.get("/all_review_content")
async def all_content_(package_name: str, limit: int = 100, filter_score: int = 5, country: str = 'us', language: str = 'en'):
    return  get_all_content( get_reviews(package_name, limit, filter_score, country, language) )

