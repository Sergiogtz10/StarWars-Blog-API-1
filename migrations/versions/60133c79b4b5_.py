"""empty message

Revision ID: 60133c79b4b5
Revises: 15791a4b1d49
Create Date: 2022-02-20 12:02:17.306529

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '60133c79b4b5'
down_revision = '15791a4b1d49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=250), nullable=False),
    sa.Column('Birth', sa.String(length=120), nullable=False),
    sa.Column('Gender', sa.String(length=120), nullable=False),
    sa.Column('Heigth', sa.Integer(), nullable=True),
    sa.Column('Skin_color', sa.String(length=120), nullable=False),
    sa.Column('Eyes_color', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=250), nullable=False),
    sa.Column('Climate', sa.Integer(), nullable=True),
    sa.Column('Population', sa.Integer(), nullable=True),
    sa.Column('Orbital_period', sa.Integer(), nullable=True),
    sa.Column('Rotation_period', sa.Integer(), nullable=True),
    sa.Column('Diameter', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('userfavorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('User_id', sa.Integer(), nullable=True),
    sa.Column('Characters_id', sa.Integer(), nullable=True),
    sa.Column('Planets_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['Characters_id'], ['characters.id'], ),
    sa.ForeignKeyConstraint(['Planets_id'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['User_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('user', 'is_active')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False))
    op.drop_table('userfavorite')
    op.drop_table('planets')
    op.drop_table('characters')
    # ### end Alembic commands ###
