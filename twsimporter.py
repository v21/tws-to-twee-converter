import pickle, sys

    
def main():
    tws_file = sys.argv[1]
    out = ""
        
    with open(tws_file) as f:
        p = pickle.load(f)
        for tiddler in p["storyPanel"]["widgets"]:
            out += tiddler["passage"].toTwee()
    
    print(out)
    
if __name__ == "__main__":
    main()