
"use strict";

let InitCircularTrajectory = require('./InitCircularTrajectory.js')
let GetPIDParams = require('./GetPIDParams.js')
let SwitchToAutomatic = require('./SwitchToAutomatic.js')
let SetPIDParams = require('./SetPIDParams.js')
let GoTo = require('./GoTo.js')
let ResetController = require('./ResetController.js')
let InitHelicalTrajectory = require('./InitHelicalTrajectory.js')
let GoToIncremental = require('./GoToIncremental.js')
let Hold = require('./Hold.js')
let ClearWaypoints = require('./ClearWaypoints.js')
let GetMBSMControllerParams = require('./GetMBSMControllerParams.js')
let GetSMControllerParams = require('./GetSMControllerParams.js')
let InitWaypointsFromFile = require('./InitWaypointsFromFile.js')
let IsRunningTrajectory = require('./IsRunningTrajectory.js')
let SetSMControllerParams = require('./SetSMControllerParams.js')
let InitRectTrajectory = require('./InitRectTrajectory.js')
let InitWaypointSet = require('./InitWaypointSet.js')
let SetMBSMControllerParams = require('./SetMBSMControllerParams.js')
let GetWaypoints = require('./GetWaypoints.js')
let StartTrajectory = require('./StartTrajectory.js')
let AddWaypoint = require('./AddWaypoint.js')
let SwitchToManual = require('./SwitchToManual.js')

module.exports = {
  InitCircularTrajectory: InitCircularTrajectory,
  GetPIDParams: GetPIDParams,
  SwitchToAutomatic: SwitchToAutomatic,
  SetPIDParams: SetPIDParams,
  GoTo: GoTo,
  ResetController: ResetController,
  InitHelicalTrajectory: InitHelicalTrajectory,
  GoToIncremental: GoToIncremental,
  Hold: Hold,
  ClearWaypoints: ClearWaypoints,
  GetMBSMControllerParams: GetMBSMControllerParams,
  GetSMControllerParams: GetSMControllerParams,
  InitWaypointsFromFile: InitWaypointsFromFile,
  IsRunningTrajectory: IsRunningTrajectory,
  SetSMControllerParams: SetSMControllerParams,
  InitRectTrajectory: InitRectTrajectory,
  InitWaypointSet: InitWaypointSet,
  SetMBSMControllerParams: SetMBSMControllerParams,
  GetWaypoints: GetWaypoints,
  StartTrajectory: StartTrajectory,
  AddWaypoint: AddWaypoint,
  SwitchToManual: SwitchToManual,
};
