"""change name of tables in app.table.table

Revision ID: 45da64995444
Revises: b969a8838c1c
Create Date: 2021-04-01 11:01:47.830980

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45da64995444'
down_revision = 'b969a8838c1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('course_room',
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['course.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], )
    )
    op.create_table('pstudent_course',
    sa.Column('pstudent_id', sa.Integer(), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['course.id'], ),
    sa.ForeignKeyConstraint(['pstudent_id'], ['pstudent.id'], )
    )
    op.drop_table('pstudentcourse')
    op.drop_table('courseroom')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('courseroom',
    sa.Column('student_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('course_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['course.id'], name='courseroom_course_id_fkey'),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], name='courseroom_student_id_fkey')
    )
    op.create_table('pstudentcourse',
    sa.Column('pstudent_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('course_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['course.id'], name='pstudentcourse_course_id_fkey'),
    sa.ForeignKeyConstraint(['pstudent_id'], ['pstudent.id'], name='pstudentcourse_pstudent_id_fkey')
    )
    op.drop_table('pstudent_course')
    op.drop_table('course_room')
    # ### end Alembic commands ###
