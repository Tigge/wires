import sys
import components.Source
import components.AndComponent
import components.Light

def main():
    
    
    s1 = components.Source.Source(True)
    s2 = components.Source.Source(True)
    
    ac = components.AndComponent.AndComponent()
    
    light = components.Light.Light()
    
    s1.outputs[0].connect(ac.inputs[0])
    s2.outputs[0].connect(ac.inputs[1])
    ac.outputs[0].connect(light.inputs[0])
    
    components.Input.Input.readylist = {}
    gadgetlist = [s1, s2, ac, light]

    while len(gadgetlist) > 0:
        print "============"
        listsize = len(gadgetlist)
        print "list size:", listsize, "\n"
        for i in range(len(gadgetlist) -1, -1, -1):
            print i, gadgetlist[i]
            if gadgetlist[i].ready():
                print "ready:", gadgetlist[i]
                gadgetlist[i].calculate()
                del gadgetlist[i]
        if listsize == len(gadgetlist):
            print "Error, loop or unconnected", listsize, len(gadgetlist)
            print gadgetlist
            break
        

if __name__ == "__main__":
    sys.exit(main())
