
import sys
import time

class StdOutput():
    
    def stdOutput(self) -> None:
        shuffle = 20
        for i in range(shuffle):
            time.sleep(1)
            print(f"Suffle dinuc [{i+1} of {shuffle}]", end="\r", flush=True)
        print("")
        pass
        
def stdOut() -> None:
    StdOutput().stdOutput()
    pass

        
if __name__ == "__main__":
    stdOut()
