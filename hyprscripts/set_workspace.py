#!/usr/bin/env python3
import sys
import json
import subprocess

res = subprocess.run(["hyprctl", "activeworkspace", "-j"], capture_output=True)
monitor_id = json.loads(res.stdout)["monitorID"]
target_workspace = int(sys.argv[1]) + (monitor_id * 10)
subprocess.run(["hyprctl", "dispatch", "workspace", str(target_workspace)])
