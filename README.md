Installation Instructions:
Clone git repo into IDE of choice.

    git clone https://github.com/Dysania22/AI-testing

pip install contents of requirements.txt. 
Your IDE may prompt you to install these dependencies on its own. 
This is likely to happen when you configure the interpreter/create a virtual environment. 
If not, the following pip install commands should be sufficient. 
I really recommend that you initiate a virtual environment if prompted.

    pip install flask
    pip install pandas
    pip install scikit_learn
    pip install selenium
    pip install spacy
    pip install torch
    pip install transformers
    pip install webdriver_manager

spaCy will still need the specific model downloaded.
So we can run either of the following two commands:

    python -m spacy download en 
    python -m spacy download en_core_web_sm

If you run repeatedly into the en_core_web_sm error, close your IDE and restart.
If you still run into problems, contact me via email. 

At this point you should be able to run the program by running app.py



