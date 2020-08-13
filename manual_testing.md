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

## Accounts App Pages
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
**Regular Users**
- Fill in all fields correctly (including uploading an image for profile), click on "Update Account" and confirm that you are redirected back to the Profile page with a message confirming that your changes have been saved
- Leave all items blank, click on "Update Account" and confirm that a message is displayed prompting the user that certain fields are required
- Click on the "Back" button and confirm that you are redirected to the Profile page without any changes being saved

***Staff Users***
- Fill out form correctly and then;
    - Confirm that at the end of the edit user form a checkbox is present to make the user either staff or not staff
    - Change the setting to the opposite of the current setting 
    - Click "Update Account" and confirm that you are redirected to the All Users page and a message appears confirming changes have been saved
- Click on the "Back" button and confirm that you are redirected to the All Users page without any changes being saved

### All Orders Page
### All Users Page




## Cart App Pages
### Cart Page
## Checkout App Pages
### Checkout Page
## Home App Pages
### About Page
### Index Page / Homepage
## Products App Pages
### Add Product Page
### Edit Product Page
### Products Page
### View Product Page
## Review App Pages
### Add Review 
### All Reviews
### Edit Review
## Password Reset Functionality Pages
### Password Reset Form Page
### Password Reset Done Page
### Password Reset Confirm Page
### Password Reset Complete Page