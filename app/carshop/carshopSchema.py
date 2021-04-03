from app.carshop.carshopModel import CarshopModel
from app import ma

class CarshopSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CarshopModel
        load_instance = True
