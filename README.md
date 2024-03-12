# Python Automation

This is a repo where i write things when i learn python automation. Hope it helps other too.

## Setup VS Code

- Install VS Code
- Install Python extensions for python
- For interactive coding, install Jupytar Notebook extension.

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

- Explain: It scrapes the whole website page for html tables and create a list of all the tables. You can do many things with it then.
- Deps: `pandas`, `lxml`
- Code:
  ```py
  a_var = pandas.read_html('https://url_of_a_website')
  ```

### Read a csv file

- Explain: It reads form a csv file and creates a table. You can manipulate and do many things with it.
- Deps: `pandas`, `lxml`
- Code:
  ```py
  a_var = pandas.read_html('sample.csv')
  # to rename a column
  a_var.rename(columns = {'old_name': 'new_name'}, inplace=True)
  ```

### Read table from PDF

- Explain: It reads table from a pdf file. It can export the tables in to csv and other formats.
- Deps: `tk`, `ghostscript`,`opencv-python`,`camelot-py`
- Code:

  ```py
  import camelot

  # here pages is what page number
  tables = camelot.read_pdf('./samples/sample.pdf', pages='1')

  # the args are: name of the file, f is the format to export, compress is whether to compress or not.
  tables.export('sample.csv', f='csv', compress=True)
  tables[0].to_csv('./samples/table_pdf.csv')
  ```

### HTML & Xpath

- **HTML** is the main building block of a website. It's the skeleton. It consists of different elements. They are called **tags**. Tags are used to write different part of a webpage. There are different types of tag.
- Code:
  ```html
  <h1 class="a_class">A heading</h1>
  <!-- Here <h1></h1> is a tag to define heading. class is called attribute. There can be multiple attributes.-->
  ```
- **XPath** is a way to indicate a specific tag. It starts with `//` in the beginning. Here are some examples. Try the [playground](https://scrapinghub.github.io/xpath-playground/)
- Code:
  ```sh
  # this finds all h1 tags with 'class' attribute that _contains_ a_class
  //h1[contains(@class, "a_class")] 
  # this finds the first p tag
  //p[1]
  # this finds all the p tags with 'attribute' whose _value_ is a_class and returns the inner value of it by text()
  //p[@class="a_class"].text()
  # you can use and / or
  //p[@class="a_class" or @class="b_class"]
  # finds all the 'direct child' h1 of the tag main and return innerText
  //main/h1/text()
  # finds every h1 tag (direct child or more deep level) of main
  //main//h1
  ```
