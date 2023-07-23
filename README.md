[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]




<br />
<img src="images/zaprogramuj_zycie.png" alt="Zaprogramuj Zycie logo">
<div align="center">
  <a href="https://github.com/DEENUU1/">
<br>
<br>
    <img src="images/pngwing.com.png" alt="Logo" width="100" height="100">
  </a>

  <h3 align="center">MyFridge</h3>

  <p align="center">
    Control your health with a few click!
    <br />
    <br />
    <a href="https://github.com/DEENUU1/MyFridge/issues">Report Bug</a>
    ·
    <a href="https://github.com/DEENUU1/MyFridge/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->

### Table of Contents
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#key-features">Key features</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#configuration">Configuration</a></li>
      </ul>
    </li>
    <li><a href="#unit-tests">Tests</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#author">Author</a></li>
  </ol>

<!-- ABOUT THE PROJECT -->
## About The Project

The project is a Django-based application that allows users to browse various recipes and filter them by date, ingredients, dietary preferences, categories, and more. Additionally, the application features a perfect weight calculator, BMI calculator, and calorie needs calculator. Users can create shopping lists, write blog posts, follow other users, create meal plans, and share them with others. They can create medicine cabinets and add medications, and if a medication's expiration date passes, a notification is sent to the user's email. When browsing a recipe, users can send the required ingredients to their email. Users can register, log in, change passwords, delete accounts, add descriptions, and earn points by adding recipes to favorites or writing comments. There is a user ranking system. Users can add their daily weight statistics and view their analysis. They can also contact the site administrator if they have any questions. Users receive notifications within the application after being followed, receiving a review on their blog post or recipe.
### Built With
- Python
- Django
- HTML, CSS, BOOTSTRAP 5
- Docker
- Redis
- Celery
- Django Celery Beat
- Postgresql

## Key Features
- Browse and filter recipes by various criteria (date, ingredients, preferences, categories, etc.)
- Perfect weight calculator, BMI calculator, and calorie needs calculator
- Create and manage shopping lists
- Write blog posts and follow other users
- Create and share meal plans
- Manage medicine cabinets and receive email notifications for expired medications
- Email ingredients of a recipe to the user
- User registration, login, password management, and account deletion
- Add descriptions and earn points for favorites and comments
- User ranking system
- Track and analyze daily weight statistics
- Contact the site administrator
- Receive notifications for follows and reviews
- Send verification emails (register, password change)

<img src="images/app1.jpg">
<img src="images/app 2.jpg">
<img src="images/app 3.jpg">
<img src="images/app 4.jpg">
<img src="images/app 5.jpg">
<img src="images/app 6.jpg">
<img src="images/app 7.jpg">
<img src="images/bmi 1.jpg">
<img src="images/bmi 2.jpg">
<div style="display: flex;">
  <div style="flex: 1;">
        <img src="images/caloric 1.jpg">
  </div>
  <div style="flex: 1;">
        <img src="images/caloric 2.jpg">
  </div>
</div>
<img src="images/daily meal.jpg">
<img src="images/daily stats.jpg">
<img src="images/follow.jpg">
<img src="images/notify.jpg">
<div style="display: flex;">
  <div style="flex: 1;">
        <img src="images/perfect.jpg">
  </div>
  <div style="flex: 1;">
        <img src="images/perfect 2.jpg">
  </div>
</div>
<img src="images/profile.jpg">
<img src="images/profile 2.jpg">
<img src="images/register.jpg">
<img src="images/login.jpg">
<img src="images/search user.jpg">
<img src="images/shopping list.jpg">





<!-- GETTING STARTED -->
## Getting Started

### Installation


First, you need to clone this repository
```bash
git clone <link>
```

### Configuration
1. Add a .env file in the 'web' directory
```bash
SECRET_KEY=<SOME SECRET KEY>
EMAIL_USERNAME=<YOUR GMAIL EMAIL>
EMAIL_PASSWORD=<YOUR PASSWORD TO GMAIL>
````
2. Then install all requirements
```bash
pip install -r requirements.txt
```
3. Run the project
```bash
python main.py
```

## Unit tests
To run pytest you need to use this command
```bash
pytest
```

To get Coverage details type this command
```bash
coverage run -m pytest
```



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favourites to kick things off!

* [Always Check for the Hidden API when Web Scraping](https://www.youtube.com/watch?v=DqtlR0y0suo)


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.


## Author

- [@DEENUU1](https://www.github.com/DEENUU1)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/DEENUU1/OLX-Analytics.svg?style=for-the-badge
[contributors-url]: https://github.com/DEENUU1/OLX-Analytics/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/DEENUU1/OLX-Analytics.svg?style=for-the-badge
[forks-url]: https://github.com/DEENUU1/OLX-Analytics/network/members
[stars-shield]: https://img.shields.io/github/stars/DEENUU1/OLX-Analytics.svg?style=for-the-badge
[stars-url]: https://github.com/DEENUU1/OLX-Analytics/stargazers
[issues-shield]: https://img.shields.io/github/issues/DEENUU1/OLX-Analytics.svg?style=for-the-badge
[issues-url]: https://github.com/DEENUU1/OLX-Analytics/issues
[license-shield]: https://img.shields.io/github/license/DEENUU1/OLX-Analytics.svg?style=for-the-badge
[license-url]: https://github.com/DEENUU1/OLX-Analytics/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/kacper-wlodarczyk/
