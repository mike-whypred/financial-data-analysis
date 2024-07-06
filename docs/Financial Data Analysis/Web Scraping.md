# Web Scraping


Web scraping is a useful skill to have as a data analyst. It involves extracting data from websites in order to build your own  proprietary datasets that can then be analysed. Websites may only display data that covers a short timeframe, so it is useful to scrape such data periodically in order to create a dataset that covers a much longer timeframe. 

Examples of data that can be scraped from a website include text, links, images and tables. Sources of data that could be scraped include company financials, economic indicators, calendar events, etc.



## Robots.txt

Data analysts must exercise caution when scraping data from a website to ensure they are adhering to legal and ethical considerations. One important step that you should take before scraping a website is to check its 'robots.txt' file - which specifies pages of a website that are off-limits to bots for scraping.

For example, if you wanted to check the 'robots.txt' file for the FRED Economic Data website, simply type 'robots.txt' after the website's URL in your browser window:

```
https://fred.stlouisfed.org/robots.txt
``` 

## Web Scraping Libraries

Before we dive into a worked example, let's quickly review a few Python libraries that are used in web scraping.

### BeautifulSoup

BeautifulSoup is a Python library that is used to pull data out of a website's HTML code. It works by converting a web page's HTML code into a Python object that can then be navigated, in order to locate the specific content that you wish to scrape.

### Selenium

The Selenium library it used for automating web browsers, enabling users to programmatically control browser actions such as clicking buttons, filling forms, scrolling and navigating between pages.



## Web Scraping Example

### Import libraries


In your Python IDE (whether it is Collab, Jupyter Notebook or Spyder), first let's import the required libraries for this example. You may need to pip install any libraries that aren't currently installed.

```
### import libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from bs4 import BeautifulSoup
from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.chrome.options import Options
```


### Set URL and Browser Options

Next we need to specify the URL of the website we wish to scrape. In this example we want to scrape the M&A table from Benzinga's website. 


```
### set url

url = 'https://www.benzinga.com/calendars/m-a'
```

After this we need to specify which browser for Python to use (e.g Chrome or Mozilla - in this instance we'll use Chrome). We specify Chrome by initialising **webdriver.ChromeService** to point to **binary_path** which contains the ChromeDriver (don't worry too much about how this works, when you install the **chromedriver_py** library this is taken care of).

We then create an instance of Chrome's options using **options()**, which we have left to default settings here. Next we create a browser instance by using **webdriver.Chrome**.  

Python will open the URL when you run the **driver.get(url)** line.
It is good practice to force your code to pause after loading the website, in case the website takes some time to load, and also to avoid overloading the website with traffic, so we incorporate pauses such as **driver.implicitly_wait** and **time.sleep**. Websites will also incorporate measures to track bots excessively loading their webpages so using pauses in your code will prevent you from getting blocked from the website.

**driver.implicitly_wait** forces the browser window to wait, to give the webpage time to load, whilst **time.sleep** forces your Python code itself to pause for a specified amount of time.



```
### set webdriver
svc = webdriver.ChromeService(executable_path = binary_path)

# set browser options
options = Options()
driver = webdriver.Chrome(service = svc, options = options)
driver.implicitly_wait(5)
driver.get(url)
time.sleep(3)
```


### Get HTML Code for Website

Now we use BeautifulSoup to get the html code for the website in Python. 


```
# get html code for website
soup = BeautifulSoup(driver.page_source, 'lxml')
```

When you ran the **driver.get(url)** line, a Chrome browser should have popped up. We will now explore the HTML code of the website to get a feel for where the data is located.

In the browser window, within the M&A table right click the first cell under the 'Announced' column header, and then click 'Inspect'. A new pane should pop up on the right side of the Chrome browser.

```html
<td class="sc-jgFdch fqijjh table-cell-date max-w-[300px] ticker-cell" colspan="1" title="06/14/2024">06/14/2024</td>
```

You will see that this is the html element is highlighted - it contains the deal announcement date for the deal in the first row.

If you look at the next line below, this is the html element for the expected deal close date:

```html
<td class="sc-jgFdch hatJXV table-cell-date_expected max-w-[300px] ticker-cell" colspan="1" title="2024-06">2024-06</td>
```

You should notice that these various td class elements correspond to a cell within the row. On the right pane, if you hover your mouse over each td class element, you will see the respective cell being highlighted in the table on the webpage.

You should also notice that these various td class elements sit within a tr class element:

