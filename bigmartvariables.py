from pydantic import BaseModel

class bigmartsalespredict(BaseModel):
    Item_MRP: float
    Outlet_Type: int
    Outlet_Identifier_OUT027: float
    Outlet_Location_Type: int
    Outlet_Identifier_OUT035: float
    Outlet_age: int
    Item_Visibility: float
    Outlet_Size: int
    Outlet_Identifier_OUT010: float
    Outlet_Identifier_OUT019: float