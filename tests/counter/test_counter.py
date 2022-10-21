from src.counter import count_ocurrences


def test_counter():
    result = count_ocurrences("./src/jobs.csv", "python")
    assert result == 1639

    result = count_ocurrences("./src/jobs.csv", "javascript")
    assert result == 122
