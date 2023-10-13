# Assignment: Student Marks service
The Student Marks service has a RESTful API using the FastAPI framework in Python. The purpose of the service is to allow applications to query for summarised statistical data about student marks.

## Objective
The objective of this assignment is to help us understand your competency working with Python and designing a service that exposes a RESTful API.

## Get Started
### Setup
1. Fork this repository. Later, you will share a link to your repository as your assignment submission.

2. If you are downloading this code to work offline, follow these steps:
   1. Create a new Python environment in your favourity environment manager, then be sure to activate it.
   2. Install [Poetry](https://python-poetry.org/docs/#installation)
   3. Install dependencies using Poetry
        ```bash
        poetry install
        ```

### Running
You can start your API app using the following command:
```bash
poetry run uvicorn app.main:app --reload
```
### Debugging
You can also debug your API app using the launch configuration supplied for VSCode.

### Sample Data
A database of student marks is simulated via a JSON file called [sample_marks.json](./sample_data/student_marks.json). It contains an array of student marks where each student mark consists of a timestamp, student_id and mark. 

You may recreate the data using the associated Python script. 

The tasks below will require you to write code to **read** and **write** this file.

## Evaluation
### Time
I understand and appreciate your time is precious and this assignment will take probably take a couple hours to complete. If you would like additional time, perhaps because you are learning or there have been unexpected events, please pop me a message to let me know.

### Assistance
This is a take home assignment; therefore, I fully expect that you will use all tools at your disposal. I do ask that you consider this assignment like a confidential task at work. This means you should not share the code to other people, including AI services; however, you are allowed to discuss concepts and ask for examples.

### Best Practices
If you have time, we would love to see you demonstrate what you consider best practices in your project setup, design, test and implementation. This may include but not limited to:
* tests
* comments
* models
* error handling
* git workflows

## Tasks
A brief description and desired implementation/output is provided for each task, and each task is designed to be more difficult than the previous, so please feel free to stop when you have completed as many as you can.

You may deviate from the desired implementation/output; however, please an provide explanation as comments in code.

### Task 1 - A Student Mark
Add a new route that returns a student's individual mark. If there are multiple instances of a student, you may return the first instance.

`GET /v1/students/{student_id}/mark/`

which returns the result in this example format:
```json
{
    "timestamp": "2023-05-05T16:22:53.400859",
    "student_id": 123,
    "mark": 123,
}
```

### Task 2 - Average Mark
Add a new route that returns the average mark of all students.

`GET /v1/marks?q=average` 

which returns the result in this example format:
```json
{
  "average_mark": 123,
}
```
where ```average_mark``` is the average mark of all results in the database.

### Task 3 - Top Students
Add a new route that returns the top X students based on their average marks.

`GET /v1/students/{student_id}/top?q=5`

which returns the result in this example format:
```json
{
  "top_students": [
    {
      "student_id": 123,
      "average_mark": 123,
    },
    {
      "student_id": 123,
      "average_mark": 123,
    },
    ...
  ]
}
```
where `average_mark` is the average mark of all results for each top student and `top` query parameter is configurable.

### Task 4 - Add Student Marks
Add a new route to add a new student mark to the database (JSON file).

`POST /v1/students/`

with this example body:
```json
{
    "student_id": 123,
    "average_mark": 123,
}
```

which returns HTTP 201 Created and the created entity in the response body: 
```json
{
    "student_id": 123,
    "average_mark": 123,
}
```

The JSON file should now also contain the new student mark.


## Submission
> Email or share your forked repository with me.

Thank-you so much for the time you have put into completing this assignment.


## Author
**Jim Lim**
* [github/jimseanlim](https://github.com/jimseanlim)
* [twitter/jimseanlim](http://twitter.com/jimseanlim)

## License
Copyright © 2023, [Jim Lim](https://github.com/jimseanlim).
Released under the [MIT license](LICENSE).