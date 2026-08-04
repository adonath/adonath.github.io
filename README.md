# adonath.github.io

[![Website](https://img.shields.io/badge/visit-website-blue.svg)](https://axeldonath.com)

The webpage uses a minimal static site generator based on [Jinja2](https://jinja.palletsprojects.com/) and [Markdown2](https://daringfireball.net/projects/markdown/).
The setup was loosely inspired by [PrettyPrinted](https://github.com/PrettyPrinted/youtube_video_code/tree/master/2019/12/16/Building%20a%20Simple%20Static%20Site%20Generator%20in%20Python). Dependencies are managed with [uv](https://docs.astral.sh/uv/). To generate the site follow these steps:

First install the dependencies from the lock file (uv creates and manages the virtual environment automatically):

```bash
uv sync
```

Then run the following command to generate the pages:

```bash
uv run make.py generate
```

Finally serve the webpage to preview the content:

```bash
uv run make.py serve
```

If needed clean up the generated files:

```bash
uv run make.py clean
```
