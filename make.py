import logging
import shutil
import time
import webbrowser
from functools import partial
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from threading import Thread

import click
from jinja2 import Environment, FileSystemLoader
from markdown2 import markdown

log = logging.getLogger(__name__)

PATH = Path(__file__).parent
PATH_OUTPUT = PATH / "site"

IP = "localhost"
PORT = 8000
SERVER_ADDRESS = (IP, PORT)
URL = f"http://{IP}:{PORT}"


def copy_static_files():
    """Copy static files"""
    log.info("Copy static files")
    shutil.copytree(PATH / "static", PATH_OUTPUT / "static")


def open_site():
    """Open site"""
    time.sleep(0.1)
    webbrowser.open(URL)


@click.group()
def cli():
    """Generate and serve webpage"""
    pass


@cli.command("generate")
def generate():
    """Generate webpage sites"""
    loader = FileSystemLoader(searchpath="./templates")
    template_env = Environment(loader=loader)

    template = template_env.get_template("main.html")

    filenames = (PATH / "content").glob("*.md")

    for filename in filenames:

        name = filename.stem

        if name == "home":
            name = "index"

        filename_output = PATH_OUTPUT / f"{name}.html"

        filename_output.parent.mkdir(exist_ok=True, parents=True)

        with filename_output.open("w") as output_file:
            log.info(f"Reading {filename}")
            content = markdown(filename.read_text())

            content_html = template.render(content=content)

            log.info(f"Writing {filename_output}")
            output_file.write(content_html)

    copy_static_files()


@cli.command("clean")
def clean():
    """Clean generated output files"""
    shutil.rmtree(PATH_OUTPUT)


@cli.command("serve")
def serve():
    """Serve the docs page and open in default browser.

    Combination of these two SO (license CC-BY-SA 4.0) answers:

    https://stackoverflow.com/a/51295415/3838691
    https://stackoverflow.com/a/52531444/3838691

    """
    Thread(target=open_site).start()
    handler = partial(SimpleHTTPRequestHandler, directory=str(PATH_OUTPUT))
    httpd = HTTPServer(SERVER_ADDRESS, handler)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    cli()
