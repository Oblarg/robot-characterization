from mako.template import Template

import os
import importlib.resources as resources


def genRobotCode(projectType, config):
    if projectType == 'Simple':
        with resources.path(__name__, 'templates') as path:
            with open(os.path.join(path, 'Simple', 'Robot.java.mako'), 'r') as template:
                return Template(template.read()).render(
                    ppr=config['encoderPPR'],
                    ports=config['motorPorts'],
                    inverted=config['motorsInverted'],
                    controllers=config['controllerTypes'],
                    encoderports=config['encoderPorts'],
                    encoderinv=config['encoderInverted'],
                    offset=config['offset'],
                    units=config['units']
            )
    elif projectType == 'Talon':
        with resources.path(__name__, 'templates') as path:
            with open(os.path.join(path, 'Talon', 'Robot.java.mako'), 'r') as template:
                return Template(template.read()).render(
                    ppr=config['encoderPPR'],
                    ports=config['motorPorts'],
                    inverted=config['motorsInverted'],
                    controllers=config['controllerTypes'],
                    encoderinv=config['encoderInverted'],
                    offset=config['offset'],
                    units=config['units']
            )

def genBuildGradle(projectType, team):
    with resources.path(__name__, 'templates') as path:
        with open(os.path.join(path, projectType, 'build.gradle.mako'), 'r') as template:
            return Template(template.read()).render(team=team)