#!/usr/bin/env python
import rospy
import roslib

import yaml

from random import shuffle
from sara_joke.srv import joke


def get_random_joke(req):

    with open(rospy.get_param("joke_"+req.language), 'r') as stream:
        try:
            jokes = yaml.load(stream=stream)

        except yaml.YAMLError as exc:
            rospy.logerr(exc)

    shuffle(jokes)
    return jokes[0]


def random_joke_server():
    rospy.init_node('sara_joke')
    s = rospy.Service('get_joke', joke, get_random_joke)
    rospy.spin()


if __name__ == "__main__":
    random_joke_server()
