import json
import loghandler
from datetime import datetime

x = loghandler.GeneralLogging("TEST SCRIPT")
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")


def format_json():
    filename = "formatted_{}.json".format(timestamp)
    try:
        f1 = open("fixme.json", "r")
        jsonfile = json.load(f1)
        f2 = open(filename, "w", encoding="utf-8")
        json.dump(jsonfile, f2, indent=4, ensure_ascii=False)
    except Exception as e:
        x.exception(e)


format_json()
