# Manual Testing Documentation
In this stage, the developer requested several colleagues to follow the steps outlined below for each of the pages and to document any error messages or UX discrepencies so that they could be addressed after this process was complete. 

Testers were requested to also test the "Navigation UX" (outlined below) on each of the pages as they were conducting those tests to ensure that there was no possible issues relating to specific pages. 

## Navigation UX
### Nav Bar
#### Pre-Login 
- Click on the Magical Deals logo and confirm that it redirects to the homepage (index.html)
- Click on the "Home" button on the NavBar links and confirm that it redirects to the homepage (index.html)
- Click on the "About Us" button on the NavBar links and confirm that it redirects to the About Us page
- Click on the "Sign Up" button on the NavBar links and confirm that it redirects to the Sign Up page
- Click on the "Log In" button on the NavBar links and confirm that it redirects to the Login page

#### Post-Login 
- Click on the "Products" button on the NavBar links and confirm that it redirects to the Products page
- Click on the "Cart" button on the NavBar links and confirm that it redirects to the Shopping Cart page
- Click on the "Log Out" button on the NavBar links and confirm that you are redirected to the homepage and that a message is displayed confirming that you have logged out

### Footer
#### Pre-Login 
- Click on the "Home" button on the Site Map links and confirm that it redirects to the homepage (index.html)
- Click on the "Register" button on the Site Map links and confirm that it redirects to the Sign Up page
- Click on the "Log In" button on the Site Map links and confirm that it redirects to the Login page
- Click on the "Products" button on the Site Map links and confirm that it redirects to the Login page
- Click on the "About Us" button on the Site Map links and confirm that it redirects to the About Us page

#### Post-Login
- Click on the "Products" button on the Site Map links and confirm that it redirects to the Products page
- Click on the "Profile" button on the Site Map links and confirm that it redirects to the Profile page
- Click on the "Cart" button on the Site Map links and confirm that it redirects to the Cart page

## Accounts App
### Sign Up Page
- Enter "TestUser" (which exists in the DB) into the Username field and fill out the rest of the form fields correctly. Click on "Create Account" and confirm that an error message appears stating: "A user with that username already exists"
- Enter a unique username and email address correctly. Enter password into the "Password" field and an incorrect password into "Confirm Password". Click on "Create Account" and confirm that an error message appears stating: "Passwords do not match"
- Leave any field blank and on the "Create Account" button to confirm that an error message prompts the user to fill in the blank field with the following message "Please fill in this field"
- Fill out all details correctly and click on the "Create Account" button. Confirm that the user is redirected to the "Profile" page and a success message appears stating "You have successfully registered"
- Click on the "Sign In" link text beneath the "Create Account" button and confirm that the user is redirected to the "Login" page

### Login Page
- Enter the username you used to test the Sign Up page in the previous test into the username field, as well as an incorrect password into the password field and click the "Log In" button. Confirm that an error message is displayed stating "Your username or password are incorrect"
- Enter an incorrect username into the username field, as well as any password into the password field and click the "Log In" button. Confirm that an error message is displayed stating "Your username or password are incorrect"
- Leave any field blank and on the "Log In" button to confirm that an error message prompts the user to fill in the blank field with the following message "Please fill in this field"
- Enter the username you used to test the Sign Up page in the previous test into the username field, as well as the corresponding correct password into the password field and click the "Log In" button. Confirm that you are redirected to the "Profile" page and a success message appears stating "Welcome" and includes your correct username (i.e. Welcome TestUser!)
- Enter the email address you used to test the Sign Up page in the previous test into the username field, as well as the corresponding correct password into the password field and click the "Log In" button. Confirm that you are redirected to the "Profile" page and a success message appears stating "Welcome" and includes your correct username (i.e. Welcome TestUser!)
- Click on the "Sign Up Now" link text beneath the "Log In" button and confirm that the user is redirected to the "Sign Up" page
- Click on the "Forgot Password" link text beneath the "Log In" button and confirm that the user is redirected to the "Password Reset" Step 1 page

