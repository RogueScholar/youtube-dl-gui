from gettext import gettext as _

from .utils import TwoWayOrderedDict as tDict

OUTPUT_FORMATS = ()
FORMATS = ()
DEFAULT_FORMATS = ()
AUDIO_FORMATS = ()
VIDEO_FORMATS = ()


def load_formats():
    global OUTPUT_FORMATS
    global DEFAULT_FORMATS
    global VIDEO_FORMATS
    global AUDIO_FORMATS
    global FORMATS

    OUTPUT_FORMATS = tDict([
        (0, _("ID")),
        (1, _("Title")),
        (2, _("Title + ID")),
        (4, _("Title + Quality")),
        (5, _("Title + ID + Quality")),
        (3, _("Custom")),
    ])

    DEFAULT_FORMATS = tDict([("0", _("default"))])

    VIDEO_FORMATS = tDict([
        ("3gp", "3gp"),
        ("17", "3gp [144p]"),
        ("36", "3gp [240p]"),
        ("flv", "FLV"),
        ("5", "FLV [240p]"),
        ("34", "FLV [360p]"),
        ("35", "FLV [480p]"),
        ("webm", "WebM"),
        ("43", "WebM [360p]"),
        ("44", "WebM [480p]"),
        ("45", "WebM [720p]"),
        ("46", "WebM [1080p]"),
        ("mp4", "MP4"),
        ("18", "MP4 [360p]"),
        ("22", "MP4 [720p]"),
        ("37", "MP4 [1080p]"),
        ("38", "MP4 [4K]"),
        ("160", "MP4 [144p] (DASH Video)"),
        ("133", "MP4 [240p] (DASH Video)"),
        ("134", "MP4 [360p] (DASH Video)"),
        ("135", "MP4 [480p] (DASH Video)"),
        ("136", "MP4 [720p] (DASH Video)"),
        ("137", "MP4 [1080p] (DASH Video)"),
        ("264", "MP4 [1440p] (DASH Video)"),
        ("138", "MP4 [2160p] (DASH Video)"),
        ("242", "WebM [240p] (DASH Video)"),
        ("243", "WebM [360p] (DASH Video)"),
        ("244", "WebM [480p] (DASH Video)"),
        ("247", "WebM [720p] (DASH Video)"),
        ("248", "WebM [1080p] (DASH Video)"),
        ("271", "WebM [1440p] (DASH Video)"),
        ("272", "WebM [2160p] (DASH Video)"),
        ("82", "MP4 [360p] (3D)"),
        ("83", "MP4 [480p] (3D)"),
        ("84", "MP4 [720p] (3D)"),
        ("85", "MP4 [1080p] (3D)"),
        ("100", "WebM [360p] (3D)"),
        ("101", "WebM [480p] (3D)"),
        ("102", "WebM [720p] (3D)"),
        ("139", "M4A 48k (DASH Audio)"),
        ("140", "M4A 128k (DASH Audio)"),
        ("141", "M4A 256k (DASH Audio)"),
        ("171", "WebM 48k (DASH Audio)"),
        ("172", "WebM 256k (DASH Audio)"),
    ])

    AUDIO_FORMATS = tDict([
        ("mp3", "MP3"),
        ("wav", "WAB"),
        ("aac", "AAC"),
        ("m4a", "M4A"),
        ("vorbis", "Vorbis"),
        ("opus", "Opus"),
        ("flac", "FLAC"),
    ])

    FORMATS = DEFAULT_FORMATS.copy()
    FORMATS.update(VIDEO_FORMATS)
    FORMATS.update(AUDIO_FORMATS)
