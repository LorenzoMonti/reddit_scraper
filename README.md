# Reddit scraper


This is a little project that icludes a simple web scraper and sentimental analysis analyzer for [Reddit](https://www.reddit.com). With Reddit it's possibile to scrape subreddit/threads/comments easily, adding the JSON extension to the url. So, this scraping projects takes advantage of just that and is based on different step:
- In the first step, we need to retrieve the links based on your query, the file that deals with it is **scrape_link_from_query.py**.
  -  It's necessary create a folder named ``threads`` and the **retrieve_threads.py** file take all the links contained in the csv file created in the previous step. A JSON file will be saved for each link in the csv.
  - Is it also possible scrape all links with **scrape_with_Selenium.py** exploiting [Selenium](https://www.selenium.dev/)
  - [WORK IN PROGRESS] Once JSON have been scraped, **analyze.py** analyzes the file structure and applies sentiment analysis techniques.


This is an work in progress project and any pull request/help is welcome.

Enjoy :)
