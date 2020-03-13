
"use strict";

let InitCircularTrajectory = require('./InitCircularTrajectory.js')
let ResetController = require('./ResetController.js')
let GetWaypoints = require('./GetWaypoints.js')
let IsRunningTrajectory = require('./IsRunningTrajectory.js')
let SetSMControllerParams = require('./SetSMControllerParams.js')
let Hold = require('./Hold.js')
let SwitchToManual = require('./SwitchToManual.js')
let InitWaypointSet = require('./InitWaypointSet.js')
let SwitchToAutomatic = require('./SwitchToAutomatic.js')
let InitHelicalTrajectory = require('./InitHelicalTrajectory.js')
let ClearWaypoints = require('./ClearWaypoints.js')
let GetMBSMControllerParams = require('./GetMBSMControllerParams.js')
let StartTrajectory = require('./StartTrajectory.js')
let GoToIncremental = require('./GoToIncremental.js')
let GetSMControllerParams = require('./GetSMControllerParams.js')
let InitWaypointsFromFile = require('./InitWaypointsFromFile.js')
let AddWaypoint = require('./AddWaypoint.js')
let GoTo = require('./GoTo.js')
let GetPIDParams = require('./GetPIDParams.js')
let SetMBSMControllerParams = require('./SetMBSMControllerParams.js')
let InitRectTrajectory = require('./InitRectTrajectory.js')
let SetPIDParams = require('./SetPIDParams.js')

module.exports = {
  InitCircularTrajectory: InitCircularTrajectory,
  ResetController: ResetController,
  GetWaypoints: GetWaypoints,
  IsRunningTrajectory: IsRunningTrajectory,
  SetSMControllerParams: SetSMControllerParams,
  Hold: Hold,
  SwitchToManual: SwitchToManual,
  InitWaypointSet: InitWaypointSet,
  SwitchToAutomatic: SwitchToAutomatic,
  InitHelicalTrajectory: InitHelicalTrajectory,
  ClearWaypoints: ClearWaypoints,
  GetMBSMControllerParams: GetMBSMControllerParams,
  StartTrajectory: StartTrajectory,
  GoToIncremental: GoToIncremental,
  GetSMControllerParams: GetSMControllerParams,
  InitWaypointsFromFile: InitWaypointsFromFile,
  AddWaypoint: AddWaypoint,
  GoTo: GoTo,
  GetPIDParams: GetPIDParams,
  SetMBSMControllerParams: SetMBSMControllerParams,
  InitRectTrajectory: InitRectTrajectory,
  SetPIDParams: SetPIDParams,
};
