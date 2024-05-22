from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger
from plombery import Trigger, register_pipeline, get_logger
from pytz import timezone
from pipedrive_shipcloud_automation import main

register_pipeline(
    id="dfd",
    description="Pipedrive and shipcloud update pipeline",
    tasks = [main.run_pipeline],
    triggers = [
        Trigger(
            id="pipedrive_8am",
            name= 'pipedrive_8am',
            description="Run the pipeline at 8 am Germany time",
            schedule=CronTrigger(hour=8, minute=0, timezone=timezone('Europe/Berlin')),
        ),
        Trigger(
            id="pipedrive_2pm",
            name = 'pipedrive_2pm',
            description="Run the pipeline at 2 PM Germany time",
            schedule=CronTrigger(hour=14, minute=0, timezone=timezone('Europe/Berlin')),
        ),
    ],
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("plombery:get_app", reload=True, factory=True)