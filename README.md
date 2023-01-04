# adonath.github.io

The webpage uses a minimal static site generator based on [Jinja2](https://jinja.palletsprojects.com/) and [Markdown2](https://daringfireball.net/projects/markdown/).
The setup was loosely inspired by [PrettyPrinted](https://github.com/PrettyPrinted/youtube_video_code/tree/master/2019/12/16/Building%20a%20Simple%20Static%20Site%20Generator%20in%20Python).

To generate the site follow the following steps:

First create a new virtual environment:

```python3
python3 -m venv env-adonath-webpage
```

And activate it:

```python3
source env-adonath-webpage/bin/activate
```

The snstall the required dependencies stored in the `requirements.txt` file:

```python3
python -m pip install -r requirements.txt
```

And run the follwing command:

```python3
python make.py generate
```

Finally serve the webpage to preview the content:

```python3
python make.py serve
```

Cleanup generated files:

```python3
python make.py clean
```