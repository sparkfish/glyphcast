# resvg-py

`resvg-py` provides a Python interface to the `resvg` library, an open-source SVG rendering library that can be used to convert SVG images to various other formats such as PNG, PDF, and SVGZ.

The purpose of `resvg-py` is to provide a convenient way to use `resvg` from within Python code, without the need for external dependencies.  By using `resvg-py`, developers can incorporate SVG rendering functionality directly into their Python applications, making it easier to work with SVG images and to create high-quality, scalable graphics for their projects.

With `resvg-py`, developers can:

* Load SVG files and render them to various output formats
* Control the output size, resolution, and quality of the rendered images
* Modify SVG documents programmatically before rendering
* Work with SVG images directly within their Python code, without the need for external tools or libraries

Overall, `resvg-py` provides a simple and powerful way to work with SVG images in Python, and can be a useful tool for developers who need to work with vector graphics in their projects.


# Usage

```python
from pathlib import Path

import resvg_py
from PIL import Image

options = resvg_py.SVGOptions()
r = resvg_py.Resvg(options)

with Path("resources/examples/svg/octocat.svg").open("r") as f:
    rendered = r.render(f.read(), 400, 400)
    array = rendered.as_array()
    im = Image.fromarray(array)
    im.save("image.png")

```

# How To Build

## Install Rust, Set up Python Dev Requirements

**Windows**

```sh
choco install rust
```

**Set up Virtual Environemt**

```sh
python -m venv venv
.\venv\Scripts\Activate.bat
```

**Install Maturin and Pytest**

```sh
pip install -r requirements-dev.txt
```

## Build Python Wheel

```sh
maturin develop
```

## Run Tests

```sh
pytest
```

To update the snapshots:

```sh
pytest --snapshot-update
```
