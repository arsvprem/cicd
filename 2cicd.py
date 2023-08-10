import os
import sys
from nornir import InitNornir
from nornir_scrapli.tasks import send_configs_from_file
from nornir_utils.plugins.functions import print_result
from nornir.core.exceptions import NornirExecutionError

config_file = sys.argv[1]
nr = InitNornir(config_file=config_file)
nr.inventory.defaults.username = os.getenv("USERNAME")
nr.inventory.defaults.password = os.getenv("PASSWORD")


def random_configs(task):
  task.run(task=send_configs_from_file, file="configtest.txt")

results = nr.run(task=random_configs)
print_result(results)
failures = nr.data.failed_hosts
if failures:
  raise NornirExecutionError("Nornir Failure Detected")
