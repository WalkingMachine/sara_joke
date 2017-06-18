#!/usr/bin/env python
import rospy
import roslib
from random import shuffle
from sara_joke.srv import joke


def get_random_joke(req):

    if req.language == "en":
        jokes = [
            "A blind man walks into a bar. And a table. And a chair.",
            "Why was 6 afraid of 7?                  Because 7, 8, 9",
            "Trust me i was build by futur engineers",
            "A robot walks into a pharmacy. The pharmacist asks him if he'd like anything. The robot replies, A soul.",
            "Two statisticians are out hunting when one of them sees a duck. The first takes aim and shoots, but the bullet goes sailing past six inches too high. The second statisticians also takes aim and shoots, but this time the bullet goes saling past six inches too low. The two statisticians then give one another high fives and exclaim, Got him!",
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
