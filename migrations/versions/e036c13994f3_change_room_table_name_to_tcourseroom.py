"""change room table name to Tcourseroom

Revision ID: e036c13994f3
Revises: 1d1c0be07b0c
Create Date: 2021-04-01 10:55:11.053295

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e036c13994f3'
down_revision = '1d1c0be07b0c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Tcourseroom',
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['course.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], )
    )
    op.create_table('Tpstudentcourse',
    sa.Column('pstudent_id', sa.Integer(), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['course.id'], ),
    sa.ForeignKeyConstraint(['pstudent_id'], ['pstudent.id'], )
    )
    op.drop_table('room')
    op.drop_table('pstudentcourse')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pstudentcourse',
    sa.Column('pstudent_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('course_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['course.id'], name='pstudentcourse_course_id_fkey'),
    sa.ForeignKeyConstraint(['pstudent_id'], ['pstudent.id'], name='pstudentcourse_pstudent_id_fkey')
    )
    op.create_table('room',
    sa.Column('student_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('course_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['course.id'], name='room_course_id_fkey'),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], name='room_student_id_fkey')
    )
    op.drop_table('Tpstudentcourse')
    op.drop_table('Tcourseroom')
    # ### end Alembic commands ###