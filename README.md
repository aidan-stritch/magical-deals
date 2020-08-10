Travis Continuous Integration
Runs tests on the code every time a push is made to github

[![Build Status](https://travis-ci.org/aidan-stritch/magical-deals.svg?branch=master)](https://travis-ci.org/aidan-stritch/magical-deals)

Image links

- background image for Carousel slides https://www.pxfuel.com/en/free-photo-xtdhi

products images

- thors hammer: https://live.staticflickr.com/7135/6888308144_6b64f70a9d_b_d.jpg
- captain america shield: https://live.staticflickr.com/7225/7324239866_785eb0d421_b.jpg
- bow and arrow: https://c1.wallpaperflare.com/preview/382/109/172/bow-arrow-wooden-grass.jpg
- ark of cov: https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Debbie_Reynolds_Auction_-_%22David_and_Bathseba%22_full-scale_gilt-lacquered_Ark_of_the_Covenant_%285851597607%29.jpg/800px-Debbie_Reynolds_Auction_-_%22David_and_Bathseba%22_full-scale_gilt-lacquered_Ark_of_the_Covenant_%285851597607%29.jpg
- zeus bolt: https://storage.needpix.com/rsynced_images/electrician-1969132_1280.png

# Magical Deals
Magical Deals is an online store for purchasing high end replicas of famous movie/TV and historical items at magical prices. 

Every day, people all around the world see items on TV and in movies that they would love to own for themselves. Items such as Thor's Hammer and Iron Man's armour are normally only things in comics or in movies, but with Magical Deals we bring these items to life so that users can purchase them at reasonable prices. 

Users are able to create accounts where they will have their very own profile. Here they will be able to view previous orders and reviews they have made for products on the store. They will also be able to purchase items and leave reviews on other items on the website with ease. 

## UX
This project was designed to allow users to, through CRUD functionality, manage a collection of products related to TV shows, movies and history. In particular;
- Allows users to create an account through the signup form
- Allows users to edit their accounts details on their profile page
- Allows users to delete their accounts from their profile page

This website is designed for fans of popular fandom who would like a place to purchase items related to their interests as well as leaving reviews for other Magical Deal's members to help them find amazing deals. Searching through thousands of sites daily looking for the perfect gifts for your friends and family (and even yourself!) can be daunting. Magical Deals puts together a wide range of items from a long list of popular franchises and areas of interest so that you can find everything you need in one place with ease. 

I feel that this website satisfies the base requirements in that the users can create, read, update and delete data related to items in the database in an easy to use and visually appealing interface. 

There are a range of apps including Accounts, Cart, Checkout, Home, Products, Reviews and Search that all work together seamlessly to provide a beautifully designed and easy to navigate website that has been designed to appeal to a wide range of visitor types. 

A new user who does not have an account will only have access to the homepage (index.html), the about us page, the signup page, and the login page. They will also be able to view the full details of products that are visible on the homepage, but will be unable to purchase items, leave reviews or view all of the sites products. In place of these buttons and features, the user will see prompts to create an account to access this information. 

Once logged in, the user will have full access to the sites remaining functionality. 

### User Stories
## New Users
## Existing Members
## Admin / Staff Users

### Wireframes
### Entity Relationship Diagram (ERD)

## Features
### Existing Features
### Future Features
## Technologies Used
- HTML - This site uses HTML to instruct the browser how to interprit the code correctly and arrange the layout.
- CSS - This site uses CSS to aid in the style, and overall theme of the website
- Bootstrap - This site uses Bootstrap elements to help design the framework of the site
- Python - This language was chosen to code the majority of the functionality of the site
- Javascript - this was used to program some of the features on the site, such as the calendar
- Balsamiq - This was used to create the wireframes in the design phase
- Heroku - This was chosen to host the website app for deployment.

## Testing
### Manual
#### Pages
### Automated
#### Travis
#### Django / Coverage
### Responsiveness
This website has been designed to scale correctly to different screen sizes with no issues on layout. In order to ensure that the view was pleasant to the user, certain divs and items had to be arranged differently or hidden/shown depending on screen size. This was handled using CSS media queries.

In order to ensure that the navigation bar was as responsive as possible, on Desktop the menu shows accross the top of the page while on mobile screens, the menu reduced to a burger icon with only the title visible. When the burger icon is clicked, a side menu appears with the links to other pages from the nav bar. 

Each page was altered slightly between mobile and desktop for its layout to ensure that the user is getting the best UX possible, regardless of the screen size they are using. This can be seen in the wireframes section as I have included a wireframe of each page with desktop and mobile view. 
### Bugs Found

## Deployment
This project was deployed to Heroku at the address https://magical-deals.herokuapp.com/ using the following steps

#### Github:
- create a new project on GitHub
- copy the code for pushing to a GitHub repository and paste in the terminal of your project on Gitpod (git remote add origin 'link')

#### To commit the code on Gitpod to GitHub:
- in the terminal, type "git add ." to add all new changes to the code to staging area
- next, type "git status" to see which files are ready to be commited
- commit these by typing "git commit -m" and adding a detailed description of the commit in ""
- next, push the code commit to github by typing "git push -u origin master"

#### Heroku:
- Create a Heroku account
- Create a new app
- Link the Heroku app with your Github repository
- Push changes to git using the terminal and verify that the connection to Heroku is working
- Add environment variables to Heroku settings.

## Credits
### Content
Font icons imported from FontAwesome. 
### Media
### Acknowledgements
- I would like to acknowledge my mentor Anthony Ngene for all of his help and advice with this project
- I would like to thank my friends and family for their testing help and advice with this project
- I would like to also thank the Code Insitute Tutor's for all of their help with some of the trickier functionality in this project. In particular, Tim and Samantha, who have been a massive help.