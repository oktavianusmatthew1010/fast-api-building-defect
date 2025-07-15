import asyncio


import uvloop
from arq.worker import Worker

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


# -------- background tasks --------
async def sample_background_task(ctx: Worker, name: str) -> str:
    await asyncio.sleep(5)
    return f"Task {name} is complete!"

