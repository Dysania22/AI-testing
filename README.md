Installation Instructions:

These installation instructions operate from the presumption that you could theoretically open a python file in an IDE and run it. So this will not walk you through installing python and more fundamental procedures.

Clone git repo into IDE of choice. This is best done by opening a new project from Version Control in Pycharm or VisualStudio

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

At this point you should be able to run the program by running app.py/running the flask project. 

Usage instructions:

The project will load a web page. 
In the Keyword Search, input a short keyword search like would be commonly used in a google patents search.
In the Longer Holistic Query blank, input a sentence or so that you is emblematic of what you are really looking for. 
Something more complicated.

Here is a sample query:

    Keyword Search: steam wand
    Longer Holistic Query: espresso machine steam wand with automatic temperature sensing and adjustable temperature and froth levels

That should produce a result like this:

<img width="930" alt="image" src="https://github.com/user-attachments/assets/2863cb0d-5bcf-43b2-9df0-59ff331a44da">

Note that these results may take up to 20 minutes to load. 
If the page loads very quickly upon pressing search, but only load the table headings, then the webpage is just running a little slow.
Just press search again and it usually works fine. The pains of loading individual webpages instead of just using patent retrieval APIs. 
