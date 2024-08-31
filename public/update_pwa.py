import os
import requests

# Function to download the profile picture
def download_profile_pic():
    url = "https://example.com/path-to-your-profile-pic.jpg"  # Replace with your actual image URL
    img_data = requests.get(url).content
    with open('assets/scott-stankowski.jpg', 'wb') as handler:
        handler.write(img_data)
    print("Profile picture downloaded.")

# Function to update index.html
def update_index_html():
    index_html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Scott Stankowski - Realtor PWA</title>
        <link rel="stylesheet" href="styles/style.css">
        <link rel="manifest" href="public/manifest.json">
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&family=Open+Sans:wght@400;700&display=swap" rel="stylesheet">
        <script defer src="src/main.js"></script>
    </head>
    <body>
        <header>
            <h1>Scott Stankowski</h1>
            <p>Your Trusted Realtor at EXIT Realty CW</p>
        </header>
        
        <main>
            <!-- Profile Picture -->
            <img src="assets/scott-stankowski.jpg" alt="Scott Stankowski" class="profile-pic">
            
            <!-- Introduction and Install Button -->
            <section id="introduction">
                <p>Welcome to my real estate app! Explore my listings, get in touch, and discover your new home with personalized service.</p>
                <button id="installButton" style="display: none;">Install App</button>
            </section>
            
            <!-- Listings Section with Embedded 3D Tours -->
            <section id="listings">
                <h2>Featured 3D Tours</h2>
                <p>Explore some of my featured property listings in 3D below:</p>
                
                <!-- Embed Matterport 3D Tours -->
                <div class="tour-container">
                    <iframe width="853" height="480" src="https://my.matterport.com/show/?m=fjWfvWrTM5T" frameborder="0" allowfullscreen allow="xr-spatial-tracking"></iframe>
                </div>
                <div class="tour-container">
                    <iframe width="853" height="480" src="https://my.matterport.com/show/?m=KbSM4oRdT3Z" frameborder="0" allowfullscreen allow="xr-spatial-tracking"></iframe>
                </div>
            </section>
            
            <!-- Contact Information -->
            <section id="contact-info">
                <h2>Contact Scott</h2>
                <ul>
                    <li><strong>Realtor License #:</strong> 93838-94</li>
                    <li><strong>Mobile:</strong> <a href="tel:+17153212825">+1 (715) 321-2825</a></li>
                    <li><strong>Email:</strong> <a href="mailto:scott@exitcw.com">scott@exitcw.com</a></li>
                    <li><strong>Office:</strong> EXIT REALTY CW</li>
                    <li><strong>Office Address:</strong> 2006 County Rd HH, Plover, WI, 54467</li>
                </ul>

                <h3>24/7 Mobile Property Search</h3>
                <p>Text <strong>Stan</strong> to 85377</p>

                <h3>My Mobile Business Card™</h3>
                <p>Text <strong>cwscoach</strong> to 85377</p>

                <p><em>* Std. msg and data rates may apply</em></p>

                <h3>Connect with Me on Social Media</h3>
                <p>Stay updated with my latest listings and news!</p>

                <h3>Download EXIT Realty Connect App</h3>
                <p><a href="#">Download App</a></p>

                <h3>Interested in Joining EXIT Realty?</h3>
                <p><a href="#">Click to Learn More</a></p>
            </section>
        </main>
        
        <footer>
            <p>© 2024 Scott Stankowski. All rights reserved.</p>
        </footer>
    </body>
    </html>
    """
    with open('index.html', 'w') as file:
        file.write(index_html_content)
    print("index.html updated.")

# Function to update style.css
def update_style_css():
    # Ensure the 'styles' directory exists
    if not os.path.exists('styles'):
        os.makedirs('styles')

    style_css_content = """
    /* General Body and Layout */
    body {
        font-family: 'Roboto', Arial, sans-serif;
        margin: 0;
        padding: 0;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 100vh;
        background-color: #E1F5FE; /* Light teal background */
    }

    /* Header Styling */
    header {
        background-color: #00A4E4; /* EXIT Realty teal */
        color: #fff; /* White text color */
        padding: 40px 20px; /* Increased padding for more impact */
        width: 100%;
        text-align: center;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }

    header h1 {
        margin: 0;
        font-size: 2.5rem; /* Larger font for more impact */
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2); /* Subtle shadow for depth */
        font-family: 'Open Sans', sans-serif;
    }

    header p {
        margin: 10px 0 0;
        font-size: 1.2rem;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
    }

    /* Main Content Styling */
    main {
        padding: 20px;
        width: 90%;
        max-width: 800px;
        text-align: center;
        background-color: #fff;
        border-radius: 10px;
        box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
    }

    .profile-pic {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        margin-bottom: 20px;
        border: 5px solid #00A4E4; /* Teal border */
    }

    /* Button Styling */
    button {
        padding: 10px 20px;
        font-size: 1rem;
        margin: 20px 0;
        cursor: pointer;
        background-color: #00A4E4; /* Teal button */
        color: #fff;
        border: none;
        border-radius: 5px;
        transition: background-color 0.3s ease;
    }

    button:hover {
        background-color: #0077b3; /* Darker teal on hover */
    }

    /* Listings and Contact Information Sections */
    #listings, #contact-info {
        margin-bottom: 30px;
        text-align: left;
        padding: 10px;
        background-color: #f9f9f9;
        border-radius: 8px;
    }

    #listings p, #contact-info ul {
        font-size: 1rem;
        color: #333;
    }

    #contact-info ul {
        list-style-type: none;
        padding: 0;
    }

    #contact-info ul li {
        padding: 5px 0;
    }

    /* Tour Embed Styling */
    .tour-container {
        margin: 20px 0;
        width: 100%;
        max-width: 853px; /* Keeps the maximum width */
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .tour-container iframe {
        width: 100%; /* Makes it responsive */
        height: 480px;
        border: none;
    }

    /* Footer Styling */
    footer {
        margin-top: 20px;
        padding: 10px;
        background-color: #2C2C2C; /* Dark gray footer */
        color: #fff;
        width: 100%;
        text-align: center;
        border-radius: 0 0 10px 10px;
    }
    """
    with open('styles/style.css', 'w') as file:
        file.write(style_css_content)
    print("style.css updated.")

# Run the functions
if not os.path.exists('assets'):
    os.makedirs('assets')

download_profile_pic()
update_index_html()
update_style_css()
print("PWA updated successfully!")
