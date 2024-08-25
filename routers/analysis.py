from fastapi import APIRouter, Depends
from utils.open_ai import points_of_improvements

# custom
from dependencies import get_token_header
from utils.scrap import get_reviews, get_all_content


# Creating the router instance
router = APIRouter(dependencies= [
                                    Depends(get_token_header)
                                 ],
                    tags= ["Review Analysis"]
                   )


# Defining the routes
@router.get("/points_of_improvement")
async def points_of_improvement(package_name: str, country: str= 'us', language: str = 'en'):
    
    text = get_all_content( get_reviews(package_name, country= country, language= language) )
    return points_of_improvements(text)