const mongoose = require("mongoose");

const fabricSchema = mongoose.Schema(
  {
    FabricName: {
      type: String,
      required: [true, "Please provide the name of the fabric"],
    },
    FabricType: {
      type: String,
      required: [true, "Please specify the fabric type"],
      enum: [
        "Natural Fiber",
        "Synthetic Fiber",
        "Natural Fiber Blend",
        "Semi-Synthetic Fiber",
        "Natural/Synthetic",
      ],
    },
    Durability: {
      type: String,
      required: [true, "Please specify the durability"],
      enum: ["High", "Moderate", "Low"],
    },
    Texture: {
      type: String,
      required: [true, "Please specify the texture"],
      enum: ["Rough", "Smooth", "Soft"],
    },
    BestUse: {
      type: [String], // Array of best-use descriptions
      required: [true, "Please specify the best use cases"],
    },
  },
  {
    timestamps: true, // Automatically manage createdAt and updatedAt fields
  }
);

module.exports = mongoose.model("fabricDetails", fabricSchema);
