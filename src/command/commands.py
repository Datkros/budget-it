from schematics.models import Model
from schematics.types import StringType, FloatType, DateTimeType

class CreateExpenseCommand(Model):
    name: StringType = StringType(required=True)
    value: float = FloatType(required=True)
    currency: StringType(required=True)
    description: StringType(required=True)
    expense_date: datetime = DateTimeType(required=True)   
