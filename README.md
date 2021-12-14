# BasicMatcher
### Backend Home Assignment 

In this project I used Django with PostgreSQL.

#### Logic:
The match is determined by checking the title first. 
If there are suitable candidates for the title we will return the ones with the highest number of matching skills.

#### How to install and run:
  1.	Clone the repository  
  2.	Open terminal and prepare the virtual-env:   
    a.	Run `pip3 install pipenv`  
    b.	Run `pipenv install`  
    c.	Run `pipenv shell`
  3.  Run the server `python3 manage.py runserver`
  
To test the server please go to http://localhost:8000/app from Postman or any other tool from which requests can be sent to the server.

### API:  

*	**Post:**  `/job` – add new job to the DB, return the job-id 
```   
{
  title: string
  skils: list of string
  }
```  
  
  *	**Get:** `/job` – return all the jobs from the jobs table in DB
  *	**Post:** `/candidate` - add new candidate to the DB, return the candidate-id  
  ```   
{
  title: string
  skils: list of string
  }
```  
  *	**Get:**  `/candidate` – return all the candidates from the candidate table in DB
  *	**Get:** `/match/{job_id}` – return a list of the best matching candidates to the job of the given job_id

I attached to the email my postman collection with these requests (gloatApp.postman_collection)


Thank you,
Elior Abargel

