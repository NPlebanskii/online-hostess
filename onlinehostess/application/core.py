from typing import List
from application.models import User, Table, Establishment


def get_user(**kwargs) -> User:
    """Find user accoring to provided criterias in DB.
    Args:
        kwargs - criterias for user to search in DB.
    Returns:
        Found user or None if user was not found.
    """
    return User.query.filter_by(**kwargs).first()


def get_establishment(**kwargs) -> Establishment:
    """Find establishment accoring to provided criterias in DB.
    Args:
        kwargs - criterias for establishment to search in DB.
    Returns:
        Found establishment or None if establishment was not found.
    """
    return Establishment.query.filter_by(**kwargs).first()


def get_establishments() -> List[Establishment]:
    """Find all establishments in DB.
    Returns:
        List of found establishments.
    """
    return Establishment.get_all()


def get_table(**kwargs) -> Table:
    """Find table accoring to provided criterias in DB.
    Args:
        kwargs - criterias for table to search in DB.
    Returns:
        Found table or None if table was not found.
    """
    return Table.query.filter_by(**kwargs).first()
