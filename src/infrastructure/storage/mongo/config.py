"""
This module contains the configurations for the mongo client.
"""

import dotenv
from pydantic import BaseSettings, Field
from pydantic.class_validators import validator


class MongoConfig(BaseSettings):
    """
    This class contains the configurations for the mongo client.
    """

    host: str = Field(..., description="The host of the mongo client.")
    port: int = Field(..., description="The port of the mongo client.")
    username: str = Field(..., description="The username of the mongo client.")
    password: str = Field(..., description="The password of the mongo client.")
    database: str = Field(..., description="The database of the mongo client.")
    auth_source: str = Field(..., description="The auth source of the mongo client.")
    auth_mechanism: str = Field("SCRAM-SHA-256", description="The auth mechanism of the mongo client.")
    max_pool_size: int = Field(100, description="The max pool size of the mongo client.")
    min_pool_size: int = Field(10, description="The min pool size of the mongo client.")
    max_idle_time: int = Field(10000, description="The max idle time of the mongo client.")
    max_life_time: int = Field(10000, description="The max life time of the mongo client.")

    @validator("auth_source", pre=True)
    def validate_auth_source(cls, value):
        """
        This method validates the auth source of the mongo client.
        """

        if value is None:
            return cls.database
        return value

    class Config:
        env_file = dotenv.find_dotenv()
        env_prefix = "MONGO_"