### Profile Page
#### Regular Users
- Click on the "Edit Profile" button and confirm that you are redirected to the Edit User page
- Click on the "All Orders" button and confirm that you are redirected to the All Orders page
- Click on the "All Reviews" button and confirm that you are redirected to the Edit User page
- Click on the "Delete Profile" button and confirm that you are redirected to the Homepage and that a message is displayed confirming that your account has been deleted
- Before having placed any orders with the account - Confirm that in the "Recent Orders" section, a div is displayed stating that no previous orders exist yet
- Before having reviewed any products - Confirm that in the "Your Reviews" section, a div is displayed stating that there are no reviews yet
- After having placed at least one order on the website and processed the payment 
    - Confirm that the most recent orders are displayed in the "Recent Orders" and that they are ordered by Date
    - Click on the "View Product" button in the card for a product and confirm that you are redirected to the view product page for that specific product
    - Click on the "Review" button and confirm that you are redirected to the Add Review page for that product
- After having reviewed at least one product on the website
    - Confirm that the "Your Reviews" is displaying a selection of your reviews
    - Click on the "View Product" button in the card for a review and confirm that you are redirected to the view product page for that specific product
    - Click on the "Edit Review" button and confirm that you are redirected to the Edit Review page
    - Click on the "Delete Review" button and confirm that the review is deleted and that a message is displayed stating "Review successfully deleted"

#### Staff Users
- Log in with the "TestUserStaff" account and confirm that there is a div showing the extra features available to staff 
- Click on the "View All Users" button and confirm that you are redirected to the View All Users page
- Click on the "View All Products" button and confirm that you are redirected to the Products page
- Click on the "Add Product" button and confirm that you are redirected to the Add Product page

### Edit User Page
#### Regular Users
- Fill in all fields correctly (including uploading an image for profile), click on "Update Account" and confirm that you are redirected back to the Profile page with a message confirming that your changes have been saved
- Leave all items blank, click on "Update Account" and confirm that a message is displayed prompting the user that certain fields are required
- Click on the "Back" button and confirm that you are redirected to the Profile page without any changes being saved

#### Staff Users
- Fill out form correctly and then;
    - Confirm that at the end of the edit user form a checkbox is present to make the user either staff or not staff
    - Change the setting to the opposite of the current setting 
    - Click "Update Account" and confirm that you are redirected to the All Users page and a message appears confirming changes have been saved
- Click on the "Back" button and confirm that you are redirected to the All Users page without any changes being saved

### All Orders Page
- Click on the "Profile" button and confirm that you are redirected to the Profile page 
- Click on the "Continue Shopping" button and confirm that you are redirected to the Products page
- Click on the "View Product" button in the card for a product and confirm that you are redirected to the view product page for that specific product

### All Users Page
- Click on the "Profile" button and confirm that you are redirected to the Profile page 
- Click on the "Edit Profile" button and confirm that you are redirected to the Edit Profile page for that user
- Click on the "Delete Profile" button and confirm that the user is deleted and that a message appears stating that the account was successfully deleted

## Cart App
### Cart Page
- Increase the quantity of an item and click the "Update" button and confirm that the current quantity has changed and the order total increased to reflect the addition
- Decrease the quantity of an item to zero, click the "Update" button and confirm that the item is removed from the cart
- Click on the "Continue Shopping" button and confirm that you are redirected to the Products page
- Click on the "Empty Cart" button and confirm that all of the items are removed from the cart, and that you are redirected to the homepage with a message stating that the cart was successfully emptied
- Click on the "Checkout" button and confirm that you are redirected to the Checkout page

## Checkout App 
### Checkout Page
- Click on the "Submit Payment" button with no fields filled in and confirm that an error message appears stating "Could not find payment information"
- Fill in the credit card number with test data "4242424242424242", the CVV as "111" and select a year in the past. Click "Submit Payment" and confirm that a message is shown stating "Your card's expiration year is invalid."
- Fill in the credit card number with test data "4242424242424242", the CVV as "111" and select a year in the future. Click "Submit Payment" and confirm that you are redirected to the profile page and a message is shown stating "Payment successful"
 - Click on the "Cart" button and confirm that you are brought back to the cart page

