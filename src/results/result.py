import traceback
from typing import Callable, Generic, List, Literal, Optional, TypeVar, Union

B = TypeVar('B', bound=bool)
C = TypeVar('C', bound=bool)
T = TypeVar('T')
U = TypeVar('U')
E = TypeVar('E', bound=str)

class ResultBase(Generic[B, C]):
    '''
    A base class that make a typesafe difference between is_success and is_failure
    functions that can be called on Result can be placed in this base class
    '''
    def __init__(self, success: B, failure: C) -> None:
        self.is_success: B = success
        self.is_failure: C = failure

class Success(Generic[T, E], ResultBase[Literal[True], Literal[False]]):
    '''
    Representation of the success variant of result.
    '''
    def __init__(self, value: T) -> None:
        super().__init__(success=True, failure=False)
        self.value: T = value

    def map(self, callback: Callable[[T], U]) -> 'Success[U, E]':
        return Success(callback(self.value))

class Failure(Generic[T, E], ResultBase[Literal[False], Literal[True]]):
    '''
    Representation of the failure variant of result.
    '''
    def __init__(self, error_code: E, message: str, stack: Optional[List[str]] = None) -> None:
        super().__init__(success=False, failure=True)
        self.error_code = error_code
        self.message = message
        self.stack = stack if stack is not None else traceback.format_list(traceback.extract_stack())

    def map(self, _callback: Callable[[T], U]) -> 'Failure[U, E]':
        return Failure(error_code=self.error_code, message=self.message, stack=self.stack)

Result = Union[Success[T, E], Failure[T, E]]
