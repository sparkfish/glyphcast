from __future__ import annotations

from numpy import ndarray

class RenderedImage:
    def as_array(self: RenderedImage) -> ndarray: ...

class Resvg:
    def __init__(self: Resvg) -> None: ...
    def render(self: Resvg, svg: str, width: int, height: int) -> RenderedImage: ...
