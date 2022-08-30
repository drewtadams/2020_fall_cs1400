'''
Project Name: P1: Yondu Udonta
Author: Drew Adams
Due Date: 08/24/2020
Course: CS1400-X03



Put your description here, lessons learned here, and any other information someone using your
program would need to know to make it run.
'''

def main():
    '''
    Program starts here.
    '''
    
    reavers = 0
    units = 0
    
    try:
        # constant variables
        FIRST_CUT = 3
        YONDU_PCNT = .13
        PETER_PCNT = .11
        
        # get the number of reavers and units
        reavers = int(input('How many Reavers:\n'))
        units = int(input('How many units:\n'))
        
        # keep track of remaining units
        remaining_units = units
        
        # give the crew their first cut
        remaining_units -= FIRST_CUT * (reavers - 2)
        
        # give yondu his 13%
        yondu_cut = int(YONDU_PCNT * remaining_units)
        remaining_units -= yondu_cut
        
        # give peter his 11%
        peter_cut = int(PETER_PCNT * remaining_units)
        remaining_units -= peter_cut
        
        # divvy out the remaining units to the entire crew
        remaining_per_crew = remaining_units // reavers
        crew_cut = (remaining_per_crew * (reavers - 2))
        yondu_cut += remaining_per_crew
        peter_cut += remaining_per_crew
        
        # give remaining to the PBF
        rbf = remaining_units - (remaining_per_crew * reavers)
        
        # display totals
        print("Yondu's share: " + str(yondu_cut))
        print("Peter's share: " + str(peter_cut))
        print("Crew: " + str(crew_cut // (reavers - 2)))
        print("RBF: " + str(rbf))
        
    except ValueError:
        print("Enter positive integers for reavers and units.")
        return
    
    if reavers < 1 or units < 1:
        print("Enter positive integers for reavers and units.")
        return

    if reavers < 3:
        print("Not enough crew.")
        return

    if units <= 3 * reavers:
        print("Not enough units.")
        return
    
    # (2) replace pass with your code
    pass

if __name__ == "__main__":
    main()
    