"""This is an example flows module"""
from prefect import flow

from prefect_ftp.blocks import FtpBlock
from prefect_ftp.tasks import (
    goodbye_prefect_ftp,
    hello_prefect_ftp,
)


@flow
def hello_and_goodbye():
    """
    Sample flow that says hello and goodbye!
    """
    FtpBlock.seed_value_for_example()
    block = FtpBlock.load("sample-block")

    print(hello_prefect_ftp())
    print(f"The block's value: {block.value}")
    print(goodbye_prefect_ftp())
    return "Done"


if __name__ == "__main__":
    hello_and_goodbye()
