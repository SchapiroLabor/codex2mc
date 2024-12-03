import json
from pprint import pprint

def main():
    with open("test_data/metadata/experimentV4.json") as f:
        d = json.load(f)

    print(d.keys())

    print(d["slideId"])

if __name__ == "__main__":
    main()
