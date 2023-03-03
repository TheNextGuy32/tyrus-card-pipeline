from os import path
from distutils.dir_util import copy_tree

from . import componentProcessor

async def produceGame(gameRootDirectoryPath, componentFilter):
    return await componentProcessor.produceGame(gameRootDirectoryPath, componentFilter)

async def listComponents(gameRootDirectoryPath):
    await componentProcessor.listComponents(gameRootDirectoryPath)

async def convertRulesMdToHtml(gameRootDirectoryPath):
    await componentProcessor.convertRulesMdToHtml(gameRootDirectoryPath)

async def convertRulesMdToSpans(gameRootDirectoryPath):
    await componentProcessor.convertRulesMdToSpans(gameRootDirectoryPath)

async def createTemplate():
    if(path.exists("./game-compose.json")):
        print("This directory already contains a gameExisting game compose here.")
        return

    fromDirectory = path.join(path.dirname(path.realpath(__file__)), "template")
    copy_tree(fromDirectory, "./")

async def createComponent(name, type):
    await componentProcessor.createComponent(name, type)