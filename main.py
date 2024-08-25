from fastapi import FastAPI

from routers.analysis import router as analysisRouter
from routers.paraphrase_emogy import router as paraphraseEmojifyRouter
from routers.review import router as reviewRouter


# Creating the FastAPI instance
app = FastAPI()


# Defining the root route
@app.get("/")
async def root():
    return {"message": "The server is Running"}


# Including the routers
app.include_router(reviewRouter)
app.include_router(analysisRouter)
app.include_router(paraphraseEmojifyRouter)




# Running the server (or through command)
if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", reload= True)
    