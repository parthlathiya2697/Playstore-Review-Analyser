from pprint import pprint
from typing import List
from google_play_scraper import Sort, reviews

def get_all_content(review_data: List[dict]):
    return '. '.join( [ data['content'] for data in review_data ] )

def get_reviews(package_name: str, limit: int = 100, filter_score: int = 5, country: str = 'us', language: str = 'en'):
    result, continuation_token = reviews(
    package_name,
    lang= language, # defaults to 'en'
    country=country, # defaults to 'us'
    sort=Sort.NEWEST, # defaults to Sort.NEWEST
    count= limit, # defaults to 100
    filter_score_with=filter_score # defaults to None(means all score)
)
    # If you pass `continuation_token` as an argument to the reviews function at this point,
    # it will crawl the items after 3 review items.

    result, _ = reviews(
        package_name,
        continuation_token=continuation_token # defaults to None(load from the beginning)
    )
    
    return result

if __name__ == '__main__':
    
    data = get_reviews(package_name= 'com.nianticlabs.pokemongo')
    # pprint(data)
    all_content = get_all_content(review_data= data)
    print(all_content)