from pydantic_settings import BaseSettings,SettingsConfigDict


class Settings(BaseSettings):
    DB_URL:str 
    CONSUMER_KEY:str 
    CONSUMER_SECRET:str 
    POSTGRES_USER:str 
    POSTGRES_PASSWORD:str 
    POSTGRES_DB:str



    model_config=SettingsConfigDict(env_file='.env') 


settings=Settings()