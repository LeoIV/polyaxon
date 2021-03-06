from checks.worker import WorkerCheck
from polyaxon.config_settings import EventsCeleryTasks


class EventsCheck(WorkerCheck):
    WORKER_HEALTH_TASK = EventsCeleryTasks.EVENTS_HEALTH
    WORKER_NAME = 'EVENTS'
