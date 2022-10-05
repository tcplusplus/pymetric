'''
This module is not working yet, mypy is not working with this yet.
There are open tickets with python for this: https://github.com/python/typing/issues/930
'''
from typing import NoReturn, TypeVar, Union, overload

from src.results.result import Failure, Result, Success

T = TypeVar('T')
E = TypeVar('E', bound=str)

class ResultAssert:
    '''
    Goal is to use this in tests to write only once that a result is of a certain type. MyPy does not work with this yet
    current example:
      assert res.is_success
      if res.is_success:
        assert res.value == 'something'
    wanted to go to
      ResultAssert.is_success(res)
      assert res.value == 'something'
    '''
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
