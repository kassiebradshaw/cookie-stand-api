# Lab 34 - Back End Deployment

*Author*: Kassie Bradshaw

[Link to my GitHub](https://github.com/kassiebradshaw/cookie-stand-api)

[Link to my deployed URL](tbd)

## Overview

It's time to deploy!

First steps are to make sure your application is able to run well in a remote environment.

Once you are confident that your application is *deployable* then time to research deployment options.

## Feature Tasks & Requirements

* [x] Create a new repo `cookie-stand-api` (Mine is named salmon-cookies-api)
* [x] Modify your application using instructions in README.md found in root of repo
  * [ ] Change `things` app folder to be `cookie_stands`
  * [ ] Go through code base looking for `Thing`, `thing`, and `things` - change to cookie-stand related names.
    * E.g. `Thing` model becomes `CookieStand`, `ThingList` becomes `CookieStandList`
    * Pro Tip: Do a global text search looking for `thing` (search should be case insensitive)

* [x] The `CookieStand` model must contain:

    ```python
    location = models.CharField(max_length=256)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(default='', null=True, blank=True)
    hourly_sales = models.JSONField(default=list, blank=True)
    minimum_customers_per_hour = models.IntegerField(default=0)
    maximum_customers_per_hour = models.IntegerField(default=0)
    average_cookies_per_sale = models.FloatField(default=0)
    ```

### Database Deployment Requirements

* [ ] Host your Database at ElephantSQL

### Site Deployment Requirements

* [ ] Deploy (to AWS, Heroku, etc)

### Stretch Goals

* [ ] Add functionality so that when a JSON array of hourly_sales is not provided at creation time, it will be generated with random numbers based on minimum/maximum customers per hour and average cookies per sale.
* [ ] Deploy site with alternate provider

### Implementation Notes

* [x] Site must use environment variables

## User Acceptance Tests

* [ ] Manually confirm API using API Tester, Postman, or HTTPie
  * Remember to use deployed url, not localhost
