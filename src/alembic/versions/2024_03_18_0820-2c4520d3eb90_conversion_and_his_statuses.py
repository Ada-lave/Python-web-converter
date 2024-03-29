"""Conversion and his statuses

Revision ID: 2c4520d3eb90
Revises: e1dd109ff72c
Create Date: 2024-03-18 08:20:48.035649

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2c4520d3eb90'
down_revision: Union[str, None] = 'e1dd109ff72c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('conversion_statuses',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('conversions',
    sa.Column('file_id', sa.Integer(), nullable=False),
    sa.Column('conversion_status_id', sa.Integer(), nullable=False),
    sa.Column('outfile_name', sa.String(), nullable=False),
    sa.Column('time', sa.Float(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['conversion_status_id'], ['conversion_statuses.id'], ),
    sa.ForeignKeyConstraint(['file_id'], ['files.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('conversions')
    op.drop_table('conversion_statuses')
    # ### end Alembic commands ###
