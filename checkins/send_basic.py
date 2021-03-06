import click
from dotenv import load_dotenv

from checkins.config import WEBHOOK_URL


@click.command()
@click.argument("message", required=True)
def main(message: str) -> None:
    pass


if __name__ == "__main__":
    load_dotenv()
    main()
