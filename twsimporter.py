import pickle, sys

    
def main():
    tws_file = sys.argv[1]
    twee2 = '-twee2' in sys.argv
    pos = None
    out = ""
        
    with open(tws_file) as f:
        p = pickle.load(f)
        for tiddler in p["storyPanel"]["widgets"]:
            if twee2:
                pos = tiddler["pos"]
            out += tiddler["passage"].toTwee(pos)
    
    print(out)
    
if __name__ == "__main__":
    main()