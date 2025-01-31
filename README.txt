Sample datasets for use with intro to data science course. Tools to play around with these:
1 - Tableau Public: https://public.tableau.com/en-us/s/
2 - Python Pandas: https://www.datacamp.com/community/blog/python-pandas-cheat-sheet 


Two datasets are included in this exercise: 
( Easier ) LastFM - Anonymized user listening habits from a music listening service
( Harder ) Amazon - Reviews and track data from Amazon music sales site

==== LastFM ===
Source: http://www.dtic.upf.edu/~ocelma/MusicRecommendationDataset/lastfm-1K.html
    Celma, O. Music Recommendation and Discovery in the Long Tail. Springer 2010.
(Easy)  File: LastFM - Users Only
Description: list of all users of the website
Fields: 
	User Id - unique identifier. Think of it as a name
	Gender - m or f, or "0" if no gender given
	User Age - how old the user is, as entered by the user
	Country - e.g. "United States", or "0" if none given
	Account Created - Date account was setup
	Account age - Year range since account creation date
	User age range - span of years for user’s age

(Medium) File: LastFM - Users and Play Counts
Description: How many times a given user played a given artist. Only ~10,000 users are included
	Note that users are listed multiple times in the file.
	The CountD([Users]) function in Tableau will give the number of users.
Fields:
	Same user fields as "Users only" file
	Artist Id - unique identifier for the artist
	Artist Name - the name of the band. Characters which appear as symbols in Tableau were originally in Chinese, Japanese, etc.
	Plays - How many times a user played this artist
	Genre - What type of music this is (e.g. pop, hip-hop, etc)
	
==== Amazon ===
Source: https://snap.stanford.edu/data/amazon-meta.html
    J. Leskovec, L. Adamic and B. Adamic. The Dynamics of Viral Marketing. ACM Transactions on the Web (ACM TWEB), 1(1), 2007.
(Medium-Hard) File: Amazon_Products
Description: the average review and review rating for the music, and the genre's and sub-genres it belongs to
Fields:
	ASIN - unique identifier for the product
	TITLE - name of the music
	GROUP - reads "music". This dataset originally included books, movies, etc.
	SALES_RANK - how well this sells compared to similar products
	TIMES_REVIEWED - how many reviews exist for this product
	TIMES_DOWNLOADED - how many users have downloaded this product
	AVERAGE_RATING - 0-5, the average of reviews in the reviews file
    MAIN_CATEGORY - Overall genre
    SUB_CATEGORIES - Sub-Genres

(Hard) File: Amazon_Products_And_Reviews
Description: A list for each product of what reviews it was given by what users
Fields:
	Same fields as Amazon_Products
	DATE - when the review happened
	CUSTOMER - unique identifier for the customer (think of this as a name)
	RATING - what the customer rated the product 
	VOTES - how many other customers voted on the review
	HELPFUL - how many of the votes indicated the review was helpful
