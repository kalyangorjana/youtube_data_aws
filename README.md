# Youtube data extract-Public
Developed project with intention of understanding of web scrapping, flask-api integration, google api

This project provides an overview of how to implement Webscrapping using python.


<ul>
<li>application.py is the core api layer which accepts request and return a response a file</li>
  <li>Operations:
    <ul>
      <li>"/" : Redirects to home screen where you can give the video link</li>
      <li>"/channel" : Redirects to video details</li>
    </ul>
  </li>
  <li>channel_deatils.py which extract the data form the ineuron website</li>
  <li>MongoDB.py is the database related connection setting and operations</li>
  <li>Channel_Logger.py is logging files</li>
  <li>requirements.txt is the application package related information file</li>
</ul>

<h2>Libraries used</h2>
<ul>
<li>requests</li>
<li>bs4</li>
<li>flask</li>
<li>requests_html</li>
<li>pymongo</li>
<li>reportlab</li>
</ul>
