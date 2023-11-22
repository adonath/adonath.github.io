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
logging.basicConfig(level=logging.DEBUG)

PATH = Path(__file__).parent
PATH_OUTPUT = PATH / "site"

IP = "localhost"
PORT = 4000
SERVER_ADDRESS = (IP, PORT)
URL = f"http://{IP}:{PORT}"

NAVBAR_ITEMS = {
    "home": "index",
    "about": "about",
    "research": "research",
    "software": "software",
    "blog": "blog",
    "contact": "contact",
}

loader = FileSystemLoader(searchpath="./templates")
TEMPLATE_ENV = Environment(loader=loader)


def copy_static_files(overwrite):
    """Copy static files"""
    path = PATH_OUTPUT / "static"

    if path.exists() and overwrite:
        shutil.rmtree(path)

    log.info("Copy static files")
    shutil.copytree(PATH / "static", path)


def open_site():
    """Open site"""
    time.sleep(0.1)
    webbrowser.open(URL)


@click.group()
def cli():
    """Generate and serve webpage"""
    pass


@cli.command("generate")
@click.option(
    "--overwrite", default=False, is_flag=True, help="Overwrite existing output files."
)
def generate(overwrite):
    """Generate webpage sites"""
    template = TEMPLATE_ENV.get_template("main.html")

    filenames = list((PATH / "content").glob("*.md"))

    navbar_items = []

    for caption, href in NAVBAR_ITEMS.items():
        item = {"href": f"./{href}.html", "caption": caption}
        navbar_items.append(item)

    for filename in filenames:
        name = "index" if filename.stem == "home" else filename.stem

        filename_output = PATH_OUTPUT / f"{name}.html"

        filename_output.parent.mkdir(exist_ok=True, parents=True)

        with filename_output.open("w") as output_file:
            log.info(f"Reading {filename}")
            content = markdown(filename.read_text())

            content_html = template.render(
                content=content,
                navbar_items=navbar_items,
                active_page=filename.stem,
            )

            log.info(f"Writing {filename_output}")

            if filename_output.exists() and not overwrite:
                raise IOError(f"File {filename_output} already exists")

            output_file.write(content_html)

    entries = generate_blog_entries(overwrite=overwrite)

    generate_blog_index(
        navbar_items=navbar_items,
        template=template,
        overwrite=overwrite,
        entries=entries,
    )

    copy_static_files(overwrite=overwrite)


def generate_blog_index(navbar_items, template, entries, overwrite=True):
    """Generate blog index"""
    filename_output = PATH_OUTPUT / "blog.html"

    template_blog_entry = TEMPLATE_ENV.get_template("blog-entry-index.html")
    content = template_blog_entry.render(entries=entries)

    content_html = template.render(
        content=content,
        navbar_items=navbar_items,
        active_page="blog",
    )

    with filename_output.open("w") as output_file:
        if filename_output.exists() and not overwrite:
            raise IOError(f"File {filename_output} already exists")

        log.info(f"Writing {filename_output}")
        output_file.write(content_html)


def generate_blog_entries(overwrite=True):
    """Generate blog entries"""
    filenames = list((PATH / "content" / "blog").glob("**/*.md"))

    template_blog = TEMPLATE_ENV.get_template("blog.html")

    entries = []

    for filename in filenames:
        date = filename.parent.stem
        filename_output = PATH_OUTPUT / "blog" / f"{date}/{filename.stem}.html"

        filename_output.parent.mkdir(exist_ok=True, parents=True)

        with filename_output.open("w") as output_file:
            log.info(f"Reading {filename}")
            content = markdown(
                filename.read_text(),
                extras=["fenced-code-blocks", "code-friendly", "metadata", "toc"],
            )

            content_html = template_blog.render(
                toc=content.toc_html,
                content=content,
                next_page=None,
                previous_page=None,
            )

            log.info(f"Writing {filename_output}")

            if filename_output.exists() and not overwrite:
                raise IOError(f"File {filename_output} already exists")

            output_file.write(content_html)

        entries.append(
            {
                "date": date,
                "title": content.metadata.get("title", "Title missing"),
                "href": f"{filename_output.relative_to(PATH_OUTPUT)}",
                "summary": content.metadata.get("summary", "Summary missing"),
            }
        )

    return entries


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

    log.info(f"Serve website at {URL}")
    handler = partial(SimpleHTTPRequestHandler, directory=str(PATH_OUTPUT))
    httpd = HTTPServer(SERVER_ADDRESS, handler)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    cli()
