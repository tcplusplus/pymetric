
from typing import Generic, Literal, TypeVar, Union, overload

B = TypeVar('B', bound=bool)
C = TypeVar('C', bound=bool)
T = TypeVar('T')
E = TypeVar('E', bound=str)

class ResultBase(Generic[B, C]):
    def __init__(self, success: B, failure: C) -> None:
        self.is_success: B = success
        self.is_failure: C = failure

class Success(Generic[T], ResultBase[Literal[True], Literal[False]]):
    def __init__(self, value: T) -> None:
        super().__init__(success=True, failure=False)
        self.value: T = value

class Failure(Generic[E], ResultBase[Literal[False], Literal[True]]):
    def __init__(self, error_code: E) -> None:
        super().__init__(success=False, failure=True)
        self.error_code = error_code

Result = Union[Success[T], Failure[E]]


