from pydantic import Field
from pydantic_settings import BaseSettings

class MongoSettings(BaseSettings):
    MONGO_PORT: str = Field(description="the mongo database port", env="MONGO_PORT", default="27017")
    MONGO_HOST: str = Field(description="the mongo database host", env="MONGO_HOST", default="mongodb")
    MONGO_USER: str = Field(description="mongo user name", env="MONGO_USER", default="root")
    MONGO_PASSWD: str = Field(description="mongo password", env="MONGO_PASSWD", default="pass12345")
    MONGO_COLLECTION: str = Field(description="mongo collection", env="MONGO_COLLECTION", default="cora_products")
    MONGO_DATABASE: str = Field(description="mongo data base name", env="MONGO_COLLECTION", default="cora")


MongoSettings = MongoSettings()