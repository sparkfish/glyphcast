# resvg-py

## Usage

```python
from pathlib import Path

import resvg_py
from PIL import Image

r = resvg_py.Resvg()

with Path("resources/examples/svg/simple.svg").open("r") as f:
    rendered = r.render(f.read(), 120, 120)
    array = rendered.as_array()
    im = Image.fromarray(array)
    im.save("image.png")
```
