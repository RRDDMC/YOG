import requests
import os

class getter():
    def __init__(self, url, distantPath="", localPath="", manifest="versions.txt"):
        self.url = url
        self.distantPath = distantPath
        self.localPath = "{}/{}".format(os.getcwd(), localPath)

        self.versions = {}
        versionManifest = self.getStringFile(manifest)
        versionManifest = versionManifest.split("\n")
        for line in versionManifest:
            line = line.split("|")
            if len(line) == 2:
                self.versions[line[0]] = line[1]
    def getStringFile(self, filePath):
        response = requests.get(self.url + self.distantPath + filePath, headers={"Cache-Control": "no-cache", "Pragma": "no-cache"})
        if response.status_code != 200:
            raise Exception("{}; {} -> {}".format(self.distantPath + filePath, response.status_code, response.content))
        else:
            return response.text
    def getBytesFile(self, filePath):
        response = requests.get(self.url + self.distantPath + filePath, headers={"Cache-Control": "no-cache", "Pragma": "no-cache"})
        if response.status_code != 200:
            raise Exception("{}; {} -> {}".format(self.distantPath + filePath, response.status_code, response.content))
        else:
            return response.content
    def getAssets(self, version, forceUpdate=False):
        forceNextUpdate = False
        if not os.path.exists(self.localPath):
            os.mkdir(self.localPath)
        defaultPath = self.localPath
        if not os.path.exists(self.localPath):
            os.mkdir(self.localPath)
        self.distantPath = ""
        localPath = ""

        manifest = self.getStringFile(self.versions[version])
        manifest = manifest.split("\n")
        f = None
        for line in manifest:
            print(line)
            if line == "":
                pass
            elif line[0] == "-":
                if not f:
                    raise SyntaxError("No file name before {}".format(line))
                if not os.path.exists(self.localPath + localPath + f) or forceUpdate or forceNextUpdate:
                    fContent = self.getBytesFile(line[1:])
                    f = open(self.localPath + localPath + f, "wb")
                    f.write(fContent)
                    f.close()
                    if forceNextUpdate:
                        forceNextUpdate = False
                f = None
            elif line[0] == "#":
                localPath = line[1:]
                if not os.path.exists(self.localPath + localPath):
                    os.mkdir(self.localPath + localPath)
            elif line[0] == "=":
                self.distantPath = line[1:]
            else:
                if line[-1] == ":":
                    f = line[:-1]
                    if f[0] == "@":
                        forceNextUpdate = True
                else:
                    f = line
                    if f[0] == "@":
                        f = f[1:]
                        forceNextUpdate= True
                    if not os.path.exists(self.localPath + localPath + f) or forceUpdate or forceNextUpdate:
                        fContent = self.getBytesFile(f)
                        f = open(self.localPath + localPath + f, "wb")
                        f.write(fContent)
                        f.close()
                        f = None
                        if forceNextUpdate: forceNextUpdate = False
        self.localPath = defaultPath
