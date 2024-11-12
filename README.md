# ASK2WIKI: Question-Answering from Wikipedia

## Overview

ASK2WIKI is a simple yet powerful app that allows users to ask questions, and it will provide relevant answers by extracting information from Wikipedia articles. The app uses **spaCy** for natural language processing to interpret the question and identify the main topic, then fetches relevant data from Wikipedia for a quick and accurate response.

### Key Features
- **Natural Language Understanding**: Uses **spaCy** to process the question and identify key topics (like people, places, and things).
- **Wikipedia Integration**: Automatically retrieves the most relevant Wikipedia summary for the identified topic.
- **Fast Responses**: Provides a brief answer, summarizing the relevant Wikipedia page in a concise format.
- **User-Friendly Interface**: Simple, clean, and easy-to-use interface built with **Streamlit**.

## How It Works

1. **Ask a Question**: The user can type a question (e.g., "What do you know about Albert Einstein?") in the input field.
2. **Topic Identification**: The app processes the question using **spaCy** to identify the key entity (e.g., "Albert Einstein").
3. **Fetch Answer from Wikipedia**: Once the topic is identified, the app queries Wikipedia and retrieves a short summary of the relevant article.
4. **Display Answer**: The summary is displayed in the app interface as the answer to the user's question.

## Installation

To run this app locally, you'll need Python installed, along with the following libraries:

- **spaCy**: For natural language processing.
- **wikipedia-api**: For fetching Wikipedia content.
- **Streamlit**: For building the interactive web app.

You will also need to install the spaCy language model `en_core_web_sm`.

To install the required dependencies, run the following commands:

```bash
pip install spacy wikipedia-api streamlit
python -m spacy download en_core_web_sm
```

## How to Run

1. Clone or download this repository to your local machine.
2. Save the code in a Python file, for example `ask2wiki.py`.
3. In your terminal, navigate to the directory where the file is saved.
4. Run the Streamlit app with the following command:

```bash
streamlit run ask2wiki.py
```

The app will open in your browser where you can start asking questions.

## Usage

1. **Ask a question**: Type a question into the input box (e.g., "What do you know about Python programming?").
2. **Get an answer**: The app will process your question, find the most relevant Wikipedia article, and display a brief summary.
3. **View response**: The summary from Wikipedia is displayed on the page as the answer to your question.

## Example Output

For the question "What do you know about Albert Einstein?", the output might look like this:

---

**Question**: What do you know about Albert Einstein?

**Answer**:  
*Albert Einstein was a German-born theoretical physicist who developed the theory of relativity, one of the two pillars of modern physics (alongside quantum mechanics). His work is also known for its influence on the philosophy of science. He is best known for his mass–energy equivalence formula E = mc², which has been called "the most famous equation in the world".*

---

## Notes

- The app uses spaCy's dependency parsing to identify the subject of the question (the object of prepositions like "about").
- It fetches a brief summary (4 sentences) from the relevant Wikipedia page using the `wikipedia-api` library.
- The app works best for direct, factual questions related to notable entities (e.g., people, places, historical events).
  
## License

This app is open-source and available for modification under the [MIT License](LICENSE).

---

Made by [CLL](https://github.com/)
