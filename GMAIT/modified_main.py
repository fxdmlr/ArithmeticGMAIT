import gamerunner as gr
import gamehandler as gh

def static(prechoice=None):
    if prechoice is not None:
        choice = prechoice
    print("\n")
    if prechoice is None:
        choice = input("Enter the desired mode :\n1-RegDig\n2-Div\n3-FuncEval\n4-rootGameInteger\n5-ArithmeticGame\n6-complexMultGame\n7-TrachtenbergGame\n8-rootGame\n9-phasorGame\n")
    
    try:
        choice = int(choice)
    except:
        if choice == 'a':
            inpt_dict = {"ndigits" : 5, 'mode' : 0}
            stats = gr.general_runner(gh.regMulDig, (0, 20), inpt_dict, 1)#multgame.regMulGameDig(number_of_rounds=rounds, digits=a)
            print("Score : ", round(stats[0]))
            print("Total time spent : ", round(stats[1]))
            print("Time spent per item : ", round(stats[2]))
        elif choice == 'q':
            inpt_dict = {"ndigits" : 4, 'mode' : 0}
            stats = gr.general_runner(gh.regMulDig, (0, 20), inpt_dict, 1)#multgame.regMulGameDig(number_of_rounds=rounds, digits=a)
            print("Score : ", round(stats[0]))
            print("Total time spent : ", round(stats[1]))
            print("Time spent per item : ", round(stats[2]))
        elif choice == 'z':
            inpt_dict = {"ndigits" : 7, 'mode' : 0}
            stats = gr.general_runner(gh.regMulDig, (0, 20), inpt_dict, 1)#multgame.regMulGameDig(number_of_rounds=rounds, digits=a)
            print("Score : ", round(stats[0]))
            print("Total time spent : ", round(stats[1]))
            print("Time spent per item : ", round(stats[2]))
        
        elif choice == 's':
            inpt_dict = {"ndig" : 3, 'n':3, 'ndigits':2}
            print('Evaluate the result to two digits after floating point.')
            stats = gr.general_runner(gh.phasor_game, (0, 10), inpt_dict, 1)#multgame.regMulGameDig(number_of_rounds=rounds, digits=a)
            print("Score : ", round(stats[0]))
            print("Total time spent : ", round(stats[1]))
            print("Time spent per item : ", round(stats[2]))

    if choice == 1:
        md = int(input("Mode :\n 1-Static\n 2-Dynamic\n"))
        roundd = int(input("Number of rounds : ")) 
        t = 0
        if md == 2:
            t = int(input("Duration : "))
        rounds = (t, roundd)
        a = int(input("Number of Digits : "))
        m = input('Display mode (DEFAULT 0): ')
        if m == '':
            m = 0
        else:
            m = int(m)
        
        inpt_dict = {"ndigits" : a, 'mode' : m}
        stats = gr.general_runner(gh.regMulDig, rounds, inpt_dict, md)#multgame.regMulGameDig(number_of_rounds=rounds, digits=a)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 2:
        md = int(input("Mode :\n 1-Static\n 2-Dynamic\n"))
        roundd = int(input("Number of rounds : ")) 
        t = 0
        if md == 2:
            t = int(input("Duration : "))
        rounds = (t, roundd)
        a = int(input("Number of Digits : "))
        b = int(input('Result accurate to how many digits? '))
        
        inpt_dict = {"ndigits" : a, 'out' : b}
        stats = gr.general_runner(gh.divgame, rounds, inpt_dict, md)#multgame.regMulGameDig(number_of_rounds=rounds, digits=a)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 3:
        md = int(input("Mode :\n 1-Static\n 2-Dynamic\n"))
        roundd = int(input("Number of rounds : ")) 
        t = 0
        if md == 2:
            t = int(input("Duration : "))
        rounds = (t, roundd)
        
        input_digits = int(input("Input digits after floating point : "))
        digits_output = int(input("Result digits after floating point : "))
        
        inpt_dict = {"ndigits" : input_digits, "dig" : digits_output}
        stats = gr.general_runner(gh.funcEval, rounds, inpt_dict, md)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    
    if choice == 4:
        md = int(input("Mode :\n 1-Static\n 2-Dynamic\n"))
        roundd = int(input("Number of rounds : ")) 
        t = 0
        if md == 2:
            t = int(input("Duration : "))
        rounds = (t, roundd)
        a, b = input("Range of numbers whose nth root is to be found (seperated by blank space): ").split(" ")
        nranges = [int(a), int(b)]
        c, d = input("Range of n (seperated by blank space): ").split(" ")
        rranges = [int(c), int(d)]
        inpt_dict = {"nranges":nranges, "rrange":rranges}
        stats = gr.general_runner(gh.root_game_integer, rounds, inpt_dict, md)#multgame.polyEval(rounds, deg, ranges[:], inp_ranges[:])
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    
    if choice == 5:
        md = int(input("Mode :\n 1-Static\n 2-Dynamic\n"))
        roundd = int(input("Number of rounds : ")) 
        t = 0
        if md == 2:
            t = int(input("Duration : "))
        rounds = (t, roundd)
        a = int(input("Number of Digits after floating point : "))
        n = input('Number of operations (DEFAULT 3): ')
        if n == "":
            n = 3
        else:
            n = int(n)
            
        b = input('Accurate to how many digits? (DEFAULT 2) ')
        if b == "":
            b = 2
        else:
            b = int(b)
        sq = input('Include square roots ? (1-Yes 0-No) (DEFAULT NO)')
        if sq == '':
            sq = 0
        else :
            sq = int(sq)
        cmplx = input('Complex mode ? (1-Yes 0-No) (DEFAULT NO)')
        if cmplx == '':
            cmplx = 0
        else :
            cmplx = int(cmplx)
        if cmplx != 0:
            sq = 0
        inpt_dict = {"ndig" : a, 'n':n, 'ndigits':b, 'sq':sq, 'cmplx':cmplx}
        stats = gr.general_runner(gh.arithmetic_game, rounds, inpt_dict, md)#multgame.regMulGameDig(number_of_rounds=rounds, digits=a)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))

    if choice == 6:
        md = int(input("Mode :\n 1-Static\n 2-Dynamic\n"))
        roundd = int(input("Number of rounds : ")) 
        t = 0
        if md == 2:
            t = int(input("Duration : "))
        rounds = (t, roundd)
        a = int(input("Number of Digits : "))
        
        inpt_dict = {"ndigits" : a}
        stats = gr.general_runner(gh.complex_mult_game, rounds, inpt_dict, md)#multgame.regMulGameDig(number_of_rounds=rounds, digits=a)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 7:
        md = int(input("Mode :\n 1-Static\n 2-Dynamic\n"))
        roundd = int(input("Number of rounds : ")) 
        t = 0
        if md == 2:
            t = int(input("Duration : "))
        rounds = (t, roundd)
        a = int(input("Number of Digits : "))
        
        inpt_dict = {"ndigits" : a}
        stats = gr.general_runner(gh.trachtenberg, rounds, inpt_dict, md)#multgame.regMulGameDig(number_of_rounds=rounds, digits=a)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 8:
        md = int(input("Mode :\n 1-Static\n 2-Dynamic\n"))
        roundd = int(input("Number of rounds : ")) 
        t = 0
        if md == 2:
            t = int(input("Duration : "))
        rounds = (t, roundd)
        a = int(input("Number of Digits : "))
        b = int(input('Result accurate to how many digits? '))
        c = input('N : (DEFAULT 2) ')
        
        if c == '':
            c = 2
        else:
            c = int(c)
        
        inpt_dict = {"ndigits" : a, 'resdig' : b, 'n':c}
        stats = gr.general_runner(gh.rootgame, rounds, inpt_dict, md)#multgame.regMulGameDig(number_of_rounds=rounds, digits=a)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 9:
        md = int(input("Mode :\n 1-Static\n 2-Dynamic\n"))
        roundd = int(input("Number of rounds : ")) 
        t = 0
        if md == 2:
            t = int(input("Duration : "))
        rounds = (t, roundd)
        a = int(input("Number of Digits after floating point : "))
        n = input('Number of operations (DEFAULT 3): ')
        if n == "":
            n = 3
        else:
            n = int(n)
            
        b = input('Accurate to how many digits? (DEFAULT 2) ')
        if b == "":
            b = 2
        else:
            b = int(b)
        
        inpt_dict = {"ndig" : a, 'n':n, 'ndigits':b}
        stats = gr.general_runner(gh.phasor_game, rounds, inpt_dict, md)#multgame.regMulGameDig(number_of_rounds=rounds, digits=a)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))

def run():        
    while True:
        static()
        z = input("Press Enter to continue ...")

if __name__ == '__main__':
    run()