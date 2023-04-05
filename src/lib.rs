use numpy::ndarray::Array3;
use numpy::{IntoPyArray, PyArray3};
use pyo3::prelude::*;
use resvg::tiny_skia::Pixmap;
use usvg::{Tree, TreeParsing};

/// A Python class for rendering SVGs.
#[pyclass]
pub struct Resvg {}

#[pymethods]
impl Resvg {
    #[new]
    fn new() -> Self {
        Self {}
    }

    /// Renders SVG to PNG.
    ///
    /// # Arguments
    ///
    /// * `svg` - String containing SVG data.
    /// * `width` - Width of the output image.
    /// * `height` - Height of the output image.
    ///
    /// # Returns
    ///
    /// A numpy array of shape (height, width, 4) containing RGBA data.
    fn render(&self, svg: &str, width: u32, height: u32) -> RenderedImage {
        let mut pixmap = Pixmap::new(width, height).unwrap();
        let tree = Tree::from_str(svg, &usvg::Options::default()).unwrap();

        resvg::render(
            &tree,
            resvg::FitTo::Original,
            tiny_skia::Transform::default(),
            pixmap.as_mut(),
        )
        .unwrap();

        RenderedImage { pixmap }
    }
}

/// Rendered image
#[pyclass]
pub struct RenderedImage {
    pixmap: Pixmap,
}

#[pymethods]
impl RenderedImage {
    /// Get the width of the image.
    pub fn width(&self) -> u32 {
        self.pixmap.width()
    }

    /// Get the height of the image.
    pub fn height(&self) -> u32 {
        self.pixmap.height()
    }

    /// Returns the rendered image as a numpy array.
    ///
    /// The array has shape (height, width, 4) and contains RGBA data.
    pub fn as_array<'py>(&self, py: Python<'py>) -> PyResult<&'py PyArray3<u8>> {
        let pixels = self.pixmap.pixels();

        Ok(Array3::from_shape_fn(
            ((self.height()) as usize, (self.width()) as usize, 4),
            |(y, x, c)| {
                let index = y * self.width() as usize + x;
                let pixel = &pixels[index];

                match c {
                    0 => pixel.red(),
                    1 => pixel.green(),
                    2 => pixel.blue(),
                    3 => pixel.alpha(),
                    _ => unreachable!(),
                }
            },
        )
        .into_pyarray(py))
    }

    fn as_png(&self) -> PyResult<Vec<u8>> {
        self.pixmap.encode_png().map_err(|e| {
            pyo3::exceptions::PyException::new_err(format!("Failed to encode PNG: {}", e))
        })
    }
}

/// Python bindings for resvg.
#[pymodule]
fn resvg_py(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Resvg>()?;
    Ok(())
}
