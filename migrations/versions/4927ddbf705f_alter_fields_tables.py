"""alter_fields_tables

Revision ID: 4927ddbf705f
Revises: 80398e15b543
Create Date: 2023-04-18 14:58:40.926862

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4927ddbf705f'
down_revision = '80398e15b543'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('category', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=mysql.VARCHAR(length=80),
               nullable=False)

    with op.batch_alter_table('provider', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=mysql.VARCHAR(length=80),
               nullable=False)
        batch_op.alter_column('corporate_name',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('email',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('password',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
        batch_op.alter_column('email',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('name',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)

    with op.batch_alter_table('provider', schema=None) as batch_op:
        batch_op.alter_column('corporate_name',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
        batch_op.alter_column('name',
               existing_type=mysql.VARCHAR(length=80),
               nullable=True)

    with op.batch_alter_table('category', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=mysql.VARCHAR(length=80),
               nullable=True)

    # ### end Alembic commands ###