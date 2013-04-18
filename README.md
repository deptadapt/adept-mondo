adept-mondo
===========

adept-mondo is a simple Django app that simplifies using crispy_forms with django.contrib.comments

## Requirements
* Django (probably any version will work)
* crispy_forms
* Twitter Bootstrap

## Installation

Once the mondo directory has been added to the Python path, add mondo to INSTALLED_APPS and COMMENTS_APP.

Make sure that mondo is listed before django.contrib.comments so that mondo's comments templates will be used.

## Usage

You can now use the crispy templatetag to display comment forms in templates.

## About

This is my first time publishing a free open source project. Feedback is welcome!  I've been working on a personal blog and basic CMS site for personal use. This simple comment app is the first reusable app from my larger *adept* project that I feel like I can release.

Feel free to copy it for your own use. I included an AGPLv3 license because it's my preference but I'm not closed to the idea of a different license.
