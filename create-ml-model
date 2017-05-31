let AWS = require("aws-sdk");
let MachineLearning = new AWS.MachineLearning();

exports.handler = (event, context, callback) => {
    let s3Object = event.Records[0].s3;
    
    console.log(`s3://${s3Object.bucket.name}/${s3Object.object.key}`);
    //TODO: schema should be not like that
    let request = {
        DataSourceId: `${s3Object.object.eTag}${new Date().getTime()}`,
        DataSourceName: s3Object.object.eTag,
        ComputeStatistics: true,
        DataSpec: {
            DataLocationS3: `s3://${s3Object.bucket.name}/${s3Object.object.key}`,
            DataSchema: JSON.stringify({
              "version" : "1.0",
              "rowId" : null,
              "rowWeight" : null,
              "targetAttributeName" : "_Target_",
              "dataFormat" : "CSV",
              "dataFileContainsHeader" : false,
              "attributes" : [ {
                "attributeName" : "Var01",
                "attributeType" : "NUMERIC"
              }, {
                "attributeName" : "Var02",
                "attributeType" : "CATEGORICAL"
              }, {
                "attributeName" : "Var03",
                "attributeType" : "CATEGORICAL"
              }, {
                "attributeName" : "Var04",
                "attributeType" : "CATEGORICAL"
              }, {
                "attributeName" : "Var05",
                "attributeType" : "CATEGORICAL"
              }, {
                "attributeName" : "Var06",
                "attributeType" : "CATEGORICAL"
              }, {
                "attributeName" : "Var07",
                "attributeType" : "CATEGORICAL"
              }, {
                "attributeName" : "Var08",
                "attributeType" : "CATEGORICAL"
              }, {
                "attributeName" : "Var09",
                "attributeType" : "CATEGORICAL"
              }, {
                "attributeName" : "Var10",
                "attributeType" : "CATEGORICAL"
              }, {
                "attributeName" : "Var11",
                "attributeType" : "NUMERIC"
              }, {
                "attributeName" : "Var12",
                "attributeType" : "NUMERIC"
              }, {
                "attributeName" : "Var13",
                "attributeType" : "NUMERIC"
              }, {
                "attributeName" : "Var14",
                "attributeType" : "NUMERIC"
              }, {
                "attributeName" : "Var15",
                "attributeType" : "CATEGORICAL"
              }, {
                "attributeName" : "Var16",
                "attributeType" : "NUMERIC"
              }, {
                "attributeName" : "Var17",
                "attributeType" : "NUMERIC"
              }, {
                "attributeName" : "Var18",
                "attributeType" : "NUMERIC"
              }, {
                "attributeName" : "Var19",
                "attributeType" : "NUMERIC"
              }, {
                "attributeName" : "Var20",
                "attributeType" : "NUMERIC"
              }, {
                "attributeName" : "_Target_",
                "attributeType" : "BINARY"
              } ],
              "excludedAttributeNames" : [ ]
            })
        }
    }
    
    MachineLearning.createDataSourceFromS3(request, (err, data) => {
        if(err) {
            callback(err, err.toString());
        }
        
        let params = {
            MLModelId: "myMLModel", 
            MLModelName: "myMLModel", 
            MLModelType: "BINARY", 
            TrainingDataSourceId: data.DataSourceId
        };
        
        console.log(params);
        
        MachineLearning.createMLModel(params, (err, data) => {
            if(err) {
                callback(err, err.toString());
            }
            callback(null, data);    
        });
    });
    
};
