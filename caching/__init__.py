"""Matplotlib science style"""

from .caching import cached, set_cache_dir, set_log_level, set_use_hash

# https://github.com/python-poetry/poetry/pull/2366#issuecomment-652418094
# https://github.com/python-poetry/poetry/issues/144#issuecomment-623927302
try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:
    import importlib_metadata
package_name = "caching-decorator"
__version__ = importlib_metadata.version(package_name)


__all__ = ["set_cache_dir", "set_use_hash", "cached", "set_log_level"]
