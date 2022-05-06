# Voting-Portal
![Demo Image](https://i.imgur.com/81fVDCw.png)

Voting in person has been an issue since the pandemic arrived. This web applications allows it's users to create elections and organise voting activities remotely. Some of the features are:

## Election
The election feature allows users to create and manage multiple elections. Some of its operations are:

* Create an election 
* View all elections
* Delete an election

## Candidate
The Candidate feature allows users to create and manage multiple candidates. Some of its operations are:

* Candidate registration under an election category
* Approve candidate
* Delete candidate

## Voter 
The Voter feature allows users to create and manage multiple voters. Some of its operations are:

* Voter registration
* Approve voter
* Delete voter

## Time
The Time feature allows users to schedule elections and registrations activities. Some of its operations are:

* Create and schedule election time
* Create and schedule candidate registraion time

## Vote
The Vote feature allows users to cast a vote under an election. Some of its operations are:

* Create a vote 
* View vote analytics for an election
* Delete vote


## demo 
[https://2020election.dscthsosa.org/]

## dependencies
#### Python, Django==2.1, Pillow

## run 

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
