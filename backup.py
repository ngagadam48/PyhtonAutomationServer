import shutil
from datetime import datetime

source = "documents"

timestamp = datatime.now().strftime("Y%m%d")

destination = f"backup_{timestamp}"

shutil.copytree(source,destination)

print("Backup Finished")

