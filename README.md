# Angelia (/aŋ.ɟeˈli.a/):

### Sentiment-Based Automated Fact-Checking: A Novel Approach to Address Fake News Detection.

<p align='center'> 
    <img src=https://github.com/YuriBrandi/Angelia/assets/52039988/fe187280-24c1-4878-b211-98daf4e485d4 width=200>
</p>

This University work consists of an in-depth study and a fully working *privacy-oriented*, *open-source*, *lightweight* browser extension (*available at https://github.com/YuriBrandi/Angelia*) that allows to **verify** *Fake news' titles* and *AI synthetic images*. 

### Students
Raffaele Aurucci ([@raffaele-aurucci](https://github.com/raffaele-aurucci))  
Lukas Gajewski ([@LukaszG92](https://github.com/LukaszG92))  
Yuri Brandi ([@YuriBrandi](https://github.com/YuriBrandi))


## Architecture

<p align='center'> 
    <img width="250" src="https://github.com/EdgeResearch/Angelia/assets/52039988/282976eb-3bef-4f6a-bc95-8aef95bca787">
</p>

This work will be followed by a scientific paper, thus technical information won't be covered in this readme.

*Angelia* consist of 5 main modules:

- A Title Extraction module
- A Tokenization module
- A Polarity Analysis module
- An Evidence Search module
- A Reliability Evaluation module

#### Note: All these modules are exectued in local and require no external requests (no CDN is used).

![Angelia-EnglishW](https://github.com/EdgeResearch/Angelia/assets/52039988/92f388df-5190-4107-a924-b9199827ee84)

1. The extension extracts the title, and tokenizes it to facilitate News search via the API.
2. Each result is filtered by hostname through a list of **TNS** (Trusted News Sites).
3. The sentiment of the original title is compared to the one of the filtered news, this allows the polarity of news' titles to be compared.

The reliability evaluation module is in continuous development. At the moment, the polarity of each news is compared and a negativity score is given, which results in a textual outcome (e.g. *Likely Fake*, *Trustable* ...). When faced with negative-polarity comparisons, the extensions utilizes heuristics found in our studies, for instance it checks for words of disagreement such as *"No, ..."* Or *"Fake ..."*.

The sentiment analysis module is powered by the [Pyodide](https://github.com/pyodide/pyodide) interpreter, customized and lightened to the bare minimum to offer a fast and serverless experience. All the libraries come already included in the extension and no external resource is fetched.


## Download & Installation

For downloading and installing this tool please refer to the original repository of this work (https://github.com/YuriBrandi/Angelia), as this is only intended to be a scientific research repository.

## Contributions

Contributions are very much appreciated. Please well describe your changes inside your PR to make it easier to understand them.

If you encounter any problem or bug that is unrelated with your own machine, please report it and *open a new issue* with replicable steps. 

#### Note: only make contributions to the [original repository](https://github.com/YuriBrandi/Angelia)

## License

This project is distributed under the [GNU General Public License v3](LICENSE).

![GPLv3Logo](https://www.gnu.org/graphics/gplv3-127x51.png)
