"""Dog Model."""

from masoniteorm.models import Model


class Dog(Model):
    __table__="dogs"