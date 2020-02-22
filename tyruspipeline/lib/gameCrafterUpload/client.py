import os
import json
from os.path import isfile, join
import sys

def loadGame(gameRootDirectoryPath):
    if not gameRootDirectoryPath:
        raise Exception("Game root directory path cannot be None")

    with open("%s/game.json" % gameRootDirectoryPath) as game:
        return json.load(game)

def loadCompany(gameRootDirectoryPath):
    if not gameRootDirectoryPath:
        raise Exception("Game root directory path cannot be None")

    with open("%s/company.json" % gameRootDirectoryPath) as company:
        return json.load(company)

def loadComponentFile(componentDirectoryPath):
    if not componentDirectoryPath:
        raise Exception("componentDirectoryPath cannot be None")

    with open("%s/component.json" % componentDirectoryPath) as componentFile:
        return json.load(componentFile)

def uploadComponents(session, outputDirectory, cloudGame, cloudGameFolder):
    if not outputDirectory:
        raise Exception("outputDirectory cannot be None")

    for directoryPath in next(os.walk(outputDirectory))[1]:
        componentDirectoryPath = "%s/%s" % (outputDirectory, directoryPath)
        uploadComponent(session, componentDirectoryPath, cloudGame, cloudGameFolder)

def uploadComponent(session, componentDirectoryPath, cloudGame, cloudGameFolder):
    if not componentDirectoryPath:
        raise Exception("componentDirectoryPath cannot be None")

    componentFile = loadComponentFile(componentDirectoryPath)
    componentType = componentFile["type"]
    componentName = componentFile["name"]

    if componentType != "pokerDeck":
        print("Skipping %s. The %s component type is not currently supported." % (componentName, componentType))
        return
    
    print("Uploading %s %s" % (componentType, componentName))
    pieceFilepaths = []
    for f in os.listdir(componentDirectoryPath):
        filePath = join(componentDirectoryPath, f)
        
        if (isfile(filePath) and filePath.endswith(".jpg")):
            pieceFilepaths.append(filePath)
    
    for pieceFilepath in pieceFilepaths:
        uploadPiece(session, pieceFilepath)

def uploadPiece(session, pieceFilepath):
    print("Uploading %s" % (pieceFilepath))

def makePokerDeck(session, dirpath):
    asset = '%s-pdeck-%s' % (self['name'], len(self.parts))

    def face_card_test(filename):
        return filename.startswith('face') and filename.endswith('.jpg')

    return makeDeck('pokerdeck', 'pokercard', asset, dirpath, face_card_test)

def makeDeck(session, deck_kind, card_kind, asset, dirpath, face_card_test):
    folder = core.new_folder(session, asset, self.folder['id'])

    back_filepath = dirpath + '/back.jpg'
    file_result = core.new_file(back_filepath, folder['id'])

    deck = new_deck(
        deck_kind, asset, self.id, back_file_id=file_result['id']
    )

    print 'Deck'
    print deck

    self.parts.append(deck)

    file_list = [dirpath + '/' + x
                    for x in os.listdir(dirpath)
                    if face_card_test(x)]
    for filepath in file_list:
        file_result = core.new_file(filepath, folder['id'])
        card = new_card(
            card_kind,
            os.path.basename(filepath),
            deck_id=deck['id'],
            file_id=file_result['id']
        )

def makeBooklet(session, dirpath):
    asset = '%s-booklet-%s' % (self['name'], len(self.parts))
    folder = core.new_folder(self.user, asset, self.folder['id'])

    booklet = new_booklet('smallbooklet', asset, self.id)

    print 'Booklet'
    print booklet

    self.parts.append(booklet)

    file_list = [dirpath + '/' + x
                    for x in os.listdir(dirpath)
                    if x.endswith('.png')]
    for filepath in file_list:
        file_result = core.new_file(filepath, folder['id'])
        card = new_booklet_page(
            'smallbookletpage',
            os.path.basename(filepath),
            booklet_id=booklet['id'],
            image_id=file_result['id']
        )
