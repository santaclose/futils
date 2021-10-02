import os
import shutil

def folderChain(path):
	return [path[:i].replace('\\', '/') for i in range(len(path)) if path[i] == '/' or path[i] == '\\']

def getParentFolder(path):
	if path[-1] == '/' or path[-1] == '\\':
		path = path[:-1]
	if '/' not in path and '\\' not in path:
		return None
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
	parentFolder = getParentFolder(target)
	if parentFolder is not None:
		createFolder(parentFolder)
	shutil.move(src, target)

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
	parentFolder = getParentFolder(file)
	if parentFolder is not None:
		createFolder(parentFolder)
	open(file, "a+").close()

def getExtension(file):
	i = len(file) - 1
	while True:
		if i < 0:
			break
		if file[i] == '/' or file[i] == '\\':
			break
		if file[i] == '.':
			return file[i + 1:]
		i -= 1
	return None

def getName(file):
	extensionConsidered = False
	p = len(file)
	i = p - 1
	while True:
		if i < 0:
			q = 0
			break
		if file[i] == '.' and not extensionConsidered:
			p = i
			extensionConsidered = True
		if file[i] == '/' or file[i] == '\\':
			q = i + 1
			break
		i -= 1
	return file[q:p]
