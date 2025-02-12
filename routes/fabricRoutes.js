const express = require("express");
const router = express.Router();
const {getFabricByName, getFabricsByType, compareFabricsByName,getFabricsByDurability,getFabricsByTexture,getFabricsByBestUse }= require("../controllers/fabricController.js");



router.route("/name/:fabricName").get(getFabricByName);

// Route to get fabrics by type
router.route("/type/:fabricType").get(getFabricsByType);

// Route to get fabrics by durability
router.route("/durability/:durability").get(getFabricsByDurability);

// Route to get fabrics by texture
router.route("/texture/:texture").get(getFabricsByTexture);

// Route to get fabrics by best use
router.route("/best-use/:use").get(getFabricsByBestUse);
router.route("/compare/:fabricNames").get(compareFabricsByName);
module.exports = router;

