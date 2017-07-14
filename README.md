IIT Bhubaneswar News API
=====

[![License : MIT](https://img.shields.io/npm/l/express.svg)](http://aps.mit-license.org)
[![Python: 2.7.12](https://img.shields.io/badge/Python-2.7.12-red.svg)](https://www.python.org/downloads/release/python-2712/)
![](https://img.shields.io/badge/Heroku-deployed-brightgreen.svg)
![](https://img.shields.io/badge/API%20Type-JSON-orange.svg)

>A JSON API to scrap latest news, events details and notices from <http://www.iitbbs.ac.in>


## Features
* News and Updates
	* Return JSONified count, link text and URL for top 30 news and updates.
* Events
	* Return JSONified count, link text and URL of all upcoming events.
* Notices
	* Return JSONified count, link text and URL of all available notices.

## Schema
All API access is over `HTTPS`, and accessed from the `<https://iitbbs.herokuapp.com>`. All data is sent as JSON.

```bash
curl -i https://iitbbs.herokuapp.com

HTTP/1.1 200 OK
Connection: keep-alive
Server: gunicorn/19.7.1
Date: Wed, 12 Jul 2017 19:31:03 GMT
Content-Type: application/json
Content-Length: 200
Via: 1.1 vegur

{
  "author": "Aman Pratap Singh", 
  "email": "amanprtpsingh@gmail.com", 
  "endpoint": "iitbbs.herokuapp.com", 
  "project_name": "IITBBSNewsAPI", 
  "project_url": "https://apsknight.github.io/IITBBSNewsAPI", 
  "website": "https://apsknight.github.io/"
}
```

## Endpoints

### `GET: /`  
Result:  
```json
{
  "author": "Aman Pratap Singh", 
  "email": "amanprtpsingh@gmail.com", 
  "endpoint": "iitbbs.herokuapp.com", 
  "project_name": "IITBBSNewsAPI", 
  "project_url": "https://apsknight.github.io/IITBBSNewsAPI", 
  "website": "https://apsknight.github.io/"
}
```

### `GET: /news`  
Result:  
```json
{
  "count": 30, 
  "list": [
    {
      "text": "New Admission : 2017-18", 
      "url": "http://www.iitbbs.ac.in/admission-portal.php"
    }, 
    {
      "text": "Recruitment of Part-Time Coaches, Yoga Instructor & Yoga Assistant", 
      "url": "http://www.iitbbs.ac.in/notice/news_1499481442.pdf"
    }, 
    {
      "text": "Information to the provisionally selected candidates  for joining to M.Sc. Programme 2017-18", 
      "url": "http://www.iitbbs.ac.in/msc.php"
    }, 
  ]
}
```

### `GET: /events`  
Result:  
```json
{
  "count": 1, 
  "list": [
    {
      "text": "7th International Conference On Soft Computing for Problem Solving during December 23-24, 2017", 
      "url": "http://www.iitbbs.ac.in/notice/event_1488324349.pdf"
    }
  ]
}
```

### `GET: /notices`  
Result:  
```json
{
  "count": 39, 
  "list": [
    {
      "text": "Result of Physical Training Instructor", 
      "url": "http://www.iitbbs.ac.in/notice/resultofphysicaltraininginstructor_1498601014.pdf"
    }, 
    {
      "text": "Subjects to be offered for Summer Quarter 2016-17", 
      "url": "http://www.iitbbs.ac.in/notice/subjectstobeofferedforsummerquarter201617_1495022716.pdf"
    }, 
  ]
}
```

## Contributing
Feel free to submit a pull request or an issue. Sugest new features on issue tracker.
**OR**  
You can [tweet me](https://twitter.com/ultimateaps) if script deprecate.

## License

Built with ♥ by Aman Pratap Singh([@apsknight](http://amanpratapsingh.github.io)) under [MIT License](http://aps.mit-license.org/)
