"""
This module contains the mongo client wrapper.
"""

from motor.motor_asyncio import AsyncIOMotorClient

from beanie import init_beanie
from infrastructure.storage.mongo.config import MongoConfig


class MongoClient:
    """
    This class is the mongo client wrapper.
    """

    def __init__(self, config: MongoConfig):
        """
        This method initializes the mongo client wrapper.

        :param config: The configuration of the mongo client.
        """

        self._config = config
        self._client = AsyncIOMotorClient(
            host=self._config.host,
            port=self._config.port,
            username=self._config.username,
            password=self._config.password,
            authSource=self._config.auth_source,
            authMechanism=self._config.auth_mechanism,
            maxPoolSize=self._config.max_pool_size,
            minPoolSize=self._config.min_pool_size,
            maxIdleTimeMS=self._config.max_idle_time,
            maxLifeTimeMS=self._config.max_life_time,
            connect=True,
        )

    @property
    def client(self) -> AsyncIOMotorClient:
        """
        This method returns the client of the mongo client.

        :return: The client of the mongo client.
        """

        return self._client

    async def close(self) -> None:
        """
        This method closes the mongo client.
        """

        self._client.close()

    async def initialize(self, models_paths: list[str]) -> None:
        """
        This method initializes the mongo client.

        :param models_paths: The list of models/documents paths to initialize.
        """

        await init_beanie(
            database=self._client.db_name,
            document_models=models_paths,
        )
