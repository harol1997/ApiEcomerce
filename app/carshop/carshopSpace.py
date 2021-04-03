from app.carshop.carshopResource import CarshopResource

from app import api

shopcart_namespace = api.namespace(
                                    'CARSHOP',
                                    description="API TO CARSHOP"
                                )

shopcart_namespace.add_resource(CarshopResource,'/add2car')

api.add_namespace(shopcart_namespace)