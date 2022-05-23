#!/usr/bin/env python3

import asyncio
from temporalio.client import Client


async def main():
    # Create client connected to server at the given address
    client = await Client.connect("http://localhost:7233")

    # Start a workflow
    handle = await client.start_workflow(
        "my workflow name",
        "some arg",
        id="my-workflow-id",
        task_queue="my-task-queue"
    )

    print(f"Workflow started with ID {handle.id}")


if __name__ == "__main__":
    asyncio.run(main())
