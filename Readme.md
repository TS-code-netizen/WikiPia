# WikiPia Website

## YouTube description: 
[YouTube Link](https://youtu.be/A5CSVRcse18)
> If you don't want to read the description, you may view the YouTube video instead

## Project objective:
Wiki basically is a site for people to share information or ideas using webpage. This project Wikipia is simialr to an encyclopedia website, wikipedia functions as a website to share information. An online wiki site for users to add on page or read the information.

## Technologies:
Back-end:
```
Python
Django framework
```

Front-end:
```
HTML 
CSS
python-markdown2 package
```

## Project Requirements:
**Entry Page**
- Visiting /wiki/NAME, where NAME is an encyclopedia entry, the page will be rendered and display the contents of that encyclopedia entry.
- If NAME does not exist, an error message will display and indicate this requested page was not found.
- If NAME does exist, the page will display the content of the entry with NAME as the title of the page.

**Index Page**
- Main page that lists all pages. After clicking any entry name display on the page, user will be taken directly to that page.

**Search**
- A feature allows typing a query to search for an entry by typing into the search box in the sidebar.
- User will be redirected to that entry’s page if the query matches the name of an encyclopedia entry. t
- If no matching found, the user will be directed a page that displays all entries that have the query as a substring. 
- Clicking on any entry name display on the page, user will be taken directly to that page.

**New Page**
- To create a new entry page, click on “Create New Page” in the sidebar.
- On that new creation page, there's title input and in a textarea, for the content of the page.
- Users can input the title and content and click a button to save it.
- If the provided title matched with any existing title, an error message will show up.
- Else, this new entry will be saved to disk, user will be directed to the new entry’s page.

**Edit Page**
- Click a link on the entry's page will be directed to a page that user can edit entry’s content.
- The textarea area is pre-populated with the content of the page.
- After saving the changes, user will be redirected back to that entry’s page.

**Random Page**
- Clicking “Random Page” in the sidebar will be directed to a random entry's page.

**Markdown to HTML Conversion**
- Markdown content in the entry file will be converted to HTML.

## Requirement:
1. Install python3 in Visual Studio Code
2. Install Django package
``pip3 install Django``
3. Download the whole package in the master branch
4. Install markdown2 package
`` pip3 install markdown2 ``
6. Run
``python manage.py runserver``


#### Special appreciation to CS50's team
