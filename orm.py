from sqlalchemy.orm import mapper, relationship
from sqlalchemy import Column, Table, MetaData, Integer, String
from model import OrderLine  # from model.py

metadata = MetaData()

order_lines_table = Table(
    "order_lines",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("sku", String(255)),
    Column("qty", Integer, nullable=False),
    Column("orderid", String(255)),
)


# batch = Table(
# 	"batch",
# 	metadata,
# 	Column("reference", String(255), primary_key=True),
# 	Column("sku", String(255)),
# Column("eta", ), # time type?
# )


def start_mappers():
    order_lines_mapper = mapper(OrderLine, order_lines_table)
