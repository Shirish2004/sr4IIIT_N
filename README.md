# Speech Recognition for EMR

The deep Learning Model Classifies 10 word sounds namely "yes","no","on","off","up","down","right","left","stop","go" using Conv1D Neural Netwrok 

The Model achieved a validation accuracy of 84% and training accuracy of 89%. The model is somewhat overfitting but that could be reduced by using techniques like oversampling etc for the unbalanced classes.

Following method can be directly used to load the model and use it for further purpose. This process is also called tranfer learning. Using Transfer learning one can also fine tune the weights and come out with a better verison 

from keras.models import load_model

path="path to the saved model"

model=load_model(path)

model.summary()

## GUI

The intent of the project was to create an electronic medical record that does not require doctors to manually type in the data, which can save a lot of time usually consumed before checking the patient. The objective was to leverage the power of Deep Learning and methodologies like transfer learning to create a robust mechanism. However, due to constraints obtained during the data collection, as it was just after the COVID era, the leveraging idea is left to be discovered in the future. For the current instance, the use of Google speech recognition API is being done to make the mechanism robust in its own way. The limitations the project faces lie in the domain of pronunciation, timeout, and better deployability. Any opportunities to further explore it and contributions are welcomed whole heartedly.
