from typing import List,Optional
from pydantic_settings import BaseSettings
from pydantic import field_validator

# setting the deafult settings of the env variable
class Settings(BaseSettings):
    API_PREFIX: str = "/api"
    DEBUG:bool =False
    DATABASE_URL: str
    ALLOWED_ORIGINS: str = "https://your-frontend.onrender.com"
    GOOGLE_API_KEY: Optional[str] = None

# takes the allowed_origins in field_validator and converts the string (comman separated) into list else returns empty list
    @field_validator("ALLOWED_ORIGINS")
    def parse_allowed_origins(cls,v:str) ->List[str]:
        return v.split(",") if v else []
# settings so that python knows how to load our file 
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive =True

settings = Settings() # Automatically load our env variable file 
    