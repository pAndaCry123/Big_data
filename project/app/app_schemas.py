from app import  ma
from app.models import Exsam

class ExsamSchema(ma.Schema):
    class Meta:
        model = Exsam