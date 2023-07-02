"""
This module contains the entities for the conversation service.
"""


from pydantic import BaseModel, Field


class ConversationStream(BaseModel):
    """
    This class represents a conversation stream.
    """

    conversation_id: str = Field(..., description="The id of the conversation stream.")
    chunk: str = Field(..., description="The text/chunk of the conversation stream.")
    timestamp: int = Field(..., description="The timestamp of the conversation stream.")
    organization_id: str = Field(..., description="The organization id of the conversation stream.")
    project_id: str = Field(..., description="The project id of the conversation stream.")
