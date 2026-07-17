"""Source adapter protocol implementations."""

from .ltp import LtpAdapter
from .man_pages import ManPagesAdapter

__all__ = ["LtpAdapter", "ManPagesAdapter"]
