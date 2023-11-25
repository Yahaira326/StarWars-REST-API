"""empty message

Revision ID: a74fb9990697
Revises: b5139c74fc98
Create Date: 2023-01-26 18:30:27.075334

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a74fb9990697'
down_revision = 'b5139c74fc98'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('url', sa.String(length=250), nullable=False),
    sa.Column('diameter', sa.String(length=250), nullable=False),
    sa.Column('population', sa.String(length=250), nullable=False),
    sa.Column('climate', sa.String(length=250), nullable=False),
    sa.Column('terrain', sa.String(length=250), nullable=False),
    sa.Column('surfaceWater', sa.String(length=250), nullable=False),
    sa.Column('rotationPeriod', sa.String(length=250), nullable=False),
    sa.Column('orbitalPeriod', sa.String(length=250), nullable=False),
    sa.Column('gravity', sa.String(length=250), nullable=False),
    sa.Column('films', sa.String(length=250), nullable=False),
    sa.Column('created', sa.String(length=250), nullable=False),
    sa.Column('edited', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planets')
    # ### end Alembic commands ###
