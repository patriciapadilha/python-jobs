from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    dict_translet = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    assert "title" in dict_translet[0]
    assert "salary" in dict_translet[0]
    assert "type" in dict_translet[0]
