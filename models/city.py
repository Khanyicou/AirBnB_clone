#!/usr/bin/python3
"""Modules that define the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Impliments the city class.

    Attributes:
        state_id (str): The state id.
        name (str): The city name.
    """

    state_id = ""
    name = ""
