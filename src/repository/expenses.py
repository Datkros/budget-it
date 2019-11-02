from dataclasses import dataclass, field, asdict
from datetime import datetime
from entity.entities import expense_tbl
from common.utils import unique_id_creator


@dataclass
class Expense:
    expense_id: str = field(init=False, default_factory=unique_id_creator)
    name: str
    value: str
    currency: str
    description: str
    expense_date: datetime
    created_date: datetime = field(init=False, default_factory=datetime.utcnow())

class ExpensesRepository:

    def __init__(self, database):
        self.database = database

    async def create_expense(self, expense: Expense):
        async with self.database.engine.acquire() as conn:
            try:
                sql = expenses_tbl.insert().values(**asdict(expense))
                await conn.execute(sql)
            except Exception as e:
                print(e)
                raise
