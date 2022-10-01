'''
This module is not working yet, mypy is not working with this yet.
There are open tickets with python for this: https://github.com/python/typing/issues/930
'''
from typing import NoReturn, TypeVar, Union, overload

from src.results.Result import Failure, Result, Success

T = TypeVar('T')
E = TypeVar('E', bound=str)

class ResultAssert:
    @overload
    @staticmethod
    def is_success(result: Success[T, E]) -> None: ...
    @overload
    @staticmethod
    def is_success(result: Failure[T, E]) -> NoReturn: ...

    @staticmethod
    def is_success(result: Result[T, E]) -> Union[None, NoReturn]:
        if result.is_success:
            return None
        assert False

    @overload
    @staticmethod
    def is_failure(result: Success[T, E]) -> NoReturn: ...
    @overload
    @staticmethod
    def is_failure(result: Failure[T, E]) -> None: ...

    @staticmethod
    def is_failure(result: Result[T, E]) -> Union[None, NoReturn]:
        if result.is_failure:
            return None
        assert False