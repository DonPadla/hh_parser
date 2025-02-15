from src.support import get_human_readable
from tests.conftest import for_human_readable_test


def test_human_readable(list_for_test, for_human_readable_test):
    """ Тест преобразования в человекочитаемый вид """

    result = get_human_readable(list_for_test)
    extend_result = for_human_readable_test

    assert result == extend_result
