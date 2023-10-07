from prefect import flow

from prefect_ftp.tasks import (
    goodbye_prefect_ftp,
    hello_prefect_ftp,
)


def test_hello_prefect_ftp():
    @flow
    def test_flow():
        return hello_prefect_ftp()

    result = test_flow()
    assert result == "Hello, prefect-ftp!"


def goodbye_hello_prefect_ftp():
    @flow
    def test_flow():
        return goodbye_prefect_ftp()

    result = test_flow()
    assert result == "Goodbye, prefect-ftp!"
