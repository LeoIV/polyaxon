from event_manager.event import Attribute, Event

TENSORBOARD_STARTED = 'tensorboard.started'
TENSORBOARD_STOPPED = 'tensorboard.stopped'
TENSORBOARD_VIEWED = 'tensorboard.viewed'
TENSORBOARD_NEW_STATUS = 'tensorboard.new_status'


class TensorboardStartedEvent(Event):
    type = TENSORBOARD_STARTED
    attributes = (
        Attribute('id'),
        Attribute('project.id'),
        Attribute('project.user.id'),
        Attribute('actor_id')
    )


class TensorboardSoppedEvent(Event):
    type = TENSORBOARD_STOPPED
    attributes = (
        Attribute('id'),
        Attribute('project.id'),
        Attribute('project.user.id'),
        Attribute('actor_id'),
        Attribute('status'),
    )


class TensorboardViewedEvent(Event):
    type = TENSORBOARD_VIEWED
    attributes = (
        Attribute('id'),
        Attribute('project.id'),
        Attribute('project.user.id'),
        Attribute('actor_id'),
        Attribute('status'),
    )


class TensorboardNewStatusEvent(Event):
    type = TENSORBOARD_NEW_STATUS
    attributes = (
        Attribute('id'),
        Attribute('project.id'),
        Attribute('status'),
    )