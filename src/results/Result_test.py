
from typing import Literal
from .Result import Failure, Result, Success

def double_if_pos (value: int) -> Result[int, Literal['negative']]:
    if value >= 0:
        return Success(value * 2)
    return Failure('negative', f'value {value} cannot be passed to double_if_pos')

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

    def test_result_failure(self) -> None:
        ret = double_if_pos(value=-4)
        try:
            ret.value   # type: ignore
            ret.error   # type: ignore
        except:
            pass
        if ret.is_failure:
            assert ret.error_code == 'negative'

    def test_failure_message_and_stack(self) -> None:
        ret = double_if_pos(-2)
        assert ret.is_failure
        if ret.is_failure:
            assert ret.message == 'value -2 cannot be passed to double_if_pos'
            assert len(ret.stack) > 1

    def test_map_the_value_of_a_positive_result(self) -> None:
        ret = double_if_pos(4)
        new_ret = ret.map(lambda v: f'val: {v}')
        assert new_ret.is_success
        if new_ret.is_success:
            assert new_ret.value == 'val: 8'

    def test_map_the_value_if_failure(self) -> None:
        ret = double_if_pos(-4)
        new_ret = ret.map(lambda v: f'val: {v}')
        assert new_ret.is_failure
        if new_ret.is_failure:
            assert new_ret.error_code == 'negative'