```html
<tr class="sc-ikyZYM buNLDV benzinga-core-table-row">
```
If you collapse the tr class element in the Inspect pane, you will notice that it recurs in the HTML code for each row in the M&A table.

Let's go back to our Python code - we can use **find_all** to search through the webpage's HTML code for all instances of the tr class element. 

**Note:** the element may have a slightly different name in your Inspect pane (this is because the Bezinga website periodically renames their element names) - so copy and paste in the element name that you see into your Python code.


```
tablehtml = soup.find_all('tr', class_ = 'sc-ikyZYM buNLDV benzinga-core-table-row')
```

Now if you run **len(tablehtml)** you will see there are 30 instances - this matches up with the number of rows in the M&A table on the website:

```
len(tablehtml)
```

If you look at the first instance within tablehtml, you will see that it contains tr elements for each cell within the first row of the M&A table:

```
tablehtml[0]
```

### Scraping the Data

Our objective is to scrape the data in the table into a dataframe in Python. The most efficient way to do this is to iterate through each table row class, and scrape out the data for each cell into lists. 

Each list will correspond to a column in the table, which we will combine at the end into a single dataframe.

Let's first create empty lists to store the data for each column:

```
# define lists to store data

date_announced_list = []

date_expected_list = []

date_completed_list = []

acquirer_list = []

target_list = []

deal_type_list = []

deal_size_list = []

pmt_type_list = []

status_list = []
```

Let's now write a **for loop** to iterate through the 30 tr elements, and scrape out the relevant cells. You can get the element names for each cell by right clicking the cell on the webpage and clicking 'Inspect' (you'll need to copy and paste the up-to-date element names for each cell in your Python code as the names in the code excerpt below will be out of date):

```
# for loop to extract data from table
for i in range(0, len(tablehtml)):
    
    
    # get date announced
    date_announced = tablehtml[i].find_all('td', class_ = 'sc-jgFdch fqijjh table-cell-date max-w-[300px] ticker-cell')
    date_announced_list.append(date_announced[0].text)
    
    # get date expected
    date_expected = tablehtml[i].find_all('td', class_ = 'sc-jgFdch hatJXV table-cell-date_expected max-w-[300px] ticker-cell')
    date_expected_list.append(date_expected[0].text)
    
    # get date completed
    date_completed = tablehtml[i].find_all('td', class_ = 'sc-jgFdch hatKcp table-cell-date_completed max-w-[300px] ticker-cell')
    date_completed_list.append(date_completed[0].text)
    
    # get acquirer
    acquirer = tablehtml[i].find_all('td', class_ = 'sc-jgFdch fqijdw table-cell-acquirer_name max-w-[300px] ticker-cell')
    acquirer_list.append(acquirer[0].text)
    
    # get target
    target = tablehtml[i].find_all('td', class_ = 'sc-jgFdch fqijje table-cell-target_name max-w-[300px] ticker-cell')
    target_list.append(target[0].text)
    
    # get type
    deal_type = tablehtml[i].find_all('td', class_ = 'sc-jgFdch hatJXU table-cell-deal_type max-w-[300px] ticker-cell')
    deal_type_list.append(deal_type[0].text)
    
    # get size
    deal_size = tablehtml[i].find_all('td', class_ = 'sc-jgFdch hatKcr table-cell-deal_size max-w-[300px]')
    deal_size_list.append(deal_size[0].text)
    
    # payment type
    pmt_type = tablehtml[i].find_all('td', class_ = 'sc-jgFdch hatJYe table-cell-currency max-w-[300px] ticker-cell')
    pmt_type_list.append(pmt_type[0].text)
    
    # status
    status = tablehtml[i].find_all('td', class_ = 'sc-jgFdch hatJXV table-cell-deal_status max-w-[300px] ticker-cell')
    status_list.append(status[0].text) 
```

Finally let's compile the populated lists into a single dataframe:

```
# compile data into dataframe
data = pd.DataFrame({'date_announced': date_announced_list,
                     'date_expected': date_expected_list,
                     'date_completed': date_completed_list,
                     'acquirer': acquirer_list,
                     'target': target_list,
                     'deal_type': deal_type_list,
                     'deal_size': deal_size_list,
                     'pmt_type': pmt_type_list,
                     'status': status_list})
```

In your IDE you should now see a dataframe that resembles the M&A table from the website, if you run **data**:

```
data
```

Finally in our code we close the browser window:


```
# close browser
driver.quit()
```

You may choose to save your dataframe in an Excel or CSV output, or insert it into a database to store the data on your computer.




