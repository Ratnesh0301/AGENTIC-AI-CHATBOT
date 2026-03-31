from typing import Annotated, List
from pydantic import BaseModel, Field
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages

class GraphState(TypedDict):
    """Represents the state of the graph"""
    messages: Annotated[List, add_messages]
    