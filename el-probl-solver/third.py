import random
import time
from quantiphy import Quantity as Qty
import re
import sys
from problemele import *

def converted(a):

    #check if a, the INPUT STRING, is a (float)number OR any other string(non-number)
    #if it is a string, return False
    #for number return True

    try:
        number = float(a)
        # if (type(number) in (int, float)):
        if isinstance(number, float):
            # TODO also check if number isn't big/small enough not to fit in a float
            #print(type(number))
            return number
    except ValueError as my_except:    # or is it TypeError
        # print('My exception:', my_except, type(my_except))
        # print("It is possible that the number is not a float")
        return False
    except Exception as e:
        print('Exception:', e)
        print('some other exception rise in conversion str to float')
        return False
# problem 5
def generateNewPrbl(chosen_problem):
    global points, problems_counter
    #problems_counter=0  #or read an input/savedfile
    print('\n\nProblem nr:',problems_counter)
    time.sleep(.600)
    execution_ret = eval(chosen_problem)
    new_problem_questions=True
    #new problem
    while new_problem_questions:
        wrong_anser=0
        
        hint_list = execution_ret[0]
        points_list=execution_ret[1]
        question_list= execution_ret[2]
        answers_list = execution_ret[3:]
        
        nr_of_ans= len(answers_list)
        
        points_4_this_prbl = sum(points_list)     #TODO: get it returned from probe as a list, this way each question can have variable nr of points)
        
        print(f'for this problem you have available {points_4_this_prbl} points')
        time.sleep(1)
        for item in answers_list:
            print('--',item,'-- ')
        print(10 * '__')
        #exit_probl=False
    
        #answers check
        for index, ans in enumerate(answers_list):
            # if exit_probl ==True:
            #         continue
            i_have_a_hint=True
            lost_points=0
            print('QUESTION: ', index+1, '  ans=',ans )
            #get answer; check ans and/or offer quitige
            avlb_points = points_list[index]
            ans_num=['first','second','third','forth','fifth','sixth']
            
            #get/check each ans input
            while True:
                
                ######################################               
                print(10*'_________')
                print('\nFoooor the %s question you have available %d points; Calculate the %s :' % (ans_num[index],avlb_points, question_list[index]))  #### TODO: calculate n-th(first sec,third...) answeer
                input_str = input("Input your answer:\033[0m\nType q to quit. \nH for a hint or \n\033[1m\n")

                m = converted(input_str)
                #print ('==',m,'==')
                match_number = re.compile('-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *-?\ *[0-9]+)?')
                curated_nr = [float(x) for x in re.findall(match_number, input_str)]

                if input_str == 'q':
                    print('you selected \'quitige\'. Bye!')
                    print('\nYour exiting points are %d, made in %d rounds,' % (points, problems_counter))
                    exit()
                # if input_str == 'p':
                # print('For this problem there stil are available %d points' %((points_4_this_prbl)-lost_points))

                elif input_str == 'h' and i_have_a_hint is True:
                    print('your hint is, ', hint_list[index])
                    avlb_points -= 5
                    #print("out of", avlb_points, ", you lost", lost_points, 'points')
                    i_have_a_hint=False
                
                elif input_str == 'h' and i_have_a_hint is False:   
                    print('No more hints for now') 

                elif m == False:
                    print(input_str, 'input is not a number. Try again')
                    continue
                #else:
                    # break outside infinite loop, the number input is good to be used
                    #print('!!!!!!!!!!!!!!!input is a number!!!!!!')
                #   break

                # if you calculated correctly score++
                elif curated_nr[0] == ans:

                    print("\nCongrats, you got the %s number right" % ans_num[index])
                    print(lost_points,' lost points--www')
                    points = points+avlb_points
                    print('-----',points,'-----')
                    print("Way to go!") 
                    wrong_answer =0
                    # You made %d points from %d problems" % (points, counter))
                    print('index:', index+1)
                    #########
                    if index+1 == len(answers_list):
                        print ('prbl counter increment--------------')
                        problems_counter += 1
                        inp= input('all answers were good go to next probl?y/n')
                        if inp == 'y':
                            generateNewPrbl(chosen_problem)
                        else:
                            print('\nYour exiting points are %d, made in %d rounds,' % (points, problems_counter))
                            exit()
                    else:
                        #print('good answer continue answering next question(?)')
                        wrong_answer=0
                        print('rrrrrrr')
                        break
                    ############`

                    # you're right but do you want another round? get the answer
                #wrong answer    
                else:
                    avlb_points -= 2
                    print('You got it wrong (-2p), points remaining:',avlb_points,'right answer is:', ans)
                    if avlb_points<=0:
                        print('no more points available')

                        inp=input("try next probl?y/n")
                        if inp == 'y':
                            avlb_points = points_list[index]                       
                            generateNewPrbl(chosen_problem)
                        else :
                            exit()

                    inp=input('\nDo you want another try at this calculation y/n? : ')
                    if inp == "y":
                        
                        
                        print('Available points:',avlb_points)#-wrong_answer)
                                                                 
                        if wrong_anser >=10: 
                            print('\nYou lost all your points for this prbl : %d' %wrong_anser)
                            print('\nYour exiting points are %d, made in %d rounds,' % (points, problems_counter))
                            
                            #break
                            exit()
                        continue
                    # for 'n' break out of the game, any other keystroke continues with another round
                    elif inp == "n" or inp == "q":
                        #new_round = False
                        print('You chose to not answer this question')
                        #print('\nYour exiting points are %d, made in %d rounds,' % (points, problems_counter))
                        if index+2 <= len(answers_list):
                            print('index',index,'len_ans=',len(answers_list))
                            break
                        else:
                            #problems_counter +=1
                            inp= input('New problem? y/n:')
                            if inp == 'y':
                                problems_counter += 1
                                generateNewPrbl(chosen_problem)
                            else:
                                print('\nzzzzzYour exiting points are %d, made in %d rounds,' % (points, problems_counter))
                                exit()
                                
                            #generateNewPrbl(chosen_problem)
                    
                    else:
                        print('\nxxxxxxxxYour exiting points are %d, made in %d rounds,' % (points, problems_counter))
                        exit()


# ############ Game STARTs here
# Force the problem chosen to be a particular one
#prbl_list=('problem4()', 'problem4()')
prbl_list=('problem5()', 'problem5()')

# the real list, to be updated with other problems
# prbl_list=('problem4()', 'problem5()')


# todo: to fix: number of points (sa fie) > number of hints, sa fie din ce scadea si sa si ramana ceva
# todo: create the pages for action codes, main, settings etc
# todo: create so that books and chapters can be selected via gui;
# which problems will be in the pool f probable current game prblms

def start_game(prbl_list):

    # chose randomly(for now) a prbl from the list of problems
    # later you can implement the ratio of each problem to be chosen

    chosen_problem = random.choice(prbl_list)

    # name&score; 
    player = {'name': 'Nobody', 'alt': 10}
    print('\nProblematic')
    print('----' * 10)

    print('Enter player name:')
    player['name'] = input()
    print('----' * 10)

    
    
    
    global points, problems_counter
    problems_counter = 1
    points  = 0

    ############ first execution
    print(f'%s, here\'s the first problem:' % player['name'])
    time.sleep(1)
    generateNewPrbl(chosen_problem)



start_game(prbl_list)

#TODO: give me the correct answer and lose points for this question