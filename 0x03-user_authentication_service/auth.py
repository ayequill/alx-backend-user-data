#!/usr/bin/env python3
""" Module for Auth class """
from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> bytes:
    """ Hash a password """
    return hashpw(password.encode('utf-8'), gensalt())
