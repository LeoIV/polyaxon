import { Action, combineReducers } from 'redux';

import { ExperimentJobExperimentsReducer, ExperimentJobsReducer } from './experimentJobs';
import {
  ExperimentsParamsReducer,
  experimentsReducer,
  GroupExperimentsReducer,
  ProjectExperimentsReducer
} from './experiments';
import { groupsReducer, ProjectGroupsReducer } from './groups';
import { jobsReducer, ProjectJobsReducer } from './jobs';
import { projectsReducer, UserProjectsReducer } from './projects';

import { AppState } from '../constants/types';
import { activityLogsReducer } from './activityLogs';
import { buildsReducer, ProjectBuildsReducer } from './builds';
import { chartViewsReducer } from './chartViews';
import { codeReferencesReducer } from './codeReferences';
import { healthStatusReducer } from './healthStatus';
import { logsReducer } from './logs';
import { MetricsReducer } from './metrics';
import { modalReducer } from './modal';
import { searchesReducer } from './searches';
import { StatusesReducer } from './statuses';
import { tokenReducer } from './token';
import { userReducer } from './user';

const combinedReducer = combineReducers<AppState>({
  projects: projectsReducer,
  experiments: experimentsReducer,
  experimentsParams: ExperimentsParamsReducer,
  groups: groupsReducer,
  jobs: jobsReducer,
  builds: buildsReducer,
  experimentJobs: ExperimentJobsReducer,
  modal: modalReducer,
  auth: tokenReducer,
  healthStatus: healthStatusReducer,
  users: userReducer,
  // form: formReducer,
  logs: logsReducer,
  statuses: StatusesReducer,
  metrics: MetricsReducer,
  activityLogs: activityLogsReducer,
  searches: searchesReducer,
  chartViews: chartViewsReducer,
  codeReferences: codeReferencesReducer,
});

function SliceReducer(state: AppState, action: Action) {
  return {
    projects: ProjectGroupsReducer(
      ProjectExperimentsReducer(
        ProjectJobsReducer(
          ProjectBuildsReducer(
            state.projects,
            action),
          action),
        action),
      action),
    groups: GroupExperimentsReducer(state.groups, action),
    experiments: ExperimentJobExperimentsReducer(state.experiments, action),
    experimentsParams: state.experimentsParams,
    jobs: state.jobs,
    builds: state.builds,
    experimentJobs: state.experimentJobs,
    modal: state.modal,
    auth: state.auth,
    healthStatus: state.healthStatus,
    users: UserProjectsReducer(state.users, action),
    logs: state.logs,
    statuses: state.statuses,
    metrics: state.metrics,
    activityLogs: state.activityLogs,
    searches: state.searches,
    chartViews: state.chartViews,
    codeReferences: state.codeReferences,
  };
}

function appReducer(state: AppState, action: Action) {
  let _state = combinedReducer(state, action);
  _state = SliceReducer(_state, action);
  return _state;
}

export default appReducer;
