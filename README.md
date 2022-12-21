# Websumry

> This project uses the Sumy library to extract a summary of the text on a website.

## Prerequisites

Before you can use this project, you will need to have the following software installed:

- Python 3.6 or higher
- The Sumy library (install with pip install sumy)
- The requests library (install with pip install requests)
- The Beautiful Soup library (install with pip install - beautifulsoup4)

## Usage

To use this project, simply run the summarize_website.py script and pass in the following arguments:

- url: The URL of the website to summarize
- num_sentences: The number of sentences in the summary
- stop_words: A list of words that should be given less weight in the summarization process (optional)
- bonus_words: A list of words that should be given more weight in the summarization process (optional)

For example:

```bash
python summarize_website.py --url http://www.example.com --num_sentences 3 --stop_words the a an --bonus_words important
```

This will retrieve the HTML of the website at the specified url, extract the text from the HTML, preprocess the text (optional), and then use the LsaSummarizer to generate a summary of the text consisting of 3 sentences. The stop_words and bonus_words parameters will be used to specify which words should be given less or more weight in the summarization process.

## Customization

You can customize the behavior of the summarization by modifying the parameters of the `Sumy` summarizer object in the summarize_website function. For example, you can change the summarization algorithm by instantiating a different Sumy summarizer object (e.g. LuhnSummarizer, EdmundsonSummarizer). You can also adjust the number of sentences in the summary and the stop and bonus words by modifying the num_sentences, stop_words, and bonus_words parameters.

For more information on the available summarization algorithms and customization options, see the Sumy documentation.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
