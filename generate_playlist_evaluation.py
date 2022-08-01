import os, glob
from typing import List

def getSequences(sequence_dir:str,videoSuffix:str)->List[str]:
    """Returns a list of file names in specified directory that respect the given extension 
    
    Args: 
        sequence_dir: Directory containing the sequences
        videoSuffix: Video format suffix (Ex: "yuv","mp4") 
    
    Returns:
        sequenceList: List of sequences in the directory with the given suffix
    """
    currentDir = os.getcwd()
    os.chdir(sequence_dir)
    sequenceList = glob.glob("*."+videoSuffix)
    os.chdir(currentDir)
    return sequenceList

def generatePlaylist(pathSource="../videos/REF/",
                     pathVFRFRUC="../videos/VFR-FRUC/",
                     pathTraining="../videos/TRAINING  /",):
    """
    """
    #Get the YUV sequences
    sequences_all = [str(id+1) for id in range(len(os.listdir(pathSource)))]

    gray = "./videos/gray.mkv"

    with open("playlist.list", "w") as file:
        for sequence in sequences_all:
            
            line = f"{pathSource}{sequence}_LossLess.mp4 | {gray} | {pathVFRFRUC}{sequence}_VFRFRUC_labels.mp4 | {gray} | {pathSource}{sequence}_LossLess.mp4 | {gray} | {pathVFRFRUC}{sequence}_VFRFRUC_labels.mp4 \n"
            file.write(line)
            
    return sequences_all

if __name__ == '__main__':
    sequences_test = generatePlaylist()
    print("Generated playlist with the following sequences : \n >", " \n > ".join(sequences_test))