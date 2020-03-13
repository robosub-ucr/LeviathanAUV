
"use strict";

let SetCurrentVelocity = require('./SetCurrentVelocity.js')
let GetCurrentModel = require('./GetCurrentModel.js')
let TransformFromSphericalCoord = require('./TransformFromSphericalCoord.js')
let GetOriginSphericalCoord = require('./GetOriginSphericalCoord.js')
let SetCurrentModel = require('./SetCurrentModel.js')
let TransformToSphericalCoord = require('./TransformToSphericalCoord.js')
let SetOriginSphericalCoord = require('./SetOriginSphericalCoord.js')
let SetCurrentDirection = require('./SetCurrentDirection.js')

module.exports = {
  SetCurrentVelocity: SetCurrentVelocity,
  GetCurrentModel: GetCurrentModel,
  TransformFromSphericalCoord: TransformFromSphericalCoord,
  GetOriginSphericalCoord: GetOriginSphericalCoord,
  SetCurrentModel: SetCurrentModel,
  TransformToSphericalCoord: TransformToSphericalCoord,
  SetOriginSphericalCoord: SetOriginSphericalCoord,
  SetCurrentDirection: SetCurrentDirection,
};