## Home App 
### About Page
- Click on the "Sign In" button and confirm that you are redirected to the Sign In page

### Index Page / Homepage
#### Pre-Login 
- Click on the Carousel image for "Products" and confirm you are redirected to the Log In page
- In the "We have a wide range of products available" section
    - Click on the "Sign Up" button and confirm you are redirected to the Sign Up page
    - Click on the "Log In" button and confirm you are redirected to the Log In page

#### Post-Login 
- Click on the Carousel image for "Products" and confirm you are redirected to the Products page
- Click on the Carousel image for "Account Benefits" and confirm you are redirected to the About Us page
- Click on the Carousel image for "How it Works" and confirm you are redirected to the Sign Up page
- In the "Recent Magical Deals Bought By Members" section, click on the "View Product" button on the card and confirm that you are redirected to the View Product page for that specific product
- In the product cards;
    - Click on the "More Details" button and confirm that you are redirected to the View Product page for that specific product
    - Add a quantity to the qty field and click on the "Add to Basket" button. Confirm that you are brought to the Cart page and that the item was added to the Cart
- In the "We have a wide range of products available" section;
    - Click on the "All Products" button and confirm you are redirected to the Products page

## Products App 
### Products Page
- In the product search box;
    - Using one of the existing products
        - Enter a word in the products name, click on the "Search" button and confirm that the products are filtered to only show products with that word in its title
        - Enter characters or words that are not in any of the product names, click on the "Search" button and confirm that "No results for your query" message is shown and no item show
        - Click on the "Search" button with no content and confirm that a prompt appears that the input field is required
    - Click on the "All Products" button and confirm that you are redirected to the Products page showing all of the products
- In the product cards;
    - Click on the "More Details" button and confirm that you are redirected to the View Product page for that specific product
    - Add a quantity to the qty field and click on the "Add to Basket" button. Confirm that you are brought to the Cart page and that the item was added to the Cart

#### Staff Users
- Confirm that when logged in as a staff user there is a button for "Add New Product"
    - Click on the "Add New Product" button and confirm that you are redirected to the Add Product page

### Add Product Page
- Click on the "All Products" button and confirm that you are redirected to the Products page
- Test the form
    - Fill in all fields correctly - Click on the "Create Product" button and confirm that you are redirected to the Products page and that it displays the message "Product successfully created"
    - Fill in all fields correctly with the below exceptions, click on the "Create Product" button and confirm that you are prompted to fill in the missing field
        - Leave the product name field blank
        - Leave the description field blank
        - Leave the price field blank
        - Do not select any image for the image field
        - Leave the rating field blank
    - Fill in all details correctly but enter a negative amount in the Rating field. Click on the "Create Product" button and confirm an error message appears stating that the product cannot be created and a prompt appears under the rating field to state "Ensure this value is greater than or equal to 1."

### View Product Page
- Click on the "All Products" button and confirm that you are redirected to the Products page
- Add a quantity to the qty field and click on the "Add to Basket" button. Confirm that you are brought to the Cart page and that the item was added to the Cart
- Click on the "Edit" button and confirm that you are redirected to the Edit Product page
- Click on the "Delete" button and confirm that you are redirected to the Products page and a message confirms "Product successfully deleted"
- Verify that the button for "Add Review" does not show unless you have previously bought the item
    - Click on the "Add Review" button and confirm that you are redirected to the Add Review page for that product

### Edit Product Page
- Confirm that on arriving on this page the form is filled out with the products details
- Test the form
    - Fill in all fields correctly - Click on the "Save Changes" button and confirm that you are redirected to the Products page and that it displays the message "Product has successfully been updated!"
    - Fill in all fields correctly with the below exceptions, click on the "Save Changes" button and confirm that you are prompted to fill in the missing field
        - Leave the product name field blank
        - Leave the description field blank
        - Leave the price field blank
        - Do not select any image for the image field
        - Leave the rating field blank
    - Fill in all details correctly but enter a negative amount in the Rating field. Click on the "Save Changes" button and confirm an error message appears stating "Unable to update. Please rectify the problems below" and a prompt appears under the rating field to state "Ensure this value is greater than or equal to 1."

