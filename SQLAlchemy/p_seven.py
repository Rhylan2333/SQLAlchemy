from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint, CheckConstraint, Index

PrimaryKeyConstraint('user_id', name='user_pk')  # 以下的“name='XX'”看起来像是备注，可不定义name这个参数

UniqueConstraint('username', name='uix_username')

CheckConstraint('unit_cost >= 0.00', name='unit_cost_positive')
"""
If we want to select by cookie SKU and name
as a joined item, such as SKU0001 Chocolate Chip
"""
Index('ix_test', <mytable>.c.cookie_sku, <mytable>.c.cookie_name)  # cookies
