"""Run the resvg-py example."""

from __future__ import annotations

import io
import typing as t
from pathlib import Path

import pytest
from PIL import Image

import resvg_py

if t.TYPE_CHECKING:
    from pytest_snapshot.plugin import Snapshot


@pytest.mark.parametrize(
    "svg_file",
    [
        pytest.param("resources/examples/svg/octocat.svg", id="octocat"),
    ],
)
def test_render(snapshot: Snapshot, svg_file: str) -> None:
    options = resvg_py.SVGOptions()
    r = resvg_py.Resvg(options)

    with Path(svg_file).open("r") as input_file:
        rendered = r.render(input_file.read(), 400, 400)
        array = rendered.as_array()

        with io.BytesIO() as png_file:
            im = Image.fromarray(array)
            im.save(png_file, format="PNG")
            snapshot.assert_match(png_file.getvalue(), "output.png")
