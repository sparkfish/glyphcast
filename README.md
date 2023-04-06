# resvg-py

## Usage

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

## Development

### Build

```sh
maturin develop
```

### Test

```sh
pytest
```

To update the snapshots:

```sh
pytest --snapshot-update
```
