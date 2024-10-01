import sys
import argparse

from multiprocessing import Process

from src.apps.backoffice.backend.boot import backoffice_backend_process
from src.apps.quickstore.backend.boot import quickstore_backend_process

context_mapping = {
    'backoffice-backend': backoffice_backend_process,
    'quickstore-backend': quickstore_backend_process,
}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run a specific context.')

    parser.add_argument(
        '--context',
        type=str,
        choices=list(context_mapping.keys()),
        required=True,
        help='Context to run. Must be one of: %(choices)s',
    )

    args = parser.parse_args()
    context_name = args.context

    try:
        context_process: Process = context_mapping.get(context_name)

        print(f'Booting {context_name} server')

        context_process.start()
        context_process.join()

        print(f'{context_name} server started successfully')
    except KeyboardInterrupt:
        print(f'\n{context_name} server stopped by user')

        sys.exit(0)
    except Exception as e:
        print(f'Error starting {context_name} server: {str(e)}')

        sys.exit(1)
