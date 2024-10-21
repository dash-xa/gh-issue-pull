from contextlib import asynccontextmanager
from typing import Optional

from fastapi import FastAPI, HTTPException

from gh_issue_pull.classes import convert_swedataset_item_to_entry
from gh_issue_pull.helpers import fetch_unused_issue, pull_all_swebench_entries, SWEBENCH_DB_PATH, obfuscate
from gh_issue_pull.swebench_dataset import SWEDataset


dataset: Optional[SWEDataset] = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("App is starting up")
    global dataset
    dataset = SWEDataset()
    yield  # The app runs between startup and shutdown here

    print("App is shutting down")


app = FastAPI(lifespan=lifespan)


@app.get("/task")
async def get_task():
    """
    Gets the current problem to be solved by validators, as a ProblemStatement object
    """
    try:
        item = dataset.get(1)
        return convert_swedataset_item_to_entry(item)
    except Exception as e:
        print("Internal server error:", e)
        raise HTTPException(status_code=500)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
