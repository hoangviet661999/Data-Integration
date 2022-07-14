const DeviceModel = require('../models/devices')

const deviceController = {}

deviceController.list = async (req, res, next) => {
    try {
        const { page } = req.body

        if (page === undefined || page === null) {
            const deviceList = await DeviceModel.find()
            return res.status(200).json({
                soLuong: deviceList.length,
                deviceList: deviceList
            })
        }

        else {
        const deviceList = await DeviceModel.find().skip((page-1)*20).limit(20)
        return res.status(200).json({
            soLuong: deviceList.length,
            deviceList: deviceList
        })
        }
    }
    catch (e) {
        return res.status(500).json({
            message: e.message
        });
    }
}

deviceController.total = async (req, res, next) => {
    try {
        const count = await DeviceModel.countDocuments()
        return res.status(200).json({
            soLuong: count
        })

    }
    catch (e) {
        return res.status(500).json({
            message: e.message
        });
    }
}


deviceController.search = async (req, res, next) => {
    try {
        const device = await DeviceModel.findById(req.params.id)
        return res.status(200).json({
            device: device
        })
    }
    catch (e) {
        return res.status(500).json({
            message: e.message
        });
    }
}

deviceController.filter = async (req, res, next) => {
    try {
        let {
            name,
            brand,
            minPrice,
            maxPrice,
            type,
            loadSize,
            page
        } = req.body

        if (brand === undefined || brand === null) brand = ''
        if (type === undefined || type=== null) type = ''
        if (loadSize === undefined || loadSize === null) loadSize = ''

        if (page === undefined || page === null) {
        let deviceList = await DeviceModel.find(
            { 
            name: { "$regex": name || "", "$options": "i"},
            //price: {$lte: maxPrice || 1000000000, $gte: minPrice || 0},
            brand: { "$regex": brand || "", "$options": "i"},
            load_size: { "$regex": loadSize || "", "$options": "i"},
            type: { "$regex": type || "", "$options": "i"},
            }
            )

        return res.status(200).json({
            soLuong: deviceList.length,
            deviceList: deviceList
        })
        } else {
            let deviceList = await DeviceModel.find(
                { 
                name: { "$regex": name || "", "$options": "i"},
                //price: {$lte: maxPrice || 1000000000, $gte: minPrice || 0},
                brand: { "$regex": brand || "", "$options": "i"},
                load_size: { "$regex": loadSize || "", "$options": "i"},
                type: { "$regex": type || "", "$options": "i"},
                }
                ).skip((page-1)*20).limit(20)
    
            return res.status(200).json({
                soLuong: deviceList.length,
                deviceList: deviceList
            })
        }
    } catch (e) {
        return res.status(500).json({
            message: e.message
        });
    }
}

module.exports = deviceController