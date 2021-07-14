import os
import shutil

def folderChain(path):
	return [path[:i].replace('\\', '/') for i in range(len(path)) if path[i] == '/' or path[i] == '\\']

def getParentFolder(path):
	if path[-1] == '/' or path[-1] == '\\':
		path = path[:-1]
	end = max(path.rfind('\\'), path.rfind('/'))
	return path[:end].replace('\\', '/')

def foldersInFolder(folder):
	return [os.path.join(folder, f).replace('\\', '/') for f in os.listdir(folder) if os.path.isdir(os.path.join(folder, f))]

def filesInFolderRec(folder):
	return [os.path.join(dp, f).replace('\\', '/') for dp, dn, filenames in os.walk(folder) for f in filenames]

def filesInFolder(folder):
	return [os.path.join(folder, f).replace('\\', '/') for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

def foldersInFolderRec(folder):
	return [os.path.join(dp, f).replace('\\', '/') for dp, dn, filenames in os.walk(folder) for f in dn]

def moveFolder(src, target):
	shutil.move(src, target)

def moveFile(src, target):
	os.rename(src, target)

def createFolder(folder):
	result = False
	for parent in folderChain(folder):
		if not os.path.isdir(parent):
			os.mkdir(parent)
			result = True

	if not os.path.isdir(folder):
		os.mkdir(folder)
		result = True

def createFile(file):
	createFolder(getParentFolder(file))
	open(file, "a+").close()
