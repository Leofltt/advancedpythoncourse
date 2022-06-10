from typing import Tuple
from pydantic import BaseModel, validator
from errors import CurrencyError

SUPPORTED_CURRENCIES = ["dollar","euro"]

class Product(BaseModel):
    """A class representing a product"""

    name: str 
    price: float
    currency: str = "dollar"

    @validator("currency")
    def validate_currency(cls, v: str, values: dict) -> str:
        """Validates that the currency is supported"""
        if v not in SUPPORTED_CURRENCIES:
            raise CurrencyError(f"{v} is not a supported currency")
        return v
    
    def to_tuple(self) -> Tuple[str, float, str]:
        """Returns a tuple of the product's attributes"""
        return (self.name, self.price, self.currency)