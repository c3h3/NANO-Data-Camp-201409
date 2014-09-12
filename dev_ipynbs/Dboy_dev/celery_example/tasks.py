from __future__ import absolute_import

from predict_test_celery.celery import app

try:
    import cPickle as pickle
except:
    import pickle
import blz, os
import numpy as np

@app.task
def modelPredictor(modelsPath_modelIndex_dataPath_colNames_tuple):
    """
    Input: A tuple, with following two attributes (with order):
            modelsPath: string, the path to the trained models. (pickle file)
            modelIndex: integer, the index of the model to predict.
            dataPath: string, the path to the data.
            colNames: a list of strings, column names of the output table. It should be like ["Id", "V1", ...]
    Output: A btable, consists of Id column, Predicted column and the data.
    
    Notes:
    modelPredictor will create following directories for you if they do not exist.
            1. Model_No{modelIndex}_predicted_array: it will be under the dataPath.
    """
    # Set up necessary constance.
    divideN = 300000
    modelsPath, modelIndex, dataPath, colNames = modelsPath_modelIndex_dataPath_colNames_tuple
    def data_abspath(colname):
        return os.path.abspath(os.path.join(dataPath, colname))
    with open(modelsPath, "rb") as rf:
        models = pickle.load(rf)
    model = models[modelIndex]
    del models
    
    # Read in data with btable.
    Id = blz.open(os.path.join(dataPath, colNames[0]))
    totalN = len(Id)
    if totalN % divideN == 0:
        nodes_list = [i * divideN for i in range(totalN / divideN + 1)]
    else:
        nodes_list = [i * divideN for i in range(totalN / divideN + 1)] + [totalN]
    nodes_pair_list = zip(nodes_list[:-1], nodes_list[1:])
    
    # Prediction.
    y_predict = np.zeros(totalN)
    print "[Model No.{modelIndex}] Prediction process begins.".format(modelIndex = modelIndex)
    for begin, end in nodes_pair_list:
        print "[Model No.{modelIndex}] Processing {begin} ~ {end} observations.".format(modelIndex=modelIndex, begin = begin + 1, end = end)
        columns = [blz.open(os.path.join(dataPath, colname))[begin:end] for colname in colNames[1:]]
        X = np.column_stack(columns)
        temp = model.predict(X)
        y_predict[begin:end] = temp
    
    columns = [Id, blz.barray(y_predict)]
    data_rootdir = os.path.join(dataPath, "Model_No{modelIndex}_predicted_array".format(modelIndex = modelIndex))
    if data_rootdir in os.listdir(dataPath):
        print "Removing Old result_table directory for new btable."
        command = "rm -rf " + data_rootdir
        os.system(command)
    final_table = blz.btable(columns = columns, names = ["Id", "Predict"], rootdir = data_rootdir)
    print "The result_table btable rootdir is under {path}".format(path=data_rootdir)
