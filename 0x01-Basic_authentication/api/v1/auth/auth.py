#!/usr/bin/env python3
"""
Authentication module
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Class to handle Authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Public method

        Return:
            bool
        """
        if path is None:
            return True

        if excluded_paths is None or excluded_paths == []:
            return True

        if path in excluded_paths:
            return False

        for excluded_path in excluded_paths:
            if excluded_path.startswith(path):
                return False
            elif path.startswith(excluded_path):
                return False
            elif excluded_path[-1] == "*":
                if path.startswith(excluded_path[:-1]):
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Public method

        Return:
            None
        """
        if request is None:
            return None
        # get header from the request
        header = request.headers.get('Authorization')

        if header is None:
            return None

        return header

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Public method

        Return:
            None
        """
        return None
