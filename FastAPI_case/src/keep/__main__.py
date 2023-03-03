import uvicorn as ucn
from keep.settings import settings

ucn.run(
    "keep.app:app",
    host=settings.server_host,
    port=settings.server_port,
    reload=True,
)