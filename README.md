# 🌭 Is-Hotdog 🌭 

Based on Jin Yang's app "Not Hotdog" on the TV series Silicon Valley, a REST API that can determine whether or not there is a hotdog in the image entered.

![image](https://user-images.githubusercontent.com/69827506/137544053-44e53b7b-09f5-4e1c-8278-5e458898e8a8.png)

**[Episode clip](https://www.youtube.com/watch?v=ACmydtFDTGs)**


## Table of Contents
1. [Release Notes](#release-notes)
2. [Demo](#demo)
3. [Purpose](#purpose)
4. [Roadmap](#roadmap)
5. [Built With](#built)
6. [How to Launch Project](#how-to)

<a name="release-notes"/>

## Demo
*A full video demo was prepared and can be viewed in this [zip file](https://github.com/RogueNPC/Is-Hotdog/files/7355648/IsHotdogDemo.mov.zip) however due to the size limitiations, we will be going through a step-by-step video demo below*

We run the API in through the browser which should open up to a page that looks like this:

![Is-Hotdog Landing Page](https://user-images.githubusercontent.com/69827506/137547552-c9692833-5a61-4864-9f74-a55b961fb275.png)

We then run our API with our first test image (a hotdog):

https://user-images.githubusercontent.com/69827506/137548005-16ae32bc-070f-4d4e-9fca-7f98d255aabc.mov

After uploading our image of a 🌭, we see that our model has a ~90% confidence rate that it looked at an image of a hotdog.

Next, we run our API with the second test image (a not-hotdog):

https://user-images.githubusercontent.com/69827506/137548481-4c1bb103-31bf-496f-99ce-9b1b47ffcf6f.mov

We uploaded an image of Pad Thai (aka not a hotdog), we see that our model was ~21% sure that the image was a hotdog which also means ~79% confident that it was not looking at a hotdog.

Lastly, I decided to include one last trick image (a kinda-hotdog):

https://user-images.githubusercontent.com/69827506/137549062-8e2cc250-f3e3-4b5d-9f97-80b9c0bb52fa.mov

The model was completely confused as it was split down the middle with a ~56% confidence rate that it was looking at a hotdog.

## Release Notes
#### v1.0.0    (Jul 13 2021)

- 🎉 first release!

<a name="purpose"/>

## Purpose
<!-- Why use this product? -->
I wanted to practice what I've learned in the Data Science field by
- Recreating the Not Hotdog app from Silicon Valley.

- Creating a Convolutional Neural Network model that can take and analyze any given image to check for a specific object within that image.

- Allow Users to add their own testing images through FastAPI.

<a name="roadmap"/>

## Roadmap
In the future, I hope to develop this project so that:

- Users can take a picture on their phone and immediately run the api call.

- Users can access the API through Heroku or other cloud platform services.

- The API can be more accurate in assessing what is or isn't a hotdog.

<a name="built"/>

## Built With
- Python
- Tensorflow
- Keras

<a name="how-to"/>

## How to Launch Project
Currently the project can only be run locally.

Here is the command to install the dependencies locally:

```
$ python3 -m venv env  
$ source env/bin/activate 
(env) $ python -m pip install -r requirements.txt
```
And then run the app using `uvicorn` in the Command Line:
```
(env) $ uvicorn app.main:app --reload  
```
Then head over to [http://localhost:8000/docs](http://localhost:8000/docs) or [http://localhost:8000/redoc](http://localhost:8000/redoc) in the browser.
