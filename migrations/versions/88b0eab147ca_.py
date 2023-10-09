"""empty message

Revision ID: 88b0eab147ca
Revises: c8ff054cb4f0
Create Date: 2023-10-09 23:38:33.799246

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88b0eab147ca'
down_revision = 'c8ff054cb4f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('gender', sa.String(length=80), nullable=False),
    sa.Column('eyes_color', sa.String(length=80), nullable=False),
    sa.Column('height', sa.String(length=80), nullable=False),
    sa.Column('hair_color', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('diametro', sa.String(length=80), nullable=False),
    sa.Column('gravedad', sa.String(length=80), nullable=False),
    sa.Column('poblacion', sa.String(length=80), nullable=False),
    sa.Column('rotacion', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('characters_id', sa.Integer(), nullable=True),
    sa.Column('planets_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['characters_id'], ['characters.id'], ),
    sa.ForeignKeyConstraint(['planets_id'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorites')
    op.drop_table('planets')
    op.drop_table('characters')
    # ### end Alembic commands ###
