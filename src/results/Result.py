
from typing import Final, Generic, Literal, TypeVar, Union, overload
from typing_extensions import Never

B = TypeVar('B', bound=bool)
T = TypeVar('T')
E = TypeVar('E', bound=str)

class ResultBase(Generic[B]):
    def __init__(self, success: B) -> None:
        self.is_success: B = success
        self.is_failure: Final = not success

class Success(Generic[T], ResultBase[Literal[True]]):
    def __init__(self, value: T) -> None:
        super().__init__(success=True)
        self.value = value

class Failure(Generic[E], ResultBase[Literal[False]]):
    def __init__(self, error_code: E) -> None:
        super().__init__(success=False)
        self.error_code = error_code

Result = Union[Success[T], Failure[E]]

class ResultAssert:
    @overload
    @staticmethod
    def is_success(result: Success[T]) -> None: ...
    @overload
    @staticmethod
    def is_success(result: Failure[E]) -> Never: ...

    @staticmethod
    def is_success(result: Result[T, E]) -> Union[None, Never]:
        if result.is_success:
            return None
        assert False

    @overload
    @staticmethod
    def is_failure(result: Success[T]) -> Never: ...
    @overload
    @staticmethod
    def is_failure(result: Failure[E]) -> None: ...

    @staticmethod
    def is_falure(result: Result[T, E]) -> Union[None, Never]:
        if result.is_failure:
            return None
        assert False
