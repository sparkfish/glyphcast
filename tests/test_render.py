"""Run the resvg-py example."""

from __future__ import annotations

import typing as t
from pathlib import Path

import pytest

import resvg_py

if t.TYPE_CHECKING:
    from pytest_snapshot.plugin import Snapshot


@pytest.mark.parametrize(
    ("svg_file", "optons"),
    [
        pytest.param(
            "resources/examples/svg/octocat.svg",
            id="octocat",
        ),
    ],
)
def test_render(snapshot: Snapshot, svg_file: str) -> None:
    rendering = resvg_py.ShapeRendering.GeometricPrecision
    options = resvg_py.SVGOptions(shape_rendering=rendering)
    r = resvg_py.Resvg(options)

    with Path(svg_file).open("r") as input_file:
        rendered = r.render(input_file.read(), 400, 400)
        snapshot.assert_match(rendered.as_png(), "output.png")
