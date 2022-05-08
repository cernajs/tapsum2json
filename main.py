#!/usr/bin/env python3

import sys
import json
from tap import parser

parser = parser.Parser()

summary = {
  "summary": [
  ]
}

def main():
	for tap_file in sys.argv[1:]:
		temp_dict = {
		      "filename": "",
		      "total": 0,
		      "passed": 0,
		      "skipped": 0,
		      "failed": 0
		    }

		temp_dict["filename"] = str(tap_file).split("/")[-1]

		for line in parser.pare_file(tap_file):
			try:
				if list(line)[0] == 1:
					temp_dict["total"] = str(line).split("..")[-1]
				if "ok" in str(line) and "skip" not in str(line):
					temp_dict["passed"] += 1
				if "not ok" in str(line):
					temp_dict["failed"] += 1
				if "skip" in str(line):
					temp_dict["skipped"] += 1
			except:
				pass

		summary["summary"].append(temp_dict)

	print(json.dumps(summary, indent=4))

if __name__ == '__main__':
	main()
