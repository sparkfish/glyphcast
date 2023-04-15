from __future__ import annotations

import os

from numpy import ndarray

class ShapeRendering:
    OptimizeSpeed = ...
    CrispEdges = ...
    GeometricPrecision = ...

class SVGOptions:
    def __init__(
        self: SVGOptions,
        *,
        dpi: float = 96.0,
        font_family: str = "Times New Roman",
        font_size: float = 12.0,
        languages: list[str] | None = None,
        shape_rendering: ShapeRendering = ...,
        resources_dir: os.PathLike | None = None,
        default_width: float = 100.0,
        default_height: float = 100.0,
    ) -> None: ...

class Resvg:
    def __init__(self: Resvg, options: SVGOptions | None = None) -> None: ...
    def render(self: Resvg, svg: str, width: int, height: int) -> RenderedImage: ...

class RenderedImage:
    def as_array(self: RenderedImage) -> ndarray: ...
    def as_png(self: RenderedImage) -> bytes: ...
