import activitylogs

from event_manager.events import experiment

activitylogs.subscribe(experiment.ExperimentCreatedEvent)
activitylogs.subscribe(experiment.ExperimentUpdatedEvent)
activitylogs.subscribe(experiment.ExperimentDeletedTriggeredEvent)
activitylogs.subscribe(experiment.ExperimentViewedEvent)
activitylogs.subscribe(experiment.ExperimentStoppedTriggeredEvent)
activitylogs.subscribe(experiment.ExperimentResumedTriggeredEvent)
activitylogs.subscribe(experiment.ExperimentRestartedTriggeredEvent)
activitylogs.subscribe(experiment.ExperimentCopiedTriggeredEvent)
activitylogs.subscribe(experiment.ExperimentResourcesViewedEvent)
activitylogs.subscribe(experiment.ExperimentLogsViewedEvent)
activitylogs.subscribe(experiment.ExperimentStatusesViewedEvent)
activitylogs.subscribe(experiment.ExperimentJobsViewedEvent)
activitylogs.subscribe(experiment.ExperimentMetricsViewedEvent)