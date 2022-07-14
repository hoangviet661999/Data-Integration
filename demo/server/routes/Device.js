const express = require("express");
const deviceController = require("../controllers/Device");
const router = express.Router();
const {asyncWrapper} = require("../utils/asyncWrapper");

router.get("/", (req, res) => {
    res.send({ response: "Server is up and running." }).status(200);
});

router.post("/device-list", asyncWrapper(deviceController.list))
router.post("/get-total", asyncWrapper(deviceController.total))
router.post("/device-filter", asyncWrapper(deviceController.filter))
  
module.exports = router;