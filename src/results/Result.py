
from abc import abstractmethod
import traceback
from typing import Callable, Generic, List, Literal, TypeVar, Union, overload

B = TypeVar('B', bound=bool)
C = TypeVar('C', bound=bool)
T = TypeVar('T')
T2 = TypeVar('T2')
E = TypeVar('E', bound=str)
E2 = TypeVar('E2', bound=str)

class ResultBase(Generic[B, C]):
    def __init__(self, success: B, failure: C) -> None:
        self.is_success: B = success
        self.is_failure: C = failure

class Success(Generic[T, E], ResultBase[Literal[True], Literal[False]]):
    def __init__(self, value: T) -> None:
        super().__init__(success=True, failure=False)
        self.value: T = value

    def map(self, callback: Callable[[T], T2]) -> 'Success[T2, E]':
        return Success(callback(self.value))

class Failure(Generic[T, E], ResultBase[Literal[False], Literal[True]]):
    def __init__(self, error_code: E, message: str, stack: List[str] = traceback.format_list(traceback.extract_stack())) -> None:
        super().__init__(success=False, failure=True)
        self.error_code = error_code
        self.message = message
        self.stack = stack

    def map(self, callback: Callable[[T], T2]) -> 'Failure[T2, E]':
        return Failure(error_code=self.error_code, message=self.message, stack=self.stack)

Result = Union[Success[T, E], Failure[T, E]]


