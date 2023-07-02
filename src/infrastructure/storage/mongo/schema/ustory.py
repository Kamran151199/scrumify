"""
This module contains the beanie ODM models for the mongo database.
"""

from beanie import Document

from domain.entity.ustory import UserStory


class UserStoryMongo(UserStory, Document):
    """
    This class is the beanie ODM model for the user story entity.
    """

    class Settings:
        name = "user_story"
