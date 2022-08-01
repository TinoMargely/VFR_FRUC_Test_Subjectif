import os, glob
from typing import List

NBSEQ = 5
BATCH_ID = 15

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

def generatePlaylist(pathYUV="E:/SequencesVFR_FRUC/YUV/",
                     pathSource="../videos/source/",
                     pathRIFE="../videos/RIFE/",
                     pathSVP="../videos/SVP/",
                     pathDuplicated="../videos/duplicated/"):
    """
    """
    #Get the YUV sequences
    sequences_all = getSequences(sequence_dir=pathYUV, videoSuffix="yuv")
    sequences_test = sequences_all[NBSEQ*BATCH_ID:NBSEQ*(BATCH_ID+1)]

    #TODOLATER
    sequences_test = [sequence for sequence in sequences_test if not "NASA" in sequence] 

    gray = "./videos/gray.mkv"

    with open("playlist.list", "w") as file:
        for sequence in sequences_test:
            
            sequence = sequence.split(".")[0]
            
            for framerate in [15,30]:
                line = f"{pathSource}{sequence}_LossLess.mp4 | {gray} | {pathRIFE}{framerate}/{sequence}_{framerate}_rife-ncnn-v23_60.mp4 | {gray} | {pathSource}{sequence}_LossLess.mp4 | {gray} | {pathRIFE}{framerate}/{sequence}_{framerate}_rife-ncnn-v23_60.mp4 \n"
                file.write(line)

                line = f"{pathSource}{sequence}_LossLess.mp4 | {gray} | {pathSVP}{framerate}/{sequence}_{framerate}_svp_60.mp4 | {gray} | {pathSource}{sequence}_LossLess.mp4 | {gray} | {pathSVP}{framerate}/{sequence}_{framerate}_svp_60.mp4 \n"
                file.write(line)

                line = f"{pathSource}{sequence}_LossLess.mp4 | {gray} | {pathDuplicated}{framerate}/{sequence}_{framerate}.mp4 | {gray} | {pathSource}{sequence}_LossLess.mp4 | {gray} | {pathDuplicated}{framerate}/{sequence}_{framerate}.mp4 \n"
                file.write(line)

    return sequences_test

if __name__ == '__main__':
    sequences_test = generatePlaylist()
    print("Generated playlist with the following sequences : \n >", " \n > ".join(sequences_test))