
<h2>Description</h2>

<p>
A server that enables you to play Settlers of Catan with your friends online.
</p>

<h2>Technology</h2>
<p>
Uses Django (Python) as a Single Page application. The initial page contains javascript that performs API calls to the backend. This actitecture makes a lot of sense for a game since it is very flexible and does not rely on page reloads (as server side rendering would).
I use vanilla Javascript instead of a modern Javascript framework (which I regret). Keeping the DOM up-to-date with the application state is very frustrating. Having to be mindfull of both the Javascript state in memory and the DOM is very annoying,
especially in a game.
</p>

<h2>Set up</h2>
<ul>
  <li>create a new virtual environment for python</li>
  <li>install the dependencies by running in the terminal in the root folder: pip install -r requirements.txt</li>
  <li>to set up the database tables use: python manage.py migrate</li>
  <li>create a super user by running: python manage.py createsuperuser</li>
  <li>start app by running in terminal: python manage.py runserver</li>
</ul>






