# Rental of tourist equipment
#### Video Demo:  https://youtu.be/SD4Ltpr_FwY
#### Description: This is a website for booking travel equipment
Projct
There are 2 files in the <image> folder: "IMG_20190511_104107.jpg" and "logotype.jpg"
The <static> folder has a <styles.css> file with my project's styles.
The HTML rental files are located in the <templates> folder.
"baseapp.html is the base HTML from which I imitated others using Ajax. I also used this file for the page on the "Data" tab under the link "produkt/info" where the data of customers and the products they reserved are in the form of a table extracted from the database The most basic page uses Boostrap 5 where the header and footers are located.
The file "about.html" is a page with a link about us. Here I emulated the "baseapp.html" page using Ajax and used two photos: background and logo.
The "index.html" file is the main page file. In it, with the help of Ajax and the "for" loop, he displayed the elements from the "Tovar" table database.
The "klient.html" file displays data from the "Persons" table and reserved goods. In the file, I used Ajax to imitate from the base file and output information in the form of a table.
The "prav.html" file displays the equipment rental rules. Each user can view and read the rental rules by going to the "Rules" tab. The text in the file is formatted using tags.
The "produkt.html" file is a form for booking goods, which contains four fields to be filled in and the "Add" button for entering booking data into the database.
By going to the "Inventory" tab, the user will see a list of goods from the "Tovar" table from the database that are available for hire. This information is in the "tovar.html" file.
In the root directory <project> there is a database file "database.db" which stores data in three tables: "Tovar", "Persons", and "Profiles" where there are data of the person who booked a certain product for a certain number of days. I also used the helper file "database.py" to create and add the product. In it, I worked with entering information on the inventory in the database before using the site.
The main file "app.py" written in Python is located in the same directory. It imports files from the database using SQLAlchemy and also has the Flask framework hooked up. In the "app.py" file, the entire basic structure of the site, transitions between pages, output of information from databases, processing of the form and entering it into the database is performed.


