use pyo3::prelude::*;

/// A shape rendering method.
///
/// `shape-rendering` attribute in the SVG.
#[derive(Clone)]
#[pyclass]
pub enum ShapeRendering {
    OptimizeSpeed,
    CrispEdges,
    GeometricPrecision,
}

impl From<ShapeRendering> for usvg::ShapeRendering {
    fn from(shape_rendering: ShapeRendering) -> Self {
        match shape_rendering {
            ShapeRendering::OptimizeSpeed => Self::OptimizeSpeed,
            ShapeRendering::CrispEdges => Self::CrispEdges,
            ShapeRendering::GeometricPrecision => Self::GeometricPrecision,
        }
    }
}

/// Specifies the default text rendering method.
///
/// Will be used when an SVG element's `text-rendering` property is set to `auto`.
///
/// Default: OptimizeLegibility
#[derive(Clone)]
#[pyclass]
pub enum TextRendering {
    OptimizeSpeed,
    OptimizeLegibility,
    GeometricPrecision,
}

impl From<TextRendering> for usvg::TextRendering {
    fn from(text_rendering: TextRendering) -> Self {
        match text_rendering {
            TextRendering::OptimizeSpeed => Self::OptimizeSpeed,
            TextRendering::OptimizeLegibility => Self::OptimizeLegibility,
            TextRendering::GeometricPrecision => Self::GeometricPrecision,
        }
    }
}

/// An image rendering method.
///
/// `image-rendering` attribute in the SVG.
#[derive(Clone)]
#[pyclass]
pub enum ImageRendering {
    OptimizeQuality,
    OptimizeSpeed,
}

impl From<ImageRendering> for usvg::ImageRendering {
    fn from(image_rendering: ImageRendering) -> Self {
        match image_rendering {
            ImageRendering::OptimizeQuality => Self::OptimizeQuality,
            ImageRendering::OptimizeSpeed => Self::OptimizeSpeed,
        }
    }
}

/// SVG parsing and rendering options.
///
/// TODO(edgarmondragon): Add more options.
#[derive(Clone)]
#[pyclass]
pub struct SVGOptions {
    /// Target DPI.
    ///
    /// Impacts units conversion.
    ///
    /// Default: 96.0
    pub dpi: f64,

    /// A default font family.
    ///
    /// Will be used when no `font-family` attribute is set in the SVG.
    ///
    /// Default: Times New Roman
    pub font_family: String,

    /// A default font size.
    ///
    /// Will be used when no `font-size` attribute is set in the SVG.
    ///
    /// Default: 12
    pub font_size: f64,

    /// Languages to use when resolving `systemLanguage` conditional attributes.
    ///
    /// Format: en, en-US.
    ///
    /// Default: `[en]`
    pub languages: Option<Vec<String>>,

    /// Specifies the default shape rendering method.
    ///
    /// Will be used when an SVG element's `shape-rendering` property is set to `auto`.
    ///
    /// Default: GeometricPrecision
    pub shape_rendering: ShapeRendering,

    /// Specifies the default text rendering method.
    ///
    /// Will be used when an SVG element's `text-rendering` property is set to `auto`.
    ///
    /// Default: OptimizeLegibility
    pub text_rendering: TextRendering,

    /// Specifies the default image rendering method.
    ///
    /// Will be used when an SVG element's `image-rendering` property is set to `auto`.
    ///
    /// Default: OptimizeQuality
    pub image_rendering: ImageRendering,

    /// Directory that will be used during relative paths resolving.
    ///
    /// Expected to be the same as the directory that contains the SVG file,
    /// but can be set to any.
    ///
    /// Default: `None
    pub resources_dir: Option<std::path::PathBuf>,

    /// Default viewport width to assume if there is no `viewBox` attribute and
    /// the `width` is relative.
    ///
    /// Default: 100.0
    pub default_width: f64,

    /// Default viewport height to assume if there is no `viewBox` attribute and
    /// the `height` is relative.
    ///
    /// Default: 100.0
    pub default_height: f64,
}


#[pymethods]
impl SVGOptions {
    #[new]
    #[pyo3(
        signature = (
            *,
            dpi = 96.0,
            font_family = "Times New Roman".to_string(),
            font_size = 12.0,
            languages = None,
            shape_rendering = ShapeRendering::GeometricPrecision,
            text_rendering = TextRendering::OptimizeLegibility,
            image_rendering = ImageRendering::OptimizeQuality,
            resources_dir = None,
            default_width = 100.0,
            default_height = 100.0,
        )
    )]
    fn new(
        dpi: f64,
        font_family: String,
        font_size: f64,
        languages: Option<Vec<String>>,
        shape_rendering: ShapeRendering,
        text_rendering: TextRendering,
        image_rendering: ImageRendering,
        resources_dir: Option<std::path::PathBuf>,
        default_width: f64,
        default_height: f64,
    ) -> Self {
        Self {
            dpi,
            font_family,
            font_size,
            languages,
            shape_rendering,
            text_rendering,
            image_rendering,
            resources_dir,
            default_width,
            default_height,
        }
    }
}
