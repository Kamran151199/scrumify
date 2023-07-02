"""
This module contains the entities for the jira service.
"""
from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class JiraCredentials(BaseModel):
    email: str = Field(..., description="The email of the jira user.")
    token: str = Field(..., description="The token of the jira user.")
    server: str = Field(..., description="The server of the jira account.")


class JiraIssue(BaseModel):
    summary: str = Field(..., description="The summary of the Jira issue.")
    description: str = Field(..., description="The description of the Jira issue.")
    project: str = Field(..., description="The key of the Jira project the issue belongs to.")
    issue_type: str = Field(None, description="The type of the Jira issue.")
    assignee: str = Field(None, description="The assignee of the Jira issue.")
    reporter: str = Field(None, description="The reporter of the Jira issue.")
    priority: str = Field(None, description="The priority of the Jira issue.")
    labels: List[str] = Field([], description="The labels associated with the Jira issue.")
    components: List[str] = Field([], description="The components associated with the Jira issue.")
    due_date: Optional[date] = Field(None, description="The due date of the Jira issue.")
    created: datetime = Field(None, description="The creation date of the Jira issue.")
    updated: datetime = Field(None, description="The last update date of the Jira issue.")
    status: str = Field(None, description="The status of the Jira issue.")
