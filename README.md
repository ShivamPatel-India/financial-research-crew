# FinancialResearcher Crew

Welcome to the FinancialResearcher Crew project, facilitating your day to day reserach of the specific company name given by the user for potential investment. These agents/crew delivers up to date financial information about the company after careful consideration of latest news and article on the internet mentioning organization. Research report will be saved in the output/report.md.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**
**Add your `SERPER_API_KEY` into the `.env` file**

- Modify `src/financial_researcher/config/agents.yaml` to define your agents
- Modify `src/financial_researcher/config/tasks.yaml` to define your tasks
- Modify `src/financial_researcher/crew.py` to add your own logic, tools and specific args
- Modify `src/financial_researcher/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the financial_researcher Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## SERPER API

Agentic crew of this project utilize the serper tool for scraping the internet in order to get the most latest news and information about the complany and eventually making the reliable and up to date report of the company.
