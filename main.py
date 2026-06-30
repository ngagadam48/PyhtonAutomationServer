from fastapi import FastAPI
import shutil

app = FastAPI()

@app.get("/")
def home():
	return {"status","running"}

@app.get("/disk")
def disk():
	total, used, free = shutil.disk_usage("/")

	return {
		"total_gb": round(total/1073741824,2),
		"used_gb": round (used/10737418224,2),
		"free_gb": round(free/1073741824,2)
	}
