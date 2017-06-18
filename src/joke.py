#!/usr/bin/env python
import rospy
import roslib
from random import shuffle
from sara_joke.srv import joke


def get_random_joke(req):

    print req.language

    if req.language == "en":
        jokes = [
            "A blind man walks into a bar. And a table. And a chair.",
            "Why was 6 afraid of 7?                  Because 7, 8, 9",
        ]
    elif req.language == "fr":
        jokes = []
    else:
        rospy.logfatal("Wrong parameters")
        rospy.logfatal("Wrong parameters")
        return "Error"

    shuffle(jokes)
    return jokes[0]


def random_joke_server():
    rospy.init_node('sara_joke')
    s = rospy.Service('get_joke', joke, get_random_joke)
    rospy.spin()


if __name__ == "__main__":
    random_joke_server()
