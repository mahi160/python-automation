# Python Automation
This is a repo where i write things when i learn python automation. Hope it helps other too.

## Pip install with venv
Go to project folder, open terminal and type the following commands
```sh
python -m venv .venv
source .venv/bin/activate
# for requirements file
python -m pip install -r requirements.txt
```

## Projects
### Get table from a website
- Deps: `pandas`, `lxml`
- Code: `a_var = pandas.read_html('https://url_of_a_website')`
- Explain: It scrapes the whole website page for html tables and create a list of all the tables.