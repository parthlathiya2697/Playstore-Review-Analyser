from dotenv import load_dotenv
load_dotenv()

import os
from enum import Enum
class Creds(Enum):
    
    def __str__(self):
        return str(self.value)

    OPENAI_API_KEY= os.environ['OPENAI_API_KEY']
    APP_TOKEN= os.environ['APP_TOKEN']