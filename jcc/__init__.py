"""Top-level package for jCalConvert"""

# jcalconvert/__init__.py

__app_name__ = "jcc"
__version__ = "0.1.0"

(
    SUCCESS,
    DIR_ERROR,
    FILE_ERROR,
    DB_READ_ERROR,
    JSON_ERROR,
) = range(5)

ERRORS = {
    DIR_ERROR: "config directory error",
    FILE_ERROR: "config file error",
    DB_READ_ERROR: "database read error",
}
