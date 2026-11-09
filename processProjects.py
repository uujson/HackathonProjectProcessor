import csv

devpostProjects = []
devpostTracks = []

mlhProjects = []
mlhTracks = []

class Project:
    def __init__(self):
        self.ProjectName = ""
        self.Submitter = ""
        self.Source = ""
        self.Tracks = []

def processDevpost(devpostFile):
    if ".csv" not in devpostFile:
        file = devpostFile + ".csv"
    else:
        file = devpostFile
    with open(file,"r",encoding="utf-8") as f:
        data = csv.reader(f)
        for project in data:
            newProject = Project()
            newProject.ProjectName = project[0]
            newProject.Submitter = project[15] + " " + project[16]
            if (project[9] != ""):    
                newProject.Source = project[9].split(", ")
                githubrepo = ""
                for source in newProject.Source:
                    if "github" in source:
                        githubrepo = source
                        break
                newProject.Source = githubrepo
            if (project[13] != ""):
                newProject.Tracks = project[13].split(", ")
                newProject.Tracks.sort()
            devpostProjects.append(newProject)
    devpostProjects.remove(devpostProjects[0])
    
    for i in devpostProjects:
        for j in i.Tracks:
            if j not in devpostTracks:
                devpostTracks.append(j)
    devpostTracks.sort()
    
    with open("devpostProcessed.csv","w",encoding="utf-8",newline="") as f:
        headers = ["Project", "Submitter", "Source"]
        for tracks in devpostTracks:
            headers.append(tracks)
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for project in devpostProjects:
            projDict = {}
            projDict["Project"] = project.ProjectName
            projDict["Submitter"] = project.Submitter
            projDict["Source"] = project.Source
            for tracks in devpostTracks:
                if tracks not in project.Tracks:
                    projDict[tracks] = ""
                else:
                    projDict[tracks] = "TRUE"
            writer.writerow(projDict)
    print("\nDevPost CSV processed and written to: \"devpostProcessed.csv\"\n")

def processMLH(mlhFile):
    if ".csv" not in mlhFile:
        file = mlhFile + ".csv"
    else:
        file = mlhFile
    with open(file,"r",encoding="utf-8") as f:
        data = csv.reader(f)
        for project in data:
            newProject = Project()
            newProject.ProjectName = project[0]
            newProject.Submitter = project[4]
            if (project[5] != ""):    
                newProject.Source = project[5]
            if (project[2] != ""):
                newProject.Tracks = project[2].split("; ")
                newProject.Tracks.sort()
            mlhProjects.append(newProject)
    mlhProjects.remove(mlhProjects[0])
    
    for i in mlhProjects:
        for j in i.Tracks:
            if j not in mlhTracks:
                mlhTracks.append(j)
    mlhTracks.sort()
    
    with open("mlhProcessed.csv","w",encoding="utf-8",newline="") as f:
        headers = ["Project", "Submitter", "Source"]
        for tracks in mlhTracks:
            headers.append(tracks)
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for project in mlhProjects:
            projDict = {}
            projDict["Project"] = project.ProjectName
            projDict["Submitter"] = project.Submitter
            projDict["Source"] = project.Source
            for tracks in mlhTracks:
                if tracks not in project.Tracks:
                    projDict[tracks] = ""
                else:
                    projDict[tracks] = "TRUE"
            writer.writerow(projDict)
    print("\nMLH CSV processed and written to: \"mlhProcessed.csv\"")

print("Enter DevPost CSV Filename\nPress Enter if None.")
devpostFile = input()
if devpostFile != "":
    processDevpost(devpostFile)
print("Enter MLH CSV Filename\nPress Enter if None.")
mlhFile = input()
if mlhFile != "":
    processMLH(mlhFile)

            
        
        