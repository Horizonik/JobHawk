![Python versions](https://img.shields.io/badge/python-3.10.10-blue.svg)
[![Docker Image CI](https://github.com/Gemesil/JobHawk/actions/workflows/docker-image.yml/badge.svg)](https://github.com/Gemesil/JobHawk/actions/workflows/docker-image.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Gemesil_JobHawk&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Gemesil_JobHawk)

### Introduction
Web App that enables users to quickly find jobs they're best suited for. 

### How it works
1. The user enters a job title, or skills they're familiar with.
2. Those keywords are then processed in an AI, that generates more keywords and topics based on what was entered.
3. Those keywords are then searched in job sites: LinkedIn, Indeed, Glassdoor. The results from those sites are scraped.
4. The scrapes data is processed in a NLP algorithm that strips and only leaves required skills and sums up what you do at said job.

### Technically speaking
The backend runs on Django, and it is where the AI model runs, the scrapers do the scraping, the results are processed in an nlp, and the jobs are saved as models.
The frontend runs on React, it is built as an SPA (Single Page Application) for the best user experience, and communicates with our backend only for passing the user's keywords.

### Production
The backend is managed by nginx and gunicorn, using wsgi.
The entire web app has been dockerized, using GitHub Actions it runs through multiple tests to verify that the app works properly after every commit.

### In the future
We may separate the dockerfile into two separate files for the front and the back and make them communicate with each other using docker-compose.
We may need to improve the NLP processing and retrain the ai model on high quality data.
