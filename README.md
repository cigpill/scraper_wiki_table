# scraper_wiki_table
This project contains a single wiki_scrapae_table function that takes a single string argument and returns the table (if available) of corresponding wikipedia page.
In the example use in the main.py asks user to enter an input, then calls the wiki_scrape_table() function with the input as an argument.

If the user enters 'Elon Musk', the function yields following result:

[['Name', 'Elon Musk'], ['Born', 'Elon Reeve Musk (1971-06-28) June 28, 1971 (age 51)Pretoria, Transvaal, South Africa'], 
['Education', '\nUniversity of Pennsylvania (BA, BS)\n'], 
['Title', 'Founder, CEO, and Chief Engineer of SpaceXCEO and product architect of Tesla, Inc.Founder of The Boring Company and X.com (now part of PayPal)Co-founder of Neuralink, OpenAI, and Zip2President of Musk Foundation'], 
['Spouse(s)', '\n\nJustine Wilson\n\u200b \u200b(m. 2000; div. 2008)\u200b\n\nTalulah Riley\n\u200b \u200b(m. 2010; div. 2012)\u200b \u200b\n \u200b(m. 2013; div. 2016)\u200b\n'], 
['Partner(s)', 'Grimes (2018–2022)[1]'], ['Children', '10[a][3]'], ['Parents', 'Errol Musk (father)Maye Musk (mother)'], 
['Relatives', '\nTosca Musk (sister)\nKimbal Musk (brother)\nLyndon Rive (cousin)\n'], ['Family', 'Musk family'], ['Awards', 'List of honors and awards']]

This obviously still requires data cleansing, but it is a quick way to scrape wiki for data.
