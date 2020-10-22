# Welcome to Squirrel Tracker!!

## General Description
We created a Django online App which allows users to track squirrels' locations and more detailed information.
The data imported in this App is from **[2018 Central Park Squirrel Census](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw)**

## App Use Guidance
The App supports:
- Add a new squirrel sighting
- Show a map of NYC Central Park with squirrel markers
- Update information of existing sightings
- Show detail information of a specific sighting chosen
- Show some calculated statistics of the sighting population

How to import/export the data:
After you download the data to your local device, write the following command in your terminal to import the data.
**python manage.py import_squirrel_data /path/to/file.csv**
To export the edited data, you can write:
**python manage.py export_squirrel_data /path/to/file.csv**

## Where to see our App
You can find our Repo on Github by clicking here **[here]**(https://github.com/fanroyi/Squirrel-Tracker.git)

## Contribution
This project is done by Group **Ruiyi & Cheng** in Class Tools for Analytics, Section 1.
UNIS: [*rf2759*, *cj2667*]
