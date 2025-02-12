const asyncHandler = require("express-async-handler");
const Fabric = require("../models/fabricSchema"); // Adjust path as needed


// @desc Compare fabrics by names
// @route GET /api/fabrics/compare/:fabricNames
// @access Public
const compareFabricsByName = asyncHandler(async (req, res) => {
  const fabricNames = decodeURIComponent(req.params.fabricNames).split(",").map(name => name.trim()); // Clean and split names

  // Fetch fabrics that match the given names
  const fabrics = await Fabric.find({ FabricName: { $in: fabricNames } });

  if (!fabrics || fabrics.length === 0) {
    res.status(404);
    throw new Error("No fabrics found with the specified names");
  }

  // Identify requested names that were not found
  const foundNames = fabrics.map(fabric => fabric.FabricName);
  const missingNames = fabricNames.filter(name => !foundNames.includes(name));

  res.status(200).json({ fabrics, missingNames });
});


// @desc Get fabric by name
// @route GET /api/fabrics/name/:fabricName
// @access Public
const getFabricByName = asyncHandler(async (req, res) => {
  const fabricName = decodeURIComponent(req.params.fabricName);

  const fabric = await Fabric.findOne({ FabricName: fabricName });

  if (!fabric) {
    res.status(404);
    throw new Error("Fabric not found with the specified name");
  }

  res.status(200).json(fabric);
});

// @desc Get fabrics by type
// @route GET /api/fabrics/type/:fabricType
// @access Public
const getFabricsByType = asyncHandler(async (req, res) => {
  const fabricType = decodeURIComponent(req.params.fabricType);

  const fabrics = await Fabric.find({ FabricType: fabricType });

  if (!fabrics || fabrics.length === 0) {
    res.status(404);
    throw new Error("No fabrics found with the specified type");
  }

  res.status(200).json(fabrics);
});

// @desc Get fabrics by durability
// @route GET /api/fabrics/durability/:durability
// @access Public
const getFabricsByDurability = asyncHandler(async (req, res) => {
  const durability = decodeURIComponent(req.params.durability);

  const fabrics = await Fabric.find({ Durability: durability });

  if (!fabrics || fabrics.length === 0) {
    res.status(404);
    throw new Error("No fabrics found with the specified durability");
  }

  res.status(200).json(fabrics);
});

// @desc Get fabrics by texture
// @route GET /api/fabrics/texture/:texture
// @access Public
const getFabricsByTexture = asyncHandler(async (req, res) => {
  const texture = decodeURIComponent(req.params.texture);

  const fabrics = await Fabric.find({ Texture: texture });

  if (!fabrics || fabrics.length === 0) {
    res.status(404);
    throw new Error("No fabrics found with the specified texture");
  }

  res.status(200).json(fabrics);
});

// @desc Get fabrics by best use
// @route GET /api/fabrics/best-use/:use
// @access Public
const getFabricsByBestUse = asyncHandler(async (req, res) => {
  const use = decodeURIComponent(req.params.use);

  const fabrics = await Fabric.find({ BestUse: { $in: [use] } }); // Check if `use` is in the `BestUse` array

  if (!fabrics || fabrics.length === 0) {
    res.status(404);
    throw new Error("No fabrics found for the specified use");
  }

  res.status(200).json(fabrics);
});

module.exports = {
  getFabricByName,
  getFabricsByType,
  getFabricsByDurability,
  getFabricsByTexture,
  getFabricsByBestUse,
  compareFabricsByName
};
