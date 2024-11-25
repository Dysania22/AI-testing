# Installation Instructions:

These installation instructions operate from the presumption that you could theoretically open a simple python file in an IDE and run it. 
So this will not walk you through installing python and more fundamental procedures.
A video walk-through of the project setup, use, and logic is available at https://youtu.be/NsKPs1MHpD4.

Clone git repo into IDE of choice. 
This is best done by opening a new project from Version Control in Pycharm or VisualStudio.
But you can always do it from the terminal with the command below. 

    git clone https://github.com/Dysania22/AI-testing

Your IDE may prompt you to install these dependencies on its own. 
This is likely to happen when you configure the interpreter/create a virtual environment. 
If not, the following pip install commands should be sufficient. 
I _really_ recommend that you initiate a virtual environment if prompted.
However, you can always pip install each dependency if you so desire.

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

# Usage instructions:

The project will load a web page. 
In the Keyword Search, input a **short** keyword search like would be commonly used in a google patents search.
In the Longer Holistic Query blank, input at least a sentence or so that you think is emblematic of what you are really looking for. 
The longer query should be more complicated than the keyword query. 
The longer and more detailed the better. 

Here is a sample query:

    Keyword Search: steam wand
    Longer Holistic Query: espresso machine steam wand with automatic temperature sensing and adjustable temperature and froth levels

That should produce a result like this:

<img width="930" alt="image" src="https://github.com/user-attachments/assets/2863cb0d-5bcf-43b2-9df0-59ff331a44da">

Note that these results may take up to 20 minutes to load. 
If the page loads very quickly upon pressing search, but only loads the table headings, then the webpage is just running a little slow.
Just press search again and it usually works fine. The pains of loading individual webpages instead of just using patent retrieval APIs. 
