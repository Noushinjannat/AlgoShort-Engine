
import argparse
from urlshortener.engine import URLShortenerEngine

def main():
    parser = argparse.ArgumentParser(description="Advanced URL Shortener CLI")
    parser.add_argument("--shorten", type=str, help="URL to shorten")
    parser.add_argument("--retrieve", type=str, help="Short code to retrieve")

    args = parser.parse_args()
    engine = URLShortenerEngine()

    if args.shorten:
        code = engine.shorten(args.shorten)
        print("Short Code:", code)

    elif args.retrieve:
        try:
            print("Original URL:", engine.retrieve(args.retrieve))
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
