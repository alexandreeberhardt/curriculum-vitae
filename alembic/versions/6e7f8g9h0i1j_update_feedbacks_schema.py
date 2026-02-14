"""Update feedbacks table schema with new fields

Revision ID: 6e7f8g9h0i1j
Revises: 5d6e7f8g9h0i
Create Date: 2026-02-14 11:00:00.000000

"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "6e7f8g9h0i1j"
down_revision: str | Sequence[str] | None = "5d6e7f8g9h0i"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Replace old feedback columns with new survey fields."""
    # Remove old columns
    op.drop_column("feedbacks", "rating")
    op.drop_column("feedbacks", "liked")
    op.drop_column("feedbacks", "improvement")

    # Add new columns
    op.add_column("feedbacks", sa.Column("profile", sa.String(100), nullable=True))
    op.add_column("feedbacks", sa.Column("target_sector", sa.String(255), nullable=True))
    op.add_column("feedbacks", sa.Column("ease_rating", sa.Integer(), nullable=False, server_default=sa.text("5")))
    op.add_column("feedbacks", sa.Column("time_spent", sa.String(50), nullable=True))
    op.add_column("feedbacks", sa.Column("obstacles", sa.Text(), nullable=True))
    op.add_column("feedbacks", sa.Column("alternative", sa.String(255), nullable=True))
    op.add_column("feedbacks", sa.Column("suggestions", sa.Text(), nullable=True))
    op.add_column("feedbacks", sa.Column("nps", sa.Integer(), nullable=True))
    op.add_column("feedbacks", sa.Column("future_help", sa.Text(), nullable=True))


def downgrade() -> None:
    """Restore old feedback columns."""
    op.drop_column("feedbacks", "future_help")
    op.drop_column("feedbacks", "nps")
    op.drop_column("feedbacks", "suggestions")
    op.drop_column("feedbacks", "alternative")
    op.drop_column("feedbacks", "obstacles")
    op.drop_column("feedbacks", "time_spent")
    op.drop_column("feedbacks", "ease_rating")
    op.drop_column("feedbacks", "target_sector")
    op.drop_column("feedbacks", "profile")

    op.add_column("feedbacks", sa.Column("rating", sa.Integer(), nullable=False, server_default=sa.text("3")))
    op.add_column("feedbacks", sa.Column("liked", sa.Text(), nullable=True))
    op.add_column("feedbacks", sa.Column("improvement", sa.Text(), nullable=True))
