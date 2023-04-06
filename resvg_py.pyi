from __future__ import annotations

import os

from numpy import ndarray

class SVGOptions:
    def __init__(
        self: SVGOptions,
        *,
        dpi: float,
        default_width: float,
        default_height: float,
        resources_dir: os.PathLike | None,
    ) -> None: ...

class Resvg:
    def __init__(self: Resvg, options: SVGOptions | None) -> None: ...
    def render(self: Resvg, svg: str, width: int, height: int) -> RenderedImage: ...

class RenderedImage:
    def as_array(self: RenderedImage) -> ndarray: ...
