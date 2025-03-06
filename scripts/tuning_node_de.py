#!/usr/bin/env python3

import rospy
from pid_tuning.evolutive_algorithms.dif_evolution import DifferentialEvolution
from pid_tuning.settings.control_gazebo import ControlGazebo

rospy.init_node("tuning_node")
rate = rospy.Rate(25)
paths = '/home/jacob/ws/src/scara_robot_description/config/paths.json'
de = DifferentialEvolution(10, 9, 2, 0.65, 0.85, 3, paths, epsilon_1=1, tm=28800)
file = open("best_pid_values_DE.txt", 'w')
gz = ControlGazebo()
gz.init_values()

if not rospy.is_shutdown():
    x = de.gen_population()
    de.evaluate(x, gz, rate)
    x_best = de.dif_evolution(x, gz, rate)
    file.write(str(x_best))
    file.close()