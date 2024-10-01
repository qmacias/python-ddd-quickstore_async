import multiprocessing

from src.apps.backoffice.backend.server import run_backoffice_backend

backoffice_backend_process = multiprocessing.Process(target=run_backoffice_backend)
