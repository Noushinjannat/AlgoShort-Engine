
# Advanced URL Shortener (Algorithm-Focused Submission)

## Features
- SHA256 Hashing
- Base62 Encoding
- O(1) LRU Cache
- Thread-Safe Operations
- Collision Handling
- Custom Exceptions
- CLI Interface

## Complexity

Shorten:
- SHA256: O(1)
- Base62: O(log n)
- Collision Resolution: O(k)

Retrieve:
- Dict Lookup: O(1)
- LRU Access: O(1)

## Run

python cli.py --shorten https://google.com
python cli.py --retrieve <short_code>
