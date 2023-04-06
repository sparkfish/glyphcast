from __future__ import annotations

import os

from numpy import ndarray

class SVGOptions:
    def __init__(
        self: SVGOptions,
        *,
        dpi: float = 96.0,
        default_width: float = 100.0,
        default_height: float = 100.0,
        resources_dir: os.PathLike | None = None,
    ) -> None: ...

class Resvg:
    def __init__(self: Resvg, options: SVGOptions | None = None) -> None: ...
    def render(self: Resvg, svg: str, width: int, height: int) -> RenderedImage: ...

class RenderedImage:
    def as_array(self: RenderedImage) -> ndarray: ...
