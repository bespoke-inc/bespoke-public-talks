# Building a Scalable AI Chatbot: From Regext to Deep Learning

Dialogue systems use a variety of mechanisms to carryout informative and coherent conversations withtheir users.   These conversations can be achieved through rule-basd,  template-based, retrieval-based approaches or in a data-driven manner that teaches the agent to learn from raw conversational data. This workshop will focus on the retreival-based method.

## Retreival-Based Chatbot
A retrieval-based agent or chatbot retrieves related responses from queries in the corpus that are similar to the given query.  We are not interested in generating a new response, but select the most suitable response (originally made to other queries) as reply to the current query. We will try to do this by having a set of questions with labelled intents and then try to classify the intent.

### Accessing Colab

- Sign in to your Google account.
- Access the [Colab Welcome Page](https://colab.research.google.com/notebooks/welcome.ipynb#recent=true) and click on ‘Github’. In the ‘Enter a GitHub URL or search by organization or user’ line enter `https://github.com/bespoke-inc/bespoke-public-talks`. We will be using the notebook in folder `2020/2020-10-31-ScipyJapan-Regex-to-DL`
- You need to tell Colab that you are interested in using a GPU. You can do this by clicking on the `Runtime` tab and selecting `Change runtime type`. A pop-up window will appear. Select `GPU` from the menu and `Save`.
- Save your work to Google Drive by clicking on ‘File’ and then ‘Save’ and then `SAVE A COPY IN DRIVE.` in the pop-up.

### Installing Dependencies
```
#install the necessary dependencies by running the following commands on a notebook cell:
!wget https://raw.githubusercontent.com/bespoke-inc/bespoke-public-talks/2020/2020-10-31-ScipyJapan-Regex-to-DL/requirements.txt
!pip install -r requirements.txt
```

### Tutorial Outline:
- Introduction to retrieval-based chatbot technology and architecture and Conversation design (30 min)
- Break
- Code a basic retrieval-based chatbot
    - Exercise: Create a simple dataset for a domain of your choice with a few sample conversations
    - Simple approaches:
        - Using regular expressions to identify user intent
        - Using string matching to identify user intent
        - Switching to ML:
            - Using Naive Bayes to classify intent
            - Using Language Model to classify intent
    - Exercise: Code your own chatbot with the data you created in the previous excercise
- Break
- Digging deeper into Language Models
- Break
- Addditional features that make a better UX
    - Answering "I don't know"
    - Excercise: add ability to answer unknown in your bot
    - Disambiguate between intents
    - Excercise: add disambiguation ability in your bot
    - Typos and Extracting Parameters (10 min)
    - Excercise: add typo correction in your bot
    - Generalizing your training data with entity classes
    - Excercise: Add named entities to one intent and make a recognizer
- Break
- Metrics to measure performance of your chatbot
- Summary and Further topics
