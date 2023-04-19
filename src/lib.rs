mod options;

use pyo3::prelude::*;
use pyo3::types::PyBytes;
use resvg::tiny_skia::Pixmap;
use usvg::{Size, Tree, TreeParsing};

use crate::options::{SVGOptions, ShapeRendering};

/// A Python class for rendering SVGs.
#[pyclass]
pub struct Resvg {
    options: Option<SVGOptions>,
}

#[pymethods]
impl Resvg {
    #[new]
    fn new(options: Option<SVGOptions>) -> Self {
        Self { options }
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

        let options = if let Some(options) = &self.options {
            usvg::Options {
                dpi: options.dpi,
                font_family: options.font_family.clone(),
                font_size: options.font_size,
                languages: options.languages.clone().unwrap_or_default(),
                shape_rendering: options.shape_rendering.clone().into(),
                text_rendering: options.text_rendering.clone().into(),
                image_rendering: options.image_rendering.clone().into(),
                resources_dir: options.resources_dir.clone(),
                default_size: Size::new(options.default_width, options.default_height).unwrap(),
                image_href_resolver: usvg::ImageHrefResolver::default(),
            }
        } else {
            usvg::Options::default()
        };

        let tree = Tree::from_str(svg, &options).unwrap();

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

    /// Returns the rendered image as bytes in PNG format.
    fn as_png(&self, py: Python) -> PyResult<PyObject> {
        self.pixmap
            .encode_png()
            .map(|b| PyBytes::new(py, &b).into())
            .map_err(|e| {
                pyo3::exceptions::PyException::new_err(format!("Failed to encode PNG: {}", e))
            })
    }
}

/// Python bindings for resvg.
#[pymodule]
fn resvg_py(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<ShapeRendering>()?;
    m.add_class::<SVGOptions>()?;
    m.add_class::<RenderedImage>()?;
    m.add_class::<Resvg>()?;
    Ok(())
}
