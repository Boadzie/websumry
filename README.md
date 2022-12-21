# Websumry

![websumry](./websumry.webm)

> WebSumry is a powerful tool that helps you quickly summarize the content of a website. With WebSumry, you can easily extract the key points and main ideas from long articles and pages, saving you time and helping you stay informed on the topics that matter to you.

> One of the key features of WebSumry is its advanced algorithm, which uses natural language processing techniques to identify and extract the most important information from a website. This allows you to get a clear and concise summary of the content, without missing any key points.

> In addition to summarizing websites, WebSumry also allows you to customize the length of the summary, so you can get a brief overview or a more detailed summary depending on your needs.

> Overall, WebSumry is a valuable tool for anyone looking to stay informed and save time by quickly and accurately summarizing the content of websites. So, it can be a great help for students, professionals, and anyone else who needs to stay up to date on the latest news and information.

## Prerequisites

Before you can use this project, you will need to have the following software installed preferably in a virtualenv:

- Python 3.10 or higher
- The Sumy library (install with pip install sumy)
- The pycurl library (install with pip install pycurl)
- The Beautiful Soup library (install with pip install bs4)

Create a virtual environment for the project. Then activate it.

```bash
# create a virtual environment for the project
python3 -m ven .myenv

# activate the virtual environment
source .myenv/bin/activate
```

Then install all the dependencies from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

## Usage

To use this project, simply run the summarize_website.py script and pass in the following arguments:

- url: The URL of the website to summarize
- num_sentences: The number of sentences in the summary
- stop_words: A list of words that should be given less weight in the summarization process (optional)
- bonus_words: A list of words that should be given more weight in the summarization process (optional)

run it like this in the project root directory:

```bash
uvicorn app:api --reload
```

This will retrieve the HTML of the website at the specified url, extract the text from the HTML, preprocess the text (optional), and then use the LsaSummarizer to generate a summary of the text consisting of 3 sentences. The stop_words and bonus_words parameters will be used to specify which words should be given less or more weight in the summarization process.

## Customization

You can customize the behavior of the summarization by modifying the parameters of the `Sumy` summarizer object in the summarize_website function. For example, you can change the summarization algorithm by instantiating a different Sumy summarizer object (e.g. LuhnSummarizer, EdmundsonSummarizer). You can also adjust the number of sentences in the summary and the stop and bonus words by modifying the num_sentences, stop_words, and bonus_words parameters.

For more information on the available summarization algorithms and customization options, see the Sumy documentation.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
