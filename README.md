# Software Engineering for Machine Learning Assignment

Please consult the [homework assignment PDF](https://web2.qatar.cmu.edu/cs/17313/homework/hw4.pdf) for full context and instructions for this code.  

<b> API Description: </b>

This API is a flask-based microservice developed for the purpose of speeding up the admissions process at CMU. The API uses student academic details to predict if the student 
would be considered a “high-quality student” by CMU or not. For reference, CMU defines a “high-quality student” as a student that achieved a final period grade (i.e. G3) of 
15 or higher out of 20.

The API expects 3 inputs -  G1, G2 and absences -  all of data type integers. For G1 and G2, the API is expecting an integer ranging from 0 to 20 while for absences, the 
range is from 0 to 93. 

For input parameters clarifications: <br>
G1: grade achieved in first period <br>
G2: grade achieved in second period <br>
Absences: number of school absences 

Once a prediction is made, the API will return either 0 or 1. A “0” indicates that the API predicts that the student with the input details doesn’t qualify as a “high-
quality” student for CMU, while a “1” indicates that the API predicts the student to be a “high-quality” student.

The API can take a single query or multiple queries. For a single query input, the API outputs a single integer “0” or “1” according to the description above. For multiple 
queries input, the API outputs an array of 0’s and 1’s corresponding to the predictions of each input query, where the value at index i in the output array corresponds to the 
prediction for the student with input query i.

<br />
<b> Features and Model Evaluation: </b>

The features chosen for training this model from the student performance data set are “G1”, “G2” and “absences”. These features were chosen as they are believed to be good 
indicators of student performance, grade progress and commitment level which directly correlate to students’ final third period grade “G3” and consequently, their prediction 
for whether they are a “high-quality student” for CMU or not.

This retrained model performs better than the baseline model in terms of the accuracy of its predictions, as evaluated by the f1_score of the model which measures model 
prediction accuracy. As the below screenshot shows, the calculated f1_score of this retrained model on the training data is 0.972 (97.2% accuracy), compared to the baseline 
model’s 0.5 (50% accuracy).

![image 1](https://github.com/NadaSolimann/Bug-Busters-hw4/blob/main/Screenshot_1.png)


Even upon randomly splitting the data set into training and testing sets (using 80/20 splitting) for cross validation, this retrained model achieves an f1_score still higher 
than the baseline’s f1_score of 0.5. Upon 10 cross validation runs, this retrained model achieves an average f1_score of 0.938, compared to the old model’s 0.099 [see code 
snippets below].

The retrained model also proved more consistent in its accuracy scores when cross validating. Despite the random re-splitting of the training and testing data in the cross 
validation runs, the retrained model experienced less variation and more consistent f1_scores than the old model. Particularly, for the 10 cross-validation runs done, the 
retrained model’s scores were closer in value with a maximum difference of 0.14, compared to a maximum difference of 0.21 in f1_scores for the baseline model [see code 
snippets below]. This implies that the retrained model is more reliable and more generalizable as it has less data-dependent deviations in accuracy.





Retrained model scores upon 10 cross validation runs:
![image 2](https://github.com/NadaSolimann/Bug-Busters-hw4/blob/main/Screenshot_2.png)


Old model scores upon 10 cross validation runs:
![image 3](https://github.com/NadaSolimann/Bug-Busters-hw4/blob/main/Screenshot_3.png)

However, it is worth noting that the retrained model may not be as insightful as the baseline model is in terms of establishing relationships between students’ attributes and 
their performance. This is because this model significantly relies on the obvious features of “G1” and “G2” for indicating the “G3” performance of a student, as opposed to 
the baseline model which relies on other non-grade related features.

<br />
<b> Deployment Instructions: </b> <br>
Below are the instructions for how to deploy the API model:

Navigate to the dockerfile directory and execute the following command to build the docker container:

    docker build -t ml:latest .

Execute the following command to run the docker container:

    docker run -d -p 5000:5000 ml

Then, run the following curl command with the input parameters values for G1, G2 and absences of the student. In the example command below, the query describes a student with 
first period grade “G1” of 6, second period grade “G2” of 8 and 5 total absences. This should output the prediction for whether the student is a “high quality” student for 
CMU or not.

    curl "http://localhost:5000/predict?G1=6&G2=8&absences=5"

<br />
<b> Test Plan: </b>

The main method used for testing the microservice model was cross-validation. The original data set (student-mat.csv) was split randomly into two sets, the training set and the testing set. It was configured so that 80% of the data was used for training and the remaining 20% was used for testing. The testing was done automatically using the metrics module from the sklearn library which auto-calculated an accuracy score for the model (f1_score). Although this method of testing resulted in a lower accuracy percentage than the original method of testing the trained data, we believe that our method provides a more meaningful model accuracy measurement since it tests on unseen data.
