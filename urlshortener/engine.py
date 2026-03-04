
import hashlib
import threading
import time
from typing import Dict, Optional

from .encoder import Base62Encoder
from .lru import LRUCache
from .exceptions import URLNotFoundError, URLExpiredError

class URLShortenerEngine:
    def __init__(self, cache_capacity: int = 1000) -> None:
        self._storage: Dict[str, dict] = {}
        self._counter: int = 1
        self._lock = threading.Lock()
        self._cache = LRUCache(cache_capacity)

    def _generate_numeric_id(self, url: str) -> int:
        hash_digest = hashlib.sha256(url.encode()).hexdigest()
        return int(hash_digest[:12], 16)

    def shorten(self, url: str, expiry_seconds: Optional[int] = None) -> str:
        with self._lock:
            numeric_id = self._generate_numeric_id(url) + self._counter
            self._counter += 1
            short_code = Base62Encoder.encode(numeric_id)

            while short_code in self._storage:
                numeric_id += 1
                short_code = Base62Encoder.encode(numeric_id)

            expiry = time.time() + expiry_seconds if expiry_seconds else None

            self._storage[short_code] = {
                "url": url,
                "created": time.time(),
                "expiry": expiry,
                "clicks": 0,
            }
            return short_code

    def retrieve(self, short_code: str) -> str:
        cached = self._cache.get(short_code)
        if cached:
            return cached

        if short_code not in self._storage:
            raise URLNotFoundError("Short code not found")

        record = self._storage[short_code]

        if record["expiry"] and time.time() > record["expiry"]:
            raise URLExpiredError("URL has expired")

        record["clicks"] += 1
        self._cache.put(short_code, record["url"])
        return record["url"]
