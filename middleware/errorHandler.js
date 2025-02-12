const {constants} = require("../routes/constants");
const errorHandler = (err,req,res,next) => {
    const statuscode = res.statuscode ? res.statuscode :500;
    switch(statuscode) {
        case constants.NOT_FOUND:
            res.json({title:"not found",message:err.message,stackTrace:err.stack});
            break;
        case constants.VALIDATION_EROOR:
            res.json({title:"validation failed",message:err.message,stackTrace:err.stack});
            break;
        case constants.FORBIDDEN:
                res.json({title:"forbidden",message:err.message,stackTrace:err.stack});
                break;
        case constants.UNAUTHORIZED:
                res.json({title:"unauthorized",message:err.message,stackTrace:err.stack});
                    break;
        case constants.SERVER_ERROR:
                res.json({title:"server error",message:err.message,stackTrace:err.stack});
                break;
        default:
            console.log("no error");
            break;
    }

};
module.exports=errorHandler;