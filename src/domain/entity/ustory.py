"""
This module contains the entities for the user-stories service.

User stories service is responsible for converting the conversation stream into user stories.
"""

from pydantic import BaseModel, Field


class UserStory(BaseModel):
    conversation_id: str = Field(..., description="The id of the conversation.")
    story: str = Field(..., description="The content of the user story")
    task: str = Field(..., description="The task which was converted into a user story.")
    window_start: int = Field(..., description="The start of the window in which the user story was created.")
    window_end: int = Field(..., description="The end of the window in which the user story was created.")
