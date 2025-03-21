import requests
import os

class getter():
    def __init__(self, url, distantPath="", localPath="", manifest="versions.txt"):
        self.url = url
        self.distantPath = distantPath
        self.localPath = localPath

        self.versions = {}
        versionManifest = self.getStringFile(manifest)
        versionManifest = versionManifest.split("\n")
        for line in versionManifest:
            line = line.split("|")
            if len(line) == 2:
                self.versions[line[0]] = line[1]
    def getStringFile(self, filePath):
        print(self.url + self.distantPath + filePath)
        response = requests.get(self.url + self.distantPath + filePath)
        if response.status_code != 200:
            raise Exception("{} -> {}".format(response.status_code, response.content))
        else:
            return response.text
    def getBytesFile(self, filePath):
        print(self.url + self.distantPath + filePath)
        response = requests.get(self.url + self.distantPath + filePath)
        if response.status_code != 200:
            raise Exception("{} -> {}".format(response.status_code, response.content))
        else:
            return response.content
    def getAssets(self, version):
        if not os.path.exists(self.localPath):
            os.mkdir(self.localPath)
        self.distantPath = ""
        self.localPath = ""

        manifest = self.getStringFile(self.versions[version])
        manifest = manifest.split("\n")
        f = None
        for line in manifest:
            print(line)
            if line == "":
                pass
            elif line[0] == "-":
                if not f:
                    raise SyntaxError("No file name befor {}".format(line))
                fContent = self.getBytesFile(line[1:])
                if not os.path.exists(self.localPath + f):
                    f = open(f, "wb")
                    f.write(fContent)
                    f.close()
            elif line[0] == "#":
                self.localPath = line[1:]
                if not os.path.exists(self.localPath):
                    os.mkdir(self.localPath)
            elif line[0] == "=":
                self.distantPath = line[1:]
            else:
                if line[-1] == ":":
                    f = line[:-1]
                else:
                    f = line
                    fContent = self.getBytesFile(self.localPath + f)
                    f = open(f, "wb")
                    f.write(fContent)
                    f.close()
                    f = None

a = getter("https://raw.githubusercontent.com/RRDDMC/YOG/main/assets/", localPath="data/")
a.getAssets("0.0.1")
