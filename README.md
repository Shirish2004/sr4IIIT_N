# Speech Recognition for EMR

The deep Learning Model Classifies 10 word sounds namely "yes","no","on","off","up","down","right","left","stop","go" using Conv1D Neural Netwrok 

The Model achieved a validation accuracy of 84% and training accuracy of 89%. The model is somewhat overfitting but that could be reduced by using techniques like oversampling etc for the unbalanced classes.

Following method can be directly used to load the model and use it for further purpose. This process is also called tranfer learning. Using Transfer learning one can also fine tune the weights and come out with a better verison 

from keras.models import load_model

path="path to the saved model"

model=load_model(path)

model.summary()
