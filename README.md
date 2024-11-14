Installation Instructions:
Clone git repo into IDE of choice.

pip install contents of requirements.txt. 
Your IDE may prompt you to install these dependencies on its own. This is likely to happen when you configure the interpreter. If not, the following pip install commands should be sufficient.

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

At this point you should be able to run the program by running app.py



