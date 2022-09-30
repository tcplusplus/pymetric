
from typing import Literal
from .Result import Failure, Result, ResultAssert, Success

def double_if_pos (value: int) -> Result[int, Literal['negative']]:
    if value >= 0:
        return Success(value * 2)
    return Failure('negative')

class TestResult:
    def test_result_success(self) -> None:
        ret = double_if_pos(value=4)
        try:
            ret.value   # type: ignore
            ret.error   # type: ignore
        except:
            pass
        if ret.is_success:
            assert ret.value == 8
        ret.value       # type: ignore
        ResultAssert.is_success(ret)
        assert ret.value == 8

    def test_result_failure(self) -> None:
        ret = double_if_pos(value=-4)
        try:
            ret.value   # type: ignore
            ret.error   # type: ignore
        except:
            pass
        if ret.is_failure:
            assert ret.error_code == 'negative'
        ret.error_code  # type: ignore
