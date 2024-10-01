import multiprocessing

from src.apps.quickstore.backend.server import run_quickstore_backend

quickstore_backend_process = multiprocessing.Process(target=run_quickstore_backend)
