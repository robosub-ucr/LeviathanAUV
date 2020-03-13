
"use strict";

let Salinity = require('./Salinity.js');
let DVL = require('./DVL.js');
let PositionWithCovariance = require('./PositionWithCovariance.js');
let PositionWithCovarianceStamped = require('./PositionWithCovarianceStamped.js');
let DVLBeam = require('./DVLBeam.js');
let ChemicalParticleConcentration = require('./ChemicalParticleConcentration.js');

module.exports = {
  Salinity: Salinity,
  DVL: DVL,
  PositionWithCovariance: PositionWithCovariance,
  PositionWithCovarianceStamped: PositionWithCovarianceStamped,
  DVLBeam: DVLBeam,
  ChemicalParticleConcentration: ChemicalParticleConcentration,
};
