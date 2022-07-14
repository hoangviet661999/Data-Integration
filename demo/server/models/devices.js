const mongoose = require("mongoose");
const Schema = mongoose.Schema;

const deviceSchema = new Schema({
    id: {
        type: String,
    },
    name: {
        type: String,
    },
    price: {
        type: String,
    },
    brand: {
        type: String,
    },
    type:{
        type: String,
    },
    load_size: {
        type: String
    },
    website: {
        type: String
    }
});

deviceSchema.set('timestamps', true);
const device = mongoose.model('devices', deviceSchema);

module.exports = device;