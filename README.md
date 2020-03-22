# Event Service API using Django Rest Framework

An application that gives API endpoints to an event management service written using Django Rest Framework
<br />
<br />
Some of the features included:
<li><b>CRUD operations on Events, Cities where events are held, Participant details and Ratings of events by participants</b></li>
<li><b>Filtered views to filter events by City or/and date</b></li>
<li><b>Views written using ViewSets and managed by a router</b></li>
<li><b>Single Serializer per model</b></li>
<br />
<br />
<b>Technical Details:</b>
<br />
<br />
<b>Framework:</b> Python, Django, Django-Rest-Framework, Viewsets, Routers, etc
<br />
<b>Database:</b> SQLite
<br />
<br /> 
<b>Models used:</b>
<br />
<br />
<b>City</b> (name)
<br />
<b>Participant</b> (full_name, city)
<br />
<b>Event</b> (name, city, date)
<br />
<b>Rating</b> (event, participant, interested, rating)
<br />
<br />
<b>Requirements of the app:</b>
<br />
<a href="https://github.com/tebbythomas/Event_Service_API_Django_Rest_Framework/blob/master/requirements.txt">Link</a>
<br />
<br />
<b>To run the app:</b>
<br />
<br />
<p>1. Clone the repo</p>
<br />
<pre><code>git clone https://github.com/tebbythomas/Event_Service_API_Django_Rest_Framework.git
</code></pre>
<br />
<br />
<p>2. Switch to project dir</p>
<br />
<pre><code>cd Event_Service_API_Django_Rest_Framework-master/
</code></pre>
<br />
<br />
<p>3. Create a python virtual environment</p>
<br />
<pre><code>python3 -m venv proj_env
</code></pre>
<br />
<br />
<p>4. Activate the environment</p>
<br />
<pre><code>source proj_env/bin/activate
</code></pre>
<br />
<br />
<p>5. Install requirements</p>
<br />
<pre><code>pip install -r requirements.txt
</code></pre>
<br />
<br />
<p>6. Switch to django project dir</p>
<br />
<pre><code>cd event_service_project/
</code></pre>
<br />
<br />
<p>7. Make DB migrations</p>
<br />
<pre><code>python manage.py makemigrations
</code></pre>
<br />
<pre><code>python manage.py migrate
</code></pre>
<br />
<br />
<p>8. Create Django user to access the admin</p>
<br />
<pre><code>python manage.py createsuperuser
</code></pre>
<br />
<br />
<p>9. Run the project</p>
<br />
<pre><code>python manage.py runserver
</code></pre>
<br />
<br />
<p>10. Run API requests either using the browser: <a href="127.0.0.1:8000/api/v1/">127.0.0.1:8000/api/v1/</a> or using Postman, etc</p>
<br />
<br />
<p><b>Postman collections used to test the project are located here:</b>
<br />
<a href="https://github.com/tebbythomas/Event_Service_API_Django_Rest_Framework/blob/master/Event_Service_Collection.postman_collection.json">Link</a>
<br />
<br />
<b>Screenshots:</b>
<br />
<br />
1. <b>Get All events</b>:
<br />
<img src="https://github.com/tebbythomas/Event_Service_API_Django_Rest_Framework/blob/master/Screenshots/Event_Requests/Get_All_Events.png" hspace="20">
<br />
<br />
2. <b>Get Individual Event</b>:
<br />
<img src="https://github.com/tebbythomas/Event_Service_API_Django_Rest_Framework/blob/master/Screenshots/Event_Requests/Get_Individual_Event.png" hspace="20">
<br />
<br />
3. <b>Get Filtered Events</b>:
<br />
<img src="https://github.com/tebbythomas/Event_Service_API_Django_Rest_Framework/blob/master/Screenshots/Event_Requests/Get_Events_Filtered_By.png" hspace="20">
<br />
<br />
4. <b>Get all users</b>:
<br />
<img src="https://github.com/tebbythomas/Event_Service_API_Django_Rest_Framework/blob/master/Screenshots/Users_Requests/Get_All_Users.png" hspace="20">
<br />
<br />
5. <b>Add Rating</b>:
<br />
<img src="https://github.com/tebbythomas/Event_Service_API_Django_Rest_Framework/blob/master/Screenshots/Rating_Requests/Add_Rating.png" hspace="20">
<br />
<br />
6. <b>Get Ratings</b>:
<br />
<img src="https://github.com/tebbythomas/Event_Service_API_Django_Rest_Framework/blob/master/Screenshots/Rating_Requests/Get_All_Ratings.png" hspace="20">
<br />
<br />