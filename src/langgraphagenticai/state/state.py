from typing import Annotated
from pydantic import BaseModel, Field
from typing_extensions import TypedDict, List
from langgraph.graph.message import add_messages

class GraphState(TypedDict):
    """Represents the state of the graph"""
    messages: Annotated[List, add_messages]
    