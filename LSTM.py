from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
from keras.preprocessing.sequence import TimeseriesGenerator
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import numpy as np
import os


def calculate_predict(task_id, filename, prediction_step, results):
    scaler = MinMaxScaler()
    extension = (filename.split("."))[1]
    if extension == "csv":   
        df = pd.read_csv(filename)
    elif (extension == "xlsx") or (extension == "xls"):
        df = pd.read_excel(filename)
    prediction_step = int(prediction_step)
    print("Filename" + filename) 
    scaler = MinMaxScaler()
    df.Month = pd.to_datetime(df.Month)
    rows_list = []
    end_month =df.Month[len(df.Month)-1]
    for i in range(1, prediction_step):
        df.loc[len(df)] = [end_month+pd.DateOffset(months=i), 0]
    df = df.set_index("Month")
    df.index.freq = 'MS'
    train_size = int(len(df) * 0.50)
    train, test = df[0:train_size], df[train_size:]
    scaler.fit(train)
    scaled_train_data = scaler.transform(train)
    scaled_test_data = scaler.transform(test)


    n_input = 12
    n_features= 1
    generator = TimeseriesGenerator(scaled_train_data, scaled_train_data, length=n_input, batch_size=1)

    lstm_model = Sequential()
    lstm_model.add(LSTM(200, activation='relu', input_shape=(n_input, n_features)))
    lstm_model.add(Dense(1))
    lstm_model.compile(optimizer='adam', loss='mse')

    #lstm_model.summary()

    lstm_model.fit_generator(generator,epochs=20)
    losses_lstm = lstm_model.history.history['loss']

    lstm_predictions_scaled = list()

    batch = scaled_train_data[-n_input:]
    current_batch = batch.reshape((1, n_input, n_features))

    for i in range(len(test)):   
        lstm_pred = lstm_model.predict(current_batch)[0]
        lstm_predictions_scaled.append(lstm_pred) 
        current_batch = np.append(current_batch[:,1:,:],[[lstm_pred]],axis=1)

    lstm_predictions = scaler.inverse_transform(lstm_predictions_scaled)

    test[test['Sales']==0] = np.nan
    test['Predictions'] = lstm_predictions
    print(test)
    test['Sales'].plot(figsize = (16,5), legend=True)
    test['Predictions'].plot(legend = True)
    #pyplot.xlim(left=0.3)
    #pyplot.show()
    strFile = './results/' + task_id + ".png"
    print(strFile)
    if os.path.isfile(strFile):
        os.remove(strFile)    
        #os.system("rm "+strFile)
    pyplot.savefig(strFile)
    pyplot.clf()    
    for i in range(0, len(results)):
        if task_id == results[i]['task_id']:
            index = i
            break
    print("Task id: " + results[index]['task_id'])            
    results[index]['status'] = True