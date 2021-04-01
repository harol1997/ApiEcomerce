"""update student table name

Revision ID: 78d7fa1329f4
Revises: e612aada1daf
Create Date: 2021-04-01 09:16:17.029392

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78d7fa1329f4'
down_revision = 'e612aada1daf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('email', sa.Text(), nullable=False),
    sa.Column('password', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_student_email'), 'student', ['email'], unique=True)
    op.create_index(op.f('ix_student_id'), 'student', ['id'], unique=True)
    op.drop_index('ix_user_email', table_name='user')
    op.drop_index('ix_user_id', table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('email', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('password', sa.TEXT(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='user_pkey')
    )
    op.create_index('ix_user_id', 'user', ['id'], unique=True)
    op.create_index('ix_user_email', 'user', ['email'], unique=True)
    op.drop_index(op.f('ix_student_id'), table_name='student')
    op.drop_index(op.f('ix_student_email'), table_name='student')
    op.drop_table('student')
    # ### end Alembic commands ###