import seaborn as sns

import caching
import time

def test_caching():

    @caching.cached(
        exclude=["num_processes"],
        exclude_if_default=["z"],
    )
    def slow_function(
        x: int,
        y: int,
        num_processes: int,
        z: int = 0
    ):
        time.sleep(2 / num_processes)
        return x + y + z
    
    caching.set_cache_dir("_cache_dir")
    #Try without hashing
    caching.set_use_hash(False)
    slow_function(1, 1, num_processes=1, z=0)
    #Try with hashing and non-default value for z.
    caching.set_use_hash(True)
    slow_function(1, 1, num_processes=1, z=2)

