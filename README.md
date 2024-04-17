# Int-Reg-Assist

Intelligent Guidance Assistance in Outpatient Department Registration. For this project, the following are what we have done:

- Collecting information about the main sites of common diseases, clinical symptoms, and the correct consultation departments.
- Using natural language processing techniques to categorize the terminological symptoms into a number of patient-perceivable and judicious discomfort
- Using them as feature attributes of the decision tree, and each disease and each patient is vectorized with the help of their values on these feature attributes
- Using cosine similarity is used to realize approximate Bayes inference.
- The algorithm design for Q&A logic generation using C4.5 Decision Tree Algorithm for dynamic decision tree construction.

- ## Installation

clone:
```
$ git clone https://github.com/SlInevitable2003/Int-Reg-Assist.git
$ cd Int-Reg-Assist
```
create & active virtual enviroment then install dependencies:
```
$ python3 -m venv env  # use `python ...` on Windows
$ source env/bin/activate  # use `env\Scripts\activate` on Windows
(env) $ pip install -r requirements.txt
```

init database and run:
```
(env) $ flask initdb
(env) $ flask run
* Running on http://127.0.0.1:5000/