## Review App 
### All Reviews
- Click on the "Profile" button and confirm that you are redirected to the Profile page 
- Click on the "Continue Shopping" button and confirm that you are redirected to the Products page
- Click on the "View Product" button in the review card confirm that you are redirected to the view product page for that specific product
- Click on the "Edit Review" button and confirm that you are redirected to the Edit Review page
- Click on the "Delete Review" button and confirm that you are redirected to the Profile page and that the review is deleted and that a message is displayed stating "Review successfully deleted" 

### Add Review 
- Click on the "back" button and confirm that you are redirected to the product view page 
-  Test the form
    - Fill in all fields correctly - Click on the "Add Review" button and confirm that you are redirected to the Profile page and that it displays the message "Review successfully created"
    - Fill in all fields correctly with the below exceptions, click on the "Add Review" button and confirm that you are prompted to fill in the missing field
        - Leave the description field blank
        - Leave the rating field blank
    - Fill in all details correctly but enter a negative amount in the Rating field. Click on the "Add Review" button and confirm an error message appears stating that the review cannot be created and a prompt appears under the rating field to state "Ensure this value is greater than or equal to 1."

### Edit Review
- Click on the "back" button and confirm that you are redirected to the Profile page 
-  Test the form
    - Fill in all fields correctly - Click on the "Save Changes" button and confirm that you are redirected to the Profile page and that it displays the message "Review has successfully been updated!"
    - Fill in all fields correctly with the below exceptions, click on the "Save Changes" button and confirm that you are prompted to fill in the missing field
        - Leave the description field blank
        - Leave the rating field blank
    - Fill in all details correctly but enter a negative amount in the Rating field. Click on the "Save Changes" button and confirm an error message appears stating that the review cannot be updated and a prompt appears under the rating field to state "Ensure this value is greater than or equal to 1."

## Password Reset Functionality Pages
### Password Reset Form Page (Step 1)
- Click on the "Back" button and confirm that you are redirected to the homepage (index.html)
- Leave the email address field blank, click the "Reset Password" button and confirm a prompt appears informing you that the email address field is required
- Enter an incorrect email (i.e. without the @ symbol) into the email address field, click the "Reset Password" button and confirm a prompt appears with suggestions of what is missing in the email address
- Enter an incorrect email (i.e. with test@ but without the .com) into the email address field, click the "Reset Password" button and confirm a prompt appears with suggestions of what is missing in the email address
- Enter a valid email address into the email address field, click on the "Reset Password" button and confirm you are redirected to the Password Reset Done page (step 2)
 
### Password Reset Done Page (Step 2)
- No tests required

### Password Reset Confirm Page (Step 3)
- Following the test for Password Reset Form Page (Step 1), find the email in your inbox and click the link provided to reset the password
    - Click on the "Change my password" button without filling in any details into the fields and confirm that a prompt appears telling you that the fields are required
    - Enter a new password into the first password field, and an incorrect password into the second password field, click on the "Change my password" button and confirm that the error message appears stating "The two password fields didn't match." 
    - Enter a new password (less than 8 characters) into both the "New password" and "Confirm password" fields that matches and click on the "change my password" button. Confirm that the error message appears stating "This password is too short. It must contain at least 8 characters."
    - Enter a new password (with 8 numeric characters only) into both the "New password" and "Confirm password" fields that matches and click on the "change my password" button. Confirm that the error message appears stating "This password is entirely numeric."
    - Enter a new password that has 8 characters and a mixture of numeric and alphanumeric into both the "New password" and "Confirm password" fields that matches and click on the "change my password" button. Confirm that you are redirected to the Password Reset Complete Page (Step 4)

### Password Reset Complete Page (Step 4)
- Click on the "Log In" button and confirm that you are redirected to the Log In page