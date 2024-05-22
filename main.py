from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger
from plombery import Trigger, register_pipeline
from pytz import timezone
from plombery import task, get_logger

@task
def pipedrive():
    from pipedrive_shipcloud_automation import main
    main.log = get_logger()
    main.run_pipeline()

register_pipeline(
    id="pipedrive_X_shipcloud",
    description="Pipedrive and shipcloud update pipeline",
    tasks = [pipedrive],
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