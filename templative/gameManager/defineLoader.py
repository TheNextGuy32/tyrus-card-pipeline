import os
import json
import csv
import io
from aiofile import AIOFile

async def loadGameCompose(gameRootDirectoryPath):
    if not gameRootDirectoryPath:
        raise Exception("Game root directory path cannot be None")

    async with AIOFile(os.path.join(gameRootDirectoryPath, "game-compose.json")) as gameCompose:
        return json.loads(await gameCompose.read())

async def loadComponentCompose(gameRootDirectoryPath):
    if not gameRootDirectoryPath:
        raise Exception("Game root directory path cannot be None")

    async with AIOFile(os.path.join(gameRootDirectoryPath, "component-compose.json")) as componentFile:
        return json.loads(await componentFile.read())

async def loadGame(gameRootDirectoryPath):
    if not gameRootDirectoryPath:
        raise Exception("Game root directory path cannot be None")

    async with AIOFile(os.path.join(gameRootDirectoryPath, "game.json")) as game:
        return json.loads(await game.read())

async def loadCompany(gameRootDirectoryPath):
    if not gameRootDirectoryPath:
        raise Exception("Game root directory path cannot be None")

    async with AIOFile(os.path.join(gameRootDirectoryPath, "company.json")) as company:
        return json.loads(await company.read())

async def loadPiecesGamedata(gameRootDirectoryPath, gameCompose, piecesGamedataFilename):
    if not gameRootDirectoryPath:
        raise Exception("Game root directory path cannot be None")

    if not piecesGamedataFilename:
        return {}

    piecesGamedataDirectory = gameCompose["piecesGamedataDirectory"]
    piecesGamedataFilenameWithExtension = "%s.csv" % (piecesGamedataFilename)
    filepath = os.path.join(gameRootDirectoryPath, piecesGamedataDirectory, piecesGamedataFilenameWithExtension)
    with open(filepath) as gamedataFile:
        reader = csv.DictReader(gamedataFile, delimiter=',', quotechar='"')

        gamedata = []
        for row in reader:
            gamedata.append(row)
        return gamedata

async def loadComponentGamedata(gameRootDirectoryPath, gameCompose, componentGamedataFilename):
    if not gameRootDirectoryPath:
        raise Exception("Game root directory path cannot be None")

    if not componentGamedataFilename:
        return {}

    componentGamedataDirectory = gameCompose["componentGamedataDirectory"]
    componentGamedataFilenameWithExtension = "%s.json" % (componentGamedataFilename)
    filepath = os.path.join(gameRootDirectoryPath, componentGamedataDirectory, componentGamedataFilenameWithExtension)
    async with AIOFile(filepath) as componentGamedata:
        return json.loads(await componentGamedata.read())

async def loadArtdata(gameRootDirectoryPath, gameCompose, artdataFilename):
    if not gameRootDirectoryPath:
        raise Exception("Game root directory path cannot be None")

    if not artdataFilename:
        return {}

    artdataDirectory = gameCompose["artdataDirectory"]
    artdataFilenameWithExtension = "%s.json" % (artdataFilename)
    filepath = os.path.join(gameRootDirectoryPath, artdataDirectory, artdataFilenameWithExtension)
    async with AIOFile(filepath) as metadataFile:
        return json.loads(await metadataFile.read())

async def loadRules(gameRootDirectoryPath):
    if not gameRootDirectoryPath:
        raise Exception("Game root directory path cannot be None")

    filepath = os.path.join(gameRootDirectoryPath, "rules.md")

    async with AIOFile(filepath, "rb") as rules:
        return await rules.read()