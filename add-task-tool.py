import os
import requests
from datetime import datetime


class Tools:
    def __init__(self):
        pass

    # Add your custom tools using pure Python code here, make sure to add type hints
    # Use Sphinx-style docstrings to document your tools, they will be used for generating tools specifications
    # Please refer to function_calling_filter_pipeline.py file from pipelines project for an example

    async def add_task(
        self, title: str, description: str, __event_emitter__=None
    ) -> str:
        """
        Store a task in an external task manager. Creates a todo list item
        for the user. Should be used whenever the user asks the agent to
        remember something, store a task, or add something to their todo list.
        :param title: the title of the task
        :param description: the description of the task
        :return: a message indicating successful task adding or an error
        """

        ### TEMPORARY YOU SHOULD PROBABLY REWRITE ###
        # goal is this will actually store to TODOist

        await __event_emitter__(
            {
                "type": "message",  # We set the type here
                "data": {"content": "Storing your tasks...", "done": False},
                # Note that with message types we do NOT have to set a done condition
            }
        )

        try:
            # Ensure tasks directory exists
            tasks_dir = "tasks"
            if not os.path.exists(tasks_dir):
                os.makedirs(tasks_dir)

            # Create a unique filename and write the description to a file
            filename = f"{tasks_dir}/{title}.md"

            with open(filename, "w") as task_file:
                task_file.write(description)

            task_file.close()

            result = f"Stored task: {title} - {description}"

        except Exception as e:
            await __event_emitter__(
                {
                    "type": "status",
                    "data": {"description": f"An error occured: {e}", "done": True},
                }
            )

            return f"Tell the user: {e}"

        await __event_emitter__(
            {
                "type": "status",
                "data": {
                    "description": f"Completed successfully! {result}",
                    "done": True,
                },
            }
        )
